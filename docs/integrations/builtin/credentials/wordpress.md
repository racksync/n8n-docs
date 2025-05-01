---
#https://www.notion.so/n8n/Frontmatter-432c2b8dff1f43d4b1c8d20075510fe4
title: WordPress credentials
description: Documentation for WordPress credentials. Use these credentials to authenticate WordPress in n8n, a workflow automation platform.
contentType: [integration, reference]
priority: medium
---

# WordPress credentials

คุณสามารถใช้ credentials นี้เพื่อเชื่อมต่อกับ node เหล่านี้:

- [WordPress](/integrations/builtin/app-nodes/n8n-nodes-base.wordpress.md)

## Prerequisites

- สมัคร [WordPress](https://wordpress.com/){:target=_blank .external-link} หรือ deploy WordPress บน server ของคุณ

## Supported authentication methods

- Basic auth

## Related resources

ดูรายละเอียดเพิ่มเติมเกี่ยวกับการใช้งาน API ได้ที่ [WordPress's API documentation](https://developer.wordpress.com/docs/api/){:target=_blank .external-link}

## Using basic auth

ถ้าจะตั้งค่า credentials นี้ คุณต้องมี:

- **Username** ของ WordPress
- **Password** ของแอปพลิเคชัน WordPress
- **WordPress URL** ของคุณ
- ตัดสินใจว่าจะ **Ignore SSL Issues** หรือไม่

การใช้งาน credentials นี้มี 3 ขั้นตอน:

1. [Enable two-step authentication](#enable-two-step-authentication)
2. [Create an application password](#create-an-application-password)
3. [Set up the credential](#set-up-the-credential)

ดูวิธีทำแต่ละขั้นตอนด้านล่าง

### Enable two-step authentication

ก่อนจะสร้าง application password ต้องเปิด Two-Step Authentication ใน WordPress ก่อน ถ้าเปิดแล้ว [ข้ามไปขั้นตอนถัดไป](#create-an-application-password) ได้เลย

1. เปิดหน้า [profile](https://wordpress.com/me){:target=_blank .external-link} ของคุณใน WordPress
2. เลือก **Security** จากเมนูซ้าย
3. เลือก **Two-Step Authentication** จะเข้าสู่หน้า **Two-Step Authentication**
4. ถ้ายังไม่ได้เปิด Two-Step Authentication ให้เปิดก่อน
5. เลือกว่าจะใช้แอป authenticator หรือ SMS codes แล้วทำตามขั้นตอน

ดูรายละเอียดเพิ่มเติมที่ [Enable Two-Step Authentication](https://wordpress.com/support/security/two-step-authentication/){:target=_blank .external-link}

### Create an application password

เมื่อเปิด Two-Step Authentication แล้ว สามารถสร้าง application password ได้เลย:

1. ที่หน้า **Security >** [**Two-Step Authentication**](https://wordpress.com/me/security/two-step) เลือก **+ Add new application password** ในส่วน **Application passwords**
2. ใส่ **Application name** เช่น `n8n integration`
3. เลือก **Generate Password**
4. คัดลอก password ที่ได้มา ใช้ใน n8n credential

### Set up the credential

เสร็จแล้ว! พร้อมตั้งค่า n8n credential ได้เลย:

1. ใส่ **Username** ของ WordPress ใน n8n credential
2. ใส่ application password ที่คัดลอกไว้ในช่อง **Password**
3. ใส่ URL ของ WordPress site ในช่อง **WordPress URL**
4. เลือก **Ignore SSL Issues** ถ้าต้องการให้ n8n credential เชื่อมต่อแม้ SSL certificate validation จะล้มเหลว (เปิด) หรือจะให้เช็ค SSL certificate ตามปกติ (ปิด)
