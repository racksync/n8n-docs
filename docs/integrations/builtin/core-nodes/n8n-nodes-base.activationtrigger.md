---
#https://www.notion.so/n8n/Frontmatter-432c2b8dff1f43d4b1c8d20075510fe4
title: เอกสาร Activation Trigger node
description: เรียนรู้วิธีใช้ Activation Trigger node ใน n8n ทำตามเอกสารเพื่อนำ Activation Trigger node ไปใช้ใน workflow ของคุณ
contentType: [integration, reference]
---

# Activation Trigger node

Activation Trigger node จะถูก trigger เมื่อมี event จาก n8n หรือ workflow

/// warning
n8n ได้ deprecated Activation Trigger node แล้ว และแทนที่ด้วย node ใหม่ 2 ตัว คือ [n8n Trigger node](/integrations/builtin/core-nodes/n8n-nodes-base.n8ntrigger.md) และ [Workflow Trigger node](/integrations/builtin/core-nodes/n8n-nodes-base.workflowtrigger.md) ดูรายละเอียดเพิ่มเติมได้ที่ [breaking changes](https://github.com/n8n-io/n8n/blob/master/packages/cli/BREAKING-CHANGES.md#01170)
///

/// note | Keep in mind
ถ้าอยากใช้ Activation Trigger node กับ workflow ให้เพิ่ม node นี้เข้าไปใน workflow ได้เลย ไม่ต้องสร้าง workflow แยก
///

Activation Trigger node จะ trigger เฉพาะ workflow ที่มี node นี้อยู่ สามารถใช้ node นี้เพื่อ trigger workflow เพื่อแจ้งสถานะของ workflow ได้

## Node parameters

- Events
    - **Activation**: ทำงานเมื่อ workflow ถูก activate
    - **Start**: ทำงานเมื่อ n8n start หรือ restart
    - **Update**: ทำงานเมื่อ workflow ถูก save ขณะที่ active อยู่

## Templates and examples

<!-- see https://www.notion.so/n8n/Pull-in-templates-for-the-integrations-pages-37c716837b804d30a33b47475f6e3780 -->
[[ templatesWidget(page.title, 'activation-trigger') ]]
