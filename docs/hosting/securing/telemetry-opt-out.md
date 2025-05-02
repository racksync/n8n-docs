---
#https://www.notion.so/n8n/Frontmatter-432c2b8dff1f43d4b1c8d20075510fe4
title: Opt out of data collection
description: "Opt out of data telemetry collection on your n8n instance."
contentType: howto
---

# Data collection

n8n จะเก็บข้อมูลบางอย่างแบบ anonymous จากการติดตั้ง n8n แบบ self-hosted ถ้าอยากปิดการเก็บข้อมูล telemetry สามารถทำตามขั้นตอนด้านล่างนี้ได้เลย

## Collected data

ดูรายละเอียดข้อมูลที่ n8n เก็บได้ที่ [Privacy | Data collection in self-hosted n8n](/privacy-security/privacy.md#data-collection-in-self-hosted-n8n)

## How collection works

n8n instance ของคุณจะส่งข้อมูลส่วนใหญ่ไปที่ n8n ทันทีที่เกิด event นั้นๆ ข้อมูลบางอย่างเช่นจำนวน workflow execution และ instance pulse จะถูกส่งเป็นระยะ (ทุก 6 ชั่วโมง) ข้อมูลเหล่านี้ส่วนใหญ่จะอยู่ในกลุ่ม telemetry collection ของ n8n

## Opting out of data collection

n8n จะเปิดการเก็บ telemetry collection เป็นค่า default ถ้าอยากปิด ให้ตั้งค่า environment variables ตามนี้

### Opt out of telemetry events

ถ้าอยากปิด telemetry events ให้ตั้งค่า environment variable `N8N_DIAGNOSTICS_ENABLED` เป็น false ตัวอย่างเช่น

```bash
export N8N_DIAGNOSTICS_ENABLED=false
```

### Opt out of checking for new versions of n8n

ถ้าไม่อยากให้เช็ค version ใหม่ของ n8n อัตโนมัติ ให้ตั้งค่า environment variable `N8N_VERSION_NOTIFICATIONS_ENABLED` เป็น false ตัวอย่างเช่น

```bash
export N8N_VERSION_NOTIFICATIONS_ENABLED=false
```

## Disable all connection to n8n servers

ถ้าอยากปิดการเชื่อมต่อกับ server ของ n8n ทั้งหมด ดูวิธีได้ที่ [Isolate n8n](/hosting/configuration/configuration-examples/isolation.md)

## Related resources

ดูข้อมูลเพิ่มเติมเกี่ยวกับ environment variables เหล่านี้ได้ที่ [Deployment environment variables](/hosting/configuration/environment-variables/deployment.md)

ดูวิธีตั้งค่า environment variables ได้ที่ [Configuration](/hosting/configuration/configuration-methods.md)
