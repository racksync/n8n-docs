---
#https://www.notion.so/n8n/Frontmatter-432c2b8dff1f43d4b1c8d20075510fe4
title: DHL credentials
description: Documentation for DHL credentials. Use these credentials to authenticate DHL in n8n, a workflow automation platform.
contentType: [integration, reference]
priority: medium
---

# DHL credentials

คุณสามารถใช้ credentials นี้เพื่อเชื่อมต่อกับ node เหล่านี้:

- [DHL](/integrations/builtin/app-nodes/n8n-nodes-base.dhl.md)

## Supported authentication methods

- API key

## Related resources

ดูรายละเอียดเพิ่มเติมเกี่ยวกับการใช้งาน API ได้ที่ [DHL's Developer documentation](https://support-developer.dhl.com/support/home){:target=_blank .external-link}

## Using API key

ถ้าจะตั้งค่า credentials นี้ คุณต้องมีบัญชี [DHL Developer](https://developer.dhl.com/user/register){:target=_blank .external-link} และ:

- **API Key**

วิธีขอ API key โดยสร้าง app:

1. ใน DHL Developer portal เลือกไอคอนผู้ใช้เพื่อเปิด [User Apps](https://developer.dhl.com/user/apps){:target=_blank .external-link} ของคุณ
2. เลือก **+ Create App**
3. ป้อน **App name** เช่น `n8n integration`
4. ป้อน **Machine name** เช่น `n8n_integration`
4. ใน **SELECT APIs** เลือก **Shipment Tracking - Unified** API จะถูกเพิ่มไปยังส่วน **Add API to app**
5. ในส่วน **Add API to app** เลือก **+** ถัดจาก API **Shipment Tracking - Unified**
6. เลือก **Create App** หน้า **Apps** จะเปิดขึ้น แสดง app ที่คุณเพิ่งสร้าง
7. เลือก app ที่คุณเพิ่งสร้างเพื่อดูรายละเอียด
8. เลือก **Show key** ถัดจาก **API Key**
9. คัดลอก **API Key** และป้อนลงใน n8n credential ของคุณ

ดูข้อมูลเพิ่มเติมได้ที่ [How to create an app?](https://support-developer.dhl.com/support/solutions/articles/47001177011-how-to-create-an-app-){:target=_blank .external-link}
