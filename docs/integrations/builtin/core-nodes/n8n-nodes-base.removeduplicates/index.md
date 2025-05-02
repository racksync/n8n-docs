---
#https://www.notion.so/n8n/Frontmatter-432c2b8dff1f43d4b1c8d20075510fe4
title: Remove Duplicates node documentation
description: Documentation for the Remove Duplicates node in n8n, a workflow automation platform. Includes guidance on usage and links to examples.
contentType: [integration, reference]
priority: medium
---

# Remove Duplicates node

ใช้ Remove Duplicates node เพื่อช่วยหาข้อมูลที่ซ้ำกันและลบออก ไม่ว่าจะเป็น:

* ข้อมูลที่เหมือนกันทุก field หรือบาง field ในการรันเดียวกัน
* ข้อมูลที่เหมือนหรือถูกแทนที่ด้วยข้อมูลจากการรันก่อนหน้า

เหมาะกับกรณีที่อาจมีข้อมูลซ้ำ เช่น user สมัคร account หลายรอบ หรือ customer ส่ง order ซ้ำ เมื่อ dataset ใหญ่ขึ้นจะยิ่งหาข้อมูลซ้ำได้ยากขึ้น

Remove Duplicates node สามารถเปรียบเทียบกับข้อมูลจาก execution ก่อนหน้าเพื่อลบข้อมูลที่เคยเจอแล้ว หรือจะเลือกให้เก็บเฉพาะข้อมูลใหม่ที่มีวันที่ใหม่กว่า หรือค่ามากกว่าก็ได้

/// note | Major changes in 1.64.0
ทีม n8n ได้ปรับปรุง node นี้ครั้งใหญ่ใน n8n 1.64.0 เอกสารนี้อ้างอิงเวอร์ชันล่าสุด ถ้าใช้ n8n เวอร์ชันเก่า ดูเอกสารเวอร์ชันก่อนหน้าได้ที่ [here](https://github.com/n8n-io/n8n-docs/blob/7a66308290e6e5b104fcb82a3beafa0d6987df36/docs/integrations/builtin/core-nodes/n8n-nodes-base.removeduplicates.md){:target=_blank .external-link}
///

## Operation modes

Remove Duplicates node จะทำงานแตกต่างกันตามค่าของ **operation** ที่เลือก:

* **[Remove Items Repeated Within Current Input](#remove-items-repeated-within-current-input)**: หาข้อมูลซ้ำใน input เดียวกัน ทั้งหมดหรือบาง field แล้วลบออก
* **[Remove Items Processed in Previous Executions](#remove-items-processed-in-previous-executions)**: เปรียบเทียบ input กับข้อมูลจาก execution ก่อนหน้าแล้วลบข้อมูลซ้ำ
* **[Clear Deduplication History](#clear-deduplication-history)**: ล้างประวัติข้อมูลที่เคยใช้เปรียบเทียบ

### Remove Items Repeated Within Current Input

ถ้าตั้งค่า "Operations" เป็น **Remove Items Repeated Within Current Input** Remove Duplicate node จะหาข้อมูลซ้ำใน input เดียวกัน สามารถเลือกเปรียบเทียบทุก field หรือเฉพาะบาง field ก็ได้

#### Remove Items Repeated Within Current Input parameters

เมื่อใช้ operation นี้ จะมี parameter ให้เลือกดังนี้:

* **Compare**: เลือกว่าจะเปรียบเทียบ field ไหนบ้างเพื่อหาข้อมูลซ้ำ มีตัวเลือกดังนี้:
	* **All Fields**: เปรียบเทียบทุก field
	* **All Fields Except**: ระบุ field ที่ไม่ต้องการเปรียบเทียบ (ใส่หลายค่าคั่นด้วย comma)
	* **Selected Fields**: ระบุ field ที่ต้องการเปรียบเทียบ (ใส่หลายค่าคั่นด้วย comma)

#### Remove Items Repeated Within Current Input options

ถ้าเลือก **All Fields Except** หรือ **Selected Fields** จะมี option เพิ่มเติม:

* **Disable Dot Notation**: เลือกว่าจะใช้ dot notation อ้างอิง child field แบบ `parent.child` หรือไม่ (ปิด/เปิด)
* **Remove Other Fields**: เลือกว่าจะลบ field อื่นที่ไม่ได้ใช้เปรียบเทียบออกหรือไม่ (เปิด/ปิด)

### Remove Items Processed in Previous Executions

ถ้าตั้งค่า "Operation" เป็น **Remove Items Processed in Previous Executions** Remove Duplicate node จะเปรียบเทียบ input กับข้อมูลจาก execution ก่อนหน้า

#### Remove Items Processed in Previous Executions parameters

เมื่อใช้ operation นี้ จะมี parameter ให้เลือกดังนี้:

* **Keep Items Where**: เลือกวิธีที่ n8n จะตัดสินใจเก็บข้อมูล มีตัวเลือกดังนี้:
	* **Value Is New**: ลบข้อมูลถ้าค่าตรงกับข้อมูลจาก execution ก่อนหน้า
	* **Value Is Higher than Any Previous Value**: ลบข้อมูลถ้าค่าไม่มากกว่าค่าก่อนหน้า
	* **Value Is a Date Later than Any Previous Date**: ลบข้อมูลถ้าวันที่ไม่ใหม่กว่าก่อนหน้า

* **Value to Dedupe On**: ระบุ field ที่จะใช้เปรียบเทียบ ขึ้นกับ **Keep Items Where** ที่เลือก:
	* ถ้าใช้ **Value Is New** ต้องเป็น field หรือ combination ที่เป็น unique ID
	* ถ้าใช้ **Value Is Higher than Any Previous Value** ต้องเป็น field หรือ combination ที่มีค่าเพิ่มขึ้นได้
	* ถ้าใช้ **Value Is a Date Later than Any Previous Date** ต้องเป็น field ที่เป็นวันที่ในรูปแบบ ISO

#### Remove Items Processed in Previous Executions options

เมื่อใช้ operation นี้ จะมี option ให้เลือกดังนี้:

* **Scope**: เลือกวิธีที่ n8n จะเก็บและใช้ข้อมูล dedupe มีตัวเลือกดังนี้:
	* **Node**: (default) เก็บข้อมูลเฉพาะ node นี้ ไม่เกี่ยวกับ Remove Duplicates node อื่นใน workflow เดียวกัน ถ้าใช้ scope นี้ สามารถ [clear the duplication history](#clear-deduplication-history) เฉพาะ node นี้ได้โดยไม่กระทบ node อื่น
	* **Workflow**: เก็บข้อมูล dedupe ระดับ workflow แชร์กับ Remove Duplicate node อื่นที่ใช้ workflow scope node ที่ใช้ node scope จะไม่เกี่ยวข้อง

ถ้าเลือก **Value Is New** ใน **Keep Items Where** จะมี option เพิ่มเติม:

* **History Size**: จำนวนข้อมูลที่ n8n จะเก็บไว้เพื่อ track duplicate ข้าม execution ขึ้นกับ **Scope** ว่าเก็บเฉพาะ node หรือทั้ง workflow ค่า default คือ 10,000 รายการ

### Clear Deduplication History

ถ้าตั้งค่า "Operation" เป็น **Clear Deduplication History** Remove Duplicates node จะจัดการและล้างข้อมูลที่เก็บไว้จาก execution ก่อนหน้า operation นี้จะไม่กระทบข้อมูล input ปัจจุบัน แต่จะล้าง database ที่ operation "Remove Items Processed in Previous Executions" ใช้เปรียบเทียบ

#### Clear Deduplication History parameters

เมื่อใช้ operation นี้ จะมี parameter ให้เลือกดังนี้:

* **Mode**: เลือกวิธีจัดการข้อมูล key/value ที่เก็บไว้ใน database มีตัวเลือกดังนี้:
	* **Clean Database**: ลบข้อมูล dedupe ทั้งหมดใน database รีเซ็ต database กลับสู่สถานะเริ่มต้น

#### Clear Deduplication History options

เมื่อใช้ operation นี้ จะมี option ให้เลือกดังนี้:

* **Scope**: เลือก scope ที่ n8n จะใช้จัดการ database dedupe
	* **Node**: (default) จัดการ database เฉพาะ Remove Duplicates node นี้
	* **Workflow**: จัดการ database ที่แชร์กับ Remove Duplicate node อื่นที่ใช้ workflow scope

## Templates and examples

สำหรับ template และตัวอย่างการใช้งาน Remove Duplicates node ดูได้ที่ [Templates and examples](/integrations/builtin/core-nodes/n8n-nodes-base.removeduplicates/templates-and-examples.md)

## Related resources

--8<-- "_snippets/integrations/builtin/core-nodes/data-transformation-actions/data-section-link.md"
