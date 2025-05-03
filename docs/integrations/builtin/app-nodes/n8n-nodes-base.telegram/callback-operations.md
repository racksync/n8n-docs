---
#https://www.notion.so/n8n/Frontmatter-432c2b8dff1f43d4b1c8d20075510fe4
title: Telegram Callback operations
description: เอกสารสำหรับ Callback operations ใน Telegram node ของ n8n. รวมรายละเอียดการตั้งค่า.
contentType: [integration, reference]
priority: critical
---

# Telegram node Callback operations

ใช้ operations เหล่านี้เพื่อตอบ callback queries จาก inline keyboard หรือ inline queries  
ดูรายละเอียดเพิ่มเติมเกี่ยวกับ Telegram node ได้ที่ [Telegram](/integrations/builtin/app-nodes/n8n-nodes-base.telegram/index.md)

--8<-- "_snippets/integrations/builtin/app-nodes/ai-tools.md"

## Answer Query

ใช้ operation นี้เพื่อส่งคำตอบของ callback queries จาก [inline keyboards](https://core.telegram.org/bots/features#inline-keyboards){:target=_blank .external-link} ผ่าน Bot API [answerCallbackQuery](https://core.telegram.org/bots/api#answercallbackquery){:target=_blank .external-link}

ป้อนพารามิเตอร์เหล่านี้:

* **Credential to connect with**: สร้างหรือเลือก [Telegram credential](/integrations/builtin/credentials/telegram.md)  
* **Resource**: เลือก **Callback**  
* **Operation**: เลือก **Answer Query**  
* **Query ID**: ใส่ตัวระบุของ query ที่ต้องการตอบ  
    * หากต้องการส่ง Query ID โดยตรง ให้ใช้ [Telegram Trigger](/integrations/builtin/trigger-nodes/n8n-nodes-base.telegramtrigger/index.md) node ที่ trigger บน **Callback Query**  
* **Results**: ใส่ JSON-serialized array ของผลลัพธ์ที่จะส่งเป็นคำตอบ ดูเอกสาร Telegram [InlineQueryResults](https://core.telegram.org/bots/api#inlinequeryresult){:target=_blank .external-link} สำหรับรูปแบบข้อมูล  

ดูเอกสาร Bot API [answerCallbackQuery](https://core.telegram.org/bots/api#answercallbackquery){:target=_blank .external-link} สำหรับข้อมูลเพิ่มเติม

<!-- vale off -->
### Answer Query additional fields

Use the **Additional Fields** to further refine the behavior of the node. Select **Add Field** to add any of the following:

* **Cache Time**: Enter the maximum amount of time in seconds that the client may cache the result of the callback query. Telegram defaults to `0` seconds for this method.
* **Show Alert**: Telegram can display the answer as a notification at the top of the chat screen or as an alert. Choose whether you want to keep the default notification display (turned off) or display the answer as an alert (turned on).
* **Text**: If you want the answer to show text, enter up to 200 characters of text here.
* **URL**: Enter a URL that will be opened by the user's client. Refer to the **url** parameter instructions at the Telegram Bot API [answerCallbackQuery](https://core.telegram.org/bots/api#answercallbackquery){:target=_blank .external-link} documentation for more information.
<!-- vale on -->

## Answer Inline Query

Use this operation to send answers to callback queries sent from inline queries using the Bot API [answerInlineQuery](https://core.telegram.org/bots/api#answerinlinequery){:target=_blank .external-link} method.

Enter these parameters:

* **Credential to connect with**: Create or select an existing [Telegram credential](/integrations/builtin/credentials/telegram.md).
* **Resource**: Select **Callback**.
* **Operation**: Select **Answer Inline Query**.
* **Query ID**: Enter the unique identifier of the query you want to answer.
    * To feed a Query ID directly into this node, use the [Telegram Trigger](/integrations/builtin/trigger-nodes/n8n-nodes-base.telegramtrigger/index.md) node triggered on the **Inline Query**.
* **Results**: Enter a JSON-serialized array of results you want to use as answers to the query. Refer to the Telegram [InlineQueryResults](https://core.telegram.org/bots/api#inlinequeryresult){:target=_blank .external-link} documentation for more information on formatting your array.

Telegram allows a maximum of 50 results per query.

Refer to the Telegram Bot API [answerInlineQuery](https://core.telegram.org/bots/api#answerinlinequery){:target=_blank .external-link} documentation for more information.

<!-- vale off -->
### Answer Inline Query additional fields

Use the **Additional Fields** to further refine the behavior of the node. Select **Add Field** to add any of the following:

* **Cache Time**: The maximum amount of time in seconds that the client may cache the result of the callback query. Telegram defaults to `300` seconds for this method.
* **Show Alert**: Telegram can display the answer as a notification at the top of the chat screen or as an alert. Choose whether you want to keep the default notification display (turned off) or display the answer as an alert (turned on).
* **Text**: If you want the answer to show text, enter up to 200 characters of text here.
* **URL**: Enter a URL that the user's client will open.
<!-- vale on -->