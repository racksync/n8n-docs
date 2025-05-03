---
#https://www.notion.so/n8n/Frontmatter-432c2b8dff1f43d4b1c8d20075510fe4
title: Custom API Operations
description: วิธีใช้ HTTP Request node กับ predefined credentials
contentType: explanation
---

# Custom API operations

--8<-- "_snippets/integrations/credential-only-intro.md"

## Predefined credential types

Predefined credential type คือ credential ที่มีอยู่แล้วใน n8n คุณสามารถใช้ predefined credential type แทน generic credentials ใน HTTP Request node ได้

ตัวอย่างเช่น: คุณสร้าง Asana credential สำหรับใช้กับ Asana node ต่อมา คุณอยากใช้งาน API ของ Asana ใน operation ที่ node ยังไม่รองรับ คุณก็สามารถใช้ Asana credential เดิมใน HTTP Request node ได้เลย โดยไม่ต้องตั้งค่าการ authentication เพิ่มเติม

### Using predefined credential types

--8<-- "_snippets/integrations/predefined-credential-type-how-to.md"

### Credential scopes

credential type บางตัวจะมี scope เฉพาะ คือ endpoint ที่ credential นั้นใช้ได้ n8n จะแจ้งเตือนคุณเมื่อเลือก credential type เหล่านี้

ตัวอย่างเช่น ทำตามขั้นตอนใน [Using predefined credential types](#using-predefined-credential-types) แล้วเลือก **Google Calendar OAuth2 API** เป็น **Credential Type** n8n จะแสดงกล่องที่มี endpoint สองตัวที่ credential นี้ใช้ได้:

![The scopes box](/_images/integrations/custom-operations/scopes.png)

