---
#https://www.notion.so/n8n/Frontmatter-432c2b8dff1f43d4b1c8d20075510fe4
title: Wise credentials
description: Documentation for Wise credentials. Use these credentials to authenticate Wise in n8n, a workflow automation platform.
contentType: [integration, reference]
---

# Wise credentials

คุณสามารถใช้ credentials เหล่านี้เพื่อยืนยันตัวตนกับ node ต่อไปนี้:

- [Wise](/integrations/builtin/app-nodes/n8n-nodes-base.wise.md)
- [Wise Trigger](/integrations/builtin/trigger-nodes/n8n-nodes-base.wisetrigger.md)

## Prerequisites

สร้างบัญชี [Wise](https://wise.com/){:target=_blank .external-link} ก่อน

## Supported authentication methods

- API token

## Related resources

ดูข้อมูลเพิ่มเติมเกี่ยวกับบริการนี้ได้ที่ [Wise's API documentation](https://docs.wise.com/api-docs/api-reference){:target=_blank .external-link}

## Using API token

ในการตั้งค่า credential นี้ คุณจะต้องมี:

- **API Token**: ไปที่ **user menu > Settings > API tokens** เพื่อสร้าง API token แล้วนำ API key ที่ได้ไปใส่ใน n8n ดูรายละเอียดเพิ่มเติมได้ที่ [Getting started with the API](https://wise.com/help/articles/2958107/getting-started-with-the-api){:target=_blank .external-link}
- **Environment**: เลือก environment ที่ตรงกับบัญชี Wise ของคุณ
    - ถ้าใช้บัญชี test sandbox ของ Wise ให้เลือก **Test**
    - ถ้าไม่ใช่ ให้เลือก **Live**
- **Private Key (Optional)**: สำหรับ endpoint แบบ live ที่ต้องใช้ Strong Customer Authentication (SCA) ให้สร้าง public และ private key แล้วนำ private key มาใส่ที่นี่ ดูรายละเอียดเพิ่มเติมได้ที่ [Add a private key](#add-a-private-key)
    - ถ้าใช้ environment แบบ **Test** จะต้องใส่ Private Key เฉพาะกรณีที่เปิดใช้งาน Strong Customer Authentication ใน [public keys management page](https://sandbox.transferwise.tech/public-keys){:target=_blank .external-link}

## Add a private key

Wise จะป้องกัน endpoint และ operation บางอย่างใน live ด้วย Strong Customer Authentication (SCA) ดูรายละเอียดที่ [Strong Customer Authentication & 2FA](https://docs.wise.com/api-docs/features/strong-customer-authentication-2fa){:target=_blank .external-link}

ถ้าคุณเรียก endpoint ที่ต้องใช้ SCA แล้วเจอ error 403 Forbidden ระบบจะขึ้นข้อความประมาณนี้:

> This request requires Strong Customer Authentication (SCA). Please add a key pair to your account and n8n credentials. See https://api-docs.transferwise.com/#strong-customer-authentication-personal-token

ถ้าต้องการใช้ endpoint ที่ต้องใช้ SCA ให้สร้าง RSA key pair แล้วเพิ่มข้อมูล key ที่เกี่ยวข้องทั้งใน Wise และ n8n:

1. สร้าง RSA key pair:

    ```sh
    $ openssl genrsa -out private.pem 2048 
    $ openssl rsa -pubout -in private.pem -out public.pem
    ```

2. นำเนื้อหา public key จาก `public.pem` ไปใส่ที่ Wise ที่ **user menu > Settings > API tokens > Manage public keys**
3. นำเนื้อหา private key จาก `private.pem` ไปใส่ใน n8n ที่ **Private Key (Optional)**

ดูรายละเอียดเพิ่มเติมได้ที่ [Personal Token SCA](https://docs.wise.com/api-docs/features/strong-customer-authentication-2fa/personal-token-sca){:target=_blank .external-link}

