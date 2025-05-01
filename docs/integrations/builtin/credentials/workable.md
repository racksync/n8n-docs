---
#https://www.notion.so/n8n/Frontmatter-432c2b8dff1f43d4b1c8d20075510fe4
title: Workable credentials
description: Documentation for Workable credentials. Use these credentials to authenticate Workable in n8n, a workflow automation platform.
contentType: [integration, reference]
---

# Workable credentials

คุณสามารถใช้ credentials นี้เพื่อยืนยันตัวตนกับ node ต่อไปนี้ได้:

- [Workable Trigger](/integrations/builtin/trigger-nodes/n8n-nodes-base.workabletrigger.md)

## Prerequisites

สร้างบัญชี [Workable](https://www.workable.com/){:target=_blank .external-link} ก่อน

## Supported authentication methods

- API key

## Related resources

ดูข้อมูลเพิ่มเติมเกี่ยวกับบริการนี้ได้ที่ [Workable's API documentation](https://workable.readme.io/reference/generate-an-access-token){:target=_blank .external-link}

## Using API key

ในการตั้งค่า credential นี้ คุณจะต้องมี:

- **Subdomain**: Subdomain ของ Workable คือส่วนที่อยู่ระหว่าง `https://` กับ `.workable.com` ในโดเมนของคุณ เช่น ถ้าโดเมนเต็มคือ `https://n8n.workable.com` subdomain ก็คือ `n8n` โดยคุณสามารถดู subdomain ได้ที่หน้า **Company Profile** ของ Workable
- **Access Token**: ไปที่ **profile >** [**Integrations**](https://workable.com/backend/settings/integrations){:target=_blank .external-link} **> Apps** แล้วเลือก **Generate API token** ดูรายละเอียดเพิ่มเติมได้ที่ [Generate a new token](https://help.workable.com/hc/en-us/articles/115015785428-Generating-revoking-access-tokens-for-Workable-s-API#Generateanewtoken)

    <!-- vale off -->
    /// note | Token scopes
    ถ้าคุณใช้ credential นี้กับ node [Workable Trigger](/integrations/builtin/trigger-nodes/n8n-nodes-base.workabletrigger.md) ให้เลือก scope `r_candidates` และ `r_jobs` ตอนสร้าง token ถ้าใช้ credential นี้กับกรณีอื่น ให้เลือก scope ที่เหมาะกับการใช้งานของคุณ

    ดูรายละเอียด scope ที่รองรับได้ที่ [Supported API scopes](https://help.workable.com/hc/en-us/articles/115015785428-Generating-revoking-access-tokens-for-Workable-s-API#SupportedAPIscopes){:target=_blank .external-link}
    ///
    <!-- vale on -->
