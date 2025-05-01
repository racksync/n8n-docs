---
#https://www.notion.so/n8n/Frontmatter-432c2b8dff1f43d4b1c8d20075510fe4
title: Xero credentials
description: Documentation for Xero credentials. Use these credentials to authenticate Xero in n8n, a workflow automation platform.
contentType: [integration, reference]
---

# Xero credentials

คุณสามารถใช้ credentials นี้เพื่อ authenticate กับ node เหล่านี้:

- [Xero](/integrations/builtin/app-nodes/n8n-nodes-base.xero.md)

## Prerequisites

สมัคร [Xero](https://www.xero.com/){:target=_blank .external-link} ให้เรียบร้อยก่อน

## Supported authentication methods

- OAuth2

## Related resources

ดูรายละเอียดเพิ่มเติมเกี่ยวกับการใช้งาน API ได้ที่ [Zero's API documentation](https://developer.xero.com/documentation/api/accounting/overview){:target=_blank .external-link}

## Using OAuth2

ถ้าจะตั้งค่า credentials นี้ คุณต้องมี:

- **Client ID**: ได้จากการสร้างแอปใหม่สำหรับ custom connection
- **Client Secret**: ได้จากการสร้างแอปใหม่สำหรับ custom connection

สร้าง Client ID และ Client Secret ได้โดย [สร้าง OAuth2 custom connection app](https://developer.xero.com/documentation/guides/oauth2/custom-connections/){:target=_blank .external-link} ใน Xero developer portal ที่ [**My Apps**](https://developer.xero.com/app/manage){:target=_blank .external-link}

ตั้งค่าแอปตามนี้:

/// note | Xero App Name

Xero ไม่อนุญาตให้ใช้ชื่อแอปที่มีคำว่า `n8n` ใน Xero Developer Centre

///

- เลือก **Web app** ใน **Integration Type**
- สำหรับ **Company or Application URL** ให้ใส่ URL ของ n8n server หรือ reverse proxy ของคุณ (เช่น cloud user: `https://your-username.app.n8n.cloud/`)
- คัดลอก **OAuth Redirect URL** จาก n8n ไปใส่ใน **OAuth 2.0 redirect URI** ของแอป
- เลือก **scopes** ที่เหมาะสมกับแอป ดูรายละเอียดที่ [OAuth2 Scopes](https://developer.xero.com/documentation/guides/oauth2/scopes/){:target=_blank .external-link}
    - ถ้าต้องการใช้ทุกฟีเจอร์ใน [Xero](/integrations/builtin/app-nodes/n8n-nodes-base.xero.md) node ให้เพิ่ม scope `accounting.contacts` และ `accounting.transactions`

ดูรายละเอียดเพิ่มเติมที่ [OAuth Custom Connections](https://developer.xero.com/documentation/guides/oauth2/custom-connections){:target=_blank .external-link}
