---
#https://www.notion.so/n8n/Frontmatter-432c2b8dff1f43d4b1c8d20075510fe4
title: Timezone and localization environment variables
description: Set the timezone and default language locale for self-hosted n8n instance.
contentType: reference
tags:
  - environment variables
hide:
  - toc
  - tags
---

# Timezone and localization environment variables

--8<-- "_snippets/self-hosting/file-based-configuration.md"

| Variable | Type  | Default  | Description |
| :------- | :---- | :------- | :---------- |
| `GENERIC_TIMEZONE` | * | `America/New_York` | timezone ของ n8n instance สำคัญสำหรับ schedule node (เช่น Cron) |
| `N8N_DEFAULT_LOCALE` | String | `en` | locale identifier ที่ compatible กับ [Accept-Language header](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Accept-Language){:target="_blank" .external-link} n8n ไม่รองรับ regional identifier เช่น `de-AT` ถ้าใช้ locale อื่นที่ไม่ใช่ default n8n จะแสดง UI เป็นภาษานั้น ถ้าไม่มีจะแสดงเป็น `en` |
