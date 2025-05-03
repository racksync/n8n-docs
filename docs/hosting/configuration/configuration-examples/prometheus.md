---
#https://www.notion.so/n8n/Frontmatter-432c2b8dff1f43d4b1c8d20075510fe4
title: เปิดใช้งาน Prometheus metrics
description: เปิดใช้งาน endpoint ของ Prometheus metrics
contentType: howto
---

# Enable Prometheus metrics 

n8n ใช้ library [prom-client](https://www.npmjs.com/package/prom-client){:target="_blank" .external-link} สำหรับเก็บและเปิดเผย metrics

endpoint `/metrics` จะถูกปิดไว้โดย default แต่สามารถเปิดได้ด้วย environment variable `N8N_METRICS`

```bash
export N8N_METRICS=true
```

ดูรายละเอียดการตั้งค่า metrics และ label ที่จะเปิดเผยได้ที่ [Environment Variables](/hosting/configuration/environment-variables/endpoints.md) (`N8N_METRICS_INCLUDE_*`)

ทั้ง instance แบบ `main` และ `worker` สามารถเปิด metrics ได้

## Queue metrics

ถ้าอยากเปิด queue metrics ให้ตั้ง `N8N_METRICS_INCLUDE_QUEUE_METRICS` เป็น `true` และปรับ refresh rate ได้ด้วย `N8N_METRICS_QUEUE_METRICS_INTERVAL`

queue metrics ใช้ได้เฉพาะกับ instance แบบ `main` ใน single-main mode เท่านั้น

```
# HELP n8n_scaling_mode_queue_jobs_active จำนวน job ที่กำลังถูก process อยู่ใน scaling mode
# TYPE n8n_scaling_mode_queue_jobs_active gauge
n8n_scaling_mode_queue_jobs_active 0

# HELP n8n_scaling_mode_queue_jobs_completed จำนวน job ที่สำเร็จใน scaling mode ตั้งแต่เริ่ม instance
# TYPE n8n_scaling_mode_queue_jobs_completed counter
n8n_scaling_mode_queue_jobs_completed 0

# HELP n8n_scaling_mode_queue_jobs_failed จำนวน job ที่ fail ใน scaling mode ตั้งแต่เริ่ม instance
# TYPE n8n_scaling_mode_queue_jobs_failed counter
n8n_scaling_mode_queue_jobs_failed 0

# HELP n8n_scaling_mode_queue_jobs_waiting จำนวน job ที่รออยู่ใน queue ใน scaling mode
# TYPE n8n_scaling_mode_queue_jobs_waiting gauge
n8n_scaling_mode_queue_jobs_waiting 0
```
