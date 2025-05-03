---
#https://www.notion.so/n8n/Frontmatter-432c2b8dff1f43d4b1c8d20075510fe4
title: ข้อมูลยืนยันตัวตน OpenWeatherMap
description: เอกสารสำหรับข้อมูลยืนยันตัวตน OpenWeatherMap ใช้ข้อมูลนี้เพื่อยืนยันตัวตน OpenWeatherMap ใน n8n แพลตฟอร์ม workflow automation
contentType: [integration, reference]
priority: medium
---

# OpenWeatherMap credentials

คุณสามารถใช้ credentials เหล่านี้เพื่อยืนยันตัวตนใน nodes ต่อไปนี้:

- [OpenWeatherMap](/integrations/builtin/app-nodes/n8n-nodes-base.openweathermap.md)

## Supported authentication methods

- API access token

## Related resources

อ้างอิง [OpenWeatherMap's API documentation](https://openweathermap.org/api){:target=_blank .external-link} สำหรับข้อมูลเพิ่มเติมเกี่ยวกับบริการนี้

## Using API access token

ในการกำหนดค่า credential นี้ คุณจะต้องมีบัญชี [OpenWeatherMap](https://openweathermap.org/){:target=_blank .external-link} และ:

- **Access Token**

วิธีรับ **Access Token** ของคุณ:

1. หลังจากที่คุณยืนยันที่อยู่อีเมลของคุณแล้ว OpenWeatherMap จะรวม **API Key** ไว้ในอีเมลต้อนรับของคุณ
2. คัดลอก key นั้นและป้อนลงใน credential ของ n8n

หากคุณต้องการสร้าง key ใหม่:

1. หากต้องการสร้าง key ใหม่ ให้ไปที่ **Account >** [**API Keys**](https://home.openweathermap.org/api_keys){:target=_blank .external-link}
2. ในส่วน **Create Key** ให้ป้อน **API Key Name** เช่น `n8n integration`
3. เลือก **Generate** เพื่อสร้าง key ของคุณ
4. คัดลอก key ที่สร้างขึ้นและป้อนลงใน credential ของ n8n
