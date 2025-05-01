---
#https://www.notion.so/n8n/Frontmatter-432c2b8dff1f43d4b1c8d20075510fe4
title: Drift credentials
description: Documentation for Drift credentials. Use these credentials to authenticate Drift in n8n, a workflow automation platform.
contentType: [integration, reference]
---

# Drift credentials

คุณสามารถใช้ credentials นี้เพื่อเชื่อมต่อกับ node เหล่านี้:

- [Drift](/integrations/builtin/app-nodes/n8n-nodes-base.drift.md)

## Prerequisites

- สมัคร [Drift](https://www.drift.com/){:target=_blank .external-link} ให้เรียบร้อยก่อน
- [สร้าง Drift app](https://devdocs.drift.com/docs/quick-start#3-install-it-to-your-drift-account-){:target=_blank .external-link}

## Supported authentication methods

- API personal access token
- OAuth2

## Related resources

ดูรายละเอียดเพิ่มเติมเกี่ยวกับการใช้งาน API ได้ที่ [Drift's API documentation](https://devdocs.drift.com/docs/using-drift-apis){:target=_blank .external-link}

## Using API personal access token

ถ้าจะตั้งค่า credentials นี้ คุณต้องมี:

- **Personal Access Token**: หากต้องการรับ token ให้ [สร้าง Drift app](https://devdocs.drift.com/docs/quick-start#3-install-it-to-your-drift-account-){:target=_blank .external-link} [ติดตั้ง app](https://devdocs.drift.com/docs/quick-start#3-install-it-to-your-drift-account-){:target=_blank .external-link} เพื่อสร้าง OAuth Access token เพิ่ม token นี้ลงใน n8n credential เป็น **Personal Access Token** ของคุณ

## Using OAuth2

--8<-- "_snippets/integrations/builtin/credentials/cloud-oauth-button.md"

หากคุณต้องการตั้งค่า OAuth2 ด้วยตัวเอง หรือต้องการรายละเอียดเพิ่มเติมเกี่ยวกับขั้นตอน OAuth web flow โปรดดูคำแนะนำใน [Drift Authentication and Scopes documentation](https://devdocs.drift.com/docs/authentication-and-scopes){:target=_blank .external-link} เพื่อตั้งค่า OAuth สำหรับ app ของคุณ
