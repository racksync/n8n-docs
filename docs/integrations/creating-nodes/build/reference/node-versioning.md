---
#https://www.notion.so/n8n/Frontmatter-432c2b8dff1f43d4b1c8d20075510fe4
title: การทำเวอร์ชัน Node
description: วิธีจัดการเวอร์ชันของ node ใน n8n
contentType: howto
---

# Node versioning

n8n รองรับการทำ node versioning คุณสามารถเปลี่ยนแปลง node ที่มีอยู่โดยไม่ทำให้พฤติกรรมเดิมเสียหาย ด้วยการเพิ่มเวอร์ชันใหม่

โปรดระวังวิธีที่ n8n เลือกโหลด node version:

* ถ้าผู้ใช้สร้างและบันทึก workflow โดยใช้เวอร์ชัน 1 n8n จะยังคงใช้เวอร์ชัน 1 ใน workflow นั้น แม้ว่าคุณจะสร้างและ publish เวอร์ชัน 2 ของ node แล้วก็ตาม
* เมื่อผู้ใช้สร้าง workflow ใหม่และเลือก node n8n จะโหลด node เวอร์ชันล่าสุดเสมอ

/// note | Versioning type restricted by node style
ถ้าคุณสร้าง node แบบ declarative จะไม่สามารถใช้ full versioning ได้
///
## Light versioning

ใช้ได้กับ node ทุกประเภท

node หนึ่งตัวสามารถมีได้หลายเวอร์ชันในไฟล์เดียวกัน เหมาะสำหรับการอัปเดตเล็กๆ โดยไม่ต้อง duplicate code วิธีใช้:

1. เปลี่ยนพารามิเตอร์ `version` หลักให้เป็น array แล้วใส่หมายเลขเวอร์ชันทั้งหมด รวมถึงเวอร์ชันที่มีอยู่
2. คุณสามารถเข้าถึงพารามิเตอร์ version ด้วย `@version` ใน `displayOptions` ของ object ใดๆ (เพื่อควบคุมว่า object ไหนจะแสดงกับเวอร์ชันไหน) หรือ query version จากฟังก์ชันด้วย `const nodeVersion = this.getNode().typeVersion;`

ตัวอย่างเช่น ถ้าคุณต้องการเพิ่ม versioning ให้กับ NasaPics node จาก [Declarative node tutorial](/integrations/creating-nodes/build/declarative-style-node.md) แล้วตั้งค่า resource ให้แสดงเฉพาะในเวอร์ชัน 2 ในไฟล์ `NasaPics.node.ts`:

```js
{
    displayName: 'NASA Pics',
    name: 'NasaPics',
    icon: 'file:nasapics.svg',
    // List the available versions
    version: [1,2,3],
    // More basic parameters here
    properties: [
        // Add a resource that's only displayed for version2
        {
            displayName: 'Resource name',
            // More resource parameters
            displayOptions: {
                show: {
                    '@version': 2,
                },
            },
        },
    ],
}
```

## Full versioning

ใช้ไม่ได้กับ declarative-style nodes

ตัวอย่างดูได้ที่ [Mattermost node](https://github.com/n8n-io/n8n/tree/master/packages/nodes-base/nodes/Mattermost){:target=_blank .external-link}

สรุป full versioning:

- base node file ควร extend `NodeVersionedType` แทนที่จะเป็น `INodeType`
- base node file ควรมี description ที่รวม `defaultVersion` (ปกติเป็นเวอร์ชันล่าสุด) ข้อมูล metadata อื่นๆ เช่น name และ list ของเวอร์ชัน ไม่ควรมีฟังก์ชัน node
- n8n แนะนำให้ตั้งชื่อโฟลเดอร์เวอร์ชันเป็น `v1`, `v2` เป็นต้น


