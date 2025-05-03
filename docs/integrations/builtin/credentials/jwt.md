---
#https://www.notion.so/n8n/Frontmatter-432c2b8dff1f43d4b1c8d20075510fe4
title: ข้อมูลยืนยันตัวตน JWT
description: เอกสารสำหรับ JWT credentials ใช้เพื่อยืนยันตัวตน JWT และ Webhook ใน n8n
contentType: [integration, reference]
priority: medium
---

# JWT credentials

คุณสามารถใช้ credentials เหล่านี้เพื่อยืนยันตัวตนกับ node ต่อไปนี้ได้:

- [JWT](/integrations/builtin/core-nodes/n8n-nodes-base.jwt.md)
- [Webhook](/integrations/builtin/core-nodes/n8n-nodes-base.webhook/index.md)

## Supported authentication methods

- Passphrase: ลงนามด้วย secret โดยใช้อัลกอริทึม HMAC
- Private key (PEM key): สำหรับใช้กับ [Private Key JWT](https://auth0.com/docs/get-started/authentication-and-authorization-flow/authenticate-with-private-key-jwt){:target=_blank .external-link} ด้วยอัลกอริทึม RSA หรือ ECDSA

## Related resources

ดูรายละเอียดเพิ่มเติมได้ที่ [JSON Web Token spec](https://datatracker.ietf.org/doc/html/rfc7519){:target=_blank .external-link}

สำหรับข้อมูลเบื้องต้นที่ละเอียดมากขึ้น โปรดดู [JWT website Introduction to JSON Web Tokens](https://jwt.io/introduction){:target=_blank .external-link} โปรดดู [JSON Web Token (JWT) Signing Algorithms Overview](https://auth0.com/blog/json-web-token-signing-algorithms-overview/){:target=_blank .external-link} สำหรับข้อมูลเพิ่มเติมเกี่ยวกับการเลือกระหว่างสองประเภทและอัลกอริทึมที่เกี่ยวข้อง

## Using Passphrase

ในการตั้งค่า credential นี้:

1.  เลือก **Key Type** เป็น **Passphrase**
2.  ป้อน Passphrase **Secret**
3.  เลือก **Algorithm** ที่ใช้ในการลงนาม assertion ดูรายการอัลกอริทึมที่รองรับได้ที่ [Available algorithms](#available-algorithms) ด้านล่าง

## Using private key (PEM key)

ในการตั้งค่า credential นี้:
1.  เลือก **Key Type** เป็น **PEM Key**
2.  **Private Key**: ได้มาจากการสร้าง Key Pair ดูตัวอย่างได้ที่ [Generate RSA Key Pair](https://auth0.com/docs/secure/application-credentials/generate-rsa-key-pair){:target=_blank .external-link}
3.  **Public Key**: ได้มาจากการสร้าง Key Pair ดูตัวอย่างได้ที่ [Generate RSA Key Pair](https://auth0.com/docs/secure/application-credentials/generate-rsa-key-pair){:target=_blank .external-link}
4.  เลือก **Algorithm** ที่ใช้ในการลงนาม assertion ดูรายการอัลกอริทึมที่รองรับได้ที่ [Available algorithms](#available-algorithms) ด้านล่าง

## Available algorithms

n8n credential นี้รองรับอัลกอริทึมต่อไปนี้:

- `HS256`
- `HS384`
- `HS512`
- `RS256`
- `RS384`
- `RS512`
- `ES256`
- `ES384`
- `ES512`
- `PS256`
- `PS384`
- `PS512`
- `none`
