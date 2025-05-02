---
#https://www.notion.so/n8n/Frontmatter-432c2b8dff1f43d4b1c8d20075510fe4
title: Deployment environment variables
description: Configure deployment options and application accessibility with environment variables for your self-hosted n8n instance. 
contentType: reference
tags:
  - environment variables
hide:
  - toc
  - tags
---

# Deployment environment variables

--8<-- "_snippets/self-hosting/file-based-configuration.md"

หน้านี้จะสรุปตัวเลือก config สำหรับ deployment ของ n8n self-hosted เช่น ตั้งค่า URL สำหรับเข้าถึง เปิด/ปิด templates ตั้งค่า encryption และรายละเอียด server

| Variable | Type  | Default  | Description |
| :------- | :---- | :------- | :---------- |
| `N8N_EDITOR_BASE_URL` | String | - | URL ที่ผู้ใช้จะเข้า editor ได้ ใช้ใน email และ redirect URL สำหรับ SAML ด้วย |
| `N8N_CONFIG_FILES` | String | - | path ไปยังไฟล์ JSON [configuration file](/hosting/configuration/configuration-methods.md) |
| `N8N_DISABLE_UI` | Boolean | `false` | ตั้งเป็น `true` เพื่อปิด UI |
| `N8N_PREVIEW_MODE` | Boolean | `false` | ตั้งเป็น `true` เพื่อรันใน preview mode |
| `N8N_TEMPLATES_ENABLED` | Boolean | `false` | เปิด [workflow templates](/glossary.md#template-n8n) (true) หรือปิด (false) |
| `N8N_TEMPLATES_HOST` | String | `https://api.n8n.io` | เปลี่ยน endpoint ถ้าจะใช้ workflow template library ของตัวเอง (API ต้องเหมือนของ n8n) ดู [Workflow templates](/workflows/templates.md) |
| `N8N_ENCRYPTION_KEY` | String | สุ่มโดย n8n | กำหนด key สำหรับ encrypt credentials ใน database ถ้าไม่กำหนด n8n จะสร้างให้เองตอนแรก |
| `N8N_USER_FOLDER` | String | `user-folder` | path ที่ n8n จะสร้างโฟลเดอร์ `.n8n` สำหรับเก็บข้อมูล user เช่น database, encryption key |
| `N8N_PATH` | String | `/` | path ที่ deploy n8n |
| `N8N_HOST` | String | `localhost` | host ที่ n8n รันอยู่ |
| `N8N_PORT` | Number | `5678` | HTTP port ที่ n8n ใช้ |
| `N8N_LISTEN_ADDRESS` | String | `0.0.0.0` | IP address ที่ n8n จะ listen |
| `N8N_PROTOCOL` | Enum string: `http`, `https` | `http` | protocol ที่ใช้เข้าถึง n8n |
| `N8N_SSL_KEY` | String | - | SSL key สำหรับ HTTPS |
| `N8N_SSL_CERT` | String | - | SSL certificate สำหรับ HTTPS |
| `N8N_PERSONALIZATION_ENABLED` | Boolean | `true` | จะถาม personalisation กับ user และปรับแต่ง n8n ให้เหมาะสมหรือไม่ |
| `N8N_VERSION_NOTIFICATIONS_ENABLED` | Boolean | `true` | ถ้าเปิด n8n จะส่งแจ้งเตือน version ใหม่และ security update |
| `N8N_VERSION_NOTIFICATIONS_ENDPOINT` | String | `https://api.n8n.io/versions/` | endpoint สำหรับดึงข้อมูล version |
| `N8N_VERSION_NOTIFICATIONS_INFO_URL` | String | `https://docs.n8n.io/getting-started/installation/updating.html` | URL สำหรับข้อมูลเพิ่มเติมใน panel New Versions |
| `N8N_DIAGNOSTICS_ENABLED` | Boolean | `true` | จะส่ง [telemetry](/privacy-security/privacy.md) แบบ anonymous ให้ n8n หรือไม่ ถ้าปิดจะใช้ Ask AI ใน Code node ไม่ได้ |
| `N8N_DIAGNOSTICS_CONFIG_FRONTEND` | String | `1zPn9bgWPzlQc0p8Gj1uiK6DOTn;https://telemetry.n8n.io` | config telemetry สำหรับ frontend |
| `N8N_DIAGNOSTICS_CONFIG_BACKEND` | String | `1zPn7YoGC3ZXE9zLeTKLuQCB4F6;https://telemetry.n8n.io/v1/batch` | config telemetry สำหรับ backend |
| `N8N_PUSH_BACKEND` | String | `websocket` | เลือก backend ที่ใช้ส่งข้อมูลไป UI (`sse` หรือ `websocket`) |
| `VUE_APP_URL_BASE_API` | String | `http://localhost:5678/` | ใช้ตอน build `n8n-editor-ui` เพื่อกำหนด base URL ของ backend API ดู [Configure the Base URL](/hosting/configuration/configuration-examples/base-url.md) |
| `N8N_HIRING_BANNER_ENABLED` | Boolean | `true` | จะโชว์ banner รับสมัครงานของ n8n ใน console หรือไม่ |
| `N8N_PUBLIC_API_SWAGGERUI_DISABLED` | Boolean | `false` | ปิด Swagger UI (API playground) หรือไม่ |
| `N8N_PUBLIC_API_DISABLED` | Boolean | `false` | ปิด public API หรือไม่ |
| `N8N_PUBLIC_API_ENDPOINT` | String | `api` | path สำหรับ public API endpoints |
| `N8N_GRACEFUL_SHUTDOWN_TIMEOUT` | Number | `30` | เวลารอ (วินาที) ให้ component shutdown ก่อนปิด process n8n |
| `N8N_DEV_RELOAD` | Boolean | `false` | ถ้าทำ dev กับ source code n8n ให้ตั้งเป็น `true` เพื่อ reload/restart อัตโนมัติเมื่อไฟล์เปลี่ยน |
| `N8N_REINSTALL_MISSING_PACKAGES` | Boolean | `false` | ถ้าตั้งเป็น `true` n8n จะพยายาม reinstall package ที่หายไปอัตโนมัติ |
| `N8N_TUNNEL_SUBDOMAIN` | String | - | กำหนด subdomain สำหรับ n8n tunnel ถ้าไม่ตั้ง n8n จะสุ่มให้เอง |
| `N8N_PROXY_HOPS` | Number | 0 | จำนวน reverse-proxy ที่ n8n รันอยู่ข้างหลัง |
