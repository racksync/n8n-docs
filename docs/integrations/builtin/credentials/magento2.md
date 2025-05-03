---
#https://www.notion.so/n8n/Frontmatter-432c2b8dff1f43d4b1c8d20075510fe4
title: ข้อมูลยืนยันตัวตน Magento 2
description: เอกสารสำหรับ Magento 2 credentials ใช้เพื่อเชื่อมต่อ Magento 2 ใน n8n
contentType: [integration, reference]
---

# Magento 2 credentials

คุณสามารถใช้ credentials เหล่านี้เพื่อยืนยันตัวตนใน node ต่อไปนี้:

- [Magento 2](/integrations/builtin/app-nodes/n8n-nodes-base.magento2.md)

## Prerequisites

- สร้างบัญชี [Magento](https://magento.com/){:target=_blank .external-link}
- ตั้งค่าร้านค้าของคุณเป็น **Allow OAuth Access Tokens to be used as standalone Bearer tokens**
    - ไปที่ **Admin > Stores > Configuration > Services > OAuth > Consumer Settings**
    - ตั้งค่าตัวเลือก **Allow OAuth Access Tokens to be used as standalone Bearer tokens** เป็น **Yes**
    - คุณยังสามารถเปิดใช้งานการตั้งค่านี้จาก CLI โดยรันคำสั่งต่อไปนี้:

        ```
        bin/magento config:set oauth/consumer/enable_integration_as_bearer 1
        ```

ขั้นตอนนี้จำเป็นจนกว่า n8n จะอัปเดต credentials ของ Magento 2 ให้ใช้ OAuth อ้างอิง [Integration Tokens](https://developer.adobe.com/commerce/webapi/get-started/authentication/gs-authentication-token/#integration-tokens){:target=_blank .external-link} สำหรับข้อมูลเพิ่มเติม

## Supported authentication methods

- API access token

## Related resources

อ้างอิง [Magento's API documentation](https://devdocs.magento.com/redoc/2.3/){:target=_blank .external-link} สำหรับข้อมูลเพิ่มเติมเกี่ยวกับบริการนี้

## Using API access token

ในการกำหนดค่า credential นี้ คุณจะต้องมี:

- **Host**: ป้อนที่อยู่ของร้านค้า Magento ของคุณ
- **Access Token**: รับ access token จาก [**Admin Panel**](https://docs.magento.com/user-guide/stores/admin.html){:target=_blank .external-link}:
    1. ไปที่ **System > Extensions > Integrations**
    2. เพิ่ม Integration ใหม่
    3. ไปที่แท็บ **API** และเลือก Magento resources ที่คุณต้องการให้ n8n integration เข้าถึง
    4. จากหน้า **Integrations** **Activate** integration ใหม่
    5. เลือก **Allow** เพื่อแสดง access token ของคุณเพื่อให้คุณสามารถคัดลอกและป้อนลงใน n8n
