---
#https://www.notion.so/n8n/Frontmatter-432c2b8dff1f43d4b1c8d20075510fe4
title: Environment Variables สำหรับ Queue Mode
description: Environment Variables สำหรับตั้งค่า Queue Mode ใน n8n Self-hosted
contentType: reference
tags:
  - environment variables
hide:
  - toc
  - tags
---

# Queue mode environment variables

--8<-- "_snippets/self-hosting/file-based-configuration.md"

คุณสามารถรัน n8n ได้หลาย mode ตามความต้องการ Queue mode จะ scale ได้ดีที่สุด ดูรายละเอียดที่ [Queue mode](/hosting/scaling/queue-mode.md)

| Variable | Type  | Default  | Description |
| :------- | :---- | :------- | :---------- |
| `QUEUE_BULL_PREFIX` | String | - | prefix สำหรับ queue key ทั้งหมด |
| `QUEUE_BULL_REDIS_DB` | Number | `0` | Redis database ที่ใช้ |
| `QUEUE_BULL_REDIS_HOST` | String | `localhost` | Redis host |
| `QUEUE_BULL_REDIS_PORT` | Number | `6379` | Redis port ที่ใช้ |
| `QUEUE_BULL_REDIS_USERNAME` | String | - | Redis username (ต้องใช้ Redis 6 ขึ้นไป ถ้าใช้ต่ำกว่านี้อย่ากำหนด) |
| `QUEUE_BULL_REDIS_PASSWORD` | String | - | Redis password |
| `QUEUE_BULL_REDIS_TIMEOUT_THRESHOLD` | Number | `10000` | Redis timeout threshold (ms) |
| `QUEUE_BULL_REDIS_CLUSTER_NODES` | String | - | รายชื่อ Redis Cluster node (คั่น comma) เช่น `host:port` ถ้าใช้ queue mode (`EXECUTIONS_MODE = queue`) แล้วตั้งตัวนี้ n8n จะใช้ Redis Cluster client แทน Redis client และจะไม่สนใจ `QUEUE_BULL_REDIS_HOST` กับ `QUEUE_BULL_REDIS_PORT` |
| `QUEUE_BULL_REDIS_TLS` | Boolean | `false` | เปิด TLS สำหรับ Redis หรือไม่ |
| `QUEUE_BULL_REDIS_DUALSTACK` | Boolean | `false` | เปิด dual-stack (IPv4/IPv6) สำหรับ Redis หรือไม่ |
| `QUEUE_WORKER_TIMEOUT` (**deprecated**) | Number | `30` | **Deprecated** ใช้ `N8N_GRACEFUL_SHUTDOWN_TIMEOUT` แทน<br/><br/>เวลารอ (วินาที) ให้ execution ที่รันอยู่จบก่อนปิด worker process |
| `QUEUE_HEALTH_CHECK_ACTIVE` | Boolean | `false` | เปิด health check หรือไม่ |
| `QUEUE_HEALTH_CHECK_PORT` | Number | - | port สำหรับ health check |
| `QUEUE_WORKER_LOCK_DURATION` | Number | `30000` | lease period (ms) ที่ worker จะได้ทำงานกับ message |
| `QUEUE_WORKER_LOCK_RENEW_TIME` | Number | `15000` | ความถี่ (ms) ที่ worker จะ renew lease time |
| `QUEUE_WORKER_STALLED_INTERVAL` | Number | `30000` | ความถี่ที่ worker จะเช็ค stalled job (0 = ไม่เช็คเลย) |
| `QUEUE_WORKER_MAX_STALLED_COUNT` | Number | `1` | จำนวนครั้งสูงสุดที่ stalled job จะถูก re-process |

## Multi-main setup

ดูรายละเอียดที่ [Configuring multi-main setup](/hosting/scaling/queue-mode.md#configuring-multi-main-setup)

| Variable | Type  | Default  | Description |
| :------- | :---- | :------- | :---------- |
| `N8N_MULTI_MAIN_SETUP_ENABLED` | Boolean | `false` | เปิด multi-main setup สำหรับ queue mode (ต้องมี license) |
| `N8N_MULTI_MAIN_SETUP_KEY_TTL` | Number | `10` | อายุ key (วินาที) สำหรับ leader ใน multi-main setup |
| `N8N_MULTI_MAIN_SETUP_CHECK_INTERVAL` | Number | `3` | ความถี่ (วินาที) ที่จะเช็ค leader ใน multi-main setup |
