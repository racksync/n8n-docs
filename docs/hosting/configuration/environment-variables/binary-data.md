---
#https://www.notion.so/n8n/Frontmatter-432c2b8dff1f43d4b1c8d20075510fe4
title: Binary data environment variables
description: Customize binary data storage modes and paths with environment variables for your self-hosted n8n instance. 
contentType: reference
tags:
  - environment variables
hide:
  - toc
  - tags
---

# Binary data environment variables

--8<-- "_snippets/self-hosting/file-based-configuration.md"

โดยปกติ n8n จะเก็บ binary data ไว้ใน memory ถ้าใช้ Enterprise จะสามารถเลือกเก็บใน external service ได้ด้วย ดูรายละเอียดเพิ่มเติมที่ [External storage](/hosting/scaling/external-storage.md) สำหรับการตั้งค่า external storage เพื่อเก็บ binary data

| Variable | Type  | Default  | Description |
| :------- | :---- | :------- | :---------- |
| `N8N_AVAILABLE_BINARY_DATA_MODES` | String | `filesystem` | รายการ binary data modes ที่ใช้ได้ (คั่นด้วย comma) |
| `N8N_BINARY_DATA_STORAGE_PATH` | String | `N8N_USER_FOLDER/binaryData` | path ที่ n8n จะเก็บ binary data |
| `N8N_DEFAULT_BINARY_DATA_MODE` | String | `default` | binary data mode ที่ใช้เป็นค่าเริ่มต้น `default` จะเก็บ binary data ใน memory ถ้าตั้งเป็น `filesystem` จะเก็บในไฟล์ หรือ `s3` จะเก็บใน AWS S3 หมายเหตุ: การ prune binary data จะทำกับ mode ที่ใช้งานอยู่เท่านั้น เช่น ถ้าเคยเก็บใน S3 แล้วเปลี่ยนมา filesystem n8n จะ prune เฉพาะใน filesystem (อาจเปลี่ยนแปลงในอนาคต) |
