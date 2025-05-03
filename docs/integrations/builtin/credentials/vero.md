---
#https://www.notion.so/n8n/Frontmatter-432c2b8dff1f43d4b1c8d20075510fe4
title: ข้อมูลเข้าสู่ระบบ Vero
description: คู่มือการตั้งค่า credentials สำหรับเชื่อมต่อ Vero กับ n8n เพื่อใช้งาน workflow automation
contentType: [integration, reference]
---

# Vero credentials

คุณสามารถใช้ credentials เหล่านี้เพื่อยืนยันตัวตนกับ node ต่อไปนี้:

- [Vero](/integrations/builtin/app-nodes/n8n-nodes-base.vero.md)

## Prerequisites

สร้างบัญชี [Vero](https://getvero.com/){:target=_blank .external-link} ก่อน

## Supported authentication methods

- API auth token

## Related resources

ดูข้อมูลเพิ่มเติมเกี่ยวกับบริการนี้ได้ที่ [Vero's API documentation](https://developers.getvero.com/track-api-reference/#/){:target=_blank .external-link}

## Using API auth token

ในการตั้งค่า credential นี้ คุณจะต้องมี:

- **Auth Token**: รับ auth token ได้จาก [settings](https://app.getvero.com/settings/project){:target=_blank .external-link} ในบัญชี Vero ของคุณ ดูรายละเอียดเพิ่มเติมได้ที่ [API authentication](https://developers.getvero.com/track-api-reference/#/#authentication){:target=_blank .external-link}

