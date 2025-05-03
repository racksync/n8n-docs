---
#https://www.notion.so/n8n/Frontmatter-432c2b8dff1f43d4b1c8d20075510fe4
title: ประเภท Node: Trigger และ Action
description: อธิบายประเภท node หลักใน n8n: trigger และ action
contentType: explanation
---

# Node types: Trigger and Action

n8n มี node อยู่ 2 ประเภทหลัก ๆ คือ trigger node และ action node

ทั้งสองแบบนี้ใช้สำหรับเชื่อมต่อกับบริการภายนอก

## Trigger nodes

[Trigger nodes](/glossary.md#trigger-node-n8n) จะเป็นตัวเริ่ม workflow และส่งข้อมูลเริ่มต้นให้ workflow หนึ่ง workflow สามารถมี trigger node ได้หลายตัว แต่เวลาทำงานจริงจะมีแค่ตัวเดียวที่ทำงานตาม event ที่เกิดขึ้น

Trigger node ใน n8n มี 3 ประเภท:

| Type | Description | Example Nodes |
| --- | --- | --- |
| Webhook | Node สำหรับบริการที่รองรับ webhook โดย node จะคอยฟัง event และ trigger workflow แบบ real time | [Zendesk Trigger](https://github.com/n8n-io/n8n/tree/master/packages/nodes-base/nodes/Zendesk){:target=_blank .external-link}, [Telegram Trigger](https://github.com/n8n-io/n8n/tree/master/packages/nodes-base/nodes/Telegram){:target=_blank .external-link}, [Brevo Trigger](https://github.com/n8n-io/n8n/tree/master/packages/nodes-base/nodes/Brevo){:target=_blank .external-link} |
| Polling | Node สำหรับบริการที่ไม่มี webhook โดย node จะเช็คข้อมูลใหม่เป็นระยะ ๆ และ trigger workflow เมื่อมีข้อมูลใหม่ | [Airtable Trigger](https://github.com/n8n-io/n8n/tree/master/packages/nodes-base/nodes/Airtable){:target=_blank .external-link}, [Gmail Trigger](https://github.com/n8n-io/n8n/tree/master/packages/nodes-base/nodes/Google/Gmail){:target=_blank .external-link}, [Google Sheet Trigger](https://github.com/n8n-io/n8n/tree/master/packages/nodes-base/nodes/Google/Sheet){:target=_blank .external-link}, [RssFeed Read Trigger](https://github.com/n8n-io/n8n/tree/master/packages/nodes-base/nodes/RssFeedRead){:target=_blank .external-link} |
| Others | Node ที่จัดการ event แบบ real-time ที่ไม่ใช่ HTTP หรือ polling เช่น message queue หรือ trigger ตามเวลา | [AMQP Trigger](https://github.com/n8n-io/n8n/tree/master/packages/nodes-base/nodes/Amqp){:target=_blank .external-link}, [RabbitMQ Trigger](https://github.com/n8n-io/n8n/tree/master/packages/nodes-base/nodes/RabbitMQ){:target=_blank .external-link}, [MQTT Trigger](https://github.com/n8n-io/n8n/tree/master/packages/nodes-base/nodes/MQTT){:target=_blank .external-link}, [Schedule Trigger](https://github.com/n8n-io/n8n/tree/master/packages/nodes-base/nodes/Schedule){:target=_blank .external-link}, [Email Trigger (IMAP)](https://github.com/n8n-io/n8n/tree/master/packages/nodes-base/nodes/EmailReadImap){:target=_blank .external-link} |

## Action nodes

Action node จะใช้สำหรับทำงานต่าง ๆ ใน workflow เช่น แก้ไขข้อมูล หรือ trigger event ไปยังระบบอื่น ๆ

