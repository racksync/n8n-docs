---
#https://www.notion.so/n8n/Frontmatter-432c2b8dff1f43d4b1c8d20075510fe4
title: Mattermost credentials
description: Documentation for Mattermost credentials. Use these credentials to authenticate Mattermost in n8n, a workflow automation platform.
contentType: [integration, reference]
priority: medium
---

# Mattermost credentials

คุณสามารถใช้ credentials เหล่านี้เพื่อยืนยันตัวตนใน nodes ต่อไปนี้:

- [Mattermost](/integrations/builtin/app-nodes/n8n-nodes-base.mattermost.md)

## Supported authentication methods

- API access token

## Related resources

อ้างอิง [Mattermost's API documentation](https://api.mattermost.com/){:target=_blank .external-link} สำหรับข้อมูลเพิ่มเติมเกี่ยวกับบริการนี้

## Using API access token

ในการกำหนดค่า credential นี้ คุณจะต้องมีบัญชี [Mattermost](https://www.mattermost.com/){:target=_blank .external-link} และ:

- **Access Token** ส่วนตัว
- **Base URL** ของ Mattermost ของคุณ

วิธีตั้งค่า:

1. ใน Mattermost ไปที่ **Profile > Security > Personal Access Tokens**

    /// warning | No Personal Access Tokens option
    หากคุณไม่เห็นตัวเลือก Personal Access Tokens อ้างอิงขั้นตอนการแก้ไขปัญหาใน [Enable personal access tokens](#enable-personal-access-tokens) ด้านล่าง
    ///

2. เลือก **Create Token**
3. ป้อน **Token description** เช่น `n8n integration`
4. เลือก **Save**
5. คัดลอก **Token ID** และป้อนเป็น **Access Token** ใน credential ของ n8n
6. ป้อน Mattermost URL ของคุณเป็น **Base URL**
7. โดยค่าเริ่มต้น n8n จะเชื่อมต่อเฉพาะเมื่อการตรวจสอบใบรับรอง SSL สำเร็จ หากต้องการเชื่อมต่อแม้ว่าการตรวจสอบใบรับรอง SSL จะล้มเหลว ให้เปิดใช้งาน **Ignore SSL Issues**

อ้างอิงเอกสาร Mattermost [Personal access tokens documentation](https://developers.mattermost.com/integrate/reference/personal-access-token/){:target=_blank .external-link} สำหรับข้อมูลเพิ่มเติม

## Enable personal access tokens

การไม่เห็นตัวเลือก **Personal Access Tokens** มีสาเหตุที่เป็นไปได้สองประการ:

- Mattermost ไม่ได้เปิดใช้งาน integration personal access tokens
- คุณกำลังพยายามสร้าง personal access token ในฐานะผู้ใช้ที่ไม่ใช่ผู้ดูแลระบบซึ่งไม่มีสิทธิ์ในการสร้าง personal access tokens

วิธีระบุสาเหตุและแก้ไข:

1. เข้าสู่ระบบ Mattermost ในฐานะผู้ดูแลระบบ
2. ไปที่ **System Console > Integrations > Integration Management**
3. ยืนยันว่า **Enable personal access tokens** ตั้งค่าเป็น **true** หากไม่ ให้เปลี่ยน
4. ไปที่ **System Console > User Management > Users**
5. ค้นหาบัญชีผู้ใช้ที่คุณต้องการอนุญาตให้สร้าง personal access tokens
6. เลือกเมนู **Actions** สำหรับผู้ใช้และเลือก **Manage roles**
7. ทำเครื่องหมายที่ช่องสำหรับ **Allow this account to generate personal access tokens** และ **Save**

อ้างอิงเอกสาร Mattermost [Personal access tokens documentation](https://developers.mattermost.com/integrate/reference/personal-access-token/){:target=_blank .external-link} สำหรับข้อมูลเพิ่มเติม
