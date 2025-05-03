---
#https://www.notion.so/n8n/Frontmatter-432c2b8dff1f43d4b1c8d20075510fe4
description: แนวทางปฏิบัติที่ดีที่สุดสำหรับการจัดการผู้ใช้
contentType: explanation
---

# Best practices for user management

หน้านี้ประกอบด้วยคำแนะนำเกี่ยวกับแนวทางปฏิบัติที่ดีที่สุดที่เกี่ยวข้องกับ user management ใน n8n

## All platforms

* n8n แนะนำให้ owners สร้าง member-level account สำหรับตนเอง Owners สามารถเห็น workflows ทั้งหมดได้ แต่ไม่มีวิธีดูว่าใครเป็นคนสร้าง workflow นั้นๆ ดังนั้นจึงมีความเสี่ยงที่จะเขียนทับงานของผู้อื่นหากคุณสร้างและแก้ไข workflows ในฐานะ owner
* ผู้ใช้ต้องระมัดระวังไม่แก้ไข workflow เดียวกันพร้อมกัน สามารถทำได้ แต่ผู้ใช้จะเขียนทับการเปลี่ยนแปลงของกันและกัน
* หากต้องการย้าย workflows ระหว่าง accounts ให้ export workflow เป็น JSON จากนั้น import ไปยัง account ใหม่ โปรดทราบว่าการกระทำนี้จะทำให้ประวัติ workflow หายไป
* Webhook paths ต้องไม่ซ้ำกันทั่วทั้ง instance ซึ่งหมายความว่า webhook path แต่ละอันต้องไม่ซ้ำกันสำหรับ workflows ทั้งหมดและผู้ใช้ทั้งหมด โดยค่าเริ่มต้น n8n จะสร้างค่าสุ่มยาวๆ สำหรับ webhook path แต่ผู้ใช้สามารถแก้ไขเป็น path ที่กำหนดเองได้ หากผู้ใช้สองคนตั้งค่า path เดียวกัน:
    * Path จะทำงานสำหรับ workflow แรกที่ถูก run หรือ activate
    * Workflows อื่นๆ จะเกิดข้อผิดพลาดหากพยายาม run ด้วย path เดียวกัน

## Self-hosted

หากคุณ run n8n หลัง reverse proxy ให้ตั้งค่า environment variables ต่อไปนี้เพื่อให้ n8n สร้างอีเมลด้วย URL ที่ถูกต้อง:

* `N8N_HOST`
* `N8N_PORT`
* `N8N_PROTOCOL`
* `N8N_EDITOR_BASE_URL`

ข้อมูลเพิ่มเติมเกี่ยวกับ variables เหล่านี้มีอยู่ใน [Environment variables](/hosting/configuration/environment-variables/index.md)

