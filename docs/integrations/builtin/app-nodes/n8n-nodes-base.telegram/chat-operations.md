---
#https://www.notion.so/n8n/Frontmatter-432c2b8dff1f43d4b1c8d20075510fe4
title: Telegram Chat operations
description: เอกสารสำหรับ Chat operations ใน Telegram node ของ n8n. รวมรายละเอียดการตั้งค่า.
contentType: [integration, reference]
priority: critical
---

# Telegram node Chat operations

ใช้ operations เหล่านี้เพื่อดึงข้อมูล chat, members, administrators, ออกจาก chat, และตั้ง title/description ของ chat  
ดูรายละเอียดเพิ่มเติมเกี่ยวกับ Telegram node ได้ที่ [Telegram](/integrations/builtin/app-nodes/n8n-nodes-base.telegram/index.md)

--8<-- "_snippets/integrations/builtin/app-nodes/ai-tools.md"

## Get Chat

ใช้ operation นี้เพื่อดึงข้อมูลล่าสุดของ chat ผ่าน Bot API [getChat](https://core.telegram.org/bots/api#getchat){:target=_blank .external-link}

ป้อนพารามิเตอร์เหล่านี้:

* **Credential to connect with**: สร้างหรือเลือก [Telegram credential](/integrations/builtin/credentials/telegram.md)  
* **Resource**: เลือก **Chat**  
* **Operation**: เลือก **Get**  
* **Chat ID**: ใส่ Chat ID หรือ username ของ channel ในรูปแบบ `@channelusername`  
    * หากต้องการส่ง Chat ID โดยตรง ให้ใช้ [Telegram Trigger](/integrations/builtin/trigger-nodes/n8n-nodes-base.telegramtrigger/index.md) แล้วดู [Common Issues | Get the Chat ID](/integrations/builtin/app-nodes/n8n-nodes-base.telegram/common-issues.md#get-the-chat-id)  

ดูเอกสาร Bot API [getChat](https://core.telegram.org/bots/api#getchat){:target=_blank .external-link} สำหรับข้อมูลเพิ่มเติม

## Get Administrators

Use this operation to get a list of all administrators in a chat using the Bot API [getChatAdministrators](https://core.telegram.org/bots/api#getchatadministrators){:target=_blank .external-link} method.

Enter these parameters:

* **Credential to connect with**: Create or select an existing [Telegram credential](/integrations/builtin/credentials/telegram.md).
* **Resource**: Select **Chat**.
* **Operation**: Select **Get Administrators**.
* **Chat ID**: Enter the Chat ID or username of the target channel in the format `@channelusername`.
    * To feed a Chat ID directly into this node, use the [Telegram Trigger](/integrations/builtin/trigger-nodes/n8n-nodes-base.telegramtrigger/index.md) node. Refer to [Common Issues | Get the Chat ID](/integrations/builtin/app-nodes/n8n-nodes-base.telegram/common-issues.md#get-the-chat-id) for more information.

Refer to the Telegram Bot API [getChatAdministrators](https://core.telegram.org/bots/api#getchatadministrators){:target=_blank .external-link} documentation for more information.

## Get Chat Member

Use this operation to get the details of a chat member using the Bot API [getChatMember](https://core.telegram.org/bots/api#getchatmember){:target=_blank .external-link} method.

Enter these parameters:

* **Credential to connect with**: Create or select an existing [Telegram credential](/integrations/builtin/credentials/telegram.md).
* **Resource**: Select **Chat**.
* **Operation**: Select **Get Member**.
* **Chat ID**: Enter the Chat ID or username of the target channel in the format `@channelusername`.
    * To feed a Chat ID directly into this node, use the [Telegram Trigger](/integrations/builtin/trigger-nodes/n8n-nodes-base.telegramtrigger/index.md) node. Refer to [Common Issues | Get the Chat ID](/integrations/builtin/app-nodes/n8n-nodes-base.telegram/common-issues.md#get-the-chat-id) for more information.
* **User ID**: Enter the unique identifier of the user whose information you want to get.

Refer to the Telegram Bot API [getChatMember](https://core.telegram.org/bots/api#getchatmember){:target=_blank .external-link} documentation for more information.

## Leave Chat

Use this operation to leave a chat using the Bot API [leaveChat](https://core.telegram.org/bots/api#leavechat){:target=_blank .external-link} method.

Enter these parameters:

* **Credential to connect with**: Create or select an existing [Telegram credential](/integrations/builtin/credentials/telegram.md).
* **Resource**: Select **Chat**.
* **Operation**: Select **Leave**.
* **Chat ID**: Enter the Chat ID or username of the channel you wish to leave in the format `@channelusername`.
    * To feed a Chat ID directly into this node, use the [Telegram Trigger](/integrations/builtin/trigger-nodes/n8n-nodes-base.telegramtrigger/index.md) node. Refer to [Common Issues | Get the Chat ID](/integrations/builtin/app-nodes/n8n-nodes-base.telegram/common-issues.md#get-the-chat-id) for more information.

Refer to the Telegram Bot API [leaveChat](https://core.telegram.org/bots/api#leavechat){:target=_blank .external-link} documentation for more information.

## Set Description

Use this operation to set the description of a chat using the Bot API [setChatDescription](https://core.telegram.org/bots/api#setchatdescription){:target=_blank .external-link} method.

Enter these parameters:

* **Credential to connect with**: Create or select an existing [Telegram credential](/integrations/builtin/credentials/telegram.md).
* **Resource**: Select **Chat**.
* **Operation**: Select **Set Description**.
* **Chat ID**: Enter the Chat ID or username of the channel you wish to leave in the format `@channelusername`.
    * To feed a Chat ID directly into this node, use the [Telegram Trigger](/integrations/builtin/trigger-nodes/n8n-nodes-base.telegramtrigger/index.md) node. Refer to [Common Issues | Get the Chat ID](/integrations/builtin/app-nodes/n8n-nodes-base.telegram/common-issues.md#get-the-chat-id) for more information.
* **Description**: Enter the new description you'd like to set the chat to use, maximum of 255 characters.

Refer to the Telegram Bot API [setChatDescription](https://core.telegram.org/bots/api#setchatdescription){:target=_blank .external-link} documentation for more information.

## Set Title

Use this operation to set the title of a chat using the Bot API [setChatTitle](https://core.telegram.org/bots/api#setchattitle){:target=_blank .external-link} method.

Enter these parameters:

* **Credential to connect with**: Create or select an existing [Telegram credential](/integrations/builtin/credentials/telegram.md).
* **Resource**: Select **Chat**.
* **Operation**: Select **Set Title**.
* **Chat ID**: Enter the Chat ID or username of the channel you wish to leave in the format `@channelusername`.
    * To feed a Chat ID directly into this node, use the [Telegram Trigger](/integrations/builtin/trigger-nodes/n8n-nodes-base.telegramtrigger/index.md) node. Refer to [Common Issues | Get the Chat ID](/integrations/builtin/app-nodes/n8n-nodes-base.telegram/common-issues.md#get-the-chat-id) for more information.
* **Title**: Enter the new title you'd like to set the chat to use, maximum of 255 characters.

Refer to the Telegram Bot API [setChatTitle](https://core.telegram.org/bots/api#setchattitle){:target=_blank .external-link} documentation for more information.
