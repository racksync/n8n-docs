---
title: ข้อมูลเข้าสู่ระบบ SecurityScorecard
description: คู่มือการตั้งค่า SecurityScorecard credentials สำหรับเชื่อมต่อ SecurityScorecard กับ n8n
contentType: [integration, reference]
---

# SecurityScorecard credentials

คุณสามารถใช้ credentials เหล่านี้เพื่อยืนยันตัวตนกับ node ต่อไปนี้:

- [SecurityScorecard](/integrations/builtin/app-nodes/n8n-nodes-base.securityscorecard.md)

## Prerequisites

สร้าง [SecurityScorecard](https://securityscorecard.com/){:target=_blank .external-link} account

## Supported authentication methods

- API key

## Related resources

ดูรายละเอียดเพิ่มเติมเกี่ยวกับบริการนี้ได้ที่ [SecurityScorecard's Developer documentation](https://securityscorecard.readme.io/docs/integrate-ratings-platform-services){:target=_blank .external-link} และ [API documentation](https://securityscorecard.readme.io/reference/introduction){:target=_blank .external-link}

## Using API key

ในการตั้งค่า credentials นี้ คุณจะต้องมี:

- **API Key**: สร้าง API key ได้ 2 วิธี:
    * ในฐานะ user ที่ [**My Settings > API**](https://platform.securityscorecard.io/#/my-settings/api){:target=_blank .external-link} ดูวิธีได้ที่ [Get an API key](https://securityscorecard.readme.io/docs/getting-started#step-1-get-an-api-key){:target=_blank .external-link}
    * ในฐานะ bot user: ดู bot user แล้วเลือก **create token** ดูวิธีได้ที่ [Authenticate with a bot user](https://securityscorecard.readme.io/docs/authentication#){:target=_blank .external-link}

