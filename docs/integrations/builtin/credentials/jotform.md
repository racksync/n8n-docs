---
#https://www.notion.so/n8n/Frontmatter-432c2b8dff1f43d4b1c8d20075510fe4
title: JotForm credentials
description: Documentation for JotForm credentials. Use these credentials to authenticate JotForm in n8n, a workflow automation platform.
contentType: [integration, reference]
priority: medium
---

# JotForm credentials

คุณสามารถใช้ credentials เหล่านี้เพื่อยืนยันตัวตนกับ node ต่อไปนี้ได้:

- [JotForm Trigger](/integrations/builtin/trigger-nodes/n8n-nodes-base.jotformtrigger.md)

## Supported authentication methods

- API key

## Related resources

ดูข้อมูลเพิ่มเติมเกี่ยวกับบริการนี้ได้ที่ [JotForm's API documentation](https://api.jotform.com/docs/){:target=_blank .external-link}

## Using API key

ในการตั้งค่า credential นี้ คุณจะต้องมีบัญชี [JotForm](https://www.jotform.com/){:target=_blank .external-link} และ:

- **API Key**
- **API Domain**

วิธีตั้งค่า:

1.  ไปที่ **Settings >** [**API**](https://www.jotform.com/myaccount/api){:target=_blank .external-link}
2.  เลือก **Create New Key**
3.  เลือก **Name** ใน JotForm เพื่ออัปเดตชื่อ API key เป็นชื่อที่มีความหมาย เช่น `n8n integration`
4.  คัดลอก **API Key** และป้อนลงใน n8n credential ของคุณ
5.  ใน n8n เลือก **API Domain** ที่ตรงกับคุณตามแบบฟอร์มที่คุณใช้:
    - **api.jotform.com**: ใช้ตัวเลือกนี้ เว้นแต่แบบฟอร์มประเภทอื่นจะตรงกับคุณ
    - **eu-api.jotform.com**: เลือกตัวเลือกนี้หากคุณใช้ JotForm [EU Safe Forms](https://www.jotform.com/eu-safe-forms/){:target=_blank .external-link}
    - **hipaa-api.jotform.com**: เลือกตัวเลือกนี้หากคุณใช้ JotForm [HIPAA forms](https://www.jotform.com/hipaa/){:target=_blank .external-link}

ดูข้อมูลเพิ่มเติมเกี่ยวกับการสร้าง keys และ API domains ได้ที่ [JotForm API documentation](https://api.jotform.com/docs/)
