---
#https://www.notion.so/n8n/Frontmatter-432c2b8dff1f43d4b1c8d20075510fe4
description: Get metrics for a health check
contentType: howto
---

# Monitoring

มี API endpoint 3 ตัวที่คุณสามารถเรียกดูสถานะของ instance ได้ คือ `/healthz`, `healthz/readiness`, และ `/metrics`

<!-- vale off -->
## healthz and healthz/readiness
<!-- vale on -->
endpoint `/healthz` จะคืนค่า HTTP status code ปกติ 200 หมายถึง instance เข้าถึงได้ แต่ไม่ได้บอกสถานะของฐานข้อมูล endpoint นี้ใช้ได้ทั้ง self-hosted และ Cloud

เข้าถึง endpoint นี้ได้ที่:

```
<your-instance-url>/healthz
```

endpoint `/healthz/readiness` จะคล้ายกับ `/healthz` แต่จะคืนค่า HTTP 200 ก็ต่อเมื่อเชื่อมต่อฐานข้อมูลและ migrate แล้ว ดังนั้น instance พร้อมรับ traffic

เข้าถึง endpoint นี้ได้ที่:

```
<your-instance-url>/healthz/readiness
```

## metrics

endpoint `/metrics` จะให้ข้อมูลสถานะของ instance แบบละเอียดมากขึ้น

เข้าถึง endpoint นี้ได้ที่:

```
<your-instance-url>/metrics
```

/// info | Feature availability
endpoint `/metrics` ยังไม่เปิดให้ใช้บน n8n Cloud
///
<!-- vale off -->
## Enable metrics and healthz for self-hosted n8n
<!-- vale on -->
endpoint `/metrics` และ `/healthz` ถูกปิดไว้เป็นค่าเริ่มต้น ถ้าต้องการเปิดใช้งาน ให้ตั้งค่า n8n instance ของคุณแบบนี้:

```shell
# metrics
N8N_METRICS=true
# healthz
QUEUE_HEALTH_CHECK_ACTIVE=true
```

ดูรายละเอียดเพิ่มเติมเกี่ยวกับการตั้งค่าด้วย environment variable ได้ที่ [Configuration methods](/hosting/configuration/configuration-methods.md)
