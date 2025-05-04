---
#https://www.notion.so/n8n/Frontmatter-432c2b8dff1f43d4b1c8d20075510fe4
title: ข้อมูล Binary
description: ทำความเข้าใจและใช้ข้อมูล binary ใน n8n
contentType: overview
tags:
  - binary data
hide:
  - tags
---

# Binary data

Binary data คือข้อมูลประเภทไฟล์ใดๆ เช่น ไฟล์รูปภาพ หรือเอกสาร รวบรวมแหล่งข้อมูลที่เกี่ยวข้องกับ binary data ใน n8n

## Working with binary data in your workflows

คุณสามารถประมวลผล binary data ใน n8n workflows ได้ n8n มี nodes ที่ช่วยให้คุณทำงานกับ binary data คุณยังสามารถใช้ code ได้อีกด้วย

### Nodes

มี nodes หลักสามตัวที่ใช้สำหรับจัดการไฟล์ binary data โดยเฉพาะ:

- [Read/Write Files from Disk](/integrations/builtin/core-nodes/n8n-nodes-base.readwritefile.md) เพื่ออ่านและเขียนไฟล์จาก/ไปยังเครื่องที่ n8n กำลังทำงานอยู่
- [Convert to File](/integrations/builtin/core-nodes/n8n-nodes-base.converttofile.md) เพื่อรับ input data และส่งออกเป็นไฟล์
- [Extract From File](/integrations/builtin/core-nodes/n8n-nodes-base.extractfromfile.md) เพื่อดึงข้อมูลจากรูปแบบ binary และแปลงเป็น JSON

มี nodes แยกต่างหากสำหรับทำงานกับข้อมูล XML และ HTML:

* [HTML](/integrations/builtin/core-nodes/n8n-nodes-base.html.md)
* [XML](/integrations/builtin/core-nodes/n8n-nodes-base.xml.md)

และ nodes สำหรับทำงานทั่วไป:

* [Compression](/integrations/builtin/core-nodes/n8n-nodes-base.compression.md)
* [Edit Image](/integrations/builtin/core-nodes/n8n-nodes-base.editimage.md)
* [FTP](/integrations/builtin/core-nodes/n8n-nodes-base.ftp.md)

คุณสามารถ trigger workflow ตามการเปลี่ยนแปลงของไฟล์ในเครื่องโดยใช้ [Local File trigger](/integrations/builtin/core-nodes/n8n-nodes-base.localfiletrigger.md)

หากต้องการแยกหรือเชื่อมต่อ binary data items ให้ใช้ [data transformation nodes](/data/index.md#data-transformation-nodes)

### Code

คุณสามารถใช้ [Code node](/code/code-node.md) เพื่อจัดการ binary data ใน workflows ของคุณ ตัวอย่างเช่น [Get the binary data buffer](/code/cookbook/code-node/get-binary-data-buffer.md): ดึงข้อมูล binary data ที่มีอยู่ใน workflow ของคุณ


## Configure binary data mode when self-hosting

คุณสามารถกำหนดค่าว่า n8n instance ที่ self-host ของคุณจัดการ binary data อย่างไรโดยใช้ [Binary data environment variables](/hosting/configuration/environment-variables/binary-data.md) ซึ่งรวมถึงงานต่างๆ เช่น การตั้งค่าเส้นทางการจัดเก็บ และการเลือกวิธีการจัดเก็บ binary data

การกำหนดค่าของคุณมีผลต่อความสามารถในการ scale ของ n8n: [Scaling | Binary data filesystem mode](/hosting/scaling/binary-data.md)

การอ่านและเขียนไฟล์ binary อาจมีผลกระทบด้านความปลอดภัย หากคุณต้องการปิดใช้งานการอ่านและเขียน binary data ให้ใช้ environment variable `NODES_EXCLUDE` อ้างอิงถึง [Environment variables | Nodes](/hosting/configuration/environment-variables/nodes.md) สำหรับข้อมูลเพิ่มเติม
