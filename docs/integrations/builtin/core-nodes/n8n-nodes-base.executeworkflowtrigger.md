---
#https://www.notion.so/n8n/Frontmatter-432c2b8dff1f43d4b1c8d20075510fe4
title: Execute Sub-workflow Trigger node documentation
description: Learn how to use the Execute Sub-workflow Trigger node in n8n. Follow technical documentation to integrate Execute Sub-workflow Trigger node into your workflows.
contentType: [integration, reference]
priority: high
---

# Execute Sub-workflow Trigger node

ใช้ node นี้เพื่อเริ่ม workflow เมื่อถูกเรียกจาก workflow อื่น ควรเป็น node แรกใน workflow

n8n สามารถเรียก workflow อื่นจาก workflow ปัจจุบันได้ เหมาะสำหรับกรณี:

* reuse workflow เช่น มี workflow หลายอันดึงข้อมูลจากแหล่งต่างๆ แล้วให้ทุกอันเรียก workflow เดียวที่สร้าง report
* แบ่ง workflow ใหญ่เป็นส่วนย่อย

## Usage

node นี้จะรันเมื่อถูกเรียกจาก [Execute Sub-workflow](/integrations/builtin/core-nodes/n8n-nodes-base.executeworkflow.md) หรือ [Call n8n Workflow Tool](/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.toolworkflow.md)

--8<-- "_snippets/flow-logic/subworkflow-usage.md"

## Templates and examples

<!-- see https://www.notion.so/n8n/Pull-in-templates-for-the-integrations-pages-37c716837b804d30a33b47475f6e3780 -->
[[ templatesWidget(page.title, 'execute-workflow-trigger') ]]

## How data passes between workflows

--8<-- "_snippets/flow-logic/subworkflow-data-flow.md"
