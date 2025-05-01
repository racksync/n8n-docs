---
#https://www.notion.so/n8n/Frontmatter-432c2b8dff1f43d4b1c8d20075510fe4
contentType: howto
---

# Troubleshooting and errors

## Error: Missing packages

n8n จะติดตั้ง community nodes ลงบน hard disk โดยตรง ไฟล์เหล่านี้ต้องมีอยู่ตอนที่ n8n เริ่มทำงาน ไม่งั้นจะเจอ error แจ้งว่า missing packages

ถ้าใช้งาน n8n ผ่าน Docker: ขึ้นอยู่กับการตั้งค่า Docker ของคุณ อาจทำให้ package หายไปตอนสร้าง container ใหม่หรืออัปเกรด n8n คุณต้องเลือกวิธีใดวิธีหนึ่งต่อไปนี้:

* เก็บข้อมูลในโฟลเดอร์ `~/.n8n/nodes` ให้คงอยู่เสมอ วิธีนี้ดีที่สุด ถ้าทำตามคู่มือ [Docker installation](/hosting/installation/docker.md) จะมีขั้นตอนให้เก็บโฟลเดอร์นี้ไว้
* ตั้งค่า environment variable `N8N_REINSTALL_MISSING_PACKAGES` เป็น `true`

วิธีที่สองอาจทำให้เวลาเริ่มต้นนานขึ้น และอาจทำให้ health check ล้มเหลวได้
