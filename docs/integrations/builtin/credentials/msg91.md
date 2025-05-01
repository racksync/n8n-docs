---
#https://www.notion.so/n8n/Frontmatter-432c2b8dff1f43d4b1c8d20075510fe4
title: MSG91 credentials
description: Documentation for MSG91 credentials. Use these credentials to authenticate MSG91 in n8n, a workflow automation platform.
contentType: [integration, reference]
---

# MSG91 credentials

คุณสามารถใช้ credentials เหล่านี้เพื่อยืนยันตัวตนใน nodes ต่อไปนี้:

- [MSG91](/integrations/builtin/app-nodes/n8n-nodes-base.msg91.md)

## Prerequisites

สร้างบัญชี [MSG91](https://msg91.com/){:target=_blank .external-link}

## Supported authentication methods

- API key

## Related resources

อ้างอิง [MSG91's API documentation](https://docs.msg91.com/overview){:target=_blank .external-link} สำหรับข้อมูลเพิ่มเติมเกี่ยวกับบริการนี้

## Using API key

ในการกำหนดค่า credential นี้ คุณจะต้องมี:

- **Authentication Key**: หากต้องการรับ Authentication Key ของคุณ ให้ไปที่เมนูผู้ใช้และเลือก **Authkey** อ้างอิงเอกสาร [Where can I find my authentication key? documentation](https://msg91.com/help/where-can-i-find-my-authentication-key){:target=_blank .external-link} ของ MSG91 สำหรับข้อมูลเพิ่มเติม

## IP Security

MSG91 เปิดใช้งาน [IP Security](https://msg91.com/help/what-do-you-mean-by-api-security){:target=_blank .external-link} โดยค่าเริ่มต้นสำหรับ authkeys

เพื่อให้ credentials ของ n8n ทำงานได้เมื่อเปิดใช้งานการตั้งค่านี้ ให้เพิ่ม [n8n IP addresses](/manage-cloud/cloud-ip.md) ทั้งหมดเป็น IP ที่อนุญาต (whitelisted IPs) ใน MSG91 คุณสามารถเพิ่มได้ในสองที่ ขึ้นอยู่กับระดับความปลอดภัยที่คุณต้องการ:

- หากต้องการอนุญาตให้ authkeys ใดๆ/ทั้งหมดในบัญชีทำงานกับ n8n ได้ ให้เพิ่ม n8n IP addresses ในส่วน **Company's whitelisted IPs** ของหน้า **Authkey**
- หากต้องการอนุญาตให้เฉพาะ authkeys ที่ระบุทำงานกับ n8n ได้ ให้เพิ่ม n8n IP addresses ในส่วน **Whitelisted IPs** ของรายละเอียด authkey
