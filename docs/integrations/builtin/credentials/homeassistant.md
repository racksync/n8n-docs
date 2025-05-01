---
#https://www.notion.so/n8n/Frontmatter-432c2b8dff1f43d4b1c8d20075510fe4
title: Home Assistant credentials
description: Documentation for Home Assistant credentials. Use these credentials to authenticate Home Assistant in n8n, a workflow automation platform.
contentType: [integration, reference]
priority: medium
---

# Home Assistant credentials

คุณสามารถใช้ credentials เหล่านี้เพื่อยืนยันตัวตนกับ node ต่อไปนี้ได้:

- [Home Assistant](/integrations/builtin/app-nodes/n8n-nodes-base.homeassistant.md)

## Supported authentication methods

- API access token

## Related resources

ดูข้อมูลเพิ่มเติมเกี่ยวกับบริการนี้ได้ที่ [Home Assistant's API documentation](https://developers.home-assistant.io/docs/api/rest){:target=_blank .external-link}

## Using API access token

ในการตั้งค่า credential นี้ คุณจะต้อง [Install](https://www.home-assistant.io/installation/) Home Assistant, สร้างบัญชี [Home Assistant](https://www.home-assistant.io/getting-started/onboarding) และมี:

- **Host** ของคุณ
- **Port**
- Long-Lived **Access Token**

วิธีสร้าง access token และตั้งค่า credential:

1.  ในการสร้าง **Access Token** ของคุณ ให้เข้าสู่ระบบ Home Assistant และเปิด [User profile](https://my.home-assistant.io/redirect/profile){:target=_blank .external-link} ของคุณ
2.  ในส่วน **Long-Lived Access Tokens** สร้าง token ใหม่
3.  คัดลอก token นี้และป้อนลงใน n8n เป็น **Access Token** ของคุณ
4.  ป้อน URL หรือ IP address ของ **Host** Home Assistant ของคุณ โดยไม่มี protocol `http://` หรือ `https://` เช่น `your.awesome.home`
5.  สำหรับ **Port** ให้ป้อน port ที่เหมาะสม:
	- หากคุณไม่ได้เปลี่ยนแปลง port ใดๆ และเข้าถึง Home Assistant ที่ `http://` ให้คงค่าเริ่มต้นเป็น `8123`
	- หากคุณไม่ได้เปลี่ยนแปลง port ใดๆ และเข้าถึง Home Assistant ที่ `https://` ให้ป้อน `443`
	- หากคุณกำหนดค่า Home Assistant ให้ใช้ port เฉพาะ ให้ป้อน port นั้น
6.  หากคุณเปิดใช้งาน SSL ใน Home Assistant ใน [config.yml map key](https://developers.home-assistant.io/docs/add-ons/configuration/?_highlight=ssl#add-on-configuration){:target=_blank .external-link} ให้เปิด toggle **SSL** ใน n8n หากคุณไม่แน่ใจ ควรเปิดการตั้งค่านี้หากคุณเข้าถึง UI ของ home assistant โดยใช้ `https://` แทน `http://`

