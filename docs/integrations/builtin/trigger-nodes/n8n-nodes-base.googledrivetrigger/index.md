---
#https://www.notion.so/n8n/Frontmatter-432c2b8dff1f43d4b1c8d20075510fe4
title: Google Drive Trigger node documentation
description: Learn how to use the Google Drive Trigger node in n8n. Follow technical documentation to integrate Google Drive Trigger node into your workflows.
contentType: [integration, reference]
priority: medium
---

# Google Drive Trigger node

[Google Drive](https://drive.google.com){:target=_blank .external-link} คือบริการเก็บไฟล์และ sync ไฟล์ของ Google ให้ผู้ใช้เก็บไฟล์บน server, sync ไฟล์ข้ามอุปกรณ์ และแชร์ไฟล์ได้

/// note | Credentials
คุณสามารถดูข้อมูลเกี่ยวกับการตั้งค่า credentials สำหรับ node นี้ได้ [ที่นี่](/integrations/builtin/credentials/google/index.md)
///

///  note  | Examples and templates
สำหรับตัวอย่างการใช้งานและ template ที่จะช่วยให้คุณเริ่มต้นได้ง่ายขึ้น ดูได้ที่หน้า [Google Drive Trigger integrations](https://n8n.io/integrations/google-drive-trigger/){:target=_blank .external-link} ของ n8n
///

/// note | Manual Executions vs. Activation
ถ้า run แบบ manual node นี้จะคืน event ล่าสุดที่ตรงกับ search criteria ถ้าไม่มี event ตรง (เช่นดูไฟล์ที่ถูกสร้างแต่ยังไม่มีไฟล์ใหม่) จะ error ทันที แต่ถ้า save และ activate node จะเช็ค event ที่ตรงกับ criteria เป็นระยะและ trigger workflow ให้ทุก event ที่เจอ
///

## Common issues

สำหรับคำถามหรือปัญหาที่พบบ่อยและวิธีแก้ไข ดูได้ที่ [Common issues](/integrations/builtin/trigger-nodes/n8n-nodes-base.googledrivetrigger/common-issues.md)
