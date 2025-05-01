---
#https://www.notion.so/n8n/Frontmatter-432c2b8dff1f43d4b1c8d20075510fe4
title: SurveyMonkey credentials
description: Documentation for SurveyMonkey credentials. Use these credentials to authenticate SurveyMonkey in n8n, a workflow automation platform.
contentType: [integration, reference]
---

# SurveyMonkey credentials

คุณสามารถใช้ credentials นี้เพื่อยืนยันตัวตนกับ node ต่อไปนี้ได้:

- [SurveyMonkey Trigger](/integrations/builtin/trigger-nodes/n8n-nodes-base.surveymonkeytrigger.md)

## Prerequisites

- สร้างบัญชี [SurveyMonkey](https://www.surveymonkey.com){:target=_blank .external-link}
- [ลงทะเบียนแอป](https://api.surveymonkey.com/v3/docs?api_key=3yr7n6m8sjwvm48x8nhxej52#registering-an-app){:target=_blank .external-link} จาก [**Developer dashboard > My apps**](https://developer.surveymonkey.com/apps/){:target=_blank .external-link}
    - ดู [Required app scopes](#required-app-scopes) สำหรับ scope ที่ต้องใช้

## Supported authentication methods

- API access token
- OAuth2

## Related resources

ดูข้อมูลเพิ่มเติมเกี่ยวกับบริการนี้ได้ที่ [SurveyMonkey's API documentation](https://developer.surveymonkey.com/api/v3/#SurveyMonkey-Api){:target=_blank .external-link}

## Using API access token

ในการตั้งค่า credentials นี้ คุณจะต้องมี:

- **Access Token**: ได้หลังจากสร้างแอป
- **Client ID**: ได้หลังจากสร้างแอป
- **Client Secret**: ได้หลังจากสร้างแอป

เมื่อสร้างแอปและกำหนด scope ที่เหมาะสมแล้ว ไปที่ **Settings > Credentials** คัดลอก **Access Token**, **Client ID** และ **Secret** แล้วนำไปใส่ใน n8n

## Using OAuth

ในการตั้งค่า credentials นี้ คุณจะต้องมี:

- **Client ID**: ได้หลังจากสร้างแอป
- **Client Secret**: ได้หลังจากสร้างแอป

เมื่อสร้างแอปและกำหนด scope ที่เหมาะสมแล้ว:

1. ไปที่ **Settings > Settings** ของแอป
2. จาก n8n ให้คัดลอก **OAuth Redirect URL**
3. นำ URL นี้ไปวางแทนที่ **OAuth Redirect URL** เดิมของแอป
4. กด **Submit Changes**
5. ตรวจสอบว่าในส่วน **Scopes** มี [Required app scopes](#required-app-scopes) ครบถ้วน

จาก **Settings > Credentials** ของแอป ให้คัดลอก **Client ID** และ **Client Secret** ไปใส่ใน n8n credential แล้วเลือก **Connect my account** จาก n8n ได้เลย

/// note | SurveyMonkey Test OAuth Flow
ตัวเลือกนี้จะใช้ได้ก็ต่อเมื่อคุณยังคงใช้ **OAuth Redirect URL** ของ SurveyMonkey ที่เป็นค่าเริ่มต้น และเพิ่ม n8n OAuth Redirect URL เป็น **Additional Redirect URL**
///

## Required app scopes

หลังจากสร้างแอปแล้ว ไปที่ **Settings > Scopes** เลือก scope เหล่านี้เพื่อให้ n8n credential ใช้งานได้:

- **View Surveys**
- **View Collectors**
- **View Responses**
- **View Response Details**
- **Create/Modify Webhooks**
- **View Webhooks**

กด **Update Scopes** เพื่อบันทึก
