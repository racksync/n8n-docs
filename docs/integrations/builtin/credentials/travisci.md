---
#https://www.notion.so/n8n/Frontmatter-432c2b8dff1f43d4b1c8d20075510fe4
title: Travis CI credentials
description: Documentation for Travis CI credentials. Use these credentials to authenticate Travis CI in n8n, a workflow automation platform.
contentType: [integration, reference]
---

# Travis CI credentials

คุณสามารถใช้ credentials นี้เพื่อยืนยันตัวตนกับ node ต่อไปนี้ได้:

- [Travis CI](/integrations/builtin/app-nodes/n8n-nodes-base.travisci.md)

## Prerequisites

สร้างบัญชี [Travis CI](https://travis-ci.org/){:target=_blank .external-link} ก่อน

## Supported authentication methods

- API token

## Related resources

ดูข้อมูลเพิ่มเติมเกี่ยวกับบริการนี้ได้ที่ [Travis CI's API documentation](https://docs.travis-ci.com/user/developer/){:target=_blank .external-link}

## Using API token

ในการตั้งค่า credentials นี้ คุณจะต้องมี:

- **API Token**: รับ token ได้ที่ **Account Settings >** [**API Token**](https://packagecloud.io/api_token){:target=_blank .external-link} หรือสร้างผ่าน [command line client](https://github.com/travis-ci/travis.rb#installation){:target=_blank .external-link} ของ Travis CI

