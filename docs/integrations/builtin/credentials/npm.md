---
#https://www.notion.so/n8n/Frontmatter-432c2b8dff1f43d4b1c8d20075510fe4
title: npm credentials
description: Documentation for the npm credentials. Use these credentials to authenticate npm in n8n, a workflow automation platform.
contentType: [integration, reference]
---

# npm credentials

คุณสามารถใช้ credentials เหล่านี้เพื่อยืนยันตัวตนใน nodes ต่อไปนี้:

- [npm](/integrations/builtin/app-nodes/n8n-nodes-base.npm.md)

## Prerequisites

สร้างบัญชี [npm](https://www.npmjs.com/){:target=_blank .external-link}

## Supported authentication methods

- API access token

## Related resources

อ้างอิง [npm's external integrations documentation](https://docs.npmjs.com/integrations/integrating-npm-with-external-services){:target=_blank .external-link} สำหรับข้อมูลเพิ่มเติมเกี่ยวกับบริการนี้

## Using API access token

ในการกำหนดค่า credential นี้ คุณจะต้องมี:

- **Access Token**: สร้าง access token โดยเลือก **Access Tokens** จากเมนูโปรไฟล์ของคุณ อ้างอิงเอกสาร [npm's Creating and viewing access tokens documentation](https://docs.npmjs.com/creating-and-viewing-access-tokens){:target=_blank .external-link} สำหรับคำแนะนำโดยละเอียดเพิ่มเติม
- **Registry URL**: หากคุณกำลังใช้ custom npm registry ให้อัปเดต **Registry URL** เป็น custom registry นั้น มิฉะนั้น ให้คงค่า public registry ไว้

