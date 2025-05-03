---
#https://www.notion.so/n8n/Frontmatter-432c2b8dff1f43d4b1c8d20075510fe4
title: ข้อมูลยืนยันตัวตน Mist
description: เอกสารสำหรับ Mist credentials ใช้เพื่อเชื่อมต่อ Mist ใน n8n
contentType: [integration, reference]
priority: medium
---

# Mist credentials

--8<-- "_snippets/integrations/builtin/credentials/cred-only-statement.md"

## Prerequisites

สร้างบัญชีและองค์กร [Mist](https://www.mist.com/){:target=_blank .external-link} อ้างอิง [Create a Mist account and Organization](https://www.mist.com/documentation/create-mist-org/){:target=_blank .external-link} สำหรับคำแนะนำโดยละเอียด

## Supported authentication methods

- API token

## Related resources

อ้างอิง [Mist's documentation](https://www.mist.com/documentation/mist-api-introduction/){:target=_blank .external-link} สำหรับข้อมูลเพิ่มเติมเกี่ยวกับบริการนี้ หากคุณเข้าสู่ระบบบัญชี Mist ของคุณ ให้ไปที่ [https://api.mist.com/api/v1/docs/Home](https://api.mist.com/api/v1/docs/Home){:target=_blank .external-link} เพื่อดูเอกสาร API ฉบับเต็ม

นี่คือ node สำหรับ credential เท่านั้น อ้างอิง [Custom API operations](/integrations/custom-operations.md) เพื่อเรียนรู้เพิ่มเติม ดู [example workflows and related content](https://n8n.io/integrations/mist/){:target=_blank .external-link} บนเว็บไซต์ของ n8n

## Using API token

ในการกำหนดค่า credential นี้ คุณจะต้องมี:

- **API Token**: คุณสามารถใช้ User API token หรือ Org API token ก็ได้ อ้างอิง [How to generate a user API token](https://www.mist.com/documentation/using-postman/){:target=_blank .external-link} สำหรับคำแนะนำในการสร้าง User API token อ้างอิง [Org API token](https://www.mist.com/documentation/org-api-token/){:target=_blank .external-link} สำหรับคำแนะนำในการสร้าง Org API token
- เลือก **Region** ที่คุณอยู่ ตัวเลือกได้แก่:
    - **Europe**: เลือกตัวเลือกนี้หากสภาพแวดล้อมคลาวด์ของคุณอยู่ในภูมิภาค EMEA ใดๆ
    - **Global**: เลือกตัวเลือกนี้หากสภาพแวดล้อมคลาวด์ของคุณอยู่ในภูมิภาค global ใดๆ
