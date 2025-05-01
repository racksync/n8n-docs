---
#https://www.notion.so/n8n/Frontmatter-432c2b8dff1f43d4b1c8d20075510fe4
title: Programmatic-style parameters
description: A reference document listing the programmatic-style parameters of the node base file.
contentType: reference
---

# Programmatic-style parameters

นี่คือ parameters ที่ใช้ได้กับ [node base file](/integrations/creating-nodes/build/reference/node-base-files/index.md) ของ programmatic-style nodes

เอกสารนี้จะมีโค้ดตัวอย่างสั้น ๆ เพื่อช่วยให้เข้าใจโครงสร้างและแนวคิด ถ้าต้องการดูตัวอย่างจริงแบบเต็ม ๆ ดูที่ [Build a programmatic-style node](/integrations/creating-nodes/build/programmatic-style-node.md)

node แบบ programmatic-style จะต้องมี method `execute()` ด้วย ดูรายละเอียดเพิ่มเติมที่ [Programmatic-style execute method](/integrations/creating-nodes/build/reference/node-base-files/programmatic-style-execute-method.md)

ดู parameters ที่ใช้ได้กับ node ทุกประเภทได้ที่ [Standard parameters](/integrations/creating-nodes/build/reference/node-base-files/standard-parameters.md)

## `defaultVersion`

_Number_ | _Optional_

ใช้ `defaultVersion` เมื่อใช้วิธี versioning แบบเต็ม

n8n รองรับ 2 วิธีการ versioning ดูรายละเอียดที่ [Node versioning](/integrations/creating-nodes/build/reference/node-versioning.md)

## `methods` and `loadOptions`

_Object_ | _Optional_

object นี้จะมี method `loadOptions` สำหรับ programmatic-style node สามารถใช้ method นี้เพื่อ query ข้อมูลจาก service เช่นดึงค่าต่าง ๆ ที่ user มี แล้วแสดงใน GUI ให้ user เลือกใช้ใน query ต่อไป

ตัวอย่างเช่น [Gmail node ของ n8n](https://github.com/n8n-io/n8n/blob/master/packages/nodes-base/nodes/Google/Gmail/Gmail.node.ts) ใช้ `loadOptions` เพื่อดึง labels ทั้งหมด:

```js
	methods = {
		loadOptions: {
			// Get all the labels and display them
			async getLabels(
				this: ILoadOptionsFunctions,
			): Promise<INodePropertyOptions[]> {
				const returnData: INodePropertyOptions[] = [];
				const labels = await googleApiRequestAllItems.call(
					this,
					'labels',
					'GET',
					'/gmail/v1/users/me/labels',
				);
				for (const label of labels) {
					const labelName = label.name;
					const labelId = label.id;
					returnData.push({
						name: labelName,
						value: labelId,
					});
				}
				return returnData;
			},
		},
	};
```

## `version`

_Number_ หรือ _Array_ | _Optional_

ถ้ามีแค่ 1 version ของ node ให้ใช้เป็นตัวเลขเดียว ถ้าต้องการรองรับหลาย version ให้ใช้ array ที่มีเลข version แต่ละอัน

n8n รองรับ 2 วิธีการ versioning node แบบ programmatic-style ใช้ได้ทั้งสองแบบ ดูรายละเอียดที่ [Node versioning](/integrations/creating-nodes/build/reference/node-versioning.md)

