---
#https://www.notion.so/n8n/Frontmatter-432c2b8dff1f43d4b1c8d20075510fe4
title: Twilio node documentation
description: Learn how to use the Twilio node in n8n. Follow technical documentation to integrate Twilio node into your workflows.
contentType: [integration, reference]
priority: medium
---

# Twilio node

ใช้ Twilio node เพื่อช่วยให้งานใน Twilio เป็นอัตโนมัติและเชื่อมต่อกับแอปพลิเคชันอื่น ๆ โดย n8n รองรับการส่งข้อความ MMS/SMS และ WhatsApp ผ่าน Twilio

/// note | Credentials
ดู [Twilio credentials](/integrations/builtin/credentials/twilio.md) สำหรับคำแนะนำในการตั้งค่า authentication.

--8<-- "_snippets/integrations/builtin/app-nodes/ai-tools.md"

## Operations

* SMS
    * Send SMS/MMS/WhatsApp message
* Call
    * Make a phone call using text-to-speech to say a message

## Templates and examples

<!-- see https://www.notion.so/n8n/Pull-in-templates-for-the-integrations-pages-37c716837b804d30a33b47475f6e3780 -->
[[ templatesWidget(page.title, 'twilio') ]]

## Related resources

ดู [Twilio's documentation](https://www.twilio.com/docs/usage/api){:target=_blank .external-link} สำหรับข้อมูลเพิ่มเติมเกี่ยวกับบริการนี้.

--8<-- "_snippets/integrations/builtin/app-nodes/operation-not-supported.md"
