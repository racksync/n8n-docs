---
#https://www.notion.so/n8n/Frontmatter-432c2b8dff1f43d4b1c8d20075510fe4
title: Stop And Error
description: Documentation for the Stop And Error node in n8n, a workflow automation platform. Includes guidance on usage, and links to examples.
contentType: [integration, reference]
priority: high
---

# Stop And Error

ใช้ Stop And Error node เพื่อแสดง error message แบบ custom, ทำให้ execution ล้มเหลวตามเงื่อนไขที่กำหนด และส่ง error ข้อมูล custom ไปยัง error workflow

## Operations

* Error Message
* Error Object

## Node parameters

ทั้งสอง operation มี parameter หลักคือ **Error Type** ใช้เลือกประเภท error ที่จะ throw เลือกได้ระหว่าง **Error Message** กับ **Error Object**

parameters อื่นๆ จะขึ้นอยู่กับ operation ที่เลือก

### Error Message parameters

ถ้าเลือก Error Message Error Type จะมี parameter เพิ่มคือ **Error Message** ให้ใส่ข้อความที่อยาก throw

### Error Object parameters

ถ้าเลือก Error Object Error Type จะมี parameter เพิ่มคือ **Error Object** ให้ใส่ JSON object ที่มี property ของ error ที่อยาก throw

## Templates and examples

<!-- see https://www.notion.so/n8n/Pull-in-templates-for-the-integrations-pages-37c716837b804d30a33b47475f6e3780 -->
[[ templatesWidget(page.title, 'stop-and-error') ]]

## Related resources

สามารถใช้ Stop And Error node คู่กับ [Error trigger](/integrations/builtin/core-nodes/n8n-nodes-base.errortrigger.md) node ได้

อ่านเพิ่มเติมเกี่ยวกับ [Error workflows](/flow-logic/error-handling.md) ใน n8n workflows

