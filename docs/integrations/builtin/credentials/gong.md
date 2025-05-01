---
#https://www.notion.so/n8n/Frontmatter-432c2b8dff1f43d4b1c8d20075510fe4
title: Gong credentials
description: Documentation for the Gong credentials. Use these credentials to authenticate Gong in n8n, a workflow automation platform.
contentType: [integration, reference]
---

# Gong credentials

คุณสามารถใช้ credentials เหล่านี้เพื่อยืนยันตัวตนกับ node ต่อไปนี้:

* [Gong](/integrations/builtin/app-nodes/n8n-nodes-base.gong.md)

## Supported authentication methods

- API access token
- OAuth2

## Related resources

ดูข้อมูลเพิ่มเติมเกี่ยวกับบริการนี้ได้ที่ [Gong's API documentation](https://gong.app.gong.io/settings/api/documentation){:target=_blank .external-link}

## Using API access token

ในการกำหนดค่า credential นี้ คุณจะต้องมีบัญชี [Gong](https://app.gong.io/welcome/sign-in) และ:

- **Access Key**
- **Access Key Secret**

คุณสามารถสร้างทั้งสองรายการนี้ได้ที่ [Gong API Page](https://app.gong.io/company/api) (คุณต้องเป็นผู้ดูแลระบบทางเทคนิคใน Gong เพื่อเข้าถึงทรัพยากรนี้)

ดูข้อมูลเพิ่มเติมเกี่ยวกับการยืนยันตัวตนกับบริการนี้ได้ที่ [Gong's API documentation](https://gong.app.gong.io/settings/api/documentation){:target=_blank .external-link}

## Using OAuth2

ในการกำหนดค่า credential นี้ คุณจะต้องมีบัญชี [Gong](https://app.gong.io/welcome/sign-in), บัญชี [Gong developer](https://gong.partnerfleet.app/application_forms/become-a-gong-technology-partner/partner_applications/new) และ:

* **Client ID**: สร้างขึ้นเมื่อคุณสร้าง Oauth app สำหรับ Gong
* **Client Secret**: สร้างขึ้นเมื่อคุณสร้าง Oauth app สำหรับ Gong

หากคุณ [self-hosting](/hosting/index.md) n8n คุณจะต้อง [create an app](https://help.gong.io/docs/create-an-app-for-gong) เพื่อกำหนดค่า OAuth2 ดูข้อมูลเพิ่มเติมเกี่ยวกับการตั้งค่า OAuth2 ได้ที่ [Gong's OAuth documentation](https://gong.app.gong.io/settings/api/documentation){:target=_blank .external-link}
