---
#https://www.notion.so/n8n/Frontmatter-432c2b8dff1f43d4b1c8d20075510fe4
title: Grist credentials
description: Documentation for Grist credentials. Use these credentials to authenticate Grist in n8n, a workflow automation platform.
contentType: [integration, reference]
---

# Grist credentials

คุณสามารถใช้ credentials เหล่านี้เพื่อยืนยันตัวตนกับ node ต่อไปนี้:

* [Grist](/integrations/builtin/app-nodes/n8n-nodes-base.grist.md)

## Prerequisites

สร้างบัญชี [Grist](https://getgrist.com/){:target=_blank .external-link}

## Supported authentication methods

- API key

## Related resources

ดูข้อมูลเพิ่มเติมเกี่ยวกับบริการนี้ได้ที่ [Grist's API documentation](https://support.getgrist.com/api/){:target=_blank .external-link}

## Using API key

ในการกำหนดค่า credential นี้ คุณจะต้องมี:

- **API Key**: ดูคำแนะนำในการสร้าง API key ได้ที่ [Grist API authentication documentation](https://support.getgrist.com/rest-api/#authentication){:target=_blank .external-link}
- เลือก Grist **Plan Type** ของคุณ ตัวเลือกได้แก่:
    - Free
    - Paid: หากเลือกตัวเลือกนี้ ให้ระบุ Grist **Custom Subdomain** ของคุณ นี่คือส่วนที่อยู่ก่อนหน้า `.getgrist.com` ตัวอย่างเช่น หาก Grist domain เต็มของเราคือ `n8n.getgrist.com` เราจะป้อน `n8n` ที่นี่
    - Self-Hosted: หากเลือกตัวเลือกนี้ ให้ระบุ Grist **Self-Hosted URL** ของคุณ ควรเป็น URL แบบเต็ม

