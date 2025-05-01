---
#https://www.notion.so/n8n/Frontmatter-432c2b8dff1f43d4b1c8d20075510fe4
title: HaloPSA credentials
description: Documentation for HaloPSA credentials. Use these credentials to authenticate HaloPSA in n8n, a workflow automation platform.
contentType: [integration, reference]
---

# HaloPSA credentials

คุณสามารถใช้ credentials เหล่านี้เพื่อยืนยันตัวตนกับ node ต่อไปนี้ได้:

- [HaloPSA](/integrations/builtin/app-nodes/n8n-nodes-base.halopsa.md)

## Prerequisites

สร้างบัญชี [HaloPSA](https://halopsa.com/) ก่อน

## Supported authentication methods

- API key

## Related resources

ดูข้อมูลเพิ่มเติมเกี่ยวกับบริการนี้ได้ที่ [HaloPSA's API documentation](https://halopsa.com/apidoc/info){:target=_blank .external-link}

## Using API key

ถ้าต้องการตั้งค่า credential นี้ คุณจะต้อง:

- เลือก **Hosting Type** ของคุณ:
    - **On Premise Solution**: เลือกอันนี้ถ้าคุณ host Halo application เองบน server ของคุณ
    - **Hosted Solution Of Halo**: เลือกอันนี้ถ้า application ของคุณ host โดย Halo ถ้าเลือกอันนี้ คุณต้องกรอก **Tenant** ของคุณด้วย
- **HaloPSA Authorisation Server URL**: ดู URL นี้ได้ใน HaloPSA ที่ **Configuration > Integrations > Halo API** ใน [API Details](https://halopsa.com/guides/article/?kbid=1737){:target=_blank .external-link}
- **Resource Server** URL: ดู Resource Server ได้ใน HaloPSA ที่ **Configuration > Integrations > Halo API** ใน [API Details](https://halopsa.com/guides/article/?kbid=1737){:target=_blank .external-link}
- **Client ID**: ได้จากการ register application ใน Halo API settings ดูวิธีโดยละเอียดที่ [HaloPSA's Authorisation documentation](https://halopsa.com/apidoc/authorisation){:target=_blank .external-link} n8n แนะนำให้ใช้ settings เหล่านี้:
    - เลือก `Client Credentials` เป็น **Authentication Method**
    - ใช้ permission `all`
- **Client Secret**: ได้จากการ register application ใน Halo API settings
- **Tenant** name: ถ้าเลือก **Hosted Solution of Halo** เป็น **Hosting Type** ต้องกรอก tenant name ด้วย ดู tenant name ได้ใน HaloPSA ที่ **Configuration > Integrations > Halo API** ใน [API Details](https://halopsa.com/guides/article/?kbid=1737){:target=_blank .external-link}

HaloPSA จะใช้ทั้ง permission ของ application และ permission ของ agent ในการกำหนดสิทธิ์การเข้าถึง API
