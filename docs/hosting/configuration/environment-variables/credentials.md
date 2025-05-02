---
#https://www.notion.so/n8n/Frontmatter-432c2b8dff1f43d4b1c8d20075510fe4
title: Credentials environment variables
description: Manage default credentials and override them through environment variables your self-hosted n8n instance.
contentType: reference
tags:
  - environment variables
hide:
  - toc
  - tags
---

# Credentials environment variables

--8<-- "_snippets/self-hosting/file-based-configuration.md"

เปิดใช้ credential overwrites ได้ด้วย environment variables เหล่านี้ ดูรายละเอียดที่ [Credential overwrites](/embed/configuration.md#credential-overwrites)

| Variable | Type  | Default  | Description |
| :------- | :---- | :------- | :---------- |
| `CREDENTIALS_OVERWRITE_DATA`<br>/`_FILE` | * | - | ข้อมูล overwrite สำหรับ credentials |
| `CREDENTIALS_OVERWRITE_ENDPOINT` | String | - | endpoint API สำหรับดึง credentials |
| `CREDENTIALS_DEFAULT_NAME` | String | `My credentials` | ชื่อ default สำหรับ credentials |
