---
#https://www.notion.so/n8n/Frontmatter-432c2b8dff1f43d4b1c8d20075510fe4
description: Methods for working with n8n metadata.
contentType: reference
hide:
  - toc
---

# n8n metadata

Methods สำหรับการทำงานกับ metadata ของ n8n

ซึ่งรวมถึง:

* การเข้าถึง n8n environment variables สำหรับ n8n ที่ self-hosted
* Metadata เกี่ยวกับ workflows, executions และ nodes
* ข้อมูลเกี่ยวกับ instance [Variables](/code/variables.md) และ [External secrets](/external-secrets.md)

/// note | Python support
คุณสามารถใช้ Python ใน Code node ได้ แต่ไม่สามารถใช้ใน expressions ได้
///
=== "JavaScript"
	| Method | Description | Available in Code node? |
	| ------ | ----------- | :-------------------------: |
	| `$env` | มี n8n instance configuration [environment variables](/hosting/configuration/environment-variables/index.md) | :white_check_mark: |
	| `$execution.customData` | ตั้งค่าและรับ custom execution data โปรดดู [Custom executions data](/workflows/executions/custom-executions-data.md) สำหรับข้อมูลเพิ่มเติม | :white_check_mark: | 
	| `$execution.id` | ID ที่ไม่ซ้ำกันของ workflow execution ปัจจุบัน | :white_check_mark: |
	| `$execution.mode` | ระบุว่า execution ถูก trigger โดยอัตโนมัติ หรือโดยการรัน workflow ด้วยตนเอง ค่าที่เป็นไปได้คือ `test` และ `production` | :white_check_mark: |
	| `$execution.resumeUrl` | webhook URL ที่จะเรียกเพื่อดำเนินการต่อ workflow ที่รออยู่ที่ [Wait node](/integrations/builtin/core-nodes/n8n-nodes-base.wait.md) | :white_check_mark: |
	| `$getWorkflowStaticData(type)` | ดู [ตัวอย่าง](/code/cookbook/builtin/get-workflow-static-data.md) Static data จะไม่คงอยู่เมื่อทดสอบ workflows workflow ต้อง active และถูกเรียกโดย trigger หรือ webhook เพื่อบันทึก static data สิ่งนี้ให้การเข้าถึง static workflow data | :white_check_mark: |
	| `$("<node-name>").isExecuted` | ตรวจสอบว่า node ได้ execute ไปแล้วหรือไม่ | :white_check_mark: |
	| `$itemIndex` | index ของ item ในรายการของ items | :x: |
	| `$nodeVersion` | รับ version ของ node ปัจจุบัน | :white_check_mark: |
	| `$prevNode.name` | ชื่อของ node ที่ input ปัจจุบันมาจาก เมื่อใช้ Merge node โปรดทราบว่า `$prevNode` จะใช้ input connector แรกเสมอ | :white_check_mark: |
	| `$prevNode.outputIndex` | index ของ output connector ที่ input ปัจจุบันมาจาก ใช้เมื่อ node ก่อนหน้ามีหลาย outputs (เช่น If หรือ Switch node) เมื่อใช้ Merge node โปรดทราบว่า `$prevNode` จะใช้ input connector แรกเสมอ | :white_check_mark: |
	| `$prevNode.runIndex` | run ของ node ก่อนหน้าที่สร้าง input ปัจจุบัน เมื่อใช้ Merge node โปรดทราบว่า `$prevNode` จะใช้ input connector แรกเสมอ | :white_check_mark: |
	| `$runIndex` | จำนวนครั้งที่ n8n ได้ execute node ปัจจุบัน เป็นแบบ Zero-based (run แรกคือ 0, run ที่สองคือ 1, และต่อไปเรื่อยๆ) | :white_check_mark: |
	| `$secrets` | มีข้อมูลเกี่ยวกับการตั้งค่า [External secrets](/external-secrets.md) ของคุณ | :white_check_mark: |
	| `$vars` | มี [Variables](/code/variables.md) ที่มีอยู่ใน environment ที่ active | :white_check_mark: |
	| `$version` | node version | :x: |
	| `$workflow.active` | ระบุว่า workflow active (true) หรือไม่ (false) | :white_check_mark: |
	| `$workflow.id` | workflow ID | :white_check_mark: |
	| `$workflow.name` | workflow name | :white_check_mark: |
=== "Python"
	| Method | Description |
	| ------ | ----------- |
	| `_env` | มี n8n instance configuration [environment variables](/hosting/configuration/environment-variables/index.md) |
	| `_execution.customData` | ตั้งค่าและรับ custom execution data โปรดดู [Custom executions data](/workflows/executions/custom-executions-data.md) สำหรับข้อมูลเพิ่มเติม | 
	| `_execution.id` | ID ที่ไม่ซ้ำกันของ workflow execution ปัจจุบัน | 
	| `_execution.mode` | ระบุว่า execution ถูก trigger โดยอัตโนมัติ หรือโดยการรัน workflow ด้วยตนเอง ค่าที่เป็นไปได้คือ `test` และ `production` | 
	| `_execution.resumeUrl` | webhook URL ที่จะเรียกเพื่อดำเนินการต่อ workflow ที่รออยู่ที่ [Wait node](/integrations/builtin/core-nodes/n8n-nodes-base.wait.md) |
	| `_getWorkflowStaticData(type)` | ดู [ตัวอย่าง](/code/cookbook/builtin/get-workflow-static-data.md) Static data จะไม่คงอยู่เมื่อทดสอบ workflows workflow ต้อง active และถูกเรียกโดย trigger หรือ webhook เพื่อบันทึก static data สิ่งนี้ให้การเข้าถึง static workflow data |
	| `_("<node-name>").isExecuted` | ตรวจสอบว่า node ได้ execute ไปแล้วหรือไม่ |
	| `_nodeVersion` | รับ version ของ node ปัจจุบัน | :white_check_mark: |
	| `_prevNode.name` | ชื่อของ node ที่ input ปัจจุบันมาจาก เมื่อใช้ Merge node โปรดทราบว่า `_prevNode` จะใช้ input connector แรกเสมอ | 
	| `_prevNode.outputIndex` | index ของ output connector ที่ input ปัจจุบันมาจาก ใช้เมื่อ node ก่อนหน้ามีหลาย outputs (เช่น If หรือ Switch node) เมื่อใช้ Merge node โปรดทราบว่า `_prevNode` จะใช้ input connector แรกเสมอ | 
	| `_prevNode.runIndex` | run ของ node ก่อนหน้าที่สร้าง input ปัจจุบัน เมื่อใช้ Merge node โปรดทราบว่า `_prevNode` จะใช้ input connector แรกเสมอ |
	| `_runIndex` | จำนวนครั้งที่ n8n ได้ execute node ปัจจุบัน เป็นแบบ Zero-based (run แรกคือ 0, run ที่สองคือ 1, และต่อไปเรื่อยๆ) |
	| `_secrets` | มีข้อมูลเกี่ยวกับการตั้งค่า [External secrets](/external-secrets.md) ของคุณ | 
	| `_vars` | มี [Variables](/code/variables.md) ที่มีอยู่ใน environment ที่ active | 
	| `_workflow.active` | ระบุว่า workflow active (true) หรือไม่ (false) |
	| `_workflow.id` | workflow ID | 
	| `_workflow.name` | workflow name |
