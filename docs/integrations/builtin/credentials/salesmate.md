---
title: ข้อมูลเข้าสู่ระบบ Salesmate
description: คู่มือการตั้งค่า Salesmate credentials สำหรับเชื่อมต่อ Salesmate กับ n8n
contentType: [integration, reference]
---

# Salesmate credentials

คุณสามารถใช้ credentials เหล่านี้เพื่อยืนยันตัวตนกับ node ต่อไปนี้:

- [Salesmate](/integrations/builtin/app-nodes/n8n-nodes-base.salesmate.md)

## Prerequisites

สร้าง [Salesmate](https://salesmate.io/){:target=_blank .external-link} account ก่อน

## Supported authentication methods

- API token

## Related resources

ดูรายละเอียดเพิ่มเติมเกี่ยวกับบริการนี้ได้ที่ [Salesmate's API documentation](https://apidocs.salesmate.io/?version=latest){:target=_blank .external-link}

## Using API token

ในการตั้งค่า credentials นี้ คุณจะต้องมี:

- **Session Token**: หรือที่เรียกว่า **Access Key** ให้ไปสร้าง access key ได้ที่ **My Account > Access Key** ดูรายละเอียดเพิ่มเติมที่ [Access Rights and Keys](https://apidocs.salesmate.io/?version=latest#ac8296ec-cb44-4937-a860-5ae032397ca0){:target=_blank .external-link}
- **URL**: คือชื่อโดเมนหรือ base URL ของ Salesmate ของคุณ เช่น `n8n.salesmate.io`

