---
#https://www.notion.so/n8n/Frontmatter-432c2b8dff1f43d4b1c8d20075510fe4
title: คู่มือการตั้งค่า Wolfram|Alpha credentials
description: วิธีตั้งค่า Wolfram|Alpha credentials เพื่อเชื่อมต่อและยืนยันตัวตนกับ Wolfram|Alpha ใน n8n
contentType: [integration, reference]
priority: medium
---

# Wolfram|Alpha credentials

คุณสามารถใช้ credentials เหล่านี้เพื่อยืนยันตัวตนกับ node ต่อไปนี้:

* [Wolfram|Alpha](/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.toolwolframalpha.md)

## Supported authentication methods

- API key

## Related resources

ดูข้อมูลเพิ่มเติมเกี่ยวกับบริการนี้ได้ที่ [Wolfram|Alpha's Simple API documentation](https://products.wolframalpha.com/simple-api/documentation){:target=_blank .external-link}

--8<-- "_snippets/integrations/builtin/cluster-nodes/langchain-overview-link.md"

## Using API key

ในการตั้งค่า credential นี้ คุณต้องมี [Wolfram ID](https://account.wolfram.com){:target=_blank .external-link} ที่ลงทะเบียนแล้ว และ:

- **App ID**

วิธีขอ App ID:

1. ไปที่ Wolfram|Alpha Developer Portal แล้วเข้า [**API Access**](https://developer.wolframalpha.com/access){:target=_blank .external-link}
2. เลือก **Get an App ID**
3. กรอก **Name** ของแอป เช่น `n8n integration`
4. กรอก **Description** ของแอป
5. เลือก **Simple API** ที่ **API**
6. กด **Submit**
6. คัดลอก **App ID** ที่ได้มาใส่ใน n8n credential

ดูรายละเอียดเพิ่มเติมได้ที่ **Getting Started** ใน [Wolfram|Alpha Simple API documentation](https://products.wolframalpha.com/simple-api/documentation){:target=_blank .external-link}

## Resolve Forbidden connection error

ถ้าคุณกรอก App ID แล้วเจอ error ว่า credential **Forbidden** ให้ตรวจสอบว่าได้ยืนยันอีเมลสำหรับ Wolfram ID แล้วหรือยัง:

1. ไปที่ [Wolfram ID Details](https://account.wolfram.com/wolframid){:target=_blank .external-link}
2. ถ้าไม่เห็นป้าย **Verified** ใต้ **Email address** ให้กดลิงก์ **Send a verification email**
3. ต้องเปิดลิงก์ในอีเมลนั้นเพื่อยืนยันอีเมล

อาจใช้เวลาหลายนาทีกว่าการยืนยันจะอัปเดตไปยัง API เมื่อเสร็จแล้วให้ลองเชื่อมต่อ credential ใน n8n ใหม่อีกครั้ง
