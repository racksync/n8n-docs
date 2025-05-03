---
#https://www.notion.so/n8n/Frontmatter-432c2b8dff1f43d4b1c8d20075510fe4
title: Environment Variables สำหรับ Endpoints
description: ปรับแต่ง API และ Webhook Endpoints ด้วย Environment Variables สำหรับ n8n Self-hosted
contentType: reference
tags:
  - environment variables
hide:
  - toc
  - tags
---

# Endpoints environment variables

--8<-- "_snippets/self-hosting/file-based-configuration.md"

หน้านี้จะสรุป environment variables สำหรับปรับแต่ง endpoint ต่าง ๆ ใน n8n

| Variable | Type  | Default  | Description |
| :------- | :---- | :------- | :---------- |
| `N8N_PAYLOAD_SIZE_MAX` | Number | `16` | ขนาด payload สูงสุด (MiB) |
| `N8N_FORMDATA_FILE_SIZE_MAX` | Number | `200` | ขนาดไฟล์สูงสุดใน form-data webhook (MiB) |
| `N8N_METRICS` | Boolean | `false` | เปิด endpoint `/metrics` หรือไม่ |
| `N8N_METRICS_PREFIX` | String | `n8n_` | prefix สำหรับชื่อ metrics ของ n8n |
| `N8N_METRICS_INCLUDE_DEFAULT_METRICS` | Boolean | `true` | เปิดเผย system metrics และ node.js metrics หรือไม่ |
| `N8N_METRICS_INCLUDE_CACHE_METRICS` | Boolean | false | เปิด metrics สำหรับ cache hit/miss หรือไม่ |
| `N8N_METRICS_INCLUDE_MESSAGE_EVENT_BUS_METRICS` | Boolean | `false` | เปิด metrics สำหรับ events หรือไม่ |
| `N8N_METRICS_INCLUDE_WORKFLOW_ID_LABEL` | Boolean | `false` | ใส่ label workflow ID ใน workflow metrics หรือไม่ |
| `N8N_METRICS_INCLUDE_NODE_TYPE_LABEL` | Boolean | `false` | ใส่ label node type ใน node metrics หรือไม่ |
| `N8N_METRICS_INCLUDE_CREDENTIAL_TYPE_LABEL` | Boolean | `false` | ใส่ label credential type ใน credential metrics หรือไม่ |
| `N8N_METRICS_INCLUDE_API_ENDPOINTS` | Boolean | `false` | เปิด metrics สำหรับ API endpoints หรือไม่ |
| `N8N_METRICS_INCLUDE_API_PATH_LABEL` | Boolean | `false` | ใส่ label path ของ API ที่ถูกเรียกหรือไม่ |
| `N8N_METRICS_INCLUDE_API_METHOD_LABEL` | Boolean | `false` | ใส่ label HTTP method (GET, POST, ...) ของ API หรือไม่ |
| `N8N_METRICS_INCLUDE_API_STATUS_CODE_LABEL` | Boolean | `false` | ใส่ label HTTP status code (200, 404, ...) ของ API หรือไม่ |
| `N8N_METRICS_INCLUDE_QUEUE_METRICS` | Boolean | `false` | เปิด metrics สำหรับ job ใน scaling mode (multi-main ยังไม่รองรับ) |
| `N8N_METRICS_QUEUE_METRICS_INTERVAL` | Integer | `20` | ความถี่ (วินาที) ในการอัปเดต queue metrics |
| `N8N_ENDPOINT_REST` | String | `rest` | path สำหรับ REST endpoint |
| `N8N_ENDPOINT_WEBHOOK` | String | `webhook` | path สำหรับ webhook endpoint |
| `N8N_ENDPOINT_WEBHOOK_TEST` | String | `webhook-test` | path สำหรับ test-webhook endpoint |
| `N8N_ENDPOINT_WEBHOOK_WAIT` | String | `webhook-waiting` | path สำหรับ waiting-webhook endpoint |
| `WEBHOOK_URL` | String | - | ใช้กำหนด Webhook URL เองถ้าอยู่หลัง reverse proxy ดู [รายละเอียด](/hosting/configuration/configuration-examples/webhook-url.md) |
| `N8N_DISABLE_PRODUCTION_MAIN_PROCESS` | Boolean | `false` | ปิด production webhooks จาก main process เพื่อไม่ให้ main process รับ HTTP traffic ถ้าใช้ webhook-specific process |
