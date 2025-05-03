---
#https://www.notion.so/n8n/Frontmatter-432c2b8dff1f43d4b1c8d20075510fe4
title: เอกสารคู่มือโหนด Stripe
description: เรียนรู้วิธีใช้โหนด Stripe ใน n8n ดูเอกสารทางเทคนิคเพื่อผสานโหนด Stripe เข้ากับ workflow ของคุณ
contentType: [integration, reference]
---

# Stripe node

ใช้ Stripe node เพื่อช่วยให้งานใน Stripe เป็นไปโดยอัตโนมัติและเชื่อมต่อกับแอปพลิเคชันอื่น ๆ ได้ง่ายดาย. n8n รองรับฟีเจอร์ของ Stripe หลากหลาย เช่น การเช็ค balance, สร้าง charge, และการลบลูกค้า.

/// note | Credentials
ดู [Stripe credentials](/integrations/builtin/credentials/stripe.md) สำหรับคำแนะนำในการตั้งค่า authentication.
///

## Operations

* Balance
    * Get a balance
* Charge
    * Create a charge
    * Get a charge
    * Get all charges
    * Update a charge
* Coupon
    * Create a coupon
    * Get all coupons
* Customer
    * Create a customer
    * Delete a customer
    * Get a customer
    * Get all customers
    * Update a customer
* Customer Card
    * Add a customer card
    * Get a customer card
    * Remove a customer card
* Source
    * Create a source
    * Delete a source
    * Get a source
* Token
    * Create a token

## Templates and examples

<!-- see https://www.notion.so/n8n/Pull-in-templates-for-the-integrations-pages-37c716837b804d30a33b47475f6e3780 -->
[[ templatesWidget(page.title, 'stripe') ]]

--8<-- "_snippets/integrations/builtin/app-nodes/operation-not-supported.md"
