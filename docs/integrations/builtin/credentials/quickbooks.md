---
#https://www.notion.so/n8n/Frontmatter-432c2b8dff1f43d4b1c8d20075510fe4
title: QuickBooks credentials
description: Documentation for QuickBooks credentials. Use these credentials to authenticate QuickBooks in n8n, a workflow automation platform.
contentType: [integration, reference]
---

# QuickBooks credentials

คุณสามารถใช้ credentials นี้เพื่อยืนยันตัวตนกับ node ต่อไปนี้ได้:

- [QuickBooks](/integrations/builtin/app-nodes/n8n-nodes-base.quickbooks.md)

## Prerequisites

สร้าง [Intuit developer](https://developer.intuit.com/){:target=_blank .external-link} account

## Supported authentication methods

- OAuth2

## Related resources

ดูข้อมูลเพิ่มเติมเกี่ยวกับบริการนี้ได้ที่ [Intuit's API documentation](https://developer.intuit.com/app/developer/qbo/docs/develop){:target=_blank .external-link}

## Using OAuth2

สำหรับการตั้งค่า credentials นี้ คุณจะต้องมี:

- **Client ID**: สร้างขึ้นเมื่อคุณสร้าง app
- **Client Secret**: สร้างขึ้นเมื่อคุณสร้าง app
- **Environment**: เลือกว่า credential นี้ควรเข้าถึง environment **Production** หรือ **Sandbox** ของคุณ

หากต้องการสร้าง **Client ID** และ **Client Secret** ของคุณ ให้ [สร้าง app](https://developer.intuit.com/app/developer/qbo/docs/get-started/start-developing-your-app#create-an-app){:target=_blank .external-link}

ใช้การตั้งค่าเหล่านี้เมื่อสร้าง app ของคุณ:

- เลือก scopes ที่เหมาะสมสำหรับ app ของคุณ ดูข้อมูลเพิ่มเติมที่ [Learn about scopes](https://developer.intuit.com/app/developer/qbo/docs/learn/scopes){:target=_blank .external-link}
- กรอก **OAuth Redirect URL** จาก n8n เป็น **Redirect URI** ในส่วน **Development > Keys & OAuth** ของ app
- คัดลอก **Client ID** และ **Client Secret** จากส่วน **Development > Keys & OAuth** ของ app เพื่อกรอกใน n8n ดูข้อมูลเพิ่มเติมที่ [Get the Client ID and Client Secret for your app](https://developer.intuit.com/app/developer/qbo/docs/get-started/get-client-id-and-client-secret){:target=_blank .external-link}

ดูข้อมูลเพิ่มเติมเกี่ยวกับกระบวนการทั้งหมดได้ที่ [Set up OAuth 2.0 documentation](https://developer.intuit.com/app/developer/qbo/docs/develop/authentication-and-authorization/oauth-2.0){:target=_blank .external-link} ของ Intuit

/// note | Environment selection
หากคุณกำลังสร้าง app ใหม่ตั้งแต่ต้น ให้เริ่มต้นด้วย environment **Sandbox** Production apps จำเป็นต้องปฏิบัติตามข้อกำหนดทั้งหมดของ Intuit ดูข้อมูลเพิ่มเติมที่ [Publish your app documentation](https://developer.intuit.com/app/developer/qbo/docs/go-live/publish-app){:target=_blank .external-link} ของ Intuit
///