---
#https://www.notion.so/n8n/Frontmatter-432c2b8dff1f43d4b1c8d20075510fe4
title: HTTP Request credentials
description: Documentation for HTTP Request credentials. Use these credentials to authenticate HTTP Request in n8n, a workflow automation platform.
contentType: [integration, reference]
priority: critical
---

# HTTP Request credentials

คุณสามารถใช้ credentials เหล่านี้เพื่อยืนยันตัวตนกับ node ต่อไปนี้ได้:

- [HTTP Request](/integrations/builtin/core-nodes/n8n-nodes-base.httprequest/index.md)
- [HTTP Request Tool (legacy)](/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.toolhttprequest.md)

## Prerequisites

คุณต้องใช้วิธีการยืนยันตัวตนที่แอปหรือบริการที่คุณต้องการ query กำหนด

หากคุณต้องการรักษาความปลอดภัยในการยืนยันตัวตนด้วย SSL certificate โปรดดู [Provide an SSL certificate](#provide-an-ssl-certificate) สำหรับข้อมูลที่คุณต้องการ

## Supported authentication methods

- Predefined credential type
- Basic auth (generic credential type)
- Custom auth (generic credential type)
- Digest auth (generic credential type)
- Header auth (generic credential type)
- Bearer auth (generic credential type)
- OAuth1 (generic credential type)
- OAuth2 (generic credential type)
- Query auth (generic credential type)

ดูข้อมูลเพิ่มเติมเกี่ยวกับ generic credential types ได้ที่ [HTTP authentication](https://developer.mozilla.org/en-US/docs/Web/HTTP/Authentication){:target=_blank .external-link}

/// note | Predefined credential types
n8n แนะนำให้ใช้ predefined credential types เมื่อใดก็ตามที่มี credential type สำหรับบริการที่คุณต้องการเชื่อมต่อ มันมีวิธีที่ง่ายกว่าในการตั้งค่าและจัดการ credentials เมื่อเทียบกับการกำหนดค่า generic credentials

คุณสามารถใช้ [Predefined credential types](/integrations/custom-operations.md#predefined-credential-types) เพื่อดำเนินการ custom operations กับ API บางตัวที่ n8n มี node สำหรับแพลตฟอร์มนั้น ตัวอย่างเช่น n8n มี Asana node และรองรับการใช้ Asana credentials ของคุณใน HTTP Request node ดูข้อมูลเพิ่มเติมได้ที่ [Custom operations](/integrations/custom-operations.md)
///

## Using predefined credential type

--8<-- "_snippets/integrations/predefined-credential-type-how-to.md"

ดูข้อมูลเพิ่มเติมได้ที่ [Custom API operations](/integrations/custom-operations.md)

--8<-- "_snippets/integrations/builtin/credentials/generic-auth/basic-auth.md"

--8<-- "_snippets/integrations/builtin/credentials/generic-auth/digest-auth.md"

--8<-- "_snippets/integrations/builtin/credentials/generic-auth/header-auth.md"

--8<-- "_snippets/integrations/builtin/credentials/generic-auth/bearer-auth.md"

## Using OAuth1

ใช้ generic authentication นี้หากแอปหรือบริการของคุณรองรับการยืนยันตัวตนแบบ OAuth1

ในการตั้งค่า credential นี้ ให้ป้อน:

- **Authorization URL**: หรือที่เรียกว่า Resource Owner Authorization URI โดยทั่วไป URL นี้จะลงท้ายด้วย `/oauth1/authorize` credentials ชั่วคราวจะถูกส่งมาที่นี่เพื่อแจ้งให้ผู้ใช้ทำการยืนยันตัวตนให้เสร็จสมบูรณ์
- **Access Token URL**: นี่คือ URI ที่ใช้สำหรับการร้องขอ credentials ชั่วคราวครั้งแรก โดยทั่วไป URL นี้จะลงท้ายด้วย `/oauth1/request` หรือ `/oauth1/token`
- **Consumer Key**: หรือที่เรียกว่า client key เหมือนกับ username สิ่งนี้ระบุ `oauth_consumer_key` ที่จะใช้สำหรับการเรียก
- **Consumer Secret**: หรือที่เรียกว่า client secret เหมือนกับ password
- **Request Token URL**: นี่คือ URI ที่ใช้ในการเปลี่ยนจาก credentials ชั่วคราวเป็น credentials ระยะยาวหลังจากการยืนยันตัวตน โดยทั่วไป URL นี้จะลงท้ายด้วย `/oauth1/access`
- เลือก **Signature Method** ที่ auth handshake ใช้ สิ่งนี้ระบุ `oauth_signature_method` ที่จะใช้สำหรับการเรียก ตัวเลือกได้แก่:
	- **HMAC-SHA1**
	- **HMAC-SHA256**
	- **HMAC-SHA512**

สำหรับการรวม OAuth1 ส่วนใหญ่ คุณจะต้องกำหนดค่าแอป บริการ หรือการรวมระบบเพื่อสร้างค่าสำหรับฟิลด์ส่วนใหญ่เหล่านี้ ใช้ **OAuth Redirect URL** ใน n8n เป็น redirect URL หรือ redirect URI สำหรับบริการดังกล่าว

อ่านเพิ่มเติมเกี่ยวกับ [OAuth1](https://oauth.net/1/){:target=_blank .external-link} และ [OAuth1 authorization flow](https://oauth1.wp-api.org/docs/basics/Auth-Flow.html){:target=_blank .external-link}

## Using OAuth2

ใช้ generic authentication นี้หากแอปหรือบริการของคุณรองรับการยืนยันตัวตนแบบ OAuth2

ข้อกำหนดในการตั้งค่า credential นี้ขึ้นอยู่กับ **Grant Type** ที่เลือก โปรดดู [OAuth Grant Types](https://oauth.net/2/grant-types/) สำหรับข้อมูลเพิ่มเติมเกี่ยวกับ grant type แต่ละประเภท

สำหรับการรวม OAuth2 ส่วนใหญ่ คุณจะต้องกำหนดค่าแอป บริการ หรือการรวมระบบ ใช้ **OAuth Redirect URL** ใน n8n เป็น redirect URL หรือ redirect URI สำหรับบริการดังกล่าว

อ่านเพิ่มเติมเกี่ยวกับ [OAuth2](https://oauth.net/2/){:target=_blank .external-link}

### Authorization Code grant type

ใช้ Authorization Code grant type เพื่อแลกเปลี่ยน authorization code เป็น access token auth flow ใช้ redirect URL เพื่อส่งผู้ใช้กลับไปยัง client จากนั้น application จะรับ authorization code จาก URL และใช้เพื่อขอ access token ดูข้อมูลเพิ่มเติมได้ที่ [Authorization Code Request](https://www.oauth.com/oauth2-servers/access-tokens/authorization-code-request/){:target=_blank .external-link}

ในการตั้งค่า credential นี้ ให้เลือก **Authorization Code** เป็น **Grant Type**

จากนั้นป้อน:

- **Authorization URL**
- **Access Token URL**
- **Client ID**: ID หรือ username ที่จะใช้เข้าสู่ระบบ
- **Client Secret**: secret หรือ password ที่ใช้เข้าสู่ระบบ
- _Optional:_ ป้อน **Scope** หนึ่งรายการหรือมากกว่าสำหรับ credential หากไม่ระบุ credential จะร้องขอ scopes ทั้งหมดที่มีให้สำหรับ client
- _Optional:_ บางบริการต้องการ query parameters เพิ่มเติม หากบริการของคุณต้องการ ให้เพิ่มเป็น **Auth URI Query Parameters**
- **Authentication** type: เลือกตัวเลือกที่เหมาะสมกับกรณีการใช้งานของคุณมากที่สุด ตัวเลือกได้แก่:
	- **Header**: ส่ง credentials เป็น basic auth header
	- **Body**: ส่ง credentials ใน body ของ request
- _Optional:_ เลือกว่าจะ **Ignore SSL Issues** หรือไม่ หากเปิดใช้งาน n8n จะเชื่อมต่อแม้ว่าการตรวจสอบ SSL จะล้มเหลว

### Client Credentials grant type

ใช้ Client Credentials grant type เมื่อ applications ขอ access token เพื่อเข้าถึง resources ของตนเอง ไม่ใช่ในนามของผู้ใช้ ดูข้อมูลเพิ่มเติมได้ที่ [Client Credentials](https://www.oauth.com/oauth2-servers/access-tokens/client-credentials/){:target=_blank .external-link}

ในการตั้งค่า credential นี้ ให้เลือก **Client Credentials** เป็น **Grant Type**

จากนั้นป้อน:

- **Access Token URL**: URL ที่จะเรียกเพื่อเริ่ม OAuth2 flow โดยทั่วไป URL นี้จะลงท้ายด้วย `/token`
- **Client ID**: ID หรือ username ที่จะใช้เข้าสู่ระบบ client
- **Client Secret**: secret หรือ password ที่ใช้เข้าสู่ระบบ client
- _Optional:_ ป้อน **Scope** หนึ่งรายการหรือมากกว่าสำหรับ credential บริการส่วนใหญ่ไม่รองรับ scopes สำหรับ Client Credentials grant types; ป้อน scopes ที่นี่เฉพาะในกรณีที่บริการของคุณรองรับเท่านั้น
- **Authentication** type: เลือกตัวเลือกที่เหมาะสมกับกรณีการใช้งานของคุณมากที่สุด ตัวเลือกได้แก่:
	- **Header**: ส่ง credentials เป็น basic auth header
	- **Body**: ส่ง credentials ใน body ของ request
- _Optional:_ เลือกว่าจะ **Ignore SSL Issues** หรือไม่ หากเปิดใช้งาน n8n จะเชื่อมต่อแม้ว่าการตรวจสอบ SSL จะล้มเหลว

### PKCE grant type

Proof Key for Code Exchange (PKCE) grant type เป็นส่วนขยายของ Authorization Code flow เพื่อป้องกันการโจมตีแบบ CSRF และ authorization code injection

ในการตั้งค่า credential นี้ ให้เลือก **PKCE** เป็น **Grant Type**

จากนั้นป้อน:

- **Authorization URL**
- **Access Token URL**
- **Client ID**: ID หรือ username ที่จะใช้เข้าสู่ระบบ
- **Client Secret**: secret หรือ password ที่ใช้เข้าสู่ระบบ
- _Optional:_ ป้อน **Scope** หนึ่งรายการหรือมากกว่าสำหรับ credential หากไม่ระบุ credential จะร้องขอ scopes ทั้งหมดที่มีให้สำหรับ client
- _Optional:_ บางบริการต้องการ query parameters เพิ่มเติม หากบริการของคุณต้องการ ให้เพิ่มเป็น **Auth URI Query Parameters**
- **Authentication** type: เลือกตัวเลือกที่เหมาะสมกับกรณีการใช้งานของคุณมากที่สุด ตัวเลือกได้แก่:
	- **Header**: ส่ง credentials เป็น basic auth header
	- **Body**: ส่ง credentials ใน body ของ request
- _Optional:_ เลือกว่าจะ **Ignore SSL Issues** หรือไม่ หากเปิดใช้งาน n8n จะเชื่อมต่อแม้ว่าการตรวจสอบ SSL จะล้มเหลว

## Using query auth

ใช้ generic authentication นี้หากแอปหรือบริการของคุณรองรับการส่งผ่านการยืนยันตัวตนเป็น query parameter แบบ key/value เดียว (สำหรับ query parameters หลายตัว ให้ใช้ [Custom Auth](#using-custom-auth))

ในการตั้งค่า credential นี้ ให้ป้อน:

- query parameter key หรือ **Name**
- query parameter **Value**

## Using custom auth

ใช้ generic authentication นี้หากแอปหรือบริการของคุณรองรับการส่งผ่านการยืนยันตัวตนเป็น query parameters แบบ key/value หลายตัว หรือคุณต้องการความยืดหยุ่นมากกว่าตัวเลือก generic auth อื่นๆ

**Custom Auth** credential คาดหวังข้อมูล JSON เพื่อกำหนด credential ของคุณ คุณสามารถใช้ `headers`, `qs`, `body` หรือผสมกันได้ ตรวจสอบตัวอย่างด้านล่างเพื่อเริ่มต้น

### Sending two headers
```json
{
	"headers": {
		"X-AUTH-USERNAME": "username",
		"X-AUTH-PASSWORD": "password"
	}
}
```

### Body
```json
{
	 "body" : {
		"user": "username",
		"pass": "password"
	}
}
```

### Query string
```json
{
	"qs": { 
		"appid": "123456",
		"apikey": "my-api-key"
	}
}
```

### Sending header and query string
```json
{
	"headers": {
		"api-version": "202404"
	},
	"qs": {
		"apikey": "my-api-key"
	}
}
```

## Provide an SSL certificate

คุณสามารถส่ง SSL certificate พร้อมกับ HTTP request ของคุณได้ สร้าง SSL certificate เป็น credential แยกต่างหากเพื่อใช้โดย node:

1.  ใน HTTP Request node **Settings** เปิดใช้งาน **SSL Certificates**
2.  บนแท็บ **Parameters** เพิ่ม SSL Certificate credential ที่มีอยู่ลงใน **Credential for SSL Certificates** หรือสร้างใหม่

ในการตั้งค่า SSL Certificates credential ของคุณ คุณจะต้องเพิ่ม:

- Certificate Authority **CA** bundle
- **Certificate** (CRT): อาจปรากฏเป็น Public Key ขึ้นอยู่กับว่า CA ที่ออกใบรับรองของคุณคือใครและจัดรูปแบบ cert อย่างไร
- **Private Key** (KEY)
- _Optional:_ หาก **Private Key** ถูกเข้ารหัส ให้ป้อน **Passphrase** สำหรับ private key

หาก SSL certificate ของคุณอยู่ในไฟล์เดียว (เช่น ไฟล์ `.pfx`) คุณจะต้องเปิดไฟล์เพื่อคัดลอกรายละเอียดจากไฟล์นั้นไปวางในฟิลด์ที่เหมาะสม:

- ป้อน Public Key/CRT เป็น **Certificate**
- ป้อน **Private Key**/KEY ในฟิลด์นั้น
