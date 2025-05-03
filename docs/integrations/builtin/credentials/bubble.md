---
#https://www.notion.so/n8n/Frontmatter-432c2b8dff1f43d4b1c8d20075510fe4
title: ข้อมูลรับรอง Bubble
description: เอกสารข้อมูลรับรอง Bubble ใช้ข้อมูลนี้เพื่อยืนยันตัวตน Bubble ใน n8n
contentType: [integration, reference]
priority: medium
---

# Bubble credentials

คุณสามารถใช้ credentials นี้เพื่อเชื่อมต่อกับ node เหล่านี้:

- [Bubble](/integrations/builtin/app-nodes/n8n-nodes-base.bubble.md)

/// note | API access
ต้องใช้แพลนแบบเสียเงินถึงจะใช้ Bubble APIs ได้
///

## วิธีการยืนยันตัวตนที่รองรับ

- API key

## แหล่งข้อมูลที่เกี่ยวข้อง

ดูรายละเอียดเพิ่มเติมเกี่ยวกับการใช้งาน API ได้ที่ [เอกสาร API ของ Bubble](https://manual.bubble.io/help-guides/integrations/api){:target=_blank .external-link}

## การใช้ API key

ถ้าจะตั้งค่า credentials นี้ คุณต้องมีบัญชี [Bubble](https://bubble.io){:target=_blank .external-link} แบบเสียเงิน และ:

- **API Token**
- **App Name**
- **Domain** ถ้าใช้ custom domain

วิธีตั้งค่า:

1. ไปที่หน้า [**Apps**](https://bubble.io/home/apps){:target=_blank .external-link} ใน Bubble
2. เลือก **Create an app**
3. ตั้งชื่อ app เช่น `n8n-integration`
4. เลือก **Get started** รายละเอียด app จะเปิดขึ้น
5. ในเมนูซ้าย เลือก **Settings** (ไอคอนรูปเฟือง)
6. เลือกแท็บ **API**
7. ในส่วน **Public API Endpoints** ให้ติ๊กถูกที่ **Enable Data API**
8. จะเห็น **Data API root URL** เช่น `https://n8n-integration.bubbleapps.io/version-test/api/1.1/obj`
9. คัดลอกส่วนของ URL หลัง `https://` และก่อน `.bubbleapps.io` ไปใส่ใน n8n เป็น **App Name** เช่นตัวอย่างข้างบนคือ `n8n-integration`
10. เลือก **Generate a new API token**
11. ตั้งชื่อ **API Token Label** เช่น `n8n integration`
12. คัดลอก **Private key** ไปใส่ใน n8n เป็น **API Token**
    - ดูวิธีสร้าง token เพิ่มเติมที่ [Data API | Authentication](https://manual.bubble.io/core-resources/api/the-bubble-api/the-data-api/authentication){:target=_blank .external-link}
13. ใน n8n เลือก **Environment** ให้ตรงกับ app:
    - เลือก **Development** ถ้ายังไม่ได้ deploy ใช้ URL `https://appname.bubbleapps.io/version-test` หรือ `https://www.mydomain.com/version-test`
    - เลือก **Live** ถ้า deploy แล้ว ใช้ URL `https://appname.bubbleapps.io` หรือ `https://www.mydomain.com`
14. ใน n8n เลือก **Hosting**:
    - ถ้าไม่ได้ใช้ custom domain เลือก **Bubble Hosting**
    - ถ้าใช้ [custom domain](https://manual.bubble.io/help-guides/getting-started/navigating-the-bubble-editor/tabs-and-sections/settings-tab/custom-domain-and-dns){:target=_blank .external-link} เลือก **Self Hosted** แล้วใส่ **Domain** ของคุณ

ดูข้อมูลเพิ่มเติมที่ [การสร้างและจัดการแอป](https://manual.bubble.io/help-guides/getting-started/creating-and-managing-apps){:target=_blank .external-link}
