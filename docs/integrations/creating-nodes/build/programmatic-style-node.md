---
#https://www.notion.so/n8n/Frontmatter-432c2b8dff1f43d4b1c8d20075510fe4
contentType: tutorial
---

# Build a programmatic-style node

tutorial นี้จะพาไปดูวิธีสร้าง node แบบ programmatic-style ก่อนเริ่ม แนะนำให้แน่ใจว่านี่คือ style ที่คุณต้องการใช้ ดูรายละเอียดเพิ่มเติมได้ที่ [Choose your node building approach](/integrations/creating-nodes/plan/choose-node-method.md)

## Prerequisites

คุณต้องติดตั้งสิ่งเหล่านี้ในเครื่องสำหรับพัฒนา:

--8<-- "_snippets/integrations/creating-nodes/prerequisites.md"

คุณควรมีความเข้าใจพื้นฐานเกี่ยวกับ:

- JavaScript/TypeScript
- REST APIs
- git
- [Expressions](/glossary.md#expression-n8n) ใน n8n

## Build your node

ในส่วนนี้ คุณจะ clone node starter repository ของ n8n และสร้าง node ที่เชื่อมต่อกับ [SendGrid](https://sendgrid.com/){:target=_blank .external-link} โดยจะสร้าง node ที่ทำงานกับฟีเจอร์เดียวของ SendGrid คือการสร้าง contact

/// note | Existing node
n8n มี SendGrid node ที่ built-in มาอยู่แล้ว เพื่อไม่ให้ชนกับ node เดิม คุณจะต้องตั้งชื่อ node ของคุณให้ต่างออกไป
///
### Step 1: Set up the project

n8n มี starter repository สำหรับพัฒนา node การใช้ starter จะช่วยให้คุณมี dependencies ที่จำเป็นครบ และมี linter ให้ด้วย

Clone repository แล้วเข้าไปใน directory:

1. [Generate a new repository](https://github.com/n8n-io/n8n-nodes-starter/generate){:target=_blank .external-link} จาก template repository
2. Clone repository ใหม่ของคุณ:
		```shell
		git clone https://github.com/<your-organization>/<your-repo-name>.git n8n-nodes-friendgrid
		cd n8n-nodes-friendgrid
		```

starter จะมีตัวอย่าง node และ credentials มาให้ ลบ directory และไฟล์เหล่านี้ออก:

* `nodes/ExampleNode`
* `nodes/HTTPBin`
* `credentials/ExampleCredentials.credentials.ts`
* `credentials/HttpBinApi.credentials.ts`

จากนั้นสร้าง directory และไฟล์เหล่านี้:

`nodes/FriendGrid`  
`nodes/FriendGrid/FriendGrid.node.json`  
`nodes/FriendGrid/FriendGrid.node.ts`  
`credentials/FriendGridApi.credentials.ts`  

ไฟล์เหล่านี้คือไฟล์หลักที่ node ทุกตัวต้องมี ดูรายละเอียดเพิ่มเติมได้ที่ [Node file structure](/integrations/creating-nodes/build/reference/node-file-structure.md)

ติดตั้ง dependencies ของโปรเจกต์:

```shell
npm i
```

### Step 2: Add an icon

เซฟโลโก้ SendGrid แบบ SVG จาก [ที่นี่](https://github.com/n8n-io/n8n/blob/master/packages/nodes-base/nodes/SendGrid/sendGrid.svg){:target=_blank .external-link} แล้วตั้งชื่อว่า `friendGrid.svg` ไว้ใน `nodes/FriendGrid/`

--8<-- "_snippets/integrations/creating-nodes/node-icons.md"

### Step 3: Define the node in the base file

node ทุกตัวต้องมี base file ดูรายละเอียด parameter ของ base file ได้ที่ [Node base file](/integrations/creating-nodes/build/reference/node-base-files/index.md)

ในตัวอย่างนี้ใช้ไฟล์ `FriendGrid.node.ts` เพื่อให้ง่ายจะใส่โค้ดทุกอย่างไว้ในไฟล์เดียว ถ้า node ซับซ้อนกว่านี้ควรแยก module ดูรายละเอียดที่ [Node file structure](/integrations/creating-nodes/build/reference/node-file-structure.md)

#### Step 3.1: Imports

เริ่มจาก import module ที่ต้องใช้:

```typescript
import {
	IExecuteFunctions,
} from 'n8n-core';

import {
	IDataObject,
	INodeExecutionData,
	INodeType,
	INodeTypeDescription,
} from 'n8n-workflow';

import {
	OptionsWithUri,
} from 'request';
```

#### Step 3.2: Create the main class

node ต้อง export interface ที่ implements `INodeType` ซึ่งต้องมี `description` interface และ `properties` array

/// note | Class names and file names
ชื่อ class กับชื่อไฟล์ต้องตรงกัน เช่น class `FriendGrid` ไฟล์ต้องชื่อ `FriendGrid.node.ts`
/// 
```typescript
export class FriendGrid implements INodeType {
	description: INodeTypeDescription = {
		// Basic node details will go here
		properties: [
			// Resources and operations will go here
		],
	};
	// The execute method will go here
	async execute(this: IExecuteFunctions): Promise<INodeExecutionData[][]> {
	}
}
```

#### Step 3.3: Add node details

node แบบ programmatic ต้องมี parameter พื้นฐาน เช่น display name และ icon เพิ่มโค้ดนี้ใน `description`:

```typescript
displayName: 'FriendGrid',
name: 'friendGrid',
icon: 'file:friendGrid.svg',
group: ['transform'],
version: 1,
description: 'Consume SendGrid API',
defaults: {
	name: 'FriendGrid',
},
inputs: ['main'],
outputs: ['main'],
credentials: [
	{
		name: 'friendGridApi',
		required: true,
	},
],
```

n8n จะใช้ property ใน `description` บางตัว เช่น `displayName`, `icon`, `description` เพื่อแสดง node ใน Editor UI

#### Step 3.4: Add the resource

resource object จะกำหนดว่า node นี้ใช้ API resource อะไร ในตัวอย่างนี้จะใช้ endpoint `/v3/marketing/contacts` ของ SendGrid ให้เพิ่ม resource object ใน `properties` array:

```typescript
{
	displayName: 'Resource',
	name: 'resource',
	type: 'options',
	options: [
		{
			name: 'Contact',
			value: 'contact',
		},
	],
	default: 'contact',
	noDataExpression: true,
	required: true,
	description: 'Create a new contact',
},
```

`type` จะกำหนดว่า UI ของ n8n จะแสดง element แบบไหน และบอก n8n ว่าควรรับข้อมูลแบบไหนจาก user `options` จะทำให้มี dropdown ให้เลือก ดูรายละเอียดที่ [Node UI elements](/integrations/creating-nodes/build/reference/ui-elements.md)

#### Step 3.5: Add operations

operations object จะกำหนดว่าสามารถทำอะไรกับ resource ได้บ้าง ปกติจะตรงกับ REST API verb (GET, POST ฯลฯ) ในตัวอย่างนี้มี operation เดียวคือ create contact และมี field ที่ต้องกรอกคือ email

เพิ่มโค้ดนี้ใน `properties` array หลัง resource object:

```typescript
{
	displayName: 'Operation',
	name: 'operation',
	type: 'options',
	displayOptions: {
		show: {
			resource: [
				'contact',
			],
		},
	},
	options: [
		{
			name: 'Create',
			value: 'create',
			description: 'Create a contact',
			action: 'Create a contact',
		},
	],
	default: 'create',
	noDataExpression: true,
},
{
	displayName: 'Email',
	name: 'email',
	type: 'string',
	required: true,
	displayOptions: {
		show: {
			operation: [
				'create',
			],
			resource: [
				'contact',
			],
		},
	},
	default:'',
	placeholder: 'name@email.com',
	description:'Primary email for the contact',
},
```

#### Step 3.6: Add optional fields

API ส่วนใหญ่รวมถึง SendGrid API จะมี field เสริมที่ไม่บังคับ เพื่อให้ user ไม่งง n8n จะซ่อน field เหล่านี้ไว้ใน **Additional Fields** ใน UI

ในตัวอย่างนี้จะเพิ่ม field สำหรับกรอกชื่อและนามสกุล contact เพิ่มโค้ดนี้ใน properties array:

```typescript
{
	displayName: 'Additional Fields',
	name: 'additionalFields',
	type: 'collection',
	placeholder: 'Add Field',
	default: {},
	displayOptions: {
		show: {
			resource: [
				'contact',
			],
			operation: [
				'create',
			],
		},
	},
	options: [
		{
			displayName: 'First Name',
			name: 'firstName',
			type: 'string',
			default: '',
		},
		{
			displayName: 'Last Name',
			name: 'lastName',
			type: 'string',
			default: '',
		},
	],
},
```

### Step 4: Add the execute method

ตอนนี้ตั้งค่า UI และข้อมูลพื้นฐานของ node เสร็จแล้ว ต่อไปจะ map UI กับ API request และทำให้ node ทำงานจริง

`execute` method จะรันทุกครั้งที่ node ทำงาน ใน method นี้คุณจะเข้าถึง input items และ parameter ที่ user กำหนดใน UI รวมถึง credentials

เพิ่มโค้ดนี้ใน `execute` method ใน `FriendGrid.node.ts`:

```typescript
// Handle data coming from previous nodes
const items = this.getInputData();
let responseData;
const returnData = [];
const resource = this.getNodeParameter('resource', 0) as string;
const operation = this.getNodeParameter('operation', 0) as string;

// For each item, make an API call to create a contact
for (let i = 0; i < items.length; i++) {
	if (resource === 'contact') {
		if (operation === 'create') {
			// Get email input
			const email = this.getNodeParameter('email', i) as string;
			// Get additional fields input
			const additionalFields = this.getNodeParameter('additionalFields', i) as IDataObject;
			const data: IDataObject = {
				email,
			};

			Object.assign(data, additionalFields);

			// Make HTTP request according to https://sendgrid.com/docs/api-reference/
			const options: OptionsWithUri = {
				headers: {
					'Accept': 'application/json',
				},
				method: 'PUT',
				body: {
					contacts: [
						data,
					],
				},
				uri: `https://api.sendgrid.com/v3/marketing/contacts`,
				json: true,
			};
			responseData = await this.helpers.requestWithAuthentication.call(this, 'friendGridApi', options);
			returnData.push(responseData);
		}
	}
}
// Map data to n8n data structure
return [this.helpers.returnJsonArray(returnData)];
```

สังเกตบรรทัดนี้:

```typescript
const items = this.getInputData();
... 
for (let i = 0; i < items.length; i++) {
	...
	const email = this.getNodeParameter('email', i) as string;
	...
}
```

user สามารถกรอกข้อมูลได้ 2 ทาง:

* กรอกตรงๆ ใน field ของ node
* map ข้อมูลจาก node ก่อนหน้าใน workflow

`getInputData()` และ loop นี้จะช่วยให้ node รองรับกรณีที่ข้อมูลมาจาก node ก่อนหน้า เช่น ถ้า node ก่อนหน้าส่ง contact มา 5 คน node FriendGrid ก็จะสร้าง contact 5 คน

### Step 5: Set up authentication

SendGrid API ต้องใช้ API key ในการ auth

เพิ่มโค้ดนี้ใน `FriendGridApi.credentials.ts`

```typescript
import {
	IAuthenticateGeneric,
	ICredentialTestRequest,
	ICredentialType,
	INodeProperties,
} from 'n8n-workflow';

export class FriendGridApi implements ICredentialType {
	name = 'friendGridApi';
	displayName = 'FriendGrid API';
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
			headers: {
				Authorization: '=Bearer {{$credentials.apiKey}}',
			},
		},
	};

	test: ICredentialTestRequest = {
		request: {
			baseURL: 'https://api.sendgrid.com/v3',
			url: '/marketing/contacts',
		},
	};
}

```

ดูรายละเอียดเกี่ยวกับ credentials file และ options ได้ที่ [Credentials file](/integrations/creating-nodes/build/reference/credentials-files.md)

### Step 6: Add node metadata

metadata ของ node จะอยู่ในไฟล์ JSON ที่ root ของ node n8n เรียกไฟล์นี้ว่า codex file ในตัวอย่างนี้คือ `FriendGrid.node.json`

เพิ่มโค้ดนี้ในไฟล์ JSON:

```json
{
	"node": "n8n-nodes-base.FriendGrid",
	"nodeVersion": "1.0",
	"codexVersion": "1.0",
	"categories": [
		"Miscellaneous"
	],
	"resources": {
		"credentialDocumentation": [
			{
				"url": ""
			}
		],
		"primaryDocumentation": [
			{
				"url": ""
			}
		]
	}
}
```

ดูรายละเอียด parameter เหล่านี้ได้ที่ [Node codex files](/integrations/creating-nodes/build/reference/node-codex-files.md)

### Step 7: Update the npm package details

รายละเอียด npm package จะอยู่ใน `package.json` ที่ root ของโปรเจกต์ ต้องใส่ object `n8n` ที่ลิงก์ไปยัง credentials และ base node file อัปเดตไฟล์นี้ให้มีข้อมูลแบบนี้:

```json
{
	// All node names must start with "n8n-nodes-"
	"name": "n8n-nodes-friendgrid",
	"version": "0.1.0",
	"description": "n8n node to create contacts in SendGrid",
	"keywords": [
		// This keyword is required for community nodes
		"n8n-community-node-package"
	],
	"license": "MIT",
	"homepage": "https://n8n.io",
	"author": {
		"name": "Test",
		"email": "test@example.com"
	},
	"repository": {
		"type": "git",
		// Change the git remote to your own repository
		// Add the new URL here
		"url": "git+<your-repo-url>"
	},
	"main": "index.js",
	"scripts": {
		// don't change
	},
	"files": [
		"dist"
	],
	// Link the credentials and node
	"n8n": {
		"n8nNodesApiVersion": 1,
		"credentials": [
			"dist/credentials/FriendGridApi.credentials.js"
		],
		"nodes": [
			"dist/nodes/FriendGrid/FriendGrid.node.js"
		]
	},
	"devDependencies": {
		// don't change
	},
	"peerDependencies": {
		// don't change
	}
}
```

คุณต้องอัปเดต `package.json` ให้มีข้อมูลของคุณเอง เช่น ชื่อและ repository URL ดูรายละเอียดเพิ่มเติมเกี่ยวกับไฟล์ `package.json` ได้ที่ [npm's package.json documentation](https://docs.npmjs.com/cli/v8/configuring-npm/package-json){:target=_blank .external-link}

## Test your node

--8<-- "_snippets/integrations/creating-nodes/testing.md"

## Next steps

* [Deploy your node](/integrations/creating-nodes/deploy/index.md)
* ดูตัวอย่าง programmatic node: n8n's [Mattermost node](https://github.com/n8n-io/n8n/tree/master/packages/nodes-base/nodes/Mattermost){:target=_blank .external-link} ตัวอย่างนี้เป็น node แบบ programmatic ที่ซับซ้อนขึ้น
* ศึกษาเรื่อง [node versioning](/integrations/creating-nodes/build/reference/node-versioning.md)
* ทำความเข้าใจ concept สำคัญ: [item linking](/data/data-mapping/data-item-linking/item-linking-concepts.md) และ [data structures](/data/data-structure.md)
