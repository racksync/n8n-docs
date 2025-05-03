---
#https://www.notion.so/n8n/Frontmatter-432c2b8dff1f43d4b1c8d20075510fe4
title: คู่มือการตั้งค่า WooCommerce credentials
description: วิธีตั้งค่า WooCommerce credentials เพื่อเชื่อมต่อและยืนยันตัวตนกับ WooCommerce ใน n8n
contentType: [integration, reference]
priority: medium
---

# WooCommerce credentials

คุณสามารถใช้ credentials เหล่านี้เพื่อยืนยันตัวตนกับ node ต่อไปนี้:

- [WooCommerce](/integrations/builtin/app-nodes/n8n-nodes-base.woocommerce.md)
- [WooCommerce Trigger](/integrations/builtin/trigger-nodes/n8n-nodes-base.woocommercetrigger.md)

## Prerequisites

- ติดตั้ง [WooCommerce](https://woocommerce.com/){:target=_blank .external-link} plugin บนเว็บไซต์ WordPress ของคุณ
- ใน WordPress ไปที่ **Settings > Permalinks** แล้วตั้งค่า permalinks ของ WordPress ให้ใช้แบบอื่นที่ไม่ใช่ **Plain**

## Supported authentication methods

- API key

## Related resources

ดูข้อมูลเพิ่มเติมเกี่ยวกับบริการนี้ได้ที่ [WooCommerce's REST API documentation](https://developer.woocommerce.com/docs/getting-started-with-the-woocommerce-rest-api/){:target=_blank .external-link}

## Using API key

ในการตั้งค่า credential นี้ คุณจะต้องมี:

- **Consumer Key**: สร้างขึ้นเมื่อคุณ generate API key
- **Consumer Secret**: สร้างขึ้นเมื่อคุณ generate API key
- **WooCommerce URL**

วิธีสร้าง API key และตั้งค่า credential:

1. ไปที่ **WooCommerce > Settings > Advanced > Rest API > Add key**
2. เลือก **Read/Write** ที่ **Permissions**
3. คัดลอก **Consumer Key** และ **Consumer Secret** ที่ได้มาใส่ใน n8n credentials
4. ใส่ URL เว็บไซต์ WordPress ของคุณใน **WooCommerce URL**
5. โดยปกติ n8n จะส่งข้อมูล credential ผ่าน Authorization header ถ้าคุณต้องการส่งผ่าน query string parameter ให้เปิด **Include Credentials in Query**

ดูรายละเอียดเพิ่มเติมได้ที่ [Generate Keys](https://developer.woocommerce.com/docs/getting-started-with-the-woocommerce-rest-api/#3-generate-keys){:target=_blank .external-link}

## Resolve "Consumer key is missing" error

ถ้าคุณเชื่อมต่อ credential แล้วเจอ error ประมาณนี้: `Consumer key is missing`

สาเหตุเกิดจาก server ไม่สามารถอ่าน Authorization header ได้เมื่อยืนยันตัวตนผ่าน SSL

วิธีแก้ไข ให้เปิด toggle **Include Credentials in Query** เพื่อส่ง consumer key/secret ผ่าน query string แทน แล้วลองเชื่อมต่อ credential ใหม่อีกครั้ง
