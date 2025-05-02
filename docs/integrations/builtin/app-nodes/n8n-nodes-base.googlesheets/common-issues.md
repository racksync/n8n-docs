---
#https://www.notion.so/n8n/Frontmatter-432c2b8dff1f43d4b1c8d20075510fe4
title: Google Sheets node common issues 
description: Documentation for common questions and solutions in the Google Sheets node in n8n, a workflow automation platform. Includes details of the issue and suggested resolutions.
contentType: [integration, reference]
priority: critical
---

# Google Sheets node common issues

นี่คือข้อผิดพลาดและปัญหาทั่วไปบางประการเกี่ยวกับ [Google Sheets node](/integrations/builtin/app-nodes/n8n-nodes-base.googlesheets/index.md) และขั้นตอนในการแก้ไขหรือแก้ไขปัญหา

## Append an array

ในการแทรก array ของข้อมูลลงใน Google Sheets คุณต้องแปลง array ให้อยู่ในรูปแบบ JSON (key, value) ที่ถูกต้อง

ในการทำเช่นนั้น ลองพิจารณาใช้:

1.  [Split Out](/integrations/builtin/core-nodes/n8n-nodes-base.splitout.md) node
1.  [AI Transform](/integrations/builtin/core-nodes/n8n-nodes-base.aitransform.md) node ตัวอย่างเช่น ลองป้อนข้อความเช่น:
    ```
    Convert 'languages' array to JSON (key, value) pairs.
    ```
1.  [Code node](/integrations/builtin/core-nodes/n8n-nodes-base.code/index.md)

<!-- vale off -->
## Column names were updated after the node's setup
<!-- vale on -->

คุณจะได้รับข้อผิดพลาดนี้หากชื่อคอลัมน์ของ Google Sheet มีการเปลี่ยนแปลงตั้งแต่คุณตั้งค่า node

หากต้องการรีเฟรชชื่อคอลัมน์ ให้เลือก **Mapping Column Mode** อีกครั้ง ซึ่งควรจะกระตุ้นให้ node ดึงชื่อคอลัมน์มาใหม่อีกครั้ง

เมื่อชื่อคอลัมน์รีเฟรชแล้ว ให้อัปเดต parameters ของ node
