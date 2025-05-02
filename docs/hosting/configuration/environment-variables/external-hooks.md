---
#https://www.notion.so/n8n/Frontmatter-432c2b8dff1f43d4b1c8d20075510fe4
title: External hooks environment variables
description: Environment variables to integrate external hooks into your self-hosted n8n instance. 
contentType: reference
tags:
  - environment variables
hide:
  - toc
  - tags
---

# External hooks environment variables

--8<-- "_snippets/self-hosting/file-based-configuration.md"

คุณสามารถกำหนด external hooks ที่ n8n จะรันทุกครั้งที่มี operation บางอย่างเกิดขึ้น ดูตัวอย่าง hooks ได้ที่ [Backend hooks](/embed/configuration.md#backend-hooks) และดูวิธีเขียนไฟล์ได้ที่ [Hook files](/embed/configuration.md#backend-hook-files)

| Variable | Type  | Description |
| :------- | :---- | :---------- |
| `EXTERNAL_HOOK_FILES` | String | ไฟล์ที่เก็บ backend external hooks (คั่นหลายไฟล์ด้วย colon ":") |
| `EXTERNAL_FRONTEND_HOOKS_URLS` | String | URL ของไฟล์ frontend external hooks (คั่นหลาย URL ด้วย colon ":") |
