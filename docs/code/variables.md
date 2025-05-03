---
#https://www.notion.so/n8n/Frontmatter-432c2b8dff1f43d4b1c8d20075510fe4

title: Custom variables
description: Custom variables ช่วยให้คุณจัดเก็บและนำค่ากลับมาใช้ซ้ำใน n8n workflows
contentType: howto
---

# Custom variables

/// info | Feature availability
* Available on Self-hosted Enterprise and Pro Cloud plans.
* คุณต้องมีสิทธิ์เข้าถึงบัญชี owner ของ n8n instance เพื่อสร้างและแก้ไข variables ผู้ใช้ทุกคนสามารถใช้ variables ที่มีอยู่ได้

Available in version 0.225.0 and above.
///	

Custom variables เป็นตัวแปรแบบอ่านอย่างเดียว (read-only) ที่คุณสามารถใช้เพื่อจัดเก็บและนำค่ากลับมาใช้ซ้ำใน n8n workflows

/// warning | Variables are shared
เมื่อคุณสร้าง variable มันจะพร้อมใช้งานสำหรับทุกคนใน n8n instance ของคุณ
///

## Create variables

วิธีสร้าง variable ใหม่:

1.  ในหน้า **Variables** เลือก **Add Variable**
2.  ป้อน **Key** และ **Value** ความยาวสูงสุดของ key คือ 50 ตัวอักษร และความยาวสูงสุดของ value คือ 220 ตัวอักษร n8n จำกัดตัวอักษรที่คุณสามารถใช้ใน key และ value ให้เป็นตัวอักษรภาษาอังกฤษพิมพ์เล็กและพิมพ์ใหญ่, ตัวเลข, และเครื่องหมายขีดล่าง (`A-Z`, `a-z`, `0-9`, `_`)
3.  เลือก **Save** ตอนนี้ variable พร้อมใช้งานใน workflows ทั้งหมดใน n8n instance แล้ว

## Edit and delete variables

วิธีแก้ไขหรือลบ variable:

1.  ในหน้า **Variables** เลื่อนเมาส์ไปเหนือ variable ที่คุณต้องการเปลี่ยนแปลง
2.  เลือก **Edit** หรือ **Delete**

## Use variables in workflows

คุณสามารถเข้าถึง variables ใน Code node และใน [expressions](/glossary.md#expression-n8n):

```javascript
// Access a variable
$vars.<variable-name>
```

Variables ทั้งหมดเป็นสตริง (strings)

ระหว่างการทำงานของ workflow, n8n จะแทนที่ variables ด้วยค่าของ variable นั้น หาก variable ไม่มีค่า n8n จะถือว่าค่าของมันเป็น `undefined` Workflows จะไม่ล้มเหลวโดยอัตโนมัติในกรณีนี้

Variables เป็นแบบอ่านอย่างเดียว (read-only) คุณต้องใช้ UI เพื่อเปลี่ยนค่า หากคุณต้องการตั้งค่าและเข้าถึงข้อมูลที่กำหนดเองภายใน workflow ของคุณ ให้ใช้ [Workflow static data](/code/cookbook/builtin/get-workflow-static-data.md)
