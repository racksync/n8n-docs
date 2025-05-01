---
#https://www.notion.so/n8n/Frontmatter-432c2b8dff1f43d4b1c8d20075510fe4
title: Postgres Trigger node documentation
description: Learn how to use the Postgres Trigger node in n8n. Follow technical documentation to integrate Postgres Trigger node into your workflows.
contentType: [integration, reference]
priority: medium
---

# Postgres Trigger node

ใช้ Postgres Trigger node เพื่อตอบสนอง event ต่างๆ ใน [Postgres](https://www.postgresql.org/){:target=_blank .external-link} และเชื่อมต่อ Postgres กับแอปอื่นๆ ได้เลย n8n รองรับ event insert, update, และ delete ในตัว

/// note | Credentials
คุณสามารถดูข้อมูลเกี่ยวกับการเชื่อมต่อบัญชี (authentication) สำหรับ node นี้ได้ [ที่นี่](/integrations/builtin/credentials/postgres.md)
///

/// note | Examples and templates
ถ้าอยากดูตัวอย่างการใช้งานหรือ template สำหรับเริ่มต้น ลองดูที่หน้า [Postgres Trigger integrations](https://n8n.io/integrations/postgres-trigger/){:target=_blank .external-link} ของ n8n ได้เลย
///

## Events

คุณสามารถตั้งค่าได้ว่า node จะฟัง event แบบไหน

* เลือก **Listen and Create Trigger Rule** แล้วเลือก event ที่ต้องการฟัง:
	* Insert
	* Update
	* Delete
* เลือก **Listen to Channel** แล้วใส่ชื่อ channel ที่ node ควร monitor

## Related resources

n8n มี app node สำหรับ Postgres ด้วยนะ ดูเอกสาร node ได้ [ที่นี่](/integrations/builtin/app-nodes/n8n-nodes-base.postgres/index.md)

ดู [example workflows และเนื้อหาอื่นๆ ที่เกี่ยวข้อง](https://n8n.io/integrations/postgres-trigger/){:target=_blank .external-link} ได้ที่เว็บไซต์ n8n
