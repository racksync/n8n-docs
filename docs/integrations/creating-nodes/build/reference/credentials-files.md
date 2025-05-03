---
#https://www.notion.so/n8n/Frontmatter-432c2b8dff1f43d4b1c8d20075510fe4
title: ไฟล์ Credentials
description: เอกสารอ้างอิงสำหรับไฟล์ credentials ของ node
contentType: reference
---

# Credentials file

ไฟล์ Credentials จะกำหนดวิธีการ authorize สำหรับ node ของคุณ การตั้งค่าในไฟล์นี้จะมีผลกับสิ่งที่ n8n แสดงใน **Credentials** modal และต้องตรงกับความต้องการ authentication ของ service ที่คุณจะเชื่อมต่อ

ในไฟล์ credentials คุณสามารถใช้ [n8n UI elements](/integrations/creating-nodes/build/reference/ui-elements.md) ได้ทั้งหมด n8n จะเข้ารหัสข้อมูลที่ถูกเก็บไว้ใน credentials ด้วย encryption key

## Structure of the credentials file

ไฟล์ credentials จะมีโครงสร้างพื้นฐานดังนี้:

1. Import statements
2. สร้าง class สำหรับ credentials
3. ใน class ให้กำหนด properties ที่ควบคุม authentication สำหรับ node

### Outline structure

```js
import {
	IAuthenticateGeneric,
	ICredentialTestRequest,
	ICredentialType,
	INodeProperties,
} from 'n8n-workflow';

export class ExampleNode implements ICredentialType {
	name = 'exampleNodeApi';
	displayName = 'Example Node API';
	documentationUrl = '';
	properties: INodeProperties[] = [
		{
			displayName: 'API Key',
			name: 'apiKey',
			type: 'string',
			default: '',
		},
	];
	authenticate: IAuthenticateGeneric = {
		type: 'generic',
		properties: {
    			// สามารถเป็น body, header, qs หรือ auth
			qs: {
        			// ใช้ค่าจาก `apiKey` ข้างบน
				'api_key': '={{$credentials.apiKey}}'
			}

		},
	};
	test: ICredentialTestRequest = {
		request: {
			baseURL: '={{$credentials?.domain}}',
			url: '/bearer',
		},
	};
}
```

## Parameters

### `name`

String. ชื่อภายในของ object นี้ ใช้อ้างอิงจากที่อื่นใน node

### `displayName`

String. ชื่อที่ n8n ใช้แสดงใน GUI

### `documentationUrl`

String. URL ไปยังเอกสาร credentials ของคุณ

### `properties`

แต่ละ object จะมี:

* `displayName`: ชื่อที่ n8n ใช้แสดงใน GUI
* `name`: ชื่อภายในของ object นี้ ใช้อ้างอิงจากที่อื่นใน node
* `type`: ประเภทข้อมูลที่ต้องการ เช่น `string`
* `default`: URL ที่ n8n จะใช้ทดสอบ credentials

### `authenticate`

* `authenticate`: Object. มี object ที่บอก n8n ว่าจะ inject ข้อมูล authentication เข้าไปใน API request อย่างไร

#### `type`

String. ถ้าใช้ authentication แบบส่งข้อมูลใน header, body หรือ query string ให้ตั้งเป็น `'generic'`

#### `properties`

Object. กำหนดวิธี authentication ตัวเลือกมี:

* `body`: Object. ส่งข้อมูล authentication ใน request body สามารถมี object ซ้อนกันได้
```typescript
authenticate: IAuthenticateGeneric = {
	type: 'generic',
	properties: {
		body: {
			username: '={{$credentials.username}}',
			password: '={{$credentials.password}}',
		},
	},
};
``` 

* `header`: Object. ส่งข้อมูล authentication ใน request header
```typescript
authenticate: IAuthenticateGeneric = {
	type: 'generic',
	properties: {
		header: {
			Authorization: '=Bearer {{$credentials.authToken}}',
		},
	},
};
``` 

* `qs`: Object. ย่อมาจาก "query string" ส่งข้อมูล authentication ใน query string ของ request
```typescript
authenticate: IAuthenticateGeneric = {
	type: 'generic',
	properties: {
		qs: {
			token: '={{$credentials.token}}',
		},
	},
};
``` 

* `auth`: Object. ใช้สำหรับ Basic Auth ต้องมี `username` และ `password` เป็น key
```typescript
authenticate: IAuthenticateGeneric = {
	type: 'generic',
	properties: {
		auth: {
			username: '={{$credentials.username}}',
			password: '={{$credentials.password}}',
		},
	},
};
```

### `test`

ให้ใส่ object `request` ที่มี URL และประเภท authentication ที่ n8n จะใช้ทดสอบ credential

```typescript
test: ICredentialTestRequest = {
		request: {
			baseURL: '={{$credentials?.domain}}',
			url: '/bearer',
		},
	};
```
