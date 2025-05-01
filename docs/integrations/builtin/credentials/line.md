---
#https://www.notion.so/n8n/Frontmatter-432c2b8dff1f43d4b1c8d20075510fe4
title: Line credentials
description: Documentation for Line credentials. Use these credentials to authenticate the Line node in n8n, a workflow automation platform.
contentType: [integration, reference]
priority: medium
---

# Line credentials

<!-- vale off -->
/// warning | Deprecated: End of service
LINE Notify จะยุติการให้บริการ ณ วันที่ 1 เมษายน 2025 และ node นี้จะไม่ทำงานอีกต่อไปหลังจากวันดังกล่าว ดูข้อมูลเพิ่มเติมได้ที่ [end of service announement](https://notify-bot.line.me/closing-announce){:target=_blank .external-link} ของ LINE Notify
///
<!-- vale on -->

คุณสามารถใช้ credentials เหล่านี้เพื่อยืนยันตัวตนกับ node ต่อไปนี้ได้:

- [Line](/integrations/builtin/app-nodes/n8n-nodes-base.line.md)

## Supported authentication methods

- Notify OAuth2

## Related resources

ดูข้อมูลเพิ่มเติมเกี่ยวกับบริการนี้ได้ที่ [Line Notify's API documentation](https://notify-bot.line.me/doc/en/){:target=_blank .external-link}

## Using Notify OAuth2

ในการตั้งค่า credential นี้ คุณจะต้องมีบัญชี [Line](https://line.me/en/){:target=_blank .external-link} และ:

- **Client ID**
- **Client Secret**

ในการสร้างทั้งสองอย่าง ให้เชื่อมต่อ Line กับ [Line Notify](https://notify-bot.line.me/en/){:target=_blank .external-link} จากนั้น:

1.  เปิดหน้า Line Notify เพื่อ [add a new service](https://notify-bot.line.me/my/services/new){:target=_blank .external-link}
2.  ป้อน **Service name** ชื่อนี้จะแสดงเมื่อมีคนพยายามเชื่อมต่อกับบริการ
3.  ป้อน **Service description**
4.  ป้อน **Service URL**
5.  ป้อน **Company/Enterprise** ของคุณ
6.  เลือก **Country/region** ของคุณ
7.  ป้อนชื่อของคุณหรือชื่อทีมเป็น **Representative**
8.  ป้อน **Email address** ที่ถูกต้อง Line จะยืนยันที่อยู่อีเมลนี้ก่อนที่บริการจะลงทะเบียนเสร็จสมบูรณ์ ใช้อีเมลที่คุณสามารถเข้าถึงได้ทันที
9.  คัดลอก **OAuth Redirect URL** จาก n8n credential ของคุณและป้อนเป็น **Callback URL** ใน Line Notify
10. เลือก **Agree and continue** เพื่อยอมรับข้อกำหนดในการให้บริการ
11. ตรวจสอบว่าข้อมูลที่คุณป้อนถูกต้องและเลือก **Add**
12. ตรวจสอบอีเมลของคุณและเปิด Line Notify Registration URL เพื่อยืนยันที่อยู่อีเมลของคุณ
13. เมื่อการยืนยันเสร็จสมบูรณ์ ให้เปิด [**My services**](https://notify-bot.line.me/my/services/){:target=_blank .external-link}
14. เลือกบริการที่คุณเพิ่งเพิ่ม
15. คัดลอก **Client ID** และป้อนลงใน n8n credential ของคุณ
16. เลือกตัวเลือกเพื่อ **Display** **Client Secret** คัดลอก **Client Secret** และป้อนลงใน n8n credential ของคุณ
17. ใน n8n เลือก **Connect my account** และทำตามคำแนะนำบนหน้าจอเพื่อสิ้นสุดการตั้งค่า credential

ดูข้อมูลเพิ่มเติมได้ที่ส่วน Authentication ของ [Line Notify's API documentation](https://notify-bot.line.me/doc/en/){:target=_blank .external-link}
