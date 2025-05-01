---
#https://www.notion.so/n8n/Frontmatter-432c2b8dff1f43d4b1c8d20075510fe4
title: MQTT credentials
description: Documentation for MQTT credentials. Use these credentials to authenticate MQTT in n8n, a workflow automation platform.
contentType: [integration, reference]
priority: medium
---

# MQTT credentials

คุณสามารถใช้ credentials เหล่านี้เพื่อยืนยันตัวตนใน nodes ต่อไปนี้:

- [MQTT](/integrations/builtin/app-nodes/n8n-nodes-base.mqtt.md)
- [MQTT Trigger](/integrations/builtin/trigger-nodes/n8n-nodes-base.mqtttrigger.md)

## Prerequisites

ติดตั้ง [MQTT broker](https://mqtt.org/){:target=_blank .external-link}

MQTT มีรายการ Servers/Brokers ที่ [MQTT Software](https://mqtt.org/software/){:target=_blank .external-link}

## Supported authentication methods

- Broker connection

## Related resources

อ้างอิง [MQTT's documentation](https://mqtt.org/){:target=_blank .external-link} สำหรับข้อมูลเพิ่มเติมเกี่ยวกับโปรโตคอล MQTT

อ้างอิงเอกสารของผู้ให้บริการ broker ของคุณสำหรับรายละเอียดและการกำหนดค่าเพิ่มเติม

## Using broker connection

ในการกำหนดค่า credential นี้ คุณจะต้องมี:

- **Protocol** ของ MQTT broker ของคุณ
- **Host**
- **Port**
- **Username** และ **Password** เพื่อยืนยันตัวตน
- หากคุณใช้ **SSL** ใบรับรองและ keys ที่เกี่ยวข้อง

วิธีตั้งค่า:

1. เลือก **Protocol** ของ broker ซึ่งกำหนด URL ที่ n8n ใช้ ตัวเลือกได้แก่:
    - **Mqtt**: เริ่มต้น URL ด้วยโปรโตคอล `mqtt:` มาตรฐาน
    - **Mqtts**: เริ่มต้น URL ด้วยโปรโตคอล `mqtts:` ที่ปลอดภัย
    - **Ws**: เริ่มต้น URL ด้วยโปรโตคอล WebSocket `ws:`
2. ป้อน **Host** ของ broker ของคุณ
3. ป้อนหมายเลข **Port** ที่ n8n ควรใช้เพื่อเชื่อมต่อกับ broker host
4. ป้อน **Username** เพื่อเข้าสู่ระบบ broker
5. ป้อน **Password** ของผู้ใช้นั้น
6. หากคุณต้องการรับข้อความ QoS 1 และ 2 ขณะออฟไลน์ ให้ปิดสวิตช์ **Clean Session**
7. ป้อน **Client ID** ที่คุณต้องการให้ credential ใช้ หากคุณเว้นว่างไว้ n8n จะสร้างให้คุณ คุณสามารถใช้ Client ID แบบคงที่หรือแบบ expression-based ได้
    - Client IDs มีประโยชน์ในการระบุและติดตามการเข้าถึงการเชื่อมต่อ n8n แนะนำให้ใช้บางอย่างที่มี `n8n` อยู่ในนั้นเพื่อให้ง่ายต่อการตรวจสอบ
8. หาก MQTT broker ของคุณใช้ SSL ให้เปิดสวิตช์ **SSL** เมื่อคุณเปิดใช้งาน:
    1. เลือกว่าจะใช้การเชื่อมต่อ **Passwordless** กับใบรับรองหรือไม่ ซึ่งเหมือนกับกลไก SASL EXTERNAL หากเปิดใช้งาน:
        1. เลือกว่าจะ **Reject Unauthorized Certificate**: หากปิดใช้งาน n8n จะเชื่อมต่อแม้ว่าการตรวจสอบใบรับรองจะล้มเหลว
        2. เพิ่ม SSL **Client Certificate**
        3. เพิ่ม SSL **Client Key** สำหรับ Client Certificate
    2. SSL **CA Certificates** หนึ่งรายการหรือมากกว่า

อ้างอิงเอกสารของผู้ให้บริการ MQTT broker ของคุณสำหรับคำแนะนำการกำหนดค่าโดยละเอียดเพิ่มเติม
