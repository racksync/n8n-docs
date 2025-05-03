---
#https://www.notion.so/n8n/Frontmatter-432c2b8dff1f43d4b1c8d20075510fe4
title: Google Sheets
description: เอกสาร Google Sheets node ใน n8n พร้อมรายละเอียดการดำเนินการ การตั้งค่า และลิงก์ตัวอย่าง
contentType: [integration, reference]
priority: critical
---

# Google Sheets

ใช้ Google Sheets node เพื่อทำงานอัตโนมัติใน Google Sheets และรวม Google Sheets เข้ากับแอปพลิเคชันอื่นๆ n8n มีการรองรับฟีเจอร์ต่างๆ ของ Google Sheets ในตัว รวมถึงการสร้าง, อัปเดต, ลบ, เพิ่มต่อท้าย, ลบออก และดึงข้อมูลเอกสาร

ในหน้านี้ คุณจะพบรายการ operations ที่ Google Sheets node รองรับ และลิงก์ไปยังแหล่งข้อมูลเพิ่มเติม

/// note | Credentials
อ้างอิงถึง [Google Sheets credentials](/integrations/builtin/credentials/google/index.md) สำหรับคำแนะนำในการตั้งค่าการยืนยันตัวตน
///

## Operations

* **Document**
    * [**Create**](/integrations/builtin/app-nodes/n8n-nodes-base.googlesheets/document-operations.md#create-a-spreadsheet): สร้าง spreadsheet
	* [**Delete**](/integrations/builtin/app-nodes/n8n-nodes-base.googlesheets/document-operations.md#delete-a-spreadsheet): ลบ spreadsheet
* **Sheet Within Document**
	* [**Append or Update Row**](/integrations/builtin/app-nodes/n8n-nodes-base.googlesheets/sheet-operations.md#append-or-update-row): เพิ่มแถวใหม่ หรืออัปเดตแถวปัจจุบันหากมีอยู่แล้ว
	* [**Append Row**](/integrations/builtin/app-nodes/n8n-nodes-base.googlesheets/sheet-operations.md#append-row): สร้างแถวใหม่
	* [**Clear**](/integrations/builtin/app-nodes/n8n-nodes-base.googlesheets/sheet-operations.md#clear-a-sheet): ล้างข้อมูลทั้งหมดออกจาก sheet
	* [**Create**](/integrations/builtin/app-nodes/n8n-nodes-base.googlesheets/sheet-operations.md#create-a-new-sheet): สร้าง sheet ใหม่
	* [**Delete**](/integrations/builtin/app-nodes/n8n-nodes-base.googlesheets/sheet-operations.md#delete-a-sheet): ลบ sheet
	* [**Delete Rows or Columns**](/integrations/builtin/app-nodes/n8n-nodes-base.googlesheets/sheet-operations.md#delete-rows-or-columns): ลบคอลัมน์และแถวออกจาก sheet
	* [**Get Row(s)**](/integrations/builtin/app-nodes/n8n-nodes-base.googlesheets/sheet-operations.md#get-rows): อ่านทุกแถวใน sheet
	* [**Update Row**](/integrations/builtin/app-nodes/n8n-nodes-base.googlesheets/sheet-operations.md#update-row): อัปเดตแถวใน sheet


## Templates and examples

<!-- see https://www.notion.so/n8n/Pull-in-templates-for-the-integrations-pages-37c716837b804d30a33b47475f6e3780 -->
[[ templatesWidget(page.title, 'google-sheets') ]]

## Related resources

อ้างอิงถึง [Google Sheet's API documentation](https://developers.google.com/sheets/api){:target=_blank .external-link} สำหรับข้อมูลเพิ่มเติมเกี่ยวกับบริการนี้

<!-- ## Examples
This example uses the Customer Datastore node to provide sample data to load into Google Sheets. It assumes you've already set up your [credentials](/integrations/builtin/credentials/google/index.md).	
	1. Set up a Google Sheet with two columns, `test1` and `test`. In `test1`, enter the names from the Customer Datastore node:  
	![The spreadsheet set up for testing](/_images/integrations/builtin/app-nodes/googlesheets/test-sheet-before.png)  
	2. Create the workflow: use the manual trigger, Customer Datastore, and Google Sheets nodes.  
	![The spreadsheet set up for testing](/_images/integrations/builtin/app-nodes/googlesheets/workflow.png)  
	3. Open the Customer Datastore node, enable **Return All**, then select **Test step**.
	4. In the Google Sheets node, go through the steps above, using these settings:
		* Select **Update Row** as the **Operation**.
		* In **Column to Match On**, select `test1`.
		* For the first field of **Values to Update**, drag in the **name** from the input view.
		* For the second field of **Values to Update**, drag in the **email** from the input view.
	5. Select **Test step**.
	6. View your spreadsheet. **test2** should now contain the email addresses that match to the names in the input data.  
	![The spreadsheet set up for testing](/_images/integrations/builtin/app-nodes/googlesheets/test-sheet-after.png)   -->

## Common issues

สำหรับคำถามหรือปัญหาทั่วไปและแนวทางแก้ไขที่แนะนำ โปรดอ้างอิงถึง [Common issues](/integrations/builtin/app-nodes/n8n-nodes-base.googlesheets/common-issues.md)

--8<-- "_snippets/integrations/builtin/app-nodes/operation-not-supported.md"
