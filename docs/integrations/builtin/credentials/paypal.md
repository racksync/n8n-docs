---
#https://www.notion.so/n8n/Frontmatter-432c2b8dff1f43d4b1c8d20075510fe4
title: ข้อมูลยืนยันตัวตน PayPal
description: เอกสารสำหรับข้อมูลยืนยันตัวตน PayPal ใช้ข้อมูลนี้เพื่อยืนยันตัวตน PayPal ใน n8n แพลตฟอร์ม workflow automation
contentType: [integration, reference]
---

# PayPal credentials

คุณสามารถใช้ credentials นี้เพื่อยืนยันตัวตนกับ node ต่อไปนี้ได้:

- [PayPal](/integrations/builtin/app-nodes/n8n-nodes-base.paypal.md)
- [PayPal Trigger](/integrations/builtin/trigger-nodes/n8n-nodes-base.paypaltrigger.md)

## Prerequisites

สร้าง [PayPal developer](https://developer.paypal.com/home){:target=_blank .external-link} account

## Supported authentication methods

- API client and secret

## Related resources

ดูข้อมูลเพิ่มเติมเกี่ยวกับบริการนี้ได้ที่ [Paypal's API documentation](https://developer.paypal.com/api/rest/){:target=_blank .external-link}

## Using API client and secret

สำหรับการตั้งค่า credentials นี้ คุณจะต้องมี:

- **Client ID**: สร้างขึ้นเมื่อคุณสร้าง app
- **Secret**: สร้างขึ้นเมื่อคุณสร้าง app
- **Environment**: เลือก **Live** หรือ **Sandbox**

หากต้องการสร้าง **Client ID** และ **Secret** ให้ล็อกอินเข้าสู่ Paypal [developer dashboard](https://developer.paypal.com/dashboard/) ของคุณ เลือก **Apps & Credentials > Rest API apps > Create app** ดูข้อมูลเพิ่มเติมที่ [Get client ID and client secret](https://developer.paypal.com/api/rest/#link-getclientidandclientsecret){:target=_blank .external-link}


