---
#https://www.notion.so/n8n/Frontmatter-432c2b8dff1f43d4b1c8d20075510fe4
title: ข้อมูลรับรอง Customer.io
description: เอกสารข้อมูลรับรอง Customer.io ใช้ข้อมูลนี้เพื่อยืนยันตัวตน Customer.io ใน n8n
contentType: [integration, reference]
---

# Customer.io credentials

คุณสามารถใช้ credentials นี้เพื่อเชื่อมต่อกับ node เหล่านี้กับ Customer.io

- [Customer.io](/integrations/builtin/app-nodes/n8n-nodes-base.customerio.md)
- [Customer.io Trigger](/integrations/builtin/trigger-nodes/n8n-nodes-base.customeriotrigger.md)

## Prerequisites

สมัคร [Customer.io](https://customer.io/) ให้เรียบร้อยก่อน

## Supported authentication methods

- API Key

## Related resources

ดูรายละเอียดเพิ่มเติมเกี่ยวกับบริการได้ที่ [Customer.io's summary API documentation](https://customer.io/docs/api/?api=journeys){:target=_blank .external-link}

สำหรับเอกสารอ้างอิง API โดยละเอียดสำหรับแต่ละ API โปรดดูที่ [Track API documentation](https://customer.io/docs/api/track/){:target=_blank .external-link} และ [App API documentation](https://customer.io/docs/api/app/){:target=_blank .external-link}

## Using API key

ถ้าจะตั้งค่า credentials นี้ คุณต้องมี:

- **Tracking API Key**: สำหรับใช้กับ [Track API](https://customer.io/docs/api/track/){:target=_blank .external-link} ที่ `https://track.customer.io/api/v1/` ดูรายละเอียดเพิ่มเติมใน FAQs ด้านล่าง
- **Region** ของคุณ: Customer.io ใช้ API subdomains ที่แตกต่างกันขึ้นอยู่กับ region ที่คุณเลือก ตัวเลือกได้แก่:
    - **Global region**: คง URLs เริ่มต้นสำหรับทั้งสอง APIs; สำหรับใช้ในทุกประเทศ/ภูมิภาคที่ไม่ใช่ EU
    - **EU region**: ปรับ Track API subdomain เป็น `track-eu` และ App API subdomain เป็น `api-eu`; ใช้เฉพาะเมื่อคุณอยู่ใน EU
- **Tracking Site ID**: จำเป็นต้องใช้กับ **Tracking API Key** ของคุณ
- **App API Key**: สำหรับใช้กับ [App API](https://customer.io/docs/api/app/){:target=_blank .external-link} ที่ `https://api.customer.io/v1/api/` ดูรายละเอียดเพิ่มเติมใน FAQs ด้านล่าง

ดูคำแนะนำในการสร้างทั้ง Tracking API และ App API keys ได้ที่ [Customer.io Finding and managing your API credentials documentation](https://customer.io/docs/accounts-and-workspaces/managing-credentials/){:target=_blank .external-link}

## Why you need a Tracking API Key and an App API Key

Customer.io มี API endpoints สองแบบที่แตกต่างกัน และสร้างและจัดเก็บ keys สำหรับแต่ละแบบแตกต่างกันเล็กน้อย:

- [Track API](https://customer.io/docs/api/track/){:target=_blank .external-link} ที่ `https://track.customer.io/api/v1/`
- [App API](https://customer.io/docs/api/app/){:target=_blank .external-link} ที่ `https://api.customer.io/v1/api/`

Track API ต้องการ Tracking Site ID; App API ไม่ต้องการ

ขึ้นอยู่กับ operation ที่คุณต้องการดำเนินการ n8n จะใช้ API key ที่ถูกต้องและ endpoint ที่สอดคล้องกัน

