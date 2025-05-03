---
#https://www.notion.so/n8n/Frontmatter-432c2b8dff1f43d4b1c8d20075510fe4
title: เอกสารคู่มือ Line node
description: เรียนรู้วิธีใช้ Line node ใน n8n และดูเอกสารทางเทคนิคเพื่อเชื่อมต่อ Line node เข้ากับ workflows ของคุณ
contentType: [integration, reference]
priority: medium
---

# Line node

<!-- vale off -->
/// warning | Deprecated: End of service
LINE Notify is discontinuing service as of April 1st 2025 and this node will no longer work after that date. View LINE Notify's [end of service announement](https://notify-bot.line.me/closing-announce){:target=_blank .external-link} for more information.
///
<!-- vale on -->

ใช้ Line node ในการทำงานอัตโนมัติใน Line และเชื่อมต่อกับแอปพลิเคชันอื่น ๆ โดย n8n รองรับการส่ง notifications ไปยังผู้ใช้หรือกลุ่ม.

ในหน้านี้ คุณจะพบรายการ operations ที่ Line node รองรับและลิงก์ไปยังข้อมูลเพิ่มเติม.

/// note | Credentials
ดู [Line credentials](/integrations/builtin/credentials/line.md) สำหรับคำแนะนำในการตั้งค่า authentication.
///

--8<-- "_snippets/integrations/builtin/app-nodes/ai-tools.md"

## Operations

* Notification
    * Sends notifications to users or groups

## Templates and examples

<!-- see https://www.notion.so/n8n/Pull-in-templates-for-the-integrations-pages-37c716837b804d30a33b47475f6e3780 -->
[[ templatesWidget(page.title, 'line') ]]

--8<-- "_snippets/integrations/builtin/app-nodes/operation-not-supported.md"
