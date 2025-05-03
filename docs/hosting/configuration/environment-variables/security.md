---
#https://www.notion.so/n8n/Frontmatter-432c2b8dff1f43d4b1c8d20075510fe4
title: Environment Variables สำหรับ Security
description: ตั้งค่า Authentication และการเข้าถึง Environment Variable ใน n8n Self-hosted
contentType: reference
tags:
  - environment variables
hide:
  - toc
  - tags
---

# Security environment variables

--8<-- "_snippets/self-hosting/file-based-configuration.md"

| Variable | Type  | Default  | Description |
| :------- | :---- | :------- | :---------- |
| `N8N_BLOCK_ENV_ACCESS_IN_NODE` | Boolean | `false` | จะอนุญาตให้ user access environment variable ใน expression/Code node หรือไม่ (false = อนุญาต, true = ไม่อนุญาต) |
| `N8N_RESTRICT_FILE_ACCESS_TO` | String |  | จำกัดการ access ไฟล์ใน directory ที่กำหนด (คั่นหลาย path ด้วย colon ":") |
| `N8N_BLOCK_FILE_ACCESS_TO_N8N_FILES` | Boolean | `true` | ตั้งเป็น `true` เพื่อ block การ access ไฟล์ใน `.n8n` และ config file ที่ user กำหนดเอง |
| `N8N_SECURITY_AUDIT_DAYS_ABANDONED_WORKFLOW` | Number | 90 | กำหนดจำนวนวันที่ workflow ไม่ถูก execute ถึงจะถือว่า abandoned |
| `N8N_SECURE_COOKIE` | Boolean | `true` | บังคับให้ cookie ส่งผ่าน HTTPS เท่านั้น เพิ่มความปลอดภัย |
| `N8N_SAMESITE_COOKIE` | Enum string: `strict`, `lax`, `none` | `lax` | ควบคุม cross-site cookie ([ดูรายละเอียด](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Set-Cookie/SameSite)):<ul><li>`strict`: ส่ง cookie เฉพาะ first-party request</li><li>`lax` (default): ส่งกับ top-level navigation</li><li>`none`: ส่งทุก context (ต้องใช้ HTTPS)</li></ul> |
