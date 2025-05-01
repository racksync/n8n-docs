---
#https://www.notion.so/n8n/Frontmatter-432c2b8dff1f43d4b1c8d20075510fe4
title: Form.io Trigger credentials
description: Documentation for Form.io Trigger credentials. Use these credentials to authenticate Form.io Trigger in n8n, a workflow automation platform.
contentType: [integration, reference]
priority: medium
---

# Form.io Trigger credentials

คุณสามารถใช้ credentials เหล่านี้เพื่อยืนยันตัวตนกับ node ต่อไปนี้:

- [Form.io Trigger](/integrations/builtin/trigger-nodes/n8n-nodes-base.formiotrigger.md)

## Supported authentication methods

- Basic auth

## Related resources

ดูข้อมูลเพิ่มเติมเกี่ยวกับบริการนี้ได้ที่ [Form.io's API documentation](https://apidocs.form.io/){:target=_blank .external-link}

## Using basic auth

ในการกำหนดค่า credential นี้ คุณจะต้องมีบัญชี [Form.io](https://www.form.io/) และ:

- **Environment** ของคุณ
- **Email address** ที่ใช้เข้าสู่ระบบของคุณ
- **Password** ของคุณ

วิธีตั้งค่า credential:

1. เลือก **Environment** ของคุณ:
    - เลือก **Cloud hosted** หากคุณไม่ได้โฮสต์ Form.io ด้วยตัวเอง
    - เลือก **Self-hosted** หากคุณโฮสต์ Form.io ด้วยตัวเอง จากนั้นเพิ่ม:
        - **Self-Hosted Domain** ของคุณ ใช้เฉพาะ domain เท่านั้น ตัวอย่างเช่น หากคุณดูฟอร์มที่ `https://yourserver.com/yourproject/manage/view` Self-Hosted Domain คือ `https://yourserver.com`
2. ป้อน **Email address** ที่คุณใช้เข้าสู่ระบบ Form.io
3. ป้อน **Password** ที่คุณใช้เข้าสู่ระบบ Form.io
