---
#https://www.notion.so/n8n/Frontmatter-432c2b8dff1f43d4b1c8d20075510fe4
contentType: explanation
---

# Deployment

--8<-- "_snippets/embed-license.md"

ดู [hosting documentation](https://docs.n8n.io/reference/server-setup.html) สำหรับตัวเลือกการ setup แบบละเอียด

## User data

n8n แนะนำให้คุณใช้แนวทางเดียวกับที่ใช้ใน n8n Cloud คือเก็บ user data ด้วย [Rook](https://rook.io/) และถ้า server n8n ล่ม ก็ให้ instance ใหม่รันบนเครื่องอื่นโดยใช้ข้อมูลเดิม

ด้วยวิธีนี้ คุณไม่จำเป็นต้อง backup ข้อมูล ยกเว้นกรณีเกิดเหตุร้ายแรง หรือผู้ใช้ต้องการกู้บัญชีในช่วงเวลาที่กำหนด (n8n Cloud กำหนดไว้สองสัปดาห์)

## Backups

n8n แนะนำให้ backup ข้อมูลทุกคืน โดยแนบ container อีกตัวแล้ว copy ข้อมูลทั้งหมดไปยัง container ที่สอง วิธีนี้ใช้ RAM น้อยมาก และไม่กระทบจำนวนผู้ใช้ที่วางบน server

## Restarting

ถ้า instance ของคุณล่มหรือ restart การรันที่พลาดไป (เช่น Cron หรือ Webhook node) ในช่วงนั้นจะไม่สามารถกู้คืนได้ ถ้าคุณต้องการ uptime 100% จริงๆ ต้องสร้าง proxy อีกตัวไว้ข้างหน้าเพื่อ cache ข้อมูล
