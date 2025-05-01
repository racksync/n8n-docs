---
#https://www.notion.so/n8n/Frontmatter-432c2b8dff1f43d4b1c8d20075510fe4
title: FileMaker credentials
description: Documentation for FileMaker credentials. Use these credentials to authenticate FileMaker in n8n, a workflow automation platform.
contentType: [integration, reference]
priority: medium
---

# FileMaker credentials

คุณสามารถใช้ credentials เหล่านี้เพื่อยืนยันตัวตนกับ node ต่อไปนี้:

- [FileMaker](/integrations/builtin/app-nodes/n8n-nodes-base.filemaker.md)

## Prerequisites

- สร้างบัญชีผู้ใช้บน [FileMaker Server](https://www.claris.com/filemaker/){:target=_blank .external-link} พร้อมสิทธิ์ขยาย `fmrest` เพื่อ [Access the FileMaker Data API](https://help.claris.com/en/data-api-guide/content/enable-access.html){:target=_blank .external-link}
- ตรวจสอบให้แน่ใจว่า FileMaker Server สามารถใช้ [FileMaker Data API](https://help.claris.com/en/data-api-guide/content/index.html){:target=_blank .external-link} ได้:
    1. เตรียมฐานข้อมูลของคุณสำหรับการเข้าถึง FileMaker Data API โดยใช้ FileMaker Pro คุณสามารถสร้างฐานข้อมูลหรือเตรียมฐานข้อมูลที่มีอยู่ได้
        - ดูข้อมูลเพิ่มเติมได้ที่ [Prepare databases for FileMaker Data API access](https://help.claris.com/en/data-api-guide/content/prepare-databases-for-access.html){:target=_blank .external-link}
    1. เขียนโค้ดที่เรียกใช้เมธอด FileMaker Data API เพื่อค้นหา สร้าง แก้ไข ทำซ้ำ และลบเรคคอร์ดในฐานข้อมูลที่โฮสต์
        - ดูข้อมูลเพิ่มเติมได้ที่ [Write FileMaker Data API calls](https://help.claris.com/en/data-api-guide/content/write-data-api-calls.html){:target=_blank .external-link}
    1. โฮสต์โซลูชันของคุณโดยเปิดใช้งานการเข้าถึง FileMaker Data API
        - ดูข้อมูลเพิ่มเติมได้ที่ [Host a FileMaker Data API solution](https://help.claris.com/en/data-api-guide/content/host-data-api-app.html){:target=_blank .external-link}
    1. ทดสอบว่าการเข้าถึง FileMaker Data API ทำงานได้
        - ดูข้อมูลเพิ่มเติมได้ที่ [Test the FileMaker Data API solution](https://help.claris.com/en/data-api-guide/content/test-data-api-app.html){:target=_blank .external-link}
    1. ตรวจสอบโซลูชันที่โฮสต์ของคุณโดยใช้ Admin Console
        - ดูข้อมูลเพิ่มเติมได้ที่ [Monitor FileMaker Data API solutions](https://help.claris.com/en/data-api-guide/content/monitor-data-api-app.html){:target=_blank .external-link}

## Supported authentication methods

- Database connection

## Related resources

ดูข้อมูลเพิ่มเติมเกี่ยวกับบริการนี้ได้ที่ [FileMaker's Data API Guide](https://help.claris.com/en/data-api-guide/content/index.html){:target=_blank .external-link}

## Using database connection

ในการกำหนดค่า credential นี้:

1. ป้อนชื่อ **Host** หรือ IP address ของ FileMaker Server ของคุณ
2. ป้อนชื่อ **Database** ควรตรงกับชื่อฐานข้อมูลตามที่ปรากฏในรายการ **Databases** ภายใน FileMaker
3. ป้อน **Login** ของบัญชีผู้ใช้สำหรับบัญชีที่มีสิทธิ์ขยาย `fmrest` ดูข้อมูลเพิ่มเติมได้ที่ส่วน [Prerequisites](#prerequisites) ก่อนหน้านี้
4. ป้อน **Password** สำหรับบัญชีผู้ใช้นั้น

