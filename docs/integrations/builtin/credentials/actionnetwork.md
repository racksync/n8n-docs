---
#https://www.notion.so/n8n/Frontmatter-432c2b8dff1f43d4b1c8d20075510fe4
title: Action Network credentials
description: Documentation for Action Network credentials. Use these credentials to authenticate Action Network in n8n, a workflow automation platform.
contentType: [integration, reference]
priority: medium
---

# Action Network credentials

คุณสามารถใช้ credentials นี้เพื่อเชื่อมต่อกับ node เหล่านี้:

- [Action Network](/integrations/builtin/app-nodes/n8n-nodes-base.actionnetwork.md)

## Supported authentication methods

- API key

## Related resources

ดูรายละเอียดเพิ่มเติมเกี่ยวกับการใช้งาน API ได้ที่ [Action Network's API documentation](https://actionnetwork.org/docs/){:target=_blank .external-link}

## Using API key

ถ้าจะตั้งค่า credentials นี้ คุณต้องมีบัญชี [Action Network](https://actionnetwork.org/){:target=_blank .external-link} ที่ [เปิดใช้งาน API key access แล้ว](#request-api-access) และ:

- **API Key**

วิธีขอ API key:

1. ล็อกอินเข้าบัญชี Action Network ของคุณ
2. จากเมนู **Start Organizing** เลือก **Details >** [**API & Sync**](https://actionnetwork.org/apis){:target=_blank .external-link}
3. เลือก list ที่คุณต้องการสร้าง API key ให้
4. สร้าง API key สำหรับ list นั้น
5. คัดลอก **API Key** แล้วนำไปใส่ใน credential ของ n8n

ดูข้อมูลเพิ่มเติมได้ที่ [Action Network API Authentication instructions](https://actionnetwork.org/docs/v2/#auth){:target=_blank .external-link}

## Request API access

แต่ละบัญชีผู้ใช้และ group บน Action Network จะมี API key แยกต่างหากสำหรับเข้าถึงข้อมูลของผู้ใช้หรือ group นั้นๆ

คุณต้องขอสิทธิ์เข้าถึง API จาก Action Network โดยตรง ซึ่งทำได้ 2 วิธี:

1. ถ้าคุณเป็นลูกค้าแบบชำระเงินอยู่แล้ว [ติดต่อพวกเขา](https://actionnetwork.org/contact) เพื่อขอ partner access ซึ่งจะรวมถึงสิทธิ์การเข้าถึง API key ด้วย
2. ถ้าคุณเป็น developer [ขอ developer account](https://actionnetwork.org/developers){:target=_blank .external-link} เมื่อคำขอของคุณได้รับอนุมัติ คุณจะได้รับสิทธิ์เข้าถึง API key
