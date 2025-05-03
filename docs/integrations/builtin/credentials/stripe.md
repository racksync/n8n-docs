---
title: ข้อมูลเข้าสู่ระบบ Stripe
description: คู่มือการตั้งค่า Stripe credentials สำหรับเชื่อมต่อ Stripe กับ n8n
contentType: [integration, reference]
priority: medium
---

# Stripe credentials

คุณสามารถใช้ credentials นี้เพื่อยืนยันตัวตนกับ node ต่อไปนี้ได้:

- [Stripe Trigger](/integrations/builtin/trigger-nodes/n8n-nodes-base.stripetrigger.md)
- [Stripe](/integrations/builtin/app-nodes/n8n-nodes-base.stripe.md)

## Supported authentication methods

- API key

## Related resources

ดูข้อมูลเพิ่มเติมเกี่ยวกับบริการนี้ได้ที่ [Stripe's API documentation](https://docs.stripe.com/api){:target=_blank .external-link}

## Using API key

ในการตั้งค่า credentials นี้ คุณจะต้องมีบัญชี admin หรือ developer ของ [Stripe](https://stripe.com/){:target=_blank .external-link} และ:

- **Secret Key** สำหรับ API

ก่อนจะสร้าง API key ให้ตัดสินใจก่อนว่าจะสร้างใน live mode หรือ test mode ดูรายละเอียดเพิ่มเติมได้ที่ [Test mode and live mode](#test-mode-and-live-mode)

### Live mode Secret key

วิธีสร้าง Secret key ใน live mode:

1. เปิด [Stripe developer dashboard](https://dashboard.stripe.com/developers){:target=_blank .external-link} แล้วเลือก [**API Keys**](https://dashboard.stripe.com/apikeys){:target=_blank .external-link}
2. ในส่วน **Standard Keys** ให้เลือก **Create secret key**
3. กรอก **Key name** เช่น `n8n integration`
4. กด **Create** แล้วจะเห็น API key ใหม่
4. คัดลอก key แล้วนำไปใส่ใน n8n credential ในช่อง **Secret Key**

ดูรายละเอียดเพิ่มเติมได้ที่ [Create a secret API key](https://docs.stripe.com/keys#create-api-secret-key){:target=_blank .external-link}

### Test mode Secret key

ถ้าต้องการใช้ Secret key ใน test mode ให้คัดลอก key ที่มีอยู่แล้ว:

1. ไปที่ [Stripe test mode developer dashboard](https://dashboard.stripe.com/test/developers){:target=_blank .external-link} แล้วเลือก [**API Keys**](https://dashboard.stripe.com/test/apikeys){:target=_blank .external-link}
2. ในส่วน **Standard Keys** ให้เลือก **Reveal test key** สำหรับ **Secret key**
3. คัดลอก key แล้วนำไปใส่ใน n8n credential ในช่อง **Secret Key**

ดูรายละเอียดเพิ่มเติมได้ที่ [Create a secret API key](https://docs.stripe.com/keys#create-api-secret-key){:target=_blank .external-link}

## Test mode and live mode

ทุก request ของ Stripe API จะอยู่ใน [test mode](https://docs.stripe.com/test-mode) หรือ live mode เท่านั้น โดยแต่ละ mode จะมี API key ของตัวเอง

ใช้ test mode เพื่อทดสอบกับข้อมูลจำลอง และ live mode สำหรับข้อมูลจริง ข้อมูลแต่ละ mode จะไม่สามารถเข้าถึงกันได้

ดูรายละเอียดเพิ่มเติมได้ที่ [API keys | Test mode versus live mode](https://docs.stripe.com/keys#test-live-modes){:target=_blank .external-link}

/// note | n8n credentials for both modes
ถ้าต้องการใช้ทั้ง live mode และ test mode ให้เก็บ key ของแต่ละ mode ใน n8n credential แยกกัน
///

## Key prefixes

Secret key ของ Stripe จะขึ้นต้นด้วย `sk_` เสมอ:

- live key จะขึ้นต้นด้วย `sk_live_`
- test key จะขึ้นต้นด้วย `sk_test_`

n8n ยังไม่ได้ทดสอบกับ Restricted keys (ขึ้นต้นด้วย `rk_`)

/// warning | Publishable keys
ห้ามใช้ Publishable keys (ขึ้นต้นด้วย `pk_`) กับ n8n credential ของคุณ
///
