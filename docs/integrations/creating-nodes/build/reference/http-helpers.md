---
#https://www.notion.so/n8n/Frontmatter-432c2b8dff1f43d4b1c8d20075510fe4
contentType: reference
---

# HTTP request helper for node builders

n8n มี helper สำหรับการทำ HTTP request ที่ยืดหยุ่นและช่วยลดความซับซ้อน

/// note | Programmatic style only
ข้อมูลในเอกสารนี้ใช้กับ node ที่สร้างแบบ programmatic เท่านั้น ไม่ใช้กับ declarative style node
///
## Usage

เรียก helper นี้ในฟังก์ชัน `execute` 

```typescript
// ถ้าไม่ต้องการ auth
const response = await this.helpers.httpRequest(options);

// ถ้าต้องการ auth
const response = await this.helpers.httpRequestWithAuthentication.call(
	this, 
	'credentialTypeName', // เช่น pipedriveApi
	options,
);
```

`options` เป็น object:

```typescript
{
	url: string;
	headers?: object;
	method?: 'GET' | 'POST' | 'PUT' | 'DELETE' | 'HEAD';
	body?: FormData | Array | string | number | object | Buffer | URLSearchParams;
	qs?: object;
	arrayFormat?: 'indices' | 'brackets' | 'repeat' | 'comma';
	auth?: {
		username: string,
		password: string,
	};
	disableFollowRedirect?: boolean;
	encoding?: 'arraybuffer' | 'blob' | 'document' | 'json' | 'text' | 'stream';
	skipSslCertificateValidation?: boolean;
	returnFullResponse?: boolean;
	proxy?: {
		host: string;
		port: string | number;
		auth?: {
			username: string;
			password: string;
		},
		protocol?: string;
	};
	timeout?: number;
	json?: boolean;
}	
```

`url` จำเป็นต้องมี ฟิลด์อื่นๆ เป็น optional method เริ่มต้นคือ `GET`

หมายเหตุเกี่ยวกับแต่ละฟิลด์:

- `body`: สามารถใช้ object ปกติสำหรับ JSON payload, buffer สำหรับ file upload, FormData สำหรับ `multipart/form-data` และ `URLSearchParams` สำหรับ `application/x-www-form-urlencoded`
- `headers`: key-value pair  
	* ถ้า `body` เป็น FormData n8n จะเพิ่ม `content-type: multipart/form-data` ให้อัตโนมัติ  
	* ถ้า `body` เป็น `URLSearchParams` n8n จะเพิ่ม `content-type: application/x-www-form-urlencoded` ให้อัตโนมัติ  
	* ถ้าต้องการ override ให้ตั้ง header `content-type` เอง
- `arrayFormat`: ถ้า query string มี array เช่น `const qs = {IDs: [15,17]}` ค่านี้จะกำหนดรูปแบบ
	* `indices` (default):  `{ a: ['b', 'c'] }` เป็น `a[0]=b&a[1]=c`  
	* `brackets`: `{ a: ['b', 'c'] }` เป็น `a[]=b&a[]=c`  
	* `repeat`: `{ a: ['b', 'c'] }` เป็น `a=b&a=c`  
	* `comma`: `{ a: ['b', 'c'] }` เป็น `a=b,c`
- `auth`: ใช้สำหรับ Basic auth ให้ใส่ `username` และ `password` n8n แนะนำให้ใช้ `helpers.httpRequestWithAuthentication(...)` แทน
- `disableFollowRedirect`: โดยปกติ n8n จะตาม redirect ถ้าไม่ต้องการให้ตั้งค่านี้เป็น true
- `skipSslCertificateValidation`: ใช้สำหรับเรียก HTTPS ที่ไม่มี certificate ที่ถูกต้อง
- `returnFullResponse`: ถ้าต้องการให้ return object ที่มีข้อมูลมากกว่า body เช่น `{body: body, headers: object, statusCode: 200, statusMessage: 'OK'}`
- `encoding`: n8n จะตรวจสอบ content type ให้อัตโนมัติ แต่สามารถระบุ `arrayBuffer` เพื่อรับ Buffer ที่สามารถอ่านและใช้งานต่อได้

## Example

ดูตัวอย่างได้ที่ [Mattermost node](https://github.com/n8n-io/n8n/blob/master/packages/nodes-base/nodes/Mattermost/v1/MattermostV1.node.ts){:target=_blank .external-link}

## Deprecation of the previous helper

helper แบบเก่าที่ใช้ `this.helpers.request(options)` และ expose ไลบรารี `request-promise` ถูกถอดออกในเวอร์ชัน 1

เพื่อให้เข้ากันได้ n8n จึงเปลี่ยนไปใช้ไลบรารี `Axios` แบบโปร่งใส

ถ้าคุณเจอปัญหา สามารถแจ้งได้ที่ [Community Forums](https://community.n8n.io/){:target=_blank .external-link} หรือ [GitHub](https://github.com/n8n-io/n8n/issues){:target=_blank .external-link}

## Migration guide to the new helper

helper ตัวใหม่ robust ขึ้น ใช้งานง่ายขึ้น และไม่ผูกกับไลบรารีใดๆ

node ใหม่ควรใช้ helper ตัวนี้ทั้งหมด และควรพิจารณา migrate node เดิมด้วย ข้อควรระวังหลักๆ:

- ต้องใช้ `url` ไม่รองรับ `uri`
- `encoding: null` ต้องเปลี่ยนเป็น `encoding: arrayBuffer`
- `rejectUnauthorized: false` ต้องเปลี่ยนเป็น `skipSslCertificateValidation: true`
- ใช้ `body` ให้ตรงกับ `content-type` header เพื่อความชัดเจน
- `resolveWithFullResponse` เปลี่ยนเป็น `returnFullResponse` และมีพฤติกรรมคล้ายกัน
