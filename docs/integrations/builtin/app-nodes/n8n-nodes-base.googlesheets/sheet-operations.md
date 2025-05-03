---
#https://www.notion.so/n8n/Frontmatter-432c2b8dff1f43d4b1c8d20075510fe4
title: การดำเนินการ Sheet ใน Google Sheets
description: เอกสารการดำเนินการ Sheet ใน Google Sheets node ของ n8n พร้อมรายละเอียด การตั้งค่า และลิงก์ตัวอย่าง
contentType: [integration, reference]
priority: critical
---

# Google Sheets Sheet Within Document operations

ใช้ operation นี้เพื่อสร้าง, อัปเดต, ล้างข้อมูล หรือลบ sheet ใน Google spreadsheet จาก Google Sheets อ้างอิงถึง [Google Sheets](/integrations/builtin/app-nodes/n8n-nodes-base.googlesheets/index.md) สำหรับข้อมูลเพิ่มเติมเกี่ยวกับ Google Sheets node

--8<-- "_snippets/integrations/builtin/app-nodes/ai-tools.md"

## Append or Update Row

ใช้ operation นี้เพื่ออัปเดตแถวที่มีอยู่ หรือเพิ่มแถวใหม่ต่อท้ายข้อมูล หากไม่พบรายการที่ตรงกันใน sheet

ป้อน parameters เหล่านี้:

- **Credential to connect with**: สร้างหรือเลือก [Google Sheets credentials](/integrations/builtin/credentials/google/index.md) ที่มีอยู่
- **Resource**: เลือก **Sheet Within Document**
- **Operation**: เลือก **Append or Update Row**
- **Document**: เลือก spreadsheet ที่มี sheet ที่คุณต้องการเพิ่มหรืออัปเดตแถว
    - เลือก **From list** เพื่อเลือกชื่อ spreadsheet จากรายการดรอปดาวน์, **By URL** เพื่อป้อน URL ของ spreadsheet, หรือ **By ID** เพื่อป้อน `spreadsheetId`
    - คุณสามารถหา `spreadsheetId` ได้ใน URL ของ Google Sheets: `https://docs.google.com/spreadsheets/d/spreadsheetId/edit#gid=0`
- **Sheet**: เลือก sheet ที่คุณต้องการเพิ่มหรืออัปเดตแถว
    - เลือก **From list** เพื่อเลือกชื่อ sheet จากรายการดรอปดาวน์, **By URL** เพื่อป้อน URL ของ sheet, **By ID** เพื่อป้อน `sheetId`, หรือ **By Name** เพื่อป้อนชื่อ sheet
    - คุณสามารถหา `sheetId` ได้ใน URL ของ Google Sheets: `https://docs.google.com/spreadsheets/d/aBC-123_xYz/edit#gid=sheetId`
- **Mapping Column Mode**:
	- **Map Each Column Manually**: ป้อน **Values to Send** สำหรับแต่ละคอลัมน์
	- **Map Automatically**: n8n จะค้นหาข้อมูลขาเข้าที่ตรงกับคอลัมน์ใน Google Sheets โดยอัตโนมัติ ในโหมดนี้ ตรวจสอบให้แน่ใจว่าฟิลด์ข้อมูลขาเข้าเหมือนกับคอลัมน์ใน Google Sheets (ใช้ [Edit Fields](/integrations/builtin/core-nodes/n8n-nodes-base.set.md) node ก่อนหน้า node นี้เพื่อเปลี่ยนแปลงหากจำเป็น)
    - **Nothing**: ไม่ต้อง map ข้อมูลใดๆ

### Options
--8<-- "_snippets/integrations/builtin/app-nodes/googlesheets/node-options.md"

อ้างอิงถึงเอกสาร API [Method: spreadsheets.values.update | Google Sheets](https://developers.google.com/sheets/api/reference/rest/v4/spreadsheets.values/update){:target=_blank .external-link} สำหรับข้อมูลเพิ่มเติม

## Append Row

ใช้ operation นี้เพื่อเพิ่มแถวใหม่ต่อท้ายข้อมูลใน sheet

ป้อน parameters เหล่านี้:

- **Credential to connect with**: สร้างหรือเลือก [Google Sheets credentials](/integrations/builtin/credentials/google/index.md) ที่มีอยู่
- **Resource**: เลือก **Sheet Within Document**
- **Operation**: เลือก **Append Row**
- **Document**: เลือก spreadsheet ที่มี sheet ที่คุณต้องการเพิ่มแถว
    - เลือก **From list** เพื่อเลือกชื่อ spreadsheet จากรายการดรอปดาวน์, **By URL** เพื่อป้อน URL ของ spreadsheet, หรือ **By ID** เพื่อป้อน `spreadsheetId`
    - คุณสามารถหา `spreadsheetId` ได้ใน URL ของ Google Sheets: `https://docs.google.com/spreadsheets/d/spreadsheetId/edit#gid=0`
- **Sheet**: เลือก sheet ที่คุณต้องการเพิ่มแถว
    - เลือก **From list** เพื่อเลือกชื่อ sheet จากรายการดรอปดาวน์, **By URL** เพื่อป้อน URL ของ sheet, **By ID** เพื่อป้อน `sheetId`, หรือ **By Name** เพื่อป้อนชื่อ sheet
    - คุณสามารถหา `sheetId` ได้ใน URL ของ Google Sheets: `https://docs.google.com/spreadsheets/d/aBC-123_xYz/edit#gid=sheetId`
- **Mapping Column Mode**:
	- **Map Each Column Manually**: เลือก **Column to Match On** เมื่อค้นหาแถวที่จะอัปเดต ป้อน **Values to Send** สำหรับแต่ละคอลัมน์
	- **Map Automatically**: n8n จะค้นหาข้อมูลขาเข้าที่ตรงกับคอลัมน์ใน Google Sheets โดยอัตโนมัติ ในโหมดนี้ ตรวจสอบให้แน่ใจว่าฟิลด์ข้อมูลขาเข้าเหมือนกับคอลัมน์ใน Google Sheets (ใช้ [Edit Fields](/integrations/builtin/core-nodes/n8n-nodes-base.set.md) node ก่อนหน้า node นี้เพื่อเปลี่ยนแปลงหากจำเป็น)
    - **Nothing**: ไม่ต้อง map ข้อมูลใดๆ

### Options
--8<-- "_snippets/integrations/builtin/app-nodes/googlesheets/node-options.md"

อ้างอิงถึงเอกสาร API [Method: spreadsheets.values.append | Google Sheets](https://developers.google.com/sheets/api/reference/rest/v4/spreadsheets.values/append){:target=_blank .external-link} สำหรับข้อมูลเพิ่มเติม

## Clear a sheet

ใช้ operation นี้เพื่อล้างข้อมูลทั้งหมดออกจาก sheet

ป้อน parameters เหล่านี้:

- **Credential to connect with**: สร้างหรือเลือก [Google Sheets credentials](/integrations/builtin/credentials/google/index.md) ที่มีอยู่
- **Resource**: เลือก **Sheet Within Document**
- **Operation**: เลือก **Clear**
- **Document**: เลือก spreadsheet ที่มี sheet ที่คุณต้องการล้างข้อมูล
    - เลือก **From list** เพื่อเลือกชื่อ spreadsheet จากรายการดรอปดาวน์, **By URL** เพื่อป้อน URL ของ spreadsheet, หรือ **By ID** เพื่อป้อน `spreadsheetId`
    - คุณสามารถหา `spreadsheetId` ได้ใน URL ของ Google Sheets: `https://docs.google.com/spreadsheets/d/spreadsheetId/edit#gid=0`
- **Sheet**: เลือก sheet ที่คุณต้องการล้างข้อมูล
    - เลือก **From list** เพื่อเลือกชื่อ sheet จากรายการดรอปดาวน์, **By URL** เพื่อป้อน URL ของ sheet, **By ID** เพื่อป้อน `sheetId`, หรือ **By Name** เพื่อป้อนชื่อ sheet
    - คุณสามารถหา `sheetId` ได้ใน URL ของ Google Sheets: `https://docs.google.com/spreadsheets/d/aBC-123_xYz/edit#gid=sheetId`
- **Clear**: เลือกข้อมูลที่คุณต้องการล้างออกจาก sheet
    - **Whole Sheet**: ล้างข้อมูลทั้ง sheet เปิด **Keep First Row** เพื่อเก็บแถวแรกของ sheet ไว้
    - **Specific Rows**: ล้างข้อมูลจากแถวที่ระบุ ป้อนข้อมูลเพิ่มเติม:
        - **Start Row Number**: ป้อนหมายเลขแถวแรกที่คุณต้องการล้าง
        - **Number of Rows to Delete**: ป้อนจำนวนแถวที่ต้องการล้าง `1` จะล้างข้อมูลเฉพาะแถวใน **Start Row Number**
    - **Specific Columns**: ล้างข้อมูลจากคอลัมน์ที่ระบุ ป้อนข้อมูลเพิ่มเติม:
        - **Start Column**: ป้อนคอลัมน์แรกที่คุณต้องการล้างโดยใช้สัญกรณ์ตัวอักษร
        - **Number of Columns to Delete**: ป้อนจำนวนคอลัมน์ที่ต้องการล้าง `1` จะล้างข้อมูลเฉพาะใน **Start Column**
    - **Specific Range**: ป้อนช่วงตารางที่ต้องการล้างข้อมูลในรูปแบบ [A1 notation](https://developers.google.com/sheets/api/guides/concepts#cell){:target=_blank .external-link}

อ้างอิงถึงเอกสาร API [Method: spreadsheets.values.clear | Google Sheets](https://developers.google.com/sheets/api/reference/rest/v4/spreadsheets.values/clear){:target=_blank .external-link} สำหรับข้อมูลเพิ่มเติม

## Create a new sheet

ใช้ operation นี้เพื่อสร้าง sheet ใหม่

ป้อน parameters เหล่านี้:

- **Credential to connect with**: สร้างหรือเลือก [Google Sheets credentials](/integrations/builtin/credentials/google/index.md) ที่มีอยู่
- **Resource**: เลือก **Sheet Within Document**
- **Operation**: เลือก **Create**
- **Document**: เลือก spreadsheet ที่คุณต้องการสร้าง sheet ใหม่
    - เลือก **From list** เพื่อเลือกชื่อ spreadsheet จากรายการดรอปดาวน์, **By URL** เพื่อป้อน URL ของ spreadsheet, หรือ **By ID** เพื่อป้อน `spreadsheetId`
    - คุณสามารถหา `spreadsheetId` ได้ใน URL ของ Google Sheets: `https://docs.google.com/spreadsheets/d/spreadsheetId/edit#gid=0`
- **Title**: ป้อนชื่อสำหรับ sheet ใหม่ของคุณ

### Options

- **Hidden**: เปิดตัวเลือกนี้เพื่อซ่อน sheet ใน UI
- **Right To Left**: เปิดตัวเลือกนี้เพื่อใช้ sheet แบบ RTL แทน sheet แบบ LTR
- **Sheet ID**: ป้อน ID ของ sheet
	- คุณสามารถหา `sheetId` ได้ใน URL ของ Google Sheets: `https://docs.google.com/spreadsheets/d/aBC-123_xYz/edit#gid=sheetId`
- **Sheet Index**: โดยค่าเริ่มต้น sheet ใหม่จะเป็น sheet สุดท้ายใน spreadsheet หากต้องการเปลี่ยนค่านี้ ให้ป้อน index ที่คุณต้องการให้ sheet ใหม่ใช้ เมื่อคุณเพิ่ม sheet ที่ index ที่กำหนด Google จะเพิ่ม indices สำหรับ sheet ทั้งหมดที่ตามมา อ้างอิงถึงเอกสาร [Sheets | SheetProperties](https://developers.google.com/sheets/api/reference/rest/v4/spreadsheets/sheets#SheetProperties){:target=_blank .external-link} สำหรับข้อมูลเพิ่มเติม
- **Tab Color**: ป้อนสีเป็นรหัส hex หรือใช้ตัวเลือกสีเพื่อตั้งค่าสีของแท็บใน UI

อ้างอิงถึงเอกสาร API [Method: spreadsheets.batchUpdate | Google Sheets](https://developers.google.com/sheets/api/reference/rest/v4/spreadsheets/batchUpdate){:target=_blank .external-link} สำหรับข้อมูลเพิ่มเติม

## Delete a sheet

ใช้ operation นี้เพื่อลบ sheet อย่างถาวร

ป้อน parameters เหล่านี้:

- **Credential to connect with**: สร้างหรือเลือก [Google Sheets credentials](/integrations/builtin/credentials/google/index.md) ที่มีอยู่
- **Resource**: เลือก **Sheet Within Document**
- **Operation**: เลือก **Delete**
- **Document**: เลือก spreadsheet ที่มี sheet ที่คุณต้องการลบ
    - เลือก **From list** เพื่อเลือกชื่อ spreadsheet จากรายการดรอปดาวน์, **By URL** เพื่อป้อน URL ของ spreadsheet, หรือ **By ID** เพื่อป้อน `spreadsheetId`
    - คุณสามารถหา `spreadsheetId` ได้ใน URL ของ Google Sheets: `https://docs.google.com/spreadsheets/d/spreadsheetId/edit#gid=0`
- **Sheet**: เลือก sheet ที่คุณต้องการลบ
    - เลือก **From list** เพื่อเลือกชื่อ sheet จากรายการดรอปดาวน์, **By URL** เพื่อป้อน URL ของ sheet, **By ID** เพื่อป้อน `sheetId`, หรือ **By Name** เพื่อป้อนชื่อของ sheet
    - คุณสามารถหา `sheetId` ได้ใน URL ของ Google Sheets: `https://docs.google.com/spreadsheets/d/aBC-123_xYz/edit#gid=sheetId`

อ้างอิงถึงเอกสาร API [Method: spreadsheets.batchUpdate | Google Sheets](https://developers.google.com/sheets/api/reference/rest/v4/spreadsheets/batchUpdate){:target=_blank .external-link} สำหรับข้อมูลเพิ่มเติม

## Delete Rows or Columns

ใช้ operation นี้เพื่อลบแถวหรือคอลัมน์ใน sheet

ป้อน parameters เหล่านี้:

- **Credential to connect with**: สร้างหรือเลือก [Google Sheets credentials](/integrations/builtin/credentials/google/index.md) ที่มีอยู่
- **Resource**: เลือก **Sheet Within Document**
- **Operation**: เลือก **Delete Rows or Columns**
- **Document**: เลือก spreadsheet ที่มี sheet ที่คุณต้องการลบแถวหรือคอลัมน์
    - เลือก **From list** เพื่อเลือกชื่อ spreadsheet จากรายการดรอปดาวน์, **By URL** เพื่อป้อน URL ของ spreadsheet, หรือ **By ID** เพื่อป้อน `spreadsheetId`
    - คุณสามารถหา `spreadsheetId` ได้ใน URL ของ Google Sheets: `https://docs.google.com/spreadsheets/d/spreadsheetId/edit#gid=0`
- **Sheet**: เลือก sheet ที่คุณต้องการลบแถวหรือคอลัมน์
    - เลือก **From list** เพื่อเลือกชื่อ sheet จากรายการดรอปดาวน์, **By URL** เพื่อป้อน URL ของ sheet, **By ID** เพื่อป้อน `sheetId`, หรือ **By Name** เพื่อป้อนชื่อของ sheet
    - คุณสามารถหา `sheetId` ได้ใน URL ของ Google Sheets: `https://docs.google.com/spreadsheets/d/aBC-123_xYz/edit#gid=sheetId`
- **Start Row Number** หรือ **Start Column**: ป้อนหมายเลขแถวหรือตัวอักษรคอลัมน์เพื่อเริ่มลบ
- **Number of Rows to Delete** หรือ **Number of Columns to delete**: ป้อนจำนวนแถวหรือคอลัมน์ที่ต้องการลบ

อ้างอิงถึงเอกสาร API [Method: spreadsheets.batchUpdate | Google Sheets](https://developers.google.com/sheets/api/reference/rest/v4/spreadsheets/batchUpdate){:target=_blank .external-link} สำหรับข้อมูลเพิ่มเติม

## Get Row(s)

ใช้ operation นี้เพื่ออ่านหนึ่งแถวหรือมากกว่าจาก sheet

ป้อน parameters เหล่านี้:

- **Credential to connect with**: สร้างหรือเลือก [Google Sheets credentials](/integrations/builtin/credentials/google/index.md) ที่มีอยู่
- **Resource**: เลือก **Sheet Within Document**
- **Operation**: เลือก **Get Row(s)**
- **Document**: เลือก spreadsheet ที่มี sheet ที่คุณต้องการดึงข้อมูลแถว
    - เลือก **From list** เพื่อเลือกชื่อ spreadsheet จากรายการดรอปดาวน์, **By URL** เพื่อป้อน URL ของ spreadsheet, หรือ **By ID** เพื่อป้อน `spreadsheetId`
    - คุณสามารถหา `spreadsheetId` ได้ใน URL ของ Google Sheets: `https://docs.google.com/spreadsheets/d/spreadsheetId/edit#gid=0`
- **Sheet**: เลือก sheet ที่คุณต้องการอ่านข้อมูลแถว
    - เลือก **From list** เพื่อเลือกชื่อ sheet จากรายการดรอปดาวน์, **By URL** เพื่อป้อน URL ของ sheet, **By ID** เพื่อป้อน `sheetId`, หรือ **By Name** เพื่อป้อนชื่อของ sheet
    - คุณสามารถหา `sheetId` ได้ใน URL ของ Google Sheets: `https://docs.google.com/spreadsheets/d/aBC-123_xYz/edit#gid=sheetId`
- **Filters**: โดยค่าเริ่มต้น node จะคืนค่าทุกแถวใน sheet ตั้งค่า filters เพื่อคืนค่าชุดผลลัพธ์ที่จำกัด:
  	- **Column**: เลือกคอลัมน์ใน sheet ของคุณเพื่อใช้ค้นหา
  	- **Value**: ป้อนค่า cell ที่ต้องการค้นหา คุณสามารถลาก parameters ข้อมูลขาเข้ามาที่นี่ได้
	หาก filter ของคุณตรงกับหลายแถว n8n จะคืนค่าผลลัพธ์แรก หากคุณต้องการแถวที่ตรงกันทั้งหมด:
    	1. ใต้ **Options**, เลือก **Add Option** > **When Filter Has Multiple Matches**
        2. เปลี่ยน **When Filter Has Multiple Matches** เป็น **Return All Matches**

### Options

- **Data Location on Sheet**: ใช้ตัวเลือกนี้เพื่อระบุช่วงข้อมูล โดยค่าเริ่มต้น n8n จะตรวจจับช่วงโดยอัตโนมัติจนถึงแถวสุดท้ายใน sheet
- **Output Formatting**: ใช้ตัวเลือกนี้เพื่อเลือกว่า n8n จะจัดรูปแบบข้อมูลที่คืนค่าโดย Google Sheets อย่างไร
  - **General Formatting**:
    - **Values (unformatted)** (ค่าเริ่มต้น): n8n จะลบสัญลักษณ์สกุลเงินและการจัดรูปแบบพิเศษอื่นๆ ประเภทข้อมูลยังคงเป็นตัวเลข
    - **Values (formatted)**: n8n จะแสดงค่าตามที่ปรากฏใน Google Sheets (เช่น คงเครื่องหมายจุลภาคหรือสัญลักษณ์สกุลเงินไว้) โดยการแปลงประเภทข้อมูลจากตัวเลขเป็นสตริง
    - **Formulas**: n8n จะคืนค่าสูตร ไม่คำนวณผลลัพธ์ของสูตร ตัวอย่างเช่น หากเซลล์ B2 มีสูตร `=A2`, n8n จะคืนค่าของ B2 เป็น `=A2` (ในรูปแบบข้อความ) อ้างอิงถึง [About date & time values | Google Sheets](https://developers.google.com/sheets/api/guides/formats#about_date_time_values){:target=_blank .external-link} สำหรับข้อมูลเพิ่มเติม
  - **Date Formatting**: อ้างอิงถึง [DateTimeRenderOption | Google Sheets](https://developers.google.com/sheets/api/reference/rest/v4/DateTimeRenderOption){:target=_blank .external-link} สำหรับข้อมูลเพิ่มเติม
     	- **Formatted Text** (ค่าเริ่มต้น): ตามที่แสดงใน Google Sheets ซึ่งขึ้นอยู่กับ locale ของ spreadsheet ตัวอย่างเช่น `01/01/2024`
     	- **Serial Number**: จำนวนวันนับตั้งแต่วันที่ 30 ธันวาคม 1899
- **When Filter Has Multiple Matches**: ตั้งค่าเป็น **Return All Matches** เพื่อรับผลลัพธ์ที่ตรงกันหลายรายการ โดยค่าเริ่มต้นจะคืนค่าเฉพาะผลลัพธ์แรกเท่านั้น

/// note | First row
n8n ถือว่าแถวแรกใน Google Sheet เป็นแถวหัวเรื่อง และจะไม่คืนค่าเมื่ออ่านทุกแถว หากคุณต้องการอ่านแถวแรก ให้ใช้ **Options** เพื่อตั้งค่า **Data Location on Sheet**
///

อ้างอิงถึงเอกสาร API [Method: spreadsheets.batchUpdate | Google Sheets](https://developers.google.com/sheets/api/reference/rest/v4/spreadsheets/batchUpdate){:target=_blank .external-link} สำหรับข้อมูลเพิ่มเติม

## Update Row

ใช้ operation นี้เพื่ออัปเดตแถวที่มีอยู่ใน sheet operation นี้จะอัปเดตเฉพาะแถวที่มีอยู่เท่านั้น หากต้องการเพิ่มแถวเมื่อไม่พบรายการที่ตรงกันใน sheet ให้ใช้ operation **Append or Update Row** แทน

ป้อน parameters เหล่านี้:

- **Credential to connect with**: สร้างหรือเลือก [Google Sheets credentials](/integrations/builtin/credentials/google/index.md) ที่มีอยู่
- **Resource**: เลือก **Sheet Within Document**
- **Operation**: เลือก **Update Row**
- **Document**: เลือก spreadsheet ที่มี sheet ที่คุณต้องการอัปเดต
    - เลือก **From list** เพื่อเลือกชื่อ spreadsheet จากรายการดรอปดาวน์, **By URL** เพื่อป้อน URL ของ spreadsheet, หรือ **By ID** เพื่อป้อน `spreadsheetId`
    - คุณสามารถหา `spreadsheetId` ได้ใน URL ของ Google Sheets: `https://docs.google.com/spreadsheets/d/spreadsheetId/edit#gid=0`
- **Sheet**: เลือก sheet ที่คุณต้องการอัปเดต
    - เลือก **From list** เพื่อเลือกชื่อ sheet จากรายการดรอปดาวน์, **By URL** เพื่อป้อน URL ของ sheet, **By ID** เพื่อป้อน `sheetId`, หรือ **By Name** เพื่อป้อนชื่อ sheet
    - คุณสามารถหา `sheetId` ได้ใน URL ของ Google Sheets: `https://docs.google.com/spreadsheets/d/aBC-123_xYz/edit#gid=sheetId`
- **Mapping Column Mode**:
	- **Map Each Column Manually**: ป้อน **Values to Send** สำหรับแต่ละคอลัมน์
	- **Map Automatically**: n8n จะค้นหาข้อมูลขาเข้าที่ตรงกับคอลัมน์ใน Google Sheets โดยอัตโนมัติ ในโหมดนี้ ตรวจสอบให้แน่ใจว่าฟิลด์ข้อมูลขาเข้าเหมือนกับคอลัมน์ใน Google Sheets (ใช้ [Edit Fields](/integrations/builtin/core-nodes/n8n-nodes-base.set.md) node ก่อนหน้า node นี้เพื่อเปลี่ยนแปลงหากจำเป็น)
    - **Nothing**: ไม่ต้อง map ข้อมูลใดๆ

### Options

- **Cell Format**: ใช้ตัวเลือกนี้เพื่อเลือกว่าจะจัดรูปแบบข้อมูลในเซลล์อย่างไร อ้างอิงถึง [Google Sheets API | CellFormat](https://developers.google.com/sheets/api/reference/rest/v4/spreadsheets/cells#CellFormat){:target=_blank .external-link} สำหรับข้อมูลเพิ่มเติม
    - **Let Google Sheets format** (ค่าเริ่มต้น): n8n จะจัดรูปแบบข้อความและตัวเลขในเซลล์ตามการตั้งค่าเริ่มต้นของ Google Sheets
    - **Let n8n format**: เซลล์ใหม่ใน sheet ของคุณจะมีประเภทข้อมูลเหมือนกับข้อมูลขาเข้าที่ n8n ให้มา
- **Data Location on Sheet**: ใช้ตัวเลือกนี้เมื่อคุณต้องการระบุตำแหน่งช่วงข้อมูลบน sheet ของคุณ
    - **Header Row**: ระบุ index ของแถวที่มีส่วนหัวของคอลัมน์
    - **First Data Row**: ระบุ index ของแถวที่ข้อมูลจริงเริ่มต้น

อ้างอิงถึงเอกสาร API [Method: spreadsheets.batchUpdate | Google Sheets](https://developers.google.com/sheets/api/reference/rest/v4/spreadsheets/batchUpdate){:target=_blank .external-link} สำหรับข้อมูลเพิ่มเติม