---
#https://www.notion.so/n8n/Frontmatter-432c2b8dff1f43d4b1c8d20075510fe4
title: คู่มือการตั้งค่า Zabbix credentials
description: วิธีตั้งค่า Zabbix credentials เพื่อเชื่อมต่อและยืนยันตัวตนกับ Zabbix ใน n8n
contentType: [integration, reference]
---

# Zabbix credentials

--8<-- "_snippets/integrations/builtin/credentials/cred-only-statement.md"

## Prerequisites

สมัคร [Zabbix Cloud](https://www.zabbix.com/) หรือ self-host Zabbix server ของคุณเอง

## Supported authentication methods

* API key

## Related resources

ดูรายละเอียดเพิ่มเติมเกี่ยวกับการใช้งาน API ได้ที่ [Zabbix's API documentation](https://www.zabbix.com/documentation/current/en/manual/api){:target=_blank .external-link}

This is a credential-only node. ดูวิธีใช้งานเพิ่มเติมที่ [Custom API operations](/integrations/custom-operations.md) และดูตัวอย่าง workflow ได้ที่ [example workflows and related content](https://n8n.io/integrations/zabbix/){:target=_blank .external-link}

## Using API key

ถ้าจะตั้งค่า credentials นี้ คุณต้องมี:

- **API Token**: เป็น API key ของ user ใน Zabbix
- **URL**: URL ของ Zabbix server (ไม่ต้องใส่ `/zabbix` ใน URL)

ดูรายละเอียดเพิ่มเติมที่ [Zabbix's API documentation](https://www.zabbix.com/documentation/current/en/manual/api#authentication){:target=_blank .external-link}
