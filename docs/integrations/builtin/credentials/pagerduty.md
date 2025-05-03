---
#https://www.notion.so/n8n/Frontmatter-432c2b8dff1f43d4b1c8d20075510fe4
title: ข้อมูลยืนยันตัวตน PagerDuty
description: เอกสารสำหรับข้อมูลยืนยันตัวตน PagerDuty ใช้ข้อมูลนี้เพื่อยืนยันตัวตน PagerDuty ใน n8n แพลตฟอร์ม workflow automation
contentType: [integration, reference]
---

# PagerDuty credentials

คุณสามารถใช้ credentials นี้เพื่อยืนยันตัวตนกับ node ต่อไปนี้ได้:

- [PagerDuty](/integrations/builtin/app-nodes/n8n-nodes-base.pagerduty.md)

## Prerequisites

สร้าง [PagerDuty](https://pagerduty.com/){:target=_blank .external-link} account

## Supported authentication methods

- API token
- OAuth2

## Related resources

ดูข้อมูลเพิ่มเติมเกี่ยวกับบริการนี้ได้ที่ [PagerDuty's API documentation](https://developer.pagerduty.com/docs/531092d4c6658-rest-api-v2-overview){:target=_blank .external-link}

## Using API token

สำหรับการตั้งค่า credentials นี้ คุณจะต้องมี:

- general access **API Token**: หากต้องการสร้าง API token ให้ไปที่ **Integrations > Developer Tools > API Access Keys > Create New API Key** ดูข้อมูลเพิ่มเติมที่ [Generate a General Access REST API key](https://support.pagerduty.com/docs/api-access-keys#generate-a-general-access-rest-api-key){:target=_blank .external-link}

## Using OAuth2

--8<-- "_snippets/integrations/builtin/credentials/cloud-oauth-button.md"

หากคุณต้องการกำหนดค่า OAuth2 ตั้งแต่ต้น ให้ [register a new Pagerduty app](https://developer.pagerduty.com/docs/dd91fbd09a1a1-register-an-app){:target=_blank .external-link}

ใช้การตั้งค่าเหล่านี้สำหรับการลงทะเบียน app ของคุณ:

- ใน dropdown list **Category** เลือก **Infrastructure Automation**
- ในส่วน **Functionality** เลือก **OAuth 2.0**

เมื่อคุณ **Save** app ของคุณแล้ว ให้เปิดรายละเอียด app และ [edit your app configuration](https://developer.pagerduty.com/docs/dd91fbd09a1a1-register-an-app#editing-your-app-configuration){:target=_blank .external-link} เพื่อใช้การตั้งค่าเหล่านี้:

- ภายในส่วน **OAuth 2.0** เลือก **Add**
- คัดลอก **OAuth Callback URL** จาก n8n และวางลงในฟิลด์ **Redirect URL**
- คัดลอก **Client ID** และ **Client Secret** จาก PagerDuty และเพิ่มลงใน n8n credentials ของคุณ
- เลือก **Read/Write** จาก dropdown list **Set Permission Scopes**

ดูข้อมูลเพิ่มเติมเกี่ยวกับฟังก์ชันการทำงานที่มีอยู่ใน [App functionality](https://developer.pagerduty.com/docs/b25fd1b8acb1b-app-functionality){:target=_blank .external-link} ดูข้อมูลเพิ่มเติมเกี่ยวกับ OAuth flow ได้ที่ [OAuth Functionality documentation](https://developer.pagerduty.com/docs/f59fdbd94ceab-o-auth-functionality){:target=_blank .external-link} ของ PagerDuty


