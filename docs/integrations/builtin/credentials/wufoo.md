---
#https://www.notion.so/n8n/Frontmatter-432c2b8dff1f43d4b1c8d20075510fe4
title: Wufoo credentials
description: Documentation for Wufoo credentials. Use these credentials to authenticate Wufoo in n8n, a workflow automation platform.
contentType: [integration, reference]
---

# Wufoo credentials

คุณสามารถใช้ credentials นี้เพื่อ authenticate กับ node เหล่านี้:

- [Wufoo Trigger](/integrations/builtin/trigger-nodes/n8n-nodes-base.wufootrigger.md)

## Prerequisites

สมัคร [Wufoo](https://wufoo.com){:target=_blank .external-link} ให้เรียบร้อยก่อน

## Supported authentication methods

- API key

## Related resources

ดูรายละเอียดเพิ่มเติมเกี่ยวกับการใช้งาน API ได้ที่ [Wufoo's API documentation](https://wufoo.github.io/docs/){:target=_blank .external-link}

## Using API key

ถ้าจะตั้งค่า credentials นี้ คุณต้องมี:

- **API Key**: หา API key ได้จาก [Wufoo Form Manager](https://app.wufoo.com/#/form-manager){:target=_blank .external-link} ที่ขวาของฟอร์ม ให้เลือก **More > API Information** ดูรายละเอียดที่ [Using API Information and Webhooks](https://help.surveymonkey.com/en/wufoo/integrations/wufoo-api/){:target=_blank .external-link}
- **Subdomain**: subdomain คือส่วนของ URL Wufoo ที่อยู่หลัง `https://` และก่อน `wufoo.com` เช่นถ้า domain เต็มคือ `https://n8n.wufoo.com` subdomain คือ `n8n` แอดมินสามารถดู subdomain ได้ใน [**Account Manager**](https://help.surveymonkey.com/en/wufoo/account-manager){:target=_blank .external-link} ดูรายละเอียดที่ [Your Subdomain](https://help.surveymonkey.com/en/wufoo/account/your-subdomain/){:target=_blank .external-link}

