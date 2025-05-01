---
#https://www.notion.so/n8n/Frontmatter-432c2b8dff1f43d4b1c8d20075510fe4
title: Box Trigger node documentation
description: Learn how to use the Box Trigger node in n8n. Follow technical documentation to integrate Box Trigger node into your workflows.
contentType: [integration, reference]
---

# Box Trigger node

[Box](https://www.box.com/){:target=_blank .external-link} เป็นบริษัท cloud computing ที่ให้บริการแชร์ไฟล์, ทำงานร่วมกัน และเครื่องมืออื่น ๆ สำหรับจัดการไฟล์ที่อัปโหลดไว้บน server ของ Box

/// note | Credentials
คุณสามารถดูข้อมูลการตั้งค่า authentication สำหรับ node นี้ได้ [ที่นี่](/integrations/builtin/credentials/box.md)
///

///  note  | Examples and templates
ถ้าต้องการดูตัวอย่างการใช้งานและ workflow template เพื่อเริ่มต้นใช้งาน ลองดูที่หน้า [Box Trigger integrations](https://n8n.io/integrations/box-trigger/){:target=_blank .external-link} ของ n8n ได้เลย
///

## Find your Box Target ID

วิธีหา Target ID ใน Box:

1. เปิดไฟล์หรือโฟลเดอร์ที่ต้องการ monitor
2. คัดลอก string หลัง `folder/` ใน URL ตัวอย่างเช่น `https://app.box.com/folder/12345` เลข `12345` คือ target ID
3. นำไปวางในช่อง **Target ID** ใน n8n

