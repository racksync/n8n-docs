---
#https://www.notion.so/n8n/Frontmatter-432c2b8dff1f43d4b1c8d20075510fe4
title: ข้อมูลรับรอง Calendly
description: เอกสารข้อมูลรับรอง Calendly ใช้ข้อมูลนี้เพื่อยืนยันตัวตน Calendly ใน n8n
contentType: [integration, reference]
priority: medium
---

# Calendly credentials

คุณสามารถใช้ credentials นี้เพื่อเชื่อมต่อกับ node เหล่านี้:

- [Calendly Trigger](/integrations/builtin/trigger-nodes/n8n-nodes-base.calendlytrigger.md)

/// warning | Supported Calendly plans
Calendly Trigger node อาศัย Calendly webhooks Calendly ให้สิทธิ์เข้าถึง webhooks เฉพาะในแผนแบบชำระเงินเท่านั้น
///

## Supported authentication methods

- API access token
- OAuth2

## Related resources

ดูข้อมูลเพิ่มเติมเกี่ยวกับบริการได้ที่ [Calendly's API documentation](https://developer.calendly.com/getting-started){:target=_blank .external-link}

## Using API access token

ถ้าจะตั้งค่า credentials นี้ คุณต้องมีบัญชี [Calendly](https://www.calendly.com/){:target=_blank .external-link} และ:

- API Key หรือ **Personal Access Token**

วิธีรับ access token ของคุณ:

1. ไปที่หน้า [**Integrations & apps**](https://calendly.com/integrations){:target=_blank .external-link} ของ Calendly
2. เลือก [**API & Webhooks**](https://calendly.com/integrations/api_webhooks){:target=_blank .external-link}
3. ใน **Your Personal Access Tokens** เลือก **Generate new token**
4. ป้อน **Name** สำหรับ access token ของคุณ เช่น `n8n integration`
5. เลือก **Create token**
6. เลือก **Copy token** และป้อนลงใน n8n credential ของคุณ

ดูข้อมูลเพิ่มเติมได้ที่ [Calendly's API authentication documentation](https://developer.calendly.com/how-to-authenticate-with-personal-access-tokens){:target=_blank .external-link}

## Using OAuth2

ถ้าจะตั้งค่า credentials นี้ คุณต้องมีบัญชี [Calendly developer](https://developer.calendly.com){:target=_blank .external-link} และ:

- **Client ID**
- **Client Secret**

หากต้องการรับทั้งสองอย่าง ให้สร้าง OAuth app ใหม่ใน Calendly:

1. ล็อกอินเข้าสู่ developer portal ของ Calendly และไปที่ [**My apps**](https://developer.calendly.com/console/apps){:target=_blank .external-link}
1. เลือก **Create new app**
1. ป้อน **Name of app** เช่น `n8n integration`
2. ใน **Kind of app** เลือก **Web**
3. ใน **Environment type** เลือก environment ที่สอดคล้องกับการใช้งานของคุณ ไม่ว่าจะเป็น **Sandbox** หรือ **Production**
    - Calendly แนะนำให้เริ่มต้นด้วย **Sandbox** สำหรับการพัฒนา และสร้าง application ที่สองสำหรับ **Production** เมื่อคุณพร้อมที่จะใช้งานจริง
4. คัดลอก **OAuth Redirect URL** จาก n8n และป้อนเป็น **Redirect URI** ใน OAuth app
5. เลือก **Save & Continue** รายละเอียด app จะแสดงขึ้น
5. คัดลอก **Client ID** และป้อนเป็น **Client ID** ของ n8n
6. คัดลอก **Client secret** และป้อนเป็น **Client Secret** ของ n8n
1. เลือก **Connect my account** ใน n8n และทำตามคำแนะนำบนหน้าจอเพื่ออนุญาต credential ให้เสร็จสิ้น

ดูข้อมูลเพิ่มเติมได้ที่ [Registering your application with Calendly](https://developer.calendly.com/create-a-developer-account){:target=_blank .external-link}
