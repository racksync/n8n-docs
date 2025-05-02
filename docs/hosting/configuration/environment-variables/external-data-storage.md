---
#https://www.notion.so/n8n/Frontmatter-432c2b8dff1f43d4b1c8d20075510fe4
title: External data storage environment variables
description: Environment variables to configure external data storage for your self-hosted n8n instance. 
contentType: reference
tags:
  - environment variables
  - external storage
  - storage
hide:
  - toc
  - tags
---

# External data storage environment variables

--8<-- "_snippets/self-hosting/file-based-configuration.md"

ดูรายละเอียดเพิ่มเติมเกี่ยวกับการใช้ external storage สำหรับ binary data ได้ที่ [External storage](/hosting/scaling/external-storage.md)

| Variable | Type  | Default  | Description |
| :------- | :---- | :------- | :---------- |
| `N8N_EXTERNAL_STORAGE_S3_HOST` | String | - | host ของ bucket n8n ใน S3-compatible external storage เช่น `s3.us-east-1.amazonaws.com` |
| `N8N_EXTERNAL_STORAGE_S3_BUCKET_NAME` | String | - | ชื่อ bucket n8n ใน S3-compatible external storage |
| `N8N_EXTERNAL_STORAGE_S3_BUCKET_REGION` | String | - | region ของ bucket n8n ใน S3-compatible external storage เช่น `us-east-1`|
| `N8N_EXTERNAL_STORAGE_S3_ACCESS_KEY` | String | - | access key ใน S3-compatible external storage |
| `N8N_EXTERNAL_STORAGE_S3_ACCESS_SECRET` | String | - | access secret ใน S3-compatible external storage |
| `N8N_EXTERNAL_STORAGE_S3_AUTH_AUTO_DETECT` | Boolean | - | ใช้ automatic credential detection สำหรับ S3 external storage จะไม่สนใจ access key/secret แล้วใช้ [credential provider chain](https://docs.aws.amazon.com/sdk-for-javascript/v3/developer-guide/setting-credentials-node.html#credchain) แทน |
