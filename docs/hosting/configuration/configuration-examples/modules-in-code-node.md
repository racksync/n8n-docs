---
#https://www.notion.so/n8n/Frontmatter-432c2b8dff1f43d4b1c8d20075510fe4
title: เปิดใช้งาน module ใน Code node
description: อนุญาตให้ใช้ module ทั้ง built-in และ external ใน Code node
contentType: howto
---

# Enable modules in Code node

ด้วยเหตุผลด้านความปลอดภัย Code node จะไม่อนุญาตให้ import module ต่าง ๆ โดย default แต่คุณสามารถยกเลิกข้อจำกัดนี้สำหรับ built-in และ external module ได้โดยตั้ง environment variables เหล่านี้:

- `NODE_FUNCTION_ALLOW_BUILTIN`: สำหรับ built-in modules
- `NODE_FUNCTION_ALLOW_EXTERNAL`: สำหรับ external modules ที่อยู่ใน n8n/node_modules ถ้าไม่ตั้ง environment variable นี้จะไม่สามารถใช้ external module ได้

```bash
# อนุญาตให้ใช้ built-in module ทั้งหมด
export NODE_FUNCTION_ALLOW_BUILTIN=*

# อนุญาตให้ใช้เฉพาะ crypto
export NODE_FUNCTION_ALLOW_BUILTIN=crypto

# อนุญาตให้ใช้ crypto และ fs
export NODE_FUNCTION_ALLOW_BUILTIN=crypto,fs

# อนุญาตให้ใช้ external npm modules
export NODE_FUNCTION_ALLOW_EXTERNAL=moment,lodash
```
ดูรายละเอียดตัวแปรเหล่านี้เพิ่มเติมได้ที่ [Environment variables reference](/hosting/configuration/environment-variables/nodes.md)
