---
#https://www.notion.so/n8n/Frontmatter-432c2b8dff1f43d4b1c8d20075510fe4
title: License environment variables
description: Environment variables to configure license settings in n8n, including options to hide the usage page, manage license activation and auto-renewal settings, and specify the server URL for license retrieval.
contentType: reference
tags:
  - environment variables
hide:
  - toc
  - tags
---

# License environment variables

--8<-- "_snippets/self-hosting/file-based-configuration.md"

ถ้าต้องการใช้ฟีเจอร์ที่ต้องมี license ต้อง activate license ก่อน จะ activate ผ่าน UI หรือ environment variable ก็ได้ ดูรายละเอียดที่ [license key](/license-key.md)

| Variable | Type  | Default  | Description |
| :------- | :---- | :------- | :---------- |
| `N8N_HIDE_USAGE_PAGE` | boolean | `false` | ซ่อนหน้า usage และ plans ในแอป |
| `N8N_LICENSE_ACTIVATION_KEY` | String | `''` | activation key สำหรับ initialize license (ใช้เฉพาะตอน activate ครั้งแรก) |
| `N8N_LICENSE_AUTO_RENEW_ENABLED` | Boolean | `true` | เปิด/ปิด autorenewal สำหรับ license <br>ถ้าปิดต้องต่ออายุเองทุก 10 วันที่ **Settings** > **Usage and plan** แล้วกด `F5` ถ้าไม่ต่ออายุจะใช้ฟีเจอร์ที่ต้อง license ไม่ได้ |
| `N8N_LICENSE_DETACH_FLOATING_ON_SHUTDOWN` | Boolean | `true` | จะคืน [floating entitlements](/glossary.md#entitlement-n8n) กลับ pool ตอน shutdown หรือไม่ ถ้าอยากให้ instance production เก็บ entitlement ไว้ตลอดให้ตั้งเป็น `false` |
| `N8N_LICENSE_SERVER_URL` | String | `http://license.n8n.io/v1` | server URL สำหรับดึง license |
| `N8N_LICENSE_TENANT_ID` | Number | `1` | tenant ID ที่ผูกกับ license (ตั้งเฉพาะถ้า n8n แจ้งให้ตั้ง) |
| `https_proxy_license_server` | String | `https://user:pass@proxy:port` | proxy server URL สำหรับ HTTPS request ไป license server (ตัวแปรนี้ต้องเป็นตัวเล็กทั้งหมด) |
