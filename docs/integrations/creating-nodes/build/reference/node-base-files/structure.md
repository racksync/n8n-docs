---
#https://www.notion.so/n8n/Frontmatter-432c2b8dff1f43d4b1c8d20075510fe4
title: โครงสร้างของ Node Base File
description: เอกสารอ้างอิงเกี่ยวกับโครงสร้างพื้นฐานของ node base file
contentType: reference
---

# Structure of the node base file

ไฟล์ node base จะมีโครงสร้างหลัก ๆ ดังนี้:

1. ใส่ import statements.
2. สร้าง class สำหรับ node.
3. ใน class node ให้สร้าง object ที่ชื่อว่า `description` ซึ่งจะกำหนดรายละเอียดของ node

ถ้าเป็น node แบบ programmatic-style จะต้องมี method `execute()` ด้วย ซึ่ง method นี้จะอ่านข้อมูลที่เข้ามาและ parameters แล้วสร้าง request ขึ้นมา ส่วนแบบ declarative จะใช้ key `routing` ใน object `properties` ที่อยู่ใน `descriptions` แทน

## Outline structure for a declarative-style node

โค้ดตัวอย่างนี้เป็นโครงสร้างของ node แบบ declarative

```js
import { INodeType, INodeTypeDescription } from 'n8n-workflow';

export class ExampleNode implements INodeType {
	description: INodeTypeDescription = {
		// Basic node details here
		properties: [
			// Resources and operations here
		]
	};
}
```
ดูรายละเอียด parameters ที่ใช้ได้กับ node ทุกประเภทได้ที่ [Standard parameters](/integrations/creating-nodes/build/reference/node-base-files/standard-parameters.md) และสำหรับ parameters ที่ใช้กับ declarative-style nodes ดูที่ [Declarative-style parameters](/integrations/creating-nodes/build/reference/node-base-files/declarative-style-parameters.md)

## Outline structure for a programmatic-style node

โค้ดตัวอย่างนี้เป็นโครงสร้างของ node แบบ programmatic

```js
import { IExecuteFunctions } from 'n8n-core';
import { INodeExecutionData, INodeType, INodeTypeDescription } from 'n8n-workflow';

export class ExampleNode implements INodeType {
	description: INodeTypeDescription = {
    // Basic node details here
    properties: [
      // Resources and operations here
    ]
  };

  async execute(this: IExecuteFunctions): Promise<INodeExecutionData[][]> {
    // Process data and return
  }
};
```

ดูรายละเอียด parameters ที่ใช้ได้กับ node ทุกประเภทได้ที่ [Standard parameters](/integrations/creating-nodes/build/reference/node-base-files/standard-parameters.md) และสำหรับ programmatic-style nodes ดูที่ [Programmatic-style parameters](/integrations/creating-nodes/build/reference/node-base-files/programmatic-style-parameters.md) และ [Programmatic-style execute method](/integrations/creating-nodes/build/reference/node-base-files/programmatic-style-execute-method.md)