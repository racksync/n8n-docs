---
#https://www.notion.so/n8n/Frontmatter-432c2b8dff1f43d4b1c8d20075510fe4
title: Task runner environment variables
description: Environment variables to confgure task runners your self-hosted n8n instance.
contentType: reference
tags:
  - environment variables
hide:
  - toc
  - tags
---

# Task runner environment variables

--8<-- "_snippets/self-hosting/file-based-configuration.md"

[Task runners](/hosting/configuration/task-runners.md) จะ execute โค้ดที่เขียนใน [Code node](/integrations/builtin/core-nodes/n8n-nodes-base.code/index.md)

## n8n instance environment variables

| Variable | Type  | Default  | Description |
| :------- | :---- | :------- | :---------- |
| `N8N_RUNNERS_ENABLED` | Boolean | `false` | เปิดใช้ task runners หรือไม่ |
| `N8N_RUNNERS_MODE` | Enum string: `internal`, `external` | `internal` | เลือกว่าจะ launch/run task runner แบบไหน `internal` = n8n launch เป็น child process, `external` = orchestrator ภายนอกเป็นคน launch |
| `N8N_RUNNERS_AUTH_TOKEN` | String | Random string | shared secret ที่ task runner ใช้ authenticate กับ n8n (ต้องตั้งถ้าใช้ `external` mode) |
| `N8N_RUNNERS_BROKER_PORT` | Number | `5679` | port ที่ task broker รอรับ connection จาก task runner |
| `N8N_RUNNERS_BROKER_LISTEN_ADDRESS` | String | `127.0.0.1` | address ที่ task broker จะ listen |
| `N8N_RUNNERS_MAX_PAYLOAD` | Number | `1 073 741 824` | ขนาด payload สูงสุด (byte) สำหรับสื่อสารระหว่าง task broker กับ runner |
| `N8N_RUNNERS_MAX_OLD_SPACE_SIZE` | String |  | option `--max-old-space-size` ที่ใช้กับ task runner (MB) ถ้าไม่ตั้ง Node.js จะกำหนดเองตาม memory ที่มี |
| `N8N_RUNNERS_MAX_CONCURRENCY` | Number | `5` | จำนวน task ที่ runner จะรันพร้อมกันได้ |
| `N8N_RUNNERS_TASK_TIMEOUT` | Number | `60` | เวลาสูงสุด (วินาที) ที่ task จะรันก่อน abort และ restart runner (ต้องมากกว่า 0) |
| `N8N_RUNNERS_HEARTBEAT_INTERVAL` | Number | `30` | ความถี่ (วินาที) ที่ runner ต้องส่ง heartbeat ให้ broker ไม่งั้น task จะ abort และ runner จะ restart (ต้องมากกว่า 0) |


## Task runner launcher environment variables

| Variable | Type  | Default  | Description |
| :------- | :---- | :------- | :---------- |
| `N8N_RUNNERS_LAUNCHER_LOG_LEVEL` | Enum string: `debug`, `info`, `warn`, `error` | `info` | ระดับ log ที่จะแสดง |
| `N8N_RUNNERS_AUTH_TOKEN` | String | - | shared secret สำหรับ authenticate กับ n8n |
| `N8N_RUNNERS_AUTO_SHUTDOWN_TIMEOUT` | Number | `15` | เวลารอ (วินาที) ก่อนปิด runner ที่ idle |
| `N8N_RUNNERS_TASK_BROKER_URI` | String | `http://127.0.0.1:5679` | URI ของ task broker server (n8n instance) |
| `N8N_RUNNERS_LAUNCHER_HEALTH_CHECK_PORT` | Number | `5680` | port สำหรับ health check server ของ launcher |
| `N8N_RUNNERS_MAX_PAYLOAD` | Number | `1 073 741 824` | ขนาด payload สูงสุด (byte) สำหรับสื่อสารระหว่าง task broker กับ runner |
| `N8N_RUNNERS_MAX_CONCURRENCY` | Number | `5` | จำนวน task ที่ runner จะรันพร้อมกันได้ |
| `NODE_OPTIONS` | String | - | [option](https://nodejs.org/api/cli.html#node_optionsoptions) สำหรับ Node.js |


## Task runner environment variables

| Variable | Type  | Default  | Description |
| :------- | :---- | :------- | :---------- |
| `N8N_RUNNERS_GRANT_TOKEN` | String | Random string | token ที่ runner ใช้ authenticate กับ task broker (launcher จะ set ให้อัตโนมัติ) |
| `N8N_RUNNERS_AUTO_SHUTDOWN_TIMEOUT` | Number | `15` | เวลารอ (วินาที) ก่อนปิด runner ที่ idle |
| `N8N_RUNNERS_TASK_BROKER_URI` | String | `http://127.0.0.1:5679` | URI ของ task broker server (n8n instance) |
| `N8N_RUNNERS_LAUNCHER_HEALTH_CHECK_PORT` | Number | `5680` | port สำหรับ health check server ของ launcher |
| `N8N_RUNNERS_MAX_PAYLOAD` | Number | `1 073 741 824` | ขนาด payload สูงสุด (byte) สำหรับสื่อสารระหว่าง task broker กับ runner |
| `N8N_RUNNERS_MAX_CONCURRENCY` | Number | `5` | จำนวน task ที่ runner จะรันพร้อมกันได้ |
| `NODE_FUNCTION_ALLOW_BUILTIN` | String | - | อนุญาตให้ import built-in module ใน Code node (ใส่ * เพื่อเปิดหมด) ปกติจะปิดหมด |
| `NODE_FUNCTION_ALLOW_EXTERNAL` | String | - | อนุญาตให้ import external module (จาก `n8n/node_modules`) ใน Code node ปกติจะปิดหมด |
| `N8N_RUNNERS_ALLOW_PROTOTYPE_MUTATION` | Boolean | `false` | อนุญาตให้ external library ทำ prototype mutation หรือไม่ (เช่น [`puppeteer`](https://pptr.dev/)) ถ้าเปิดจะลด security |
| `GENERIC_TIMEZONE` | * | `America/New_York` | [timezone default เดียวกับ n8n instance](/hosting/configuration/environment-variables/timezone-localization.md) |
