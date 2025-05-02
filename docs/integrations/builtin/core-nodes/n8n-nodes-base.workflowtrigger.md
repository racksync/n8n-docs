---
#https://www.notion.so/n8n/Frontmatter-432c2b8dff1f43d4b1c8d20075510fe4
title: Workflow Trigger node documentation
description: เรียนรู้วิธีการใช้ Workflow Trigger node ใน n8n อ่านเอกสารทางเทคนิคเพื่อรวม Workflow Trigger node เข้ากับ workflows ของคุณ
contentType: [integration, reference]
priority: high
---

# Workflow Trigger node

Workflow Trigger node จะถูก trigger เมื่อ workflow ถูกอัปเดตหรือถูกเปิดใช้งาน

/// warning | Deprecated
n8n ได้เลิกใช้งาน Workflow Trigger node แล้ว และย้ายความสามารถนี้ไปที่ [n8n Trigger node](/integrations/builtin/core-nodes/n8n-nodes-base.n8ntrigger.md)
///

/// note | Keep in mind
ถ้าคุณต้องการใช้ Workflow Trigger node กับ workflow ให้เพิ่ม node นี้เข้าไปใน workflow ได้เลย ไม่ต้องสร้าง workflow แยก
///

Workflow Trigger node จะ trigger เฉพาะ workflow ที่มันถูกเพิ่มเข้าไป คุณสามารถใช้ Workflow Trigger node เพื่อ trigger workflow เพื่อแจ้งสถานะของ workflow ได้

## Node parameters

node นี้จะมี parameter เดียวสำหรับเลือก **Events** ที่จะ trigger node ได้ เลือกได้จาก:

- **Active Workflow Updated**: ถ้าเลือก event นี้ node จะ trigger เมื่อ workflow นี้ถูกอัปเดต
- **Workflow Activated**: ถ้าเลือก event นี้ node จะ trigger เมื่อ workflow นี้ถูกเปิดใช้งาน

สามารถเลือก event ได้มากกว่าหนึ่ง

## Templates and examples

<!-- see https://www.notion.so/n8n/Pull-in-templates-for-the-integrations-pages-37c716837b804d30a33b47475f6e3780 -->
[[ templatesWidget(page.title, 'workflow-trigger') ]]
