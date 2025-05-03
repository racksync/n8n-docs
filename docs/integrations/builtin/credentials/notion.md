---
title: ข้อมูลยืนยันตัวตน Notion
description: เอกสารสำหรับการยืนยันตัวตน Notion. ใช้ข้อมูลเหล่านี้เพื่อยืนยันตัวตน Notion ใน n8n.
contentType: [integration, reference]
priority: high
---

# Notion credentials

คุณสามารถใช้ credentials เหล่านี้เพื่อยืนยันตัวตนใน nodes ต่อไปนี้:

- [Notion](/integrations/builtin/app-nodes/n8n-nodes-base.notion/index.md)
- [Notion Trigger](/integrations/builtin/trigger-nodes/n8n-nodes-base.notiontrigger.md)

## Prerequisites

สร้างบัญชี [Notion](https://notion.so){:target=_blank .external-link} ที่มีสิทธิ์ระดับ admin

## Supported authentication methods

- API integration token: ใช้สำหรับ internal integrations
- OAuth2: ใช้สำหรับ public integrations

/// note | Integration type
ไม่แน่ใจว่าจะใช้ integration type ไหน? อ้างอิง [Internal vs. public integrations](#internal-vs-public-integrations) ด้านล่างสำหรับข้อมูลเพิ่มเติม
///

## Related resources

อ้างอิง [Notion's API documentation](https://developers.notion.com/reference/intro){:target=_blank .external-link} สำหรับข้อมูลเพิ่มเติมเกี่ยวกับบริการนี้

## Using API integration token

ในการกำหนดค่า credential นี้ คุณจะต้องมี:

- **Internal Integration Secret**: สร้างขึ้นเมื่อคุณสร้าง Notion integration

วิธีสร้าง integration secret ให้ [สร้าง Notion integration](https://developers.notion.com/docs/create-a-notion-integration#create-your-integration-in-notion){:target=_blank .external-link} และรับ integration secret จากแท็บ **Secrets**:

1. ไปที่ [integration dashboard](https://www.notion.com/my-integrations){:target=_blank .external-link} ของ Notion
2. เลือกปุ่ม **+ New integration**
3. ป้อน **Name** สำหรับ integration ของคุณ เช่น `n8n integration` หากต้องการ ให้เพิ่ม **Logo**
4. เลือก **Submit** เพื่อสร้าง integration ของคุณ
5. เปิดแท็บ **Capabilities** เลือก capabilities เหล่านี้:
    - `Read content`
    - `Update content`
    - `Insert content`
    - `User information without email addresses`
6. อย่าลืม **Save changes**
7. เลือกแท็บ **Secrets**
8. คัดลอก **Internal Integration Token** และเพิ่มเป็น **Internal Integration Secret** ของ n8n

อ้างอิงเอกสาร [Internal integration auth flow setup documentation](https://developers.notion.com/docs/authorization#internal-integration-auth-flow-set-up){:target=_blank .external-link} สำหรับข้อมูลเพิ่มเติมเกี่ยวกับการยืนยันตัวตนกับบริการ

### Share Notion page(s) with the integration

เพื่อให้ integration ของคุณโต้ตอบกับ Notion ได้ คุณต้อง [ให้สิทธิ์ integration ของคุณในการเข้าถึง page](https://developers.notion.com/docs/create-a-notion-integration#give-your-integration-page-permissions){:target=_blank .external-link} ใน Notion workspace ของคุณ:

1. ไปที่ page ใน Notion workspace ของคุณ
2. เลือกเมนูสามจุดที่มุมขวาบนของ page
3. ใน **Connections** เลือก **Connect to**
4. ใช้แถบค้นหาเพื่อค้นหาและเลือก integration ของคุณจากรายการดรอปดาวน์

เมื่อคุณแชร์อย่างน้อยหนึ่ง page กับ integration แล้ว คุณสามารถเริ่มส่งคำขอ API ได้ หาก page ไม่ได้ถูกแชร์ คำขอ API ใดๆ ที่ส่งไปจะตอบกลับด้วยข้อผิดพลาด

อ้างอิง [Integration permissions](https://developers.notion.com/docs/authorization#integration-permissions){:target=_blank .external-link} สำหรับข้อมูลเพิ่มเติม

## Using OAuth2

ในการกำหนดค่า credential นี้ คุณจะต้องมี:

- **Client ID**: สร้างขึ้นเมื่อคุณกำหนดค่า public integration
- **Client Secret**: สร้างขึ้นเมื่อคุณกำหนดค่า public integration

คุณต้อง [สร้าง Notion integration](https://developers.notion.com/docs/create-a-notion-integration#create-your-integration-in-notion){:target=_blank .external-link} และตั้งค่าเป็นการเผยแพร่แบบสาธารณะ (public distribution):

1. ไปที่ [integration dashboard](https://www.notion.com/my-integrations){:target=_blank .external-link} ของ Notion
2. เลือกปุ่ม **+ New integration**
3. ป้อน **Name** สำหรับ integration ของคุณ เช่น `n8n integration` หากต้องการ ให้เพิ่ม **Logo**
4. เลือก **Submit** เพื่อสร้าง integration ของคุณ
5. เปิดแท็บ **Capabilities** เลือก capabilities เหล่านี้:
    - `Read content`
    - `Update content`
    - `Insert content`
    - `User information without email addresses`
6. เลือก **Save changes**
7. ไปที่แท็บ **Distribution**
8. เปิดใช้งานตัวควบคุม **Do you want to make this integration public?**
9. ป้อนชื่อบริษัทและเว็บไซต์ของคุณในส่วน **Organization Information**
10. คัดลอก **OAuth Redirect URL** ของ n8n และเพิ่มเป็น **Redirect URI** ในส่วน **OAuth Domain & URLs** ของ Notion integration
11. ไปที่แท็บ **Secrets**
12. คัดลอก **Client ID** และ **Client Secret** และเพิ่มลงใน credential ของ n8n

อ้างอิง [public integration auth flow setup](https://developers.notion.com/docs/authorization#public-integration-auth-flow-set-up){:target=_blank .external-link} ของ Notion สำหรับข้อมูลเพิ่มเติมเกี่ยวกับการยืนยันตัวตนกับบริการ

## Internal vs. public integrations

**Internal** integrations คือ:

* เฉพาะสำหรับ workspace เดียว
* เข้าถึงได้เฉพาะสมาชิกของ workspace นั้น
* เหมาะสำหรับการปรับปรุง workspace แบบกำหนดเอง

Internal integrations ใช้กระบวนการยืนยันตัวตนที่ง่ายกว่า (integration secret) และไม่ต้องมีการตรวจสอบความปลอดภัยก่อนเผยแพร่

**Public** integrations คือ:

* ใช้งานได้ในหลาย Notion workspaces ที่ไม่เกี่ยวข้องกัน
* เข้าถึงได้โดยผู้ใช้ Notion ทุกคน โดยไม่คำนึงถึง workspace ของพวกเขา
* เหมาะสำหรับกรณีการใช้งานที่หลากหลาย

Public integrations ใช้โปรโตคอล OAuth 2.0 สำหรับการยืนยันตัวตน ต้องมีการตรวจสอบความปลอดภัยของ Notion ก่อนเผยแพร่

สำหรับรายละเอียดเพิ่มเติมเกี่ยวกับ integration ทั้งสองประเภท อ้างอิงเอกสาร [Internal vs. Public Integrations documentation](https://developers.notion.com/docs/getting-started#internal-vs-public-integrations){:target=_blank .external-link} ของ Notion
