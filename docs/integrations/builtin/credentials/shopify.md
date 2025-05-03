---
#https://www.notion.so/n8n/Frontmatter-432c2b8dff1f43d4b1c8d20075510fe4
title: ข้อมูลเข้าสู่ระบบ Shopify (Shopify credentials)
description: คู่มือการตั้งค่า Shopify credentials สำหรับเชื่อมต่อและยืนยันตัวตนกับ Shopify ใน n8n
contentType: [integration, reference]
priority: medium
---

# Shopify credentials

คุณสามารถใช้ credentials เหล่านี้เพื่อยืนยันตัวตนกับ node ต่อไปนี้บน Shopify

- [Shopify](/integrations/builtin/app-nodes/n8n-nodes-base.shopify.md)
- [Shopify Trigger](/integrations/builtin/trigger-nodes/n8n-nodes-base.shopifytrigger.md)

## Supported authentication methods

- Access token (แนะนำ): สำหรับ private app/ใช้กับร้านเดียว สร้างได้โดย admin ทั่วไป
- OAuth2: สำหรับ public app ต้องสร้างโดย partner account
- API key: เลิกใช้แล้ว

## Related resources

ดูรายละเอียดเพิ่มเติมได้ที่ [Shopify's authentication documentation](https://shopify.dev/docs/apps/auth){:target=_blank .external-link}

## Using access token

ในการตั้งค่า credential นี้ คุณจะต้องมี [Shopify](https://shopify.com/){:target=_blank .external-link} admin account และ:

- **Shop Subdomain**
- **Access Token**: ได้ตอนสร้าง custom app
- **APP Secret Key**: ได้ตอนสร้าง custom app

ขั้นตอนการสร้าง credential:

1. ใส่ **Shop Subdomain** ของคุณ
    - subdomain จะอยู่ใน URL: `https://<subdomain>.myshopify.com` เช่น ถ้า URL คือ `https://n8n.myshopify.com` Shop Subdomain คือ `n8n`
2. ใน Shopify ไปที่ **Admin > Settings >** [**Apps and sales channels**](https://admin.shopify.com/settings/apps){:target=_blank .external-link}
3. เลือก **Develop apps**
4. เลือก **Create a custom app**

    /// note | Don't see this option?
    ถ้าไม่เห็นตัวเลือกนี้ แสดงว่า store ของคุณยังไม่ได้เปิดใช้งาน custom app development ดูวิธี [Enable custom app development](#enable-custom-app-development) เพิ่มเติม
    ///

5. กรอก **App name**
6. เลือก **App developer** (เจ้าของร้านหรือคนที่มีสิทธิ์ Develop apps)
7. เลือก **Create app**
8. เลือก **Select scopes** แล้วเลือก API scopes ที่ต้องการใน **Admin API access scopes**
    - ถ้าจะใช้ทุกฟีเจอร์ใน [Shopify](/integrations/builtin/app-nodes/n8n-nodes-base.shopify.md) ให้เพิ่ม scope `read_orders`, `write_orders`, `read_products`, `write_products`
    - ดู scope เพิ่มเติมที่ [Shopify API Access Scopes](https://shopify.dev/docs/api/usage/access-scopes){:target=_blank .external-link}
9. เลือก **Save**
10. เลือก **Install app**
11. ใน modal เลือก **Install app**
12. เปิดส่วน **API Credentials** ของแอป
13. คัดลอก **Admin API Access Token** แล้วใส่ใน n8n credential ที่ **Access Token**
14. คัดลอก **API Secret Key** แล้วใส่ใน n8n credential ที่ **APP Secret Key**

ดูรายละเอียดเพิ่มเติมที่ [Creating a custom app](https://help.shopify.com/en/manual/apps/app-types/custom-apps){:target=_blank .external-link} และ [Generate access tokens for custom apps in the Shopify admin](https://shopify.dev/docs/apps/build/authentication-authorization/access-token-types/generate-app-access-tokens-admin){:target=_blank .external-link}

## Using OAuth2

ในการตั้งค่า credential นี้ คุณจะต้องมี [Shopify partner](https://www.shopify.com/partners){:target=_blank .external-link} account และ:

- **Client ID**: ได้ตอนสร้าง custom app
- **Client Secret**: ได้ตอนสร้าง custom app
- **Shop Subdomain**

ขั้นตอนการสร้าง credential:

/// note | Custom app development
Shopify มี template สำหรับสร้างแอปใหม่ คำแนะนำด้านล่างนี้จะเน้นเฉพาะส่วนที่จำเป็นสำหรับ n8n credential ดูรายละเอียดเพิ่มเติมที่ [Build dev docs](https://shopify.dev/docs/apps/build){:target=_blank .external-link}
///

1. เปิด [Shopify Partner dashboard](https://partners.shopify.com/){:target=_blank .external-link}
2. เลือก **Apps** จากเมนูซ้าย
3. เลือก **Create app**
4. ใน **Use Shopify Partners** กรอก **App name**
6. เลือก **Create app**
7. เมื่อเข้า app แล้ว คัดลอก **Client ID** ไปใส่ใน n8n credential
8. คัดลอก **Client Secret** ไปใส่ใน n8n credential
9. ในเมนูซ้าย เลือก **Configuration**
10. ใน n8n คัดลอก **OAuth Redirect URL** ไปใส่ใน **Allowed redirection URL(s)** ใน **URLs** section
10. ใน **URLs** section กรอก **App URL** ให้ตรงกับ host ของ **Allowed redirection URL(s)** เช่น base URL ของ n8n instance
8. เลือก **Save and release**
1. เลือก **Overview** จากเมนูซ้าย ตอนนี้สามารถเลือก **Test your app** เพื่อติดตั้งในร้าน หรือ **Choose distribution** เพื่อปล่อย public
1. ใน n8n ใส่ **Shop Subdomain** ของร้านที่ติดตั้งแอป
    - subdomain จะอยู่ใน URL: `https://<subdomain>.myshopify.com` เช่น ถ้า URL คือ `https://n8n.myshopify.com` Shop Subdomain คือ `n8n`

## Using API key

/// warning | Method deprecated
Shopify ไม่สร้าง API key พร้อม password แล้ว ให้ใช้วิธี [Access token](#using-access-token) แทน
///

ในการตั้งค่า credential นี้ คุณจะต้องมี:

- **API Key**
- **Password**
- **Shop Subdomain**: subdomain จะอยู่ใน URL: `https://<subdomain>.myshopify.com` เช่น ถ้า URL คือ `https://n8n.myshopify.com` Shop Subdomain คือ `n8n`
- _Optional:_ **Shared Secret**

## Common issues

ปัญหาที่พบบ่อยในการตั้งค่า Shopify credential และวิธีแก้ไข

### Enable custom app development

ถ้าไม่เห็นตัวเลือก **Create a custom app** แสดงว่ายังไม่มีใครเปิด custom app development ให้ร้าน

ต้อง login เป็นเจ้าของร้านหรือ user ที่มีสิทธิ์ **Enable app development**:

1. ใน Shopify ไปที่ **Admin > Settings >** [**Apps and sales channels**](https://admin.shopify.com/settings/apps){:target=_blank .external-link}
2. เลือก **Develop apps**
3. เลือก **Allow custom app development**
4. อ่านคำเตือนและข้อมูล แล้วเลือก **Allow custom app development**

### Forbidden credentials error

<!-- vale off -->
ถ้าเจอ error **Couldn't connect with these settings / Forbidden - perhaps check your credentials** ตอนทดสอบ credential อาจเกิดจาก [access scope](https://shopify.dev/docs/api/usage/access-scopes){:target=_blank .external-link} ของแอป เช่น scope `read_orders` ต้องใช้ `read_products` ด้วย ตรวจสอบ scope ที่ตั้งไว้กับ action ที่จะทำ
<!-- vale on -->
