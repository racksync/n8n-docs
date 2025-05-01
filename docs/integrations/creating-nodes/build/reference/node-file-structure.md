---
#https://www.notion.so/n8n/Frontmatter-432c2b8dff1f43d4b1c8d20075510fe4
contentType: explanation
---

# Node file structure

การจัดโครงสร้างไฟล์และ directory ของ node ให้เป็นไปตาม best practices และมาตรฐาน จะช่วยให้ node ของคุณดูแลรักษาง่ายขึ้น และสะดวกถ้ามีคนอื่นต้องมาทำงานกับ code ของคุณ

โครงสร้างไฟล์และ directory ของ node จะขึ้นอยู่กับ:

* ความซับซ้อนของ node ของคุณ
* ว่าคุณใช้ node versioning หรือไม่
* จำนวน node ที่คุณรวมไว้ใน npm package

## Required files and directories

node ของคุณต้องมีไฟล์และ directory เหล่านี้:

* ไฟล์ `package.json` ที่ root ของโปรเจกต์ อันนี้จำเป็นสำหรับทุก npm module
* directory `nodes` ที่เก็บ code ของ node:
    * directory นี้ต้องมี [base file](/integrations/creating-nodes/build/reference/node-base-files/index.md) โดยใช้รูปแบบ `<node-name>.node.ts` เช่น `MyNode.node.ts`
    * n8n แนะนำให้มี [codex file](/integrations/creating-nodes/build/reference/node-codex-files.md) ซึ่งเก็บ metadata ของ node โดยชื่อไฟล์ codex ต้องตรงกับชื่อไฟล์ base เช่น ถ้า base file ชื่อ `MyNode.node.ts` codex file ก็ต้องชื่อ `MyNode.node.json`
    * directory `nodes` สามารถมีไฟล์และ subdirectory อื่นๆ ได้ เช่น directory สำหรับ version ต่างๆ หรือแยก code node ออกเป็นหลายไฟล์เพื่อให้โครงสร้าง modular มากขึ้น
* directory `credentials` สำหรับเก็บ code credentials ของคุณ โดย code นี้จะอยู่ใน [credentials file](/integrations/creating-nodes/build/reference/credentials-files.md) ไฟล์เดียว โดยใช้ชื่อไฟล์ `<node-name>.credentials.ts` เช่น `MyNode.credentials.ts`

## Modular structure
<!-- vale off -->
คุณสามารถเลือกได้ว่าจะใส่ฟังก์ชันทั้งหมดของ node ไว้ในไฟล์เดียว หรือจะแยกออกเป็น base file และ module อื่นๆ แล้วให้ base file import เข้ามา ถ้า node ของคุณไม่ได้เรียบง่ายมาก n8n แนะนำให้แยกออกเป็นหลายไฟล์จะดีกว่า
<!-- vale on -->

รูปแบบพื้นฐานคือแยก operation ออกไปดูตัวอย่างได้ที่ [HttpBin starter node](https://github.com/n8n-io/n8n-nodes-starter/tree/master/nodes/HttpBin){:target=_blank .external-link}

ถ้า node ของคุณซับซ้อนมากขึ้น n8n แนะนำให้ใช้โครงสร้าง directory แบบนี้ ดูตัวอย่างได้ที่ [Airtable node](https://github.com/n8n-io/n8n/tree/master/packages/nodes-base/nodes/Airtable){:target=_blank .external-class} หรือ [Microsoft Outlook node](https://github.com/n8n-io/n8n/tree/master/packages/nodes-base/nodes/Microsoft/Outlook){:target=_blank .external-link}

  * `actions`: directory ที่เก็บ sub-directory สำหรับแต่ละ resource
    * แต่ละ sub-directory ควรมีไฟล์สองประเภท:
      * ไฟล์ index ที่มี resource description (ชื่อไฟล์เป็น `<resourceName>.resource.ts` หรือ `index.ts`)
      * ไฟล์ operation `<operationName>.operation.ts` โดยแต่ละไฟล์ควร export สองอย่างคือ `description` ของ operation และฟังก์ชัน `execute`
  * `methods`: directory เสริมสำหรับฟังก์ชัน dynamic parameters  
  * `transport`: directory ที่เก็บ implementation สำหรับการสื่อสารกับ service

## Versioning

ถ้า node ของคุณมีมากกว่าหนึ่งเวอร์ชัน และคุณใช้ full versioning โครงสร้างไฟล์จะซับซ้อนขึ้น คุณต้องมี directory สำหรับแต่ละเวอร์ชัน พร้อม base file ที่กำหนด default version ดูรายละเอียดเพิ่มเติมได้ที่ [Node versioning](/integrations/creating-nodes/build/reference/node-versioning.md)

## Decide how many nodes to include in a package

เวลาสร้าง node มีสองแบบให้เลือก:

* หนึ่ง node ต่อหนึ่ง npm package
* หลาย node ใน npm package เดียว

n8n รองรับทั้งสองแบบ ถ้าคุณรวมหลาย node ใน package เดียว แต่ละ node ควรมี directory ของตัวเองใน `nodes`

## A best-practice example for programmatic nodes

[Airtable node](https://github.com/n8n-io/n8n/tree/master/packages/nodes-base/nodes/Airtable){:target=_blank .external-class} ที่มากับ n8n ใช้โครงสร้าง modular และ versioning ตาม pattern ที่แนะนำ


