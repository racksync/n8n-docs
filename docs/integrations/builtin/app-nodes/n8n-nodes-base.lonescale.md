---
#https://www.notion.so/n8n/Frontmatter-432c2b8dff1f43d4b1c8d20075510fe4
title: เอกสารคู่มือ LoneScale node
description: เรียนรู้วิธีใช้ LoneScale node ใน n8n และดูเอกสารทางเทคนิคเพื่อเชื่อมต่อ LoneScale node เข้ากับ workflows ของคุณ
contentType: [integration, reference]
---

# LoneScale node

ใช้ LoneScale node ในการทำงานอัตโนมัติใน LoneScale และเชื่อมต่อกับแอปพลิเคชันอื่น ๆ โดย n8n รองรับการจัดการ Lists และ Items.

ในหน้านี้ คุณจะพบรายการ operations ที่ LoneScale node รองรับและลิงก์ไปยังข้อมูลเพิ่มเติม.

/// note | Credentials
ดู [LoneScale credentials] สำหรับคำแนะนำในการตั้งค่า authentication.
///

## Operations

* List
	* Create
* Item
	* Create

## Templates and examples

<!-- see https://www.notion.so/n8n/Pull-in-templates-for-the-integrations-pages-37c716837b804d30a33b47475f6e3780 -->
[[ templatesWidget(page.title, 'lonescale') ]]

## Related resources

Refer to [LoneScales documentation](https://help-center.lonescale.com/en/articles/6454360-lonescale-public-api){:target=_blank .external-link} for more information about the service.

n8n provides a trigger node for LoneScale. You can find the trigger node docs [here](/integrations/builtin/trigger-nodes/n8n-nodes-base.lonescaletrigger.md).

--8<-- "_snippets/integrations/builtin/app-nodes/operation-not-supported.md"
