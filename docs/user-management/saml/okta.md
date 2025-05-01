---
#https://www.notion.so/n8n/Frontmatter-432c2b8dff1f43d4b1c8d20075510fe4
title: Okta Workforce Identity SAML setup
description: Use Okta Workforce Identity with n8n.
contentType: tutorial
---

# Okta Workforce Identity SAML setup

ตั้งค่า SAML SSO ใน n8n ด้วย Okta

/// note | Workforce Identity and Customer Identity
คู่มือนี้ครอบคลุมการตั้งค่า Workforce Identity ซึ่งเป็นผลิตภัณฑ์ดั้งเดิมของ Okta ส่วน Customer Identity เป็นชื่อที่ Okta ใช้เรียก Auth0 ซึ่งพวกเขาได้เข้าซื้อกิจการมา
///
## Prerequisites

คุณต้องมีบัญชี Okta Workforce Identity และ redirect URL กับ entity ID จากการตั้งค่า SAML ของ n8n

Okta Workforce อาจบังคับใช้ two factor authentication สำหรับผู้ใช้ ขึ้นอยู่กับการกำหนดค่า Okta ของคุณ

อ่านคู่มือ [Set up SAML](/user-management/saml/setup.md) ก่อน

## Setup

1. ใน Okta admin panel ของคุณ เลือก **Applications** > **Applications**
2. เลือก **Create App Integration** Okta จะเปิด modal สำหรับสร้าง app
3. เลือก **SAML 2.0** จากนั้นเลือก **Next**
4. บนแท็บ **General Settings** ป้อน `n8n` เป็น **App name**
5. เลือก **Next**
6. บนแท็บ **Configure SAML** กรอกข้อมูลในช่อง **General** ต่อไปนี้:
    * **Single sign-on URL**: **Redirect URL** จาก n8n
    * **Audience URI (SP Entity ID)**: **Entity ID** จาก n8n
    * **Default RelayState**: เว้นว่างไว้
    * **Name ID format**: `EmailAddress`
    * **Application username**: `Okta username`
    * **Update application username on**: `Create and update`
7. สร้าง **Attribute Statements**:

    | **Name** | **Name format** | **Value** |
    | -------- | --------------- | --------- |
    | http://schemas.xmlsoap.org/ws/2005/05/identity/claims/firstname | URI Reference | user.firstName |
    | http://schemas.xmlsoap.org/ws/2005/05/identity/claims/lastname | URI Reference | user.lastName |
    | http://schemas.xmlsoap.org/ws/2005/05/identity/claims/upn | URI Reference | user.login |
    | http://schemas.xmlsoap.org/ws/2005/05/identity/claims/emailaddress | URI Reference | user.email |

8. เลือก **Next** Okta อาจแจ้งให้คุณกรอกแบบฟอร์มการตลาด หรืออาจนำคุณไปยัง n8n Okta app ใหม่ของคุณโดยตรง
9. กำหนด n8n app ให้กับผู้คน:
    1. บน n8n app dashboard ใน Okta เลือก **Assignments**
    2. เลือก **Assign** > **Assign to People** Okta จะแสดง modal พร้อมรายชื่อผู้ใช้ที่มีอยู่
    3. เลือก **Assign** ถัดจากบุคคลที่คุณต้องการเพิ่ม Okta จะแสดง prompt เพื่อยืนยัน username
    4. ปล่อย username เป็น email address เลือก **Save and Go Back**
    5. เลือก **Done**
10. รับ metadata XML: บนแท็บ **Sign On** คัดลอก Metadata URL ไปที่ URL นั้น แล้วคัดลอก XML นำไปวางใน **Identity Provider Settings** ใน n8n
11. เลือก **Save settings**
12. เลือก **Test settings** n8n จะเปิดแท็บใหม่ หากคุณยังไม่ได้ login Okta จะแจ้งให้คุณ sign in จากนั้น n8n จะแสดงข้อความยืนยันความสำเร็จพร้อมกับ attributes ที่ได้รับจาก Okta

