---
title: ข้อมูลเข้าสู่ระบบ Slack
description: คู่มือการตั้งค่า Slack credentials สำหรับเชื่อมต่อ Slack กับ n8n
contentType: [integration, reference]
priority: high
---

# Slack credentials

คุณสามารถใช้ credentials เหล่านี้เพื่อยืนยันตัวตนกับ node ต่อไปนี้:

- [Slack](/integrations/builtin/app-nodes/n8n-nodes-base.slack.md)
- [Slack Trigger](/integrations/builtin/trigger-nodes/n8n-nodes-base.slacktrigger.md)

## Supported authentication methods

- API access token:
    - จำเป็นสำหรับ [Slack Trigger](/integrations/builtin/trigger-nodes/n8n-nodes-base.slacktrigger.md) node
    - ใช้กับ [Slack](/integrations/builtin/app-nodes/n8n-nodes-base.slack.md) node ได้ แต่ไม่แนะนำ
- OAuth2:
    - เป็นวิธีที่แนะนำสำหรับ [Slack](/integrations/builtin/app-nodes/n8n-nodes-base.slack.md) node
    - ใช้กับ [Slack Trigger](/integrations/builtin/trigger-nodes/n8n-nodes-base.slacktrigger.md) node ไม่ได้

## Related resources

ดูข้อมูลเพิ่มเติมเกี่ยวกับบริการนี้ได้ที่ [Slack's API documentation](https://api.slack.com/apis){:target=_blank .external-link}

## Using API access token

ในการตั้งค่า credential นี้ คุณต้องมีบัญชี [Slack](https://slack.com/){:target=_blank .external-link} และ:

- **Access Token**

วิธีสร้าง access token ให้สร้าง Slack app ขึ้นมาใหม่:

1. เปิดหน้า [Slack API Apps](https://api.slack.com/apps){:target=_blank .external-link}
2. เลือก **Create New App > From scratch**
3. กรอก **App Name**
4. เลือก **Workspace** ที่จะใช้พัฒนาแอป
5. กด **Create App** รายละเอียดแอปจะเปิดขึ้นมา
6. ที่เมนูซ้ายใต้ **Features** เลือก **OAuth & Permissions**
8. ในส่วน **Scopes** ให้เลือก scopes ที่เหมาะสมกับแอปของคุณ ดูรายการแนะนำได้ที่ [Scopes](#scopes)
9. หลังจากเพิ่ม scopes แล้ว ให้เลื่อนไปที่ส่วน **OAuth Tokens** แล้วเลือก **Install to Workspace** (ต้องเป็น admin ของ Slack workspace)
10. กด **Allow**
12. คัดลอก **Bot User OAuth Token** แล้วนำไปใส่ในช่อง **Access Token** ใน n8n credential
13. ถ้าคุณใช้ credential นี้กับ [Slack Trigger](/integrations/builtin/trigger-nodes/n8n-nodes-base.slacktrigger.md) ให้ทำตามขั้นตอนใน [Slack Trigger configuration](#slack-trigger-configuration) เพื่อจบการตั้งค่าแอป

ดูรายละเอียดเพิ่มเติมได้ที่ Slack API [Quickstart](https://api.slack.com/quickstart){:target=_blank .external-link}

### Slack Trigger configuration

ถ้าต้องการใช้ Slack app กับ [Slack Trigger](/integrations/builtin/trigger-nodes/n8n-nodes-base.slacktrigger.md) node:

1. ไปที่ **Features** > **Event Subscriptions**
2. เปิดใช้งาน **Enable Events**
3. ใน n8n ให้คัดลอก **Webhook URL** แล้วนำไปใส่ในช่อง **Request URL** ของ Slack app

    ///  note  | Request URL
    Slack อนุญาตให้ใช้ request URL ได้แค่ 1 อันต่อแอป ถ้าคุณต้องการทดสอบ workflow ให้เลือกวิธีใดวิธีหนึ่งต่อไปนี้:

    - ทดสอบด้วย **Test URL** ก่อน แล้วค่อยเปลี่ยน Slack app ไปใช้ **Production URL** หลังจากทดสอบเสร็จ
    - ใช้ **Production URL** พร้อมกับเปิด execution logging
    ///

4. เมื่อยืนยันแล้ว ให้เลือก bot events ที่ต้องการ subscribe ใช้ฟิลด์ **Trigger on** ใน n8n เพื่อกรอง request เหล่านี้
    - ถ้าต้องการใช้งาน event ที่ไม่มีในลิสต์ ให้เพิ่มเป็น bot event แล้วเลือก **Any Event** ใน n8n node

ดูรายละเอียดเพิ่มเติมได้ที่ [Quickstart | Configuring the app for event listening](https://api.slack.com/quickstart#listening){:target=_blank .external-link}

## Using OAuth2

--8<-- "_snippets/integrations/builtin/credentials/cloud-oauth-button.md"

ถ้าคุณ [self-hosting n8n](/hosting/index.md) และต้องการตั้งค่า OAuth2 เองตั้งแต่ต้น คุณต้องมีบัญชี [Slack](https://slack.com/){:target=_blank .external-link} และ:

- **Client ID**
- **Client Secret**

วิธีขอข้อมูลทั้งสองนี้ ให้สร้าง Slack app ขึ้นมาใหม่:

1. เปิดหน้า [Slack API Apps](https://api.slack.com/apps){:target=_blank .external-link}
2. เลือก **Create New App > From scratch**
3. กรอก **App Name**
4. เลือก **Workspace** ที่จะใช้พัฒนาแอป
5. กด **Create App** รายละเอียดแอปจะเปิดขึ้นมา
6. ที่ **Settings > Basic Information** เปิดส่วน **App Credentials**
7. คัดลอก **Client ID** และ **Client Secret** แล้วนำไปใส่ใน n8n
6. ที่เมนูซ้ายใต้ **Features** เลือก **OAuth & Permissions**
7. ในส่วน **Redirect URLs** ให้เลือก **Add New Redirect URL**
8. คัดลอก **OAuth Callback URL** จาก n8n แล้วนำไปใส่ใน Slack
9. กด **Add**
10. กด **Save URLs**
11. ในส่วน **Scopes** ให้เลือก scopes ที่เหมาะสมกับแอปของคุณ ดูรายการได้ที่ [Scopes](#scopes)
13. หลังจากเพิ่ม scopes แล้ว ให้เลื่อนไปที่ส่วน **OAuth Tokens** แล้วเลือก **Install to Workspace** (ต้องเป็น admin ของ Slack workspace)
14. กด **Allow**
15. ตอนนี้คุณสามารถกดปุ่ม OAuth ใน n8n credential เพื่อเชื่อมต่อได้เลย

ดูรายละเอียดเพิ่มเติมได้ที่ Slack API [Quickstart](https://api.slack.com/quickstart){:target=_blank .external-link} และ [Installing with OAuth](https://api.slack.com/authentication/oauth-v2){:target=_blank .external-link}

## Scopes

Scopes คือสิทธิ์การเข้าถึงที่แอปจะได้รับ

* ถ้าต้องการให้แอปทำงานแทนผู้ใช้ที่ authorize แอป ให้เพิ่ม scopes ที่ต้องการใน **User Token Scopes**
* ถ้าคุณสร้าง bot ให้เพิ่ม scopes ที่ต้องการใน **Bot Token Scopes**

นี่คือลิสต์ scopes ที่ OAuth credential ต้องใช้ เหมาะสำหรับเริ่มต้น:

| **Scope name** | **Notes** |
| --- | --- |
| `channels:read` | |
| `channels:write` | ใช้กับ bot token scope ไม่ได้ |
| `chat:write` | |
| `files:read` | |
| `files:write` | |
| `groups:read` | |
| `im:read` | |
| `mpim:read` | |
| `reactions:read` | |
| `reactions:write` | |
| `stars:read`| ใช้กับ bot token scope ไม่ได้ |
| `stars:write` | ใช้กับ bot token scope ไม่ได้ |
| `usergroups:read` | |
| `usergroups:write` | | 
| `users.profile:read` | |
| `users.profile:write` | ใช้กับ bot token scope ไม่ได้ |
| `users:read` | |

## Common issues

### Token expired

--8<-- "_snippets/integrations/builtin/credentials/slack/token-rotation.md"
