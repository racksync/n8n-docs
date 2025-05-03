---
#https://www.notion.so/n8n/Frontmatter-432c2b8dff1f43d4b1c8d20075510fe4
title: เอกสารคู่มือ PayPal node
description: เรียนรู้วิธีใช้ PayPal node ใน n8n และดูเอกสารทางเทคนิคเพื่อเชื่อมต่อ PayPal node เข้ากับ workflow ของคุณ
contentType: [integration, reference]
---

# PayPal node

ใช้ PayPal node เพื่อช่วยทำงานใน PayPal แบบอัตโนมัติและเชื่อมต่อกับแอปพลิเคชันอื่น ๆ. n8n มีการสนับสนุนคุณสมบัติของ PayPal หลากหลาย เช่น การสร้าง batch payout และการยกเลิก payout items ที่ยังไม่ได้รับ.

ในหน้านี้ คุณจะพบรายการของ operations ที่ PayPal node รองรับและลิงก์สำหรับข้อมูลเพิ่มเติม.

/// note | Credentials
ดูรายละเอียดเพิ่มเติมได้ที่ [PayPal credentials](/integrations/builtin/credentials/paypal.md) สำหรับคำแนะนำในการตั้งค่า authentication.
///

## Operations

* Payout
    * Create a batch payout
    * Show batch payout details
* Payout Item
    * Cancels an unclaimed payout item
    * Show payout item details

## Templates and examples

<!-- see https://www.notion.so/n8n/Pull-in-templates-for-the-integrations-pages-37c716837b804d30a33b47475f6e3780 -->
[[ templatesWidget(page.title, 'paypal') ]]
