---
#https://www.notion.so/n8n/Frontmatter-432c2b8dff1f43d4b1c8d20075510fe4
description: วิธีขอความช่วยเหลือและ support เกี่ยวกับ n8n
contentType: howto
hide:
  - toc
---

# Get help with n8n

ถ้าคุณต้องการความช่วยเหลือเกี่ยวกับ n8n สามารถขอคำแนะนำหรือสอบถามปัญหาได้ที่ [forum](https://community.n8n.io/){:target=_blank class=.external-link} ซึ่งเป็นแหล่งข้อมูลที่ดีที่สุด เพราะทั้งทีม support ของ n8n และสมาชิก community พร้อมช่วยเหลือกัน

ถ้า Cloud instance ของคุณมีปัญหา หรือถ้าคุณเป็นลูกค้า enterprise ที่ต้องการ support สามารถติดต่อ [help@n8n.io](mailto:help@n8n.io) ได้เลย

## Use the About n8n debug tool

ไม่ว่าคุณจะโพสต์ใน forum หรือส่งอีเมลหาทีม support คุณจะได้รับความช่วยเหลือเร็วขึ้นถ้าคุณให้ข้อมูลเกี่ยวกับ instance ของ n8n ในโพสต์หรืออีเมลแรก

วิธีที่เร็วที่สุดคือใช้ **About n8n** debug tool:

1. เปิดแถบด้านซ้าย
2. เลือก **Help**
3. เลือก **About n8n**
4. จะมี modal **About n8n** โผล่ขึ้นมาแสดงข้อมูลปัจจุบันของคุณ
5. กด **Copy debug information** เพื่อคัดลอกข้อมูล
6. n8n แนะนำให้นำข้อมูลนี้ไปแปะในโพสต์ forum หรืออีเมล support

/// note | Don't see **Copy debug**?
ตัวเลือก **Copy debug** จะมีตั้งแต่ n8n เวอร์ชัน 1.49.0 ขึ้นไป

ถ้าคุณใช้ n8n เวอร์ชันก่อนหน้านี้ n8n แนะนำให้แจ้งข้อมูลเหล่านี้ด้วยตัวเอง:

* n8n version
* Database
* n8n EXECUTIONS_PROCESS setting
* รัน n8n ด้วยวิธีไหน (Docker, npm, n8n cloud)
* Operating system
///
