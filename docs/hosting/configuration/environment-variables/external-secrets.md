---
#https://www.notion.so/n8n/Frontmatter-432c2b8dff1f43d4b1c8d20075510fe4
title: External secrets environment variables
description: Configure the interval for checking updates to external secrets in self-hosted n8n instance. 
contentType: reference
tags:
  - environment variables
hide:
  - toc
  - tags
---

# External secrets environment variables

--8<-- "_snippets/self-hosting/file-based-configuration.md"

คุณสามารถใช้ external secrets store เพื่อจัดการ credentials ของ n8n ดูรายละเอียดที่ [External secrets](/external-secrets.md)

| Variable | Type  | Default  | Description |
| :------- | :---- | :------- | :---------- |
| `N8N_EXTERNAL_SECRETS_UPDATE_INTERVAL` | Number | `300` (5 นาที) | ความถี่ (วินาที) ที่จะเช็ค secret update |
