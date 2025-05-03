---
#https://www.notion.so/n8n/Frontmatter-432c2b8dff1f43d4b1c8d20075510fe4
title: สร้าง Node แบบ Declarative-style
description: Tutorial สร้าง node แบบ declarative-style
contentType: tutorial
---

# Build a declarative-style node

tutorial นี้จะพาไปดูวิธีสร้าง node แบบ declarative-style ก่อนเริ่ม แนะนำให้แน่ใจว่านี่คือ style ที่คุณต้องการใช้ ดูรายละเอียดเพิ่มเติมได้ที่ [Choose your node building approach](/integrations/creating-nodes/plan/choose-node-method.md)

## Prerequisites

คุณต้องติดตั้งสิ่งเหล่านี้ในเครื่องสำหรับพัฒนา:

--8<-- "_snippets/integrations/creating-nodes/prerequisites.md"

คุณควรมีความเข้าใจพื้นฐานเกี่ยวกับ:

- JavaScript/TypeScript
- REST APIs
- git

## Build your node

ในส่วนนี้ คุณจะ clone node starter repository ของ n8n และสร้าง node ที่เชื่อมต่อกับ [NASA API](https://api.nasa.gov/){:target=_blank .external-link} โดยจะสร้าง node ที่ใช้บริการของ NASA สองตัวคือ APOD (Astronomy Picture of the Day) และ Mars Rover Photos เพื่อให้ตัวอย่างโค้ดสั้น node นี้จะไม่ได้ implement ทุก option ของ Mars Rover Photos endpoint

/// note | Existing node
n8n มี NASA node ที่ built-in มาอยู่แล้ว เพื่อไม่ให้ชนกับ node เดิม คุณจะต้องตั้งชื่อ node ของคุณให้ต่างออกไป
///
### Step 1: Set up the project

n8n มี starter repository สำหรับพัฒนา node การใช้ starter จะช่วยให้คุณมี dependencies ที่จำเป็นครบ และมี linter ให้ด้วย

Clone repository แล้วเข้าไปใน directory:

1. [Generate a new repository](https://github.com/n8n-io/n8n-nodes-starter/generate) จาก template repository
2. Clone repository ใหม่ของคุณ:
		```shell
		git clone https://github.com/<your-organization>/<your-repo-name>.git n8n-nodes-nasa-pics
		cd n8n-nodes-nasa-pics
		```

starter จะมีตัวอย่าง node และ credentials มาให้ ลบ directory และไฟล์เหล่านี้ออก:

* `nodes/ExampleNode`
* `nodes/HTTPBin`
* `credentials/ExampleCredentials.credentials.ts`
* `credentials/HttpBinApi.credentials.ts`

จากนั้นสร้าง directory และไฟล์เหล่านี้:

`nodes/NasaPics`  
`nodes/NasaPics/NasaPics.node.json`  
`nodes/NasaPics/NasaPics.node.ts`  
`credentials/NasaPicsApi.credentials.ts`  

ไฟล์เหล่านี้คือไฟล์หลักที่ node ทุกตัวต้องมี ดูรายละเอียดเพิ่มเติมได้ที่ [Node file structure](/integrations/creating-nodes/build/reference/node-file-structure.md)

ติดตั้ง dependencies ของโปรเจกต์:

```shell
npm i
```

### Step 2: Add an icon

เซฟโลโก้ NASA แบบ SVG จาก [ที่นี่](https://upload.wikimedia.org/wikipedia/commons/e/e5/NASA_logo.svg){:target=_blank .external-link} แล้วตั้งชื่อว่า `nasapics.svg` ไว้ใน `nodes/NasaPics/`

--8<-- "_snippets/integrations/creating-nodes/node-icons.md"

### Step 3: Create the node

node ทุกตัวต้องมี base file ดูรายละเอียด parameter ของ base file ได้ที่ [Node base file](/integrations/creating-nodes/build/reference/node-base-files/index.md)

ในตัวอย่างนี้ใช้ไฟล์ `NasaPics.node.ts` เพื่อให้ง่ายจะใส่โค้ดทุกอย่างไว้ในไฟล์เดียว ถ้า node ซับซ้อนกว่านี้ควรแยก module ดูรายละเอียดที่ [Node file structure](/integrations/creating-nodes/build/reference/node-file-structure.md)

#### Step 3.1: Imports

เริ่มจาก import module ที่ต้องใช้:

```typescript
import { INodeType, INodeTypeDescription } from 'n8n-workflow';
```

#### Step 3.2: Create the main class

node ต้อง export interface ที่ implements INodeType ซึ่งต้องมี `description` interface และ `properties` array

/// note | Class names and file names
ชื่อ class กับชื่อไฟล์ต้องตรงกัน เช่น class `NasaPics` ไฟล์ต้องชื่อ `NasaPics.node.ts`
/// 
```typescript
export class NasaPics implements INodeType {
	description: INodeTypeDescription = {
		// Basic node details will go here
		properties: [
		// Resources and operations will go here
		]
	};
}
```

#### Step 3.3: Add node details

node ทุกตัวต้องมี parameter พื้นฐาน เช่น display name, icon และข้อมูลพื้นฐานสำหรับ request เพิ่มโค้ดนี้ใน `description`:

```typescript
displayName: 'NASA Pics',
name: 'NasaPics',
icon: 'file:nasapics.svg',
group: ['transform'],
version: 1,
subtitle: '={{$parameter["operation"] + ": " + $parameter["resource"]}}',
description: 'Get data from NASAs API',
defaults: {
	name: 'NASA Pics',
},
inputs: ['main'],
outputs: ['main'],
credentials: [
	{
		name: 'NasaPicsApi',
		required: true,
	},
],
requestDefaults: {
	baseURL: 'https://api.nasa.gov',
	headers: {
		Accept: 'application/json',
		'Content-Type': 'application/json',
	},
},
```

n8n จะใช้ property ใน `description` บางตัว เช่น `displayName`, `icon`, `description`, `subtitle` เพื่อแสดง node ใน Editor UI

#### Step 3.4: Add resources

resource object จะกำหนดว่า node นี้ใช้ API resource อะไร ในตัวอย่างนี้จะใช้ endpoint `planetary/apod` และ `mars-photos` ของ NASA ให้เพิ่ม resource options สองตัวใน `NasaPics.node.ts` อัปเดต `properties` array ด้วย resource object:

```typescript
properties: [
	{
		displayName: 'Resource',
		name: 'resource',
		type: 'options',
		noDataExpression: true,
		options: [
			{
				name: 'Astronomy Picture of the Day',
				value: 'astronomyPictureOfTheDay',
			},
			{
				name: 'Mars Rover Photos',
				value: 'marsRoverPhotos',
			},
		],
		default: 'astronomyPictureOfTheDay',
	},
	// Operations will go here

]
```

`type` จะกำหนดว่า UI ของ n8n จะแสดง element แบบไหน และบอก n8n ว่าควรรับข้อมูลแบบไหนจาก user `options` จะทำให้มี dropdown ให้เลือก ดูรายละเอียดที่ [Node UI elements](/integrations/creating-nodes/build/reference/ui-elements.md)

#### Step 3.5: Add operations

operations object จะกำหนด operation ที่ใช้กับ resource ได้

ใน declarative-style node, operations object จะมี `routing` (ใน `options` array) เพื่อกำหนดรายละเอียด API call

เพิ่มโค้ดนี้ใน `properties` array หลัง resource object:

```typescript
{
	displayName: 'Operation',
	name: 'operation',
	type: 'options',
	noDataExpression: true,
	displayOptions: {
		show: {
			resource: [
				'astronomyPictureOfTheDay',
			],
		},
	},
	options: [
		{
			name: 'Get',
			value: 'get',
			action: 'Get the APOD',
			description: 'Get the Astronomy Picture of the day',
			routing: {
				request: {
					method: 'GET',
					url: '/planetary/apod',
				},
			},
		},
	],
	default: 'get',
},
{
	displayName: 'Operation',
	name: 'operation',
	type: 'options',
	noDataExpression: true,
	displayOptions: {
		show: {
			resource: [
				'marsRoverPhotos',
			],
		},
	},
	options: [
		{
			name: 'Get',
			value: 'get',
			action: 'Get Mars Rover photos',
			description: 'Get photos from the Mars Rover',
			routing: {
				request: {
					method: 'GET',
				},
			},
		},
	],
	default: 'get',
},
{
	displayName: 'Rover name',
	description: 'Choose which Mars Rover to get a photo from',
	required: true,
	name: 'roverName',
	type: 'options',
	options: [
		{name: 'Curiosity', value: 'curiosity'},
		{name: 'Opportunity', value: 'opportunity'},
		{name: 'Perseverance', value: 'perseverance'},
		{name: 'Spirit', value: 'spirit'},
	],
	routing: {
		request: {
			url: '=/mars-photos/api/v1/rovers/{{$value}}/photos',
		},
	},
	default: 'curiosity',
	displayOptions: {
		show: {
			resource: [
				'marsRoverPhotos',
			],
		},
	},
},
{
	displayName: 'Date',
	description: 'Earth date',
	required: true,
	name: 'marsRoverDate',
	type: 'dateTime',
	default:'',
	displayOptions: {
		show: {
			resource: [
				'marsRoverPhotos',
			],
		},
	},
	routing: {
		request: {
			// You've already set up the URL. qs appends the value of the field as a query string
			qs: {
				earth_date: '={{ new Date($value).toISOString().substr(0,10) }}',
			},
		},
	},
},
// Optional/additional fields will go here
```

โค้ดนี้จะสร้าง operation สองตัว: ตัวหนึ่งสำหรับดึง APOD ของวันนี้ และอีกตัวสำหรับดึงรูปจาก Mars Rover โดย object ชื่อ `roverName` จะให้ user เลือกว่าจะเอารูปจาก Rover ตัวไหน routing object ใน Mars Rover operation จะใช้ค่านี้สร้าง URL สำหรับ API call

#### Step 3.6: Optional fields

API ส่วนใหญ่รวมถึง NASA API จะมี field เสริมที่ไม่บังคับ เพื่อให้ user ไม่งง n8n จะซ่อน field เหล่านี้ไว้ใน **Additional Fields** ใน UI

ในตัวอย่างนี้จะเพิ่ม field เสริมให้ user เลือกวันที่สำหรับ APOD endpoint เพิ่มโค้ดนี้ใน properties array:

```typescript
{
	displayName: 'Additional Fields',
	name: 'additionalFields',
	type: 'collection',
	default: {},
	placeholder: 'Add Field',
	displayOptions: {
		show: {
			resource: [
				'astronomyPictureOfTheDay',
			],
			operation: [
				'get',
			],
		},
	},
	options: [
		{
			displayName: 'Date',
			name: 'apodDate',
			type: 'dateTime',
			default: '',
			routing: {
				request: {
					// You've already set up the URL. qs appends the value of the field as a query string
					qs: {
						date: '={{ new Date($value).toISOString().substr(0,10) }}',
					},
				},
			},
		},
	],									
}
```

### Step 4: Set up authentication

NASA API ต้องใช้ API key ในการ auth

เพิ่มโค้ดนี้ใน `nasaPicsApi.credentials.ts`:

```typescript
import {
	IAuthenticateGeneric,
	ICredentialType,
	INodeProperties,
} from 'n8n-workflow';

export class NasaPicsApi implements ICredentialType {
	name = 'NasaPicsApi';
	displayName = 'NASA Pics API';
	// Uses the link to this tutorial as an example
	// Replace with your own docs links when building your own nodes
	documentationUrl = 'https://docs.n8n.io/integrations/creating-nodes/build/declarative-style-node/';
	properties: INodeProperties[] = [
		{
			displayName: 'API Key',
			name: 'apiKey',
			type: 'string',
			default: '',
		},
	];
	authenticate = {
		type: 'generic',
		properties: {
			qs: {
				'api_key': '={{$credentials.apiKey}}'
			}
		},
	} as IAuthenticateGeneric;
}
```

ดูรายละเอียดเกี่ยวกับ credentials file และ options ได้ที่ [Credentials file](/integrations/creating-nodes/build/reference/credentials-files.md)

### Step 5: Add node metadata

metadata ของ node จะอยู่ในไฟล์ JSON ที่ root ของ node n8n เรียกไฟล์นี้ว่า codex file ในตัวอย่างนี้คือ `NasaPics.node.json`

เพิ่มโค้ดนี้ในไฟล์ JSON:

```json
{
	"node": "n8n-nodes-base.NasaPics",
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

### Step 6: Update the npm package details

รายละเอียด npm package จะอยู่ใน `package.json` ที่ root ของโปรเจกต์ ต้องใส่ object `n8n` ที่ลิงก์ไปยัง credentials และ base node file อัปเดตไฟล์นี้ให้มีข้อมูลแบบนี้:

```json
{
	// All node names must start with "n8n-nodes-"
	"name": "n8n-nodes-nasapics",
	"version": "0.1.0",
	"description": "n8n node to call NASA's APOD and Mars Rover Photo services.",
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
			"dist/credentials/NasaPicsApi.credentials.js"
		],
		"nodes": [
			"dist/nodes/NasaPics/NasaPics.node.js"
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
* ดูตัวอย่าง declarative node: n8n's [Brevo node](https://github.com/n8n-io/n8n/tree/master/packages/nodes-base/nodes/Brevo){:target=_blank .external-link} (main node เป็น declarative, trigger node เป็น programmatic)
* ศึกษาเรื่อง [node versioning](/integrations/creating-nodes/build/reference/node-versioning.md)

