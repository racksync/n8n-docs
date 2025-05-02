---
#https://www.notion.so/n8n/Frontmatter-432c2b8dff1f43d4b1c8d20075510fe4
title: MQTT node documentation
description: Learn how to use the MQTT node in n8n. Follow technical documentation to integrate MQTT node into your workflows.
contentType: [integration, reference]
priority: medium
---

# MQTT node

ใช้ MQTT node ในการทำงานอัตโนมัติใน MQTT และเชื่อมต่อกับแอปพลิเคชันอื่น ๆ โดย n8n รองรับการส่งข้อความผ่าน MQTT.

ในหน้านี้ คุณจะเห็นรายการ operations ที่ MQTT node รองรับและลิงก์ไปยังข้อมูลเพิ่มเติม.

/// note | Credentials
ดู [MQTT credentials](/integrations/builtin/credentials/mqtt.md) สำหรับคำแนะนำในการตั้งค่า authentication.
///

--8<-- "_snippets/integrations/builtin/app-nodes/ai-tools.md"

## Operations

Use the MQTT node to send a message. You can set the message topic, and choose whether to send the node input data as part of the message.

## Templates and examples

<!-- see https://www.notion.so/n8n/Pull-in-templates-for-the-integrations-pages-37c716837b804d30a33b47475f6e3780 -->
[[ templatesWidget(page.title, 'mqtt') ]]

## Related resources

n8n provides a trigger node for MQTT. You can find the trigger node docs [here](/integrations/builtin/trigger-nodes/n8n-nodes-base.mqtttrigger.md).

Refer to [MQTT's documentation](https://mqtt.org/getting-started/){:target=_blank .external-link} for more information about the service.
