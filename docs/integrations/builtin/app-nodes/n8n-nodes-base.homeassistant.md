---
#https://www.notion.so/n8n/Frontmatter-432c2b8dff1f43d4b1c8d20075510fe4
title: Home Assistant node documentation
description: Learn how to use the Home Assistant node in n8n. Follow technical documentation to integrate Home Assistant node into your workflows.
contentType: [integration, reference]
priority: medium
---

# Home Assistant node

ใช้ Home Assistant node เพื่อทำงานอัตโนมัติใน Home Assistant และเชื่อมต่อ Home Assistant กับแอปอื่นๆ ได้เลย n8n รองรับฟีเจอร์ของ Home Assistant หลายอย่าง เช่น การดึงข้อมูล สร้าง และตรวจสอบ camera proxies, configurations, logs, services และ templates

ในหน้านี้จะมีรายการ operations ที่ Home Assistant node รองรับ พร้อมลิงก์ไปยังแหล่งข้อมูลอื่นๆ

/// note | Credentials
โปรดดู [Home Assistant credentials](/integrations/builtin/credentials/homeassistant.md) สำหรับคำแนะนำการตั้งค่าการยืนยันตัวตน
///

--8<-- "_snippets/integrations/builtin/app-nodes/ai-tools.md"

## Operations

* Camera Proxy
    * Get the camera screenshot
* Config
    * Get the configuration
    * Check the configuration
* Event
    * Create an event
    * Get all events
* Log
    * Get a log for a specific entity
    * Get all logs
* Service
    * Call a service within a specific domain
    * Get all services
* State
    * Create a new record, or update the current one if it already exists (upsert)
    * Get a state for a specific entity
    * Get all states
* Template
    * Create a template

## Templates and examples

<!-- see https://www.notion.so/n8n/Pull-in-templates-for-the-integrations-pages-37c716837b804d30a33b47475f6e3780 -->
[[ templatesWidget(page.title, 'home-assistant') ]]

## Related resources

โปรดดู [Home Assistant's documentation](https://developers.home-assistant.io/docs/api/rest/){:target=_blank .external-link} สำหรับข้อมูลเพิ่มเติมเกี่ยวกับบริการนี้
