---
#https://www.notion.so/n8n/Frontmatter-432c2b8dff1f43d4b1c8d20075510fe4
title: Okta credentials
description: Documentation for the Okta credentials. Use these credentials to authenticate Okta in n8n, a workflow automation platform.
contentType: [integration, reference]
---

# Okta credentials

คุณสามารถใช้ credentials เหล่านี้เพื่อยืนยันตัวตนใน nodes ต่อไปนี้:

- [Okta](/integrations/builtin/app-nodes/n8n-nodes-base.okta.md)

## Prerequisites

สร้าง [Okta free trial](https://www.okta.com/free-trial/){:target=_blank .external-link} หรือสร้างบัญชีผู้ดูแลระบบบน Okta org ที่มีอยู่

## Supported authentication methods

- SSWS API Access token

## Related resources

อ้างอิง [Okta's documentation](https://developer.okta.com/docs/reference/){:target=_blank .external-link} สำหรับข้อมูลเพิ่มเติมเกี่ยวกับบริการนี้

## Using SSWS API access token

ในการกำหนดค่า credential นี้ คุณจะต้องมี:

- **URL**: Base URL ของ Okta org ของคุณ หรือที่เรียกว่า subdomain เฉพาะของคุณ มีสองวิธีง่ายๆ ในการเข้าถึง:
    1. ใน Admin Console เลือก **Profile** ของคุณ เลื่อนเมาส์ไปเหนือ domain ที่แสดงอยู่ใต้ชื่อผู้ใช้ของคุณ และเลือกไอคอน **Copy** วางสิ่งนี้ลงใน n8n แต่อย่าลืมเพิ่ม `https://` ข้างหน้า
    2. คัดลอก base URL ของ Admin Console URL ของคุณ ตัวอย่างเช่น `https://dev-123456-admin.okta.com` วางลงใน n8n และลบ `-admin` ออก ตัวอย่างเช่น: `https://dev-123456.okta.com`
- **SSWS Access Token**: สร้าง token โดยไปที่ **Security > API > Tokens > Create token** อ้างอิง [Create Okta API tokens](https://help.okta.com/en-us/content/topics/security/api.htm?cshid=ext-create-api-token#create-okta-api-token){:target=_blank .external-link} สำหรับข้อมูลเพิ่มเติม