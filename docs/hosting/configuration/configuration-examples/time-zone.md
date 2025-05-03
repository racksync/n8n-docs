---
#https://www.notion.so/n8n/Frontmatter-432c2b8dff1f43d4b1c8d20075510fe4
title: ตั้งค่า timezone ของ instance ที่ self-host
description: เปลี่ยน timezone เริ่มต้นสำหรับ n8n instance ที่ self-host
contentType: howto
---

# Set the self-hosted instance timezone

timezone default ของ n8n คือ America/New_York เช่น Schedule node จะใช้ timezone นี้ในการกำหนดเวลารัน workflow ถ้าอยากเปลี่ยน timezone default ให้ตั้งค่า `GENERIC_TIMEZONE` เป็นค่าที่ต้องการ เช่น ถ้าอยากใช้ timezone ของ Berlin (Germany):

```bash
export GENERIC_TIMEZONE=Europe/Berlin
```

ดูชื่อ timezone ของคุณได้ที่ [ที่นี่](https://momentjs.com/timezone/){:target="_blank" .external-link}

ดูรายละเอียดตัวแปรนี้เพิ่มเติมได้ที่ [Environment variables reference](/hosting/configuration/environment-variables/timezone-localization.md)
