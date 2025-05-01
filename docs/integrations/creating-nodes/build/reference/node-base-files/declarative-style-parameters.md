---
#https://www.notion.so/n8n/Frontmatter-432c2b8dff1f43d4b1c8d20075510fe4
title: Declarative-style parameters
description: A reference document listing the declarative-style parameters of the node base file.
contentType: reference
---

# Declarative-style parameters

นี่คือ parameters ที่ใช้ได้กับ [node base file](/integrations/creating-nodes/build/reference/node-base-files/index.md) ของ declarative-style nodes

เอกสารนี้จะมีโค้ดตัวอย่างสั้น ๆ เพื่อช่วยให้เข้าใจโครงสร้างและแนวคิด ถ้าต้องการดูตัวอย่างจริงแบบเต็ม ๆ ดูที่ [Build a declarative-style node](/integrations/creating-nodes/build/declarative-style-node.md)

ดู parameters ที่ใช้ได้กับ node ทุกประเภทได้ที่ [Standard parameters](/integrations/creating-nodes/build/reference/node-base-files/standard-parameters.md)

## `methods` and `loadOptions`

_Object_ | _Optional_

`methods` จะมี object `loadOptions` อยู่ข้างใน สามารถใช้ `loadOptions` เพื่อ query ข้อมูลจาก service เช่นดึงค่าต่าง ๆ ที่ user มี แล้วแสดงใน GUI ให้ user เลือกใช้ใน query ต่อไป object นี้ต้องมี routing สำหรับวิธี query service และ output สำหรับจัดการข้อมูลที่ได้ เช่น

```js
methods : {
	loadOptions: {
		routing: {
			request: {
				url: '/webhook/example-option-parameters',
				method: 'GET',
			},
			output: {
				postReceive: [
					{
							// ถ้าข้อมูลที่ได้ซ้อนอยู่ใน property อื่น
							// ให้ระบุ key ของ property นั้น
							type: 'rootProperty',
							properties: {
								property: 'responseData',
							},
					},
					{
						type: 'setKeyValue',
						properties: {
							name: '={{$responseItem.key}} ({{$responseItem.value}})',
							value: '={{$responseItem.value}}',
						},
					},
					{
							// ถ้าข้อมูลที่ได้เป็น array ของ object ให้ sort ตาม key
							type: 'sort',
							properties: {
								key: 'name',
							},
					},
				],
			},
		},
	}
},
```

## `routing`

_Object_ | _Required_

`routing` เป็น object ที่ใช้ใน array `options` ของ operations และ input field objects จะเก็บรายละเอียดของ API call

ตัวอย่างโค้ดด้านล่างมาจาก [Declarative-style tutorial](/integrations/creating-nodes/build/declarative-style-node.md) เป็นการตั้งค่า integration กับ NASA API แสดงวิธีใช้ `requestDefaults` สำหรับตั้งค่าพื้นฐานของ API call และใช้ `routing` สำหรับแต่ละ operation

```js
description: INodeTypeDescription = {
  // Other node info here
  requestDefaults: {
			baseURL: 'https://api.nasa.gov',
			url: '',
			headers: {
				Accept: 'application/json',
				'Content-Type': 'application/json',
			},
		},
    properties: [
      // Resources here
      {
        displayName: 'Operation'
        // Other operation details
        options: [
          {
            name: 'Get'
            value: 'get',
            description: '',
            routing: {
              request: {
                method: 'GET',
                url: '/planetary/apod'
              }
            }
          }
        ]
      }
    ]
}
```

<!--

TODO: more info on the routing object
### routing.output

include postReceive actions, including ability to dynamically disable - see DOC-400

### routing.request

### routing.send

-->

## `version`

_Number_ หรือ _Array_ | _Optional_

ถ้ามีแค่ 1 version ของ node ให้ใช้เป็นตัวเลขเดียว ถ้าต้องการรองรับหลาย version ให้ใช้ array ที่มีเลข version แต่ละอัน

n8n รองรับ 2 วิธีการ versioning แต่ declarative-style node ต้องใช้แบบ light versioning เท่านั้น ดูรายละเอียดที่ [Node versioning](/integrations/creating-nodes/build/reference/node-versioning.md)
