---
title: ทริกเกอร์ n8n (n8n Trigger)
description: คู่มือ n8n Trigger node สำหรับเริ่ม workflow จาก event ใน n8n
contentType: [integration, reference]
priority: medium
---

# n8n Trigger node

n8n Trigger node จะทำงานเมื่อ workflow ปัจจุบันถูกอัปเดตหรือเปิดใช้งาน หรือเมื่อ instance ของ n8n เริ่มต้นหรือรีสตาร์ท คุณสามารถใช้ n8n Trigger node เพื่อแจ้งเตือนเมื่อเกิด event เหล่านี้

## Node parameters

node นี้จะมี parameter เดียวสำหรับเลือก **Events** ที่ต้องการให้ trigger โดยเลือกได้จาก:

- **Active Workflow Updated**: ถ้าเลือก event นี้ node จะ trigger เมื่อ workflow นี้ถูกอัปเดต
- **Instance started**: ถ้าเลือก event นี้ node จะ trigger เมื่อ instance ของ n8n เริ่มต้นหรือรีสตาร์ท
- **Workflow Activated**: ถ้าเลือก event นี้ node จะ trigger เมื่อ workflow นี้ถูกเปิดใช้งาน

คุณสามารถเลือก event ได้มากกว่าหนึ่งอย่าง

## Templates and examples

<!-- see https://www.notion.so/n8n/Pull-in-templates-for-the-integrations-pages-37c716837b804d30a33b47475f6e3780 -->
[[ templatesWidget(page.title, 'n8n-trigger') ]]

