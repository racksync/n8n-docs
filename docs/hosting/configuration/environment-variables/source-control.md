---
#https://www.notion.so/n8n/Frontmatter-432c2b8dff1f43d4b1c8d20075510fe4
title: Source control environment variables
description: Environment variable to set the default SSH key type for source control setup.
contentType: reference
tags:
  - environment variables
hide:
  - toc
  - tags
---

# Source control environment variables

--8<-- "_snippets/self-hosting/file-based-configuration.md"

n8n ใช้ Git-based source control เพื่อรองรับ environments ดูรายละเอียดที่ [Source control and environments](/source-control-environments/setup.md) สำหรับวิธีเชื่อม Git repo กับ n8n instance และตั้งค่า source control

| Variable | Type  | Default  | Description |
| :------- | :---- | :------- | :---------- |
| `N8N_SOURCECONTROL_DEFAULT_SSH_KEY_TYPE` | String | `ed25519` | ตั้งเป็น `rsa` เพื่อให้ RSA เป็น SSH key type default สำหรับ [Source control setup](/source-control-environments/setup.md) |
