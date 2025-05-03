---
#https://www.notion.so/n8n/Frontmatter-432c2b8dff1f43d4b1c8d20075510fe4
title: เอกสารคู่มือ Paddle node
description: เรียนรู้วิธีใช้ Paddle node ใน n8n และดูเอกสารทางเทคนิคเพื่อเชื่อมต่อ Paddle node เข้ากับ workflow ของคุณ
contentType: [integration, reference]
---

# Paddle node

ใช้ Paddle node เพื่อช่วยทำงานใน Paddle แบบอัตโนมัติและเชื่อมต่อกับแอปพลิเคชันอื่น ๆ. n8n มีการสนับสนุนคุณสมบัติของ Paddle หลากหลาย เช่น การสร้าง, อัปเดต, และดึงข้อมูล coupons รวมถึงการดึงข้อมูล plans, products และ users.

ในหน้านี้ คุณจะพบรายการของ operations ที่ Paddle node รองรับและลิงก์สำหรับข้อมูลเพิ่มเติม.

/// note | Credentials
ดูรายละเอียดเพิ่มเติมได้ที่ [Paddle credentials](/integrations/builtin/credentials/paddle.md) สำหรับคำแนะนำในการตั้งค่า authentication. 
///

## Operations

* Coupon
    * Create a coupon.
    * Get all coupons.
    * Update a coupon.
* Payment
    * Get all payment.
    * Reschedule payment.
* Plan
    * Get a plan.
    * Get all plans.
* Product
    * Get all products.
* User
    * Get all users

## Templates and examples

<!-- see https://www.notion.so/n8n/Pull-in-templates-for-the-integrations-pages-37c716837b804d30a33b47475f6e3780 -->
[[ templatesWidget(page.title, 'paddle') ]]


