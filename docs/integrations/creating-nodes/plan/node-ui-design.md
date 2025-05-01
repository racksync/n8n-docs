---
#https://www.notion.so/n8n/Frontmatter-432c2b8dff1f43d4b1c8d20075510fe4
contentType: reference
---

# Design your node's user interface

Node ส่วนใหญ่จะเป็น GUI (graphical user interface) ที่แสดง API ในรูปแบบที่ใช้งานง่าย การออกแบบ UI หมายถึงการหาวิธีที่ user-friendly ในการนำเสนอ endpoint และ parameter ของ API การแปลง API ทั้งหมดเป็นฟอร์ม field ใน node อาจไม่ได้ให้ประสบการณ์ที่ดีสำหรับผู้ใช้เสมอไป

เอกสารนี้ให้แนวทางการออกแบบและมาตรฐานที่ควรปฏิบัติตาม ซึ่งเป็นแนวทางเดียวกับที่ n8n ใช้ เพื่อให้ผู้ใช้ได้รับประสบการณ์ที่ราบรื่นและสอดคล้องกัน ไม่ว่าจะใช้ node ที่สร้างโดย community หรือ built-in

## Design guidance

Node ทุกตัวจะใช้ [node UI elements](/integrations/creating-nodes/build/reference/ui-elements.md) ของ n8n อยู่แล้ว ดังนั้นคุณไม่ต้องกังวลเรื่องรายละเอียดสไตล์ เช่น สี, ขอบ ฯลฯ แต่ก็ยังควรผ่านกระบวนการออกแบบพื้นฐานดังนี้:

* อ่านเอกสารของ API ที่คุณจะเชื่อมต่อ แล้วถามตัวเองว่า:
    * อะไรที่ตัดออกได้บ้าง?
    * อะไรที่ทำให้เรียบง่ายขึ้นได้?
    * ส่วนไหนของ API ที่ดูงง? คุณจะช่วยให้ user เข้าใจได้ยังไง?
* ใช้ wireframe tool เพื่อจัด layout ของ field ถ้าคุณพบว่า node ของคุณมี field เยอะและเริ่มซับซ้อน ลองดูแนวทางของ n8n เรื่อง [showing and hiding fields](#showing-and-hiding-fields)

## Standards

### UI text style

| Element | Style |
| ------- | ----- |
| Drop-down value | Title case |
| Hint | Sentence case |
| Info box | Sentence case. ไม่ต้องใส่จุด (`.`) ถ้ามีแค่ประโยคเดียว ถ้ามีมากกว่าหนึ่งประโยคให้ใส่จุดเสมอ ช่องนี้สามารถใส่ลิงก์ได้ และควรเปิดในแท็บใหม่ |
| Node name | Title case |
| Parameter name | Title case |
| Subtitle | Title case |
| Tooltip | Sentence case. ไม่ต้องใส่จุด (`.`) ถ้ามีแค่ประโยคเดียว ถ้ามีมากกว่าหนึ่งประโยคให้ใส่จุดเสมอ ช่องนี้สามารถใส่ลิงก์ได้ และควรเปิดในแท็บใหม่ |

### UI text terminology

* ใช้คำศัพท์เดียวกับ service ที่ node เชื่อมต่อ เช่น node ของ Notion ก็ควรใช้คำว่า block ตามที่ Notion ใช้ ไม่ใช่ paragraph (แม้จะหมายถึงสิ่งเดียวกัน) ยกเว้นกรณีที่ต้องหลีกเลี่ยงศัพท์เทคนิค (ดูหัวข้อ [name and description for upsert operations](#upsert-operations))
* บางที service จะใช้คำศัพท์ต่างกันระหว่าง API กับ GUI ให้ใช้ภาษาที่ปรากฏใน GUI เพราะ user ส่วนใหญ่คุ้นเคยกับคำเหล่านั้น ถ้าคิดว่าผู้ใช้อาจต้องอ้างอิงเอกสาร API ให้ใส่ข้อมูลนี้ใน hint ได้
* อย่าใช้ศัพท์เทคนิคถ้ามีคำที่ง่ายกว่า
* ตั้งชื่อให้สอดคล้องกัน เช่น เลือกใช้ `directory` หรือ `folder` อย่างใดอย่างหนึ่งแล้วใช้ให้เหมือนกันตลอด

### Node naming conventions

| Convention | Correct | Incorrect |
| ---------- | ------- | --------- |
| ถ้า node เป็น trigger node <br>ชื่อที่แสดงควรลงท้ายด้วย 'Trigger' และมีเว้นวรรคก่อน | Shopify Trigger | ShopifyTrigger, Shopify trigger |
| อย่าใส่คำว่า 'node' ในชื่อ | Asana | Asana Node, Asana node |

### Showing and hiding fields

Field สามารถ:

* แสดงทันทีเมื่อเปิด node: ใช้กับ resource, operation และ field ที่จำเป็น
* ซ่อนไว้ใน **Optional fields** จนกว่าผู้ใช้จะคลิก: ใช้กับ field ที่ไม่จำเป็น

เปิดเผยความซับซ้อนทีละน้อย: ซ่อน field จนกว่า field ก่อนหน้าที่เกี่ยวข้องจะมีค่า เช่น ถ้ามี toggle **Filter by date** และ datepicker **Date to filter by** ให้แสดง datepicker ก็ต่อเมื่อ user เปิด toggle **Filter by date**

### Conventions by field type

#### Credentials

n8n จะโชว์ credential field ไว้ด้านบนสุดของ node ให้อัตโนมัติ

#### Resources and operations

API ส่วนใหญ่จะเกี่ยวกับการจัดการข้อมูล เช่น "get all tasks" ในตัวอย่างนี้ "task" คือ resource, "get all" คือ operation

ถ้า node ของคุณมี pattern แบบ resource-operation ให้ field แรกเป็น **Resource** และ field ที่สองเป็น **Operation**

#### Required fields

เรียง field ตามลำดับ:

* สำคัญมากไปหาน้อย
* ขอบเขต: กว้างไปแคบ เช่น มี field **Document**, **Page**, **Text to insert** ให้เรียงตามนี้

#### Optional fields

* เรียง field ตามตัวอักษร ถ้าอยากจัดกลุ่ม field ที่คล้ายกัน ให้เปลี่ยนชื่อ เช่น **Email** กับ **Secondary Email** เปลี่ยนเป็น **Email (primary)** กับ **Email (secondary)**
* ถ้า optional field มีค่า default ที่ node จะใช้เมื่อไม่ได้ตั้งค่า ให้ใส่ค่านั้นไว้ใน field และอธิบายไว้ใน description เช่น **Defaults to false**
* Field ที่เกี่ยวข้องกัน: ถ้า optional field หนึ่งขึ้นกับอีก field หนึ่ง ให้รวมไว้ด้วยกัน ใต้ option เดียวกันที่โชว์ทั้งสอง field เมื่อเลือก
* ถ้ามี optional field เยอะมาก ให้ลองจัดกลุ่มตามธีม

#### Help

GUI มี help อยู่ 5 แบบ:

* Info boxes: กล่องเหลืองระหว่าง field ดู [UI elements | Notice](/integrations/creating-nodes/build/reference/ui-elements.md#notice) สำหรับรายละเอียด
  * ใช้ info box กับข้อมูลสำคัญเท่านั้น อย่าใช้เยอะเกินไป จะได้เด่นและดึงดูดความสนใจ
* Parameter hints: ข้อความใต้ input field ใช้เมื่อมีข้อมูลที่ user ควรรู้ แต่ไม่ถึงกับต้องใช้ info box
* Node hints: ให้ความช่วยเหลือใน input panel, output panel หรือ node details ดู [UI elements | Hints](/integrations/creating-nodes/build/reference/ui-elements.md#hints)
* Tooltips: ข้อความที่โชว์เมื่อ hover ไอคอน !["Screenshot of the tooltip icon. The icon is a ? in a grey circle"](/_images/common-icons/help-tooltip.png) ใช้สำหรับข้อมูลเสริมที่ user อาจต้องการ
  * ไม่จำเป็นต้องมี tooltip ทุก field ให้ใส่เฉพาะที่มีประโยชน์
  * เขียน tooltip โดยคิดถึงสิ่งที่ user ต้องการ อย่า copy-paste จาก API ตรงๆ ถ้าอธิบายไม่ดีหรือผิด ให้ปรับปรุง
* Placeholder text: n8n สามารถโชว์ placeholder ใน field ที่ user ยังไม่ได้กรอก เพื่อช่วยให้ user เข้าใจว่าควรกรอกอะไร

Info box, hint, tooltip สามารถใส่ลิงก์ได้

#### Errors

ทำให้ชัดเจนว่า field ไหนจำเป็น

เพิ่ม validation rule ให้ field ถ้าเป็นไปได้ เช่น ถ้า field รับ email ให้เช็ค pattern ด้วย

เวลาขึ้น error ให้โชว์ข้อความหลักใน title สีแดง ข้อมูลเพิ่มเติมใส่ใน **Details**

#### Toggles

* Tooltip สำหรับ toggle ควรขึ้นต้นด้วย **Whether to . . . **
* บางทีควรใช้ list แทน toggle:
    * ใช้ toggle เมื่อสถานะ false ชัดเจน เช่น **Simplify Output?** (ถ้าไม่ simplify ก็เข้าใจได้)
    * ใช้ dropdown list ที่มีชื่อ option ชัดเจนเมื่อจำเป็น เช่น **Append?** (ถ้าไม่ append อาจไม่ชัดว่าเกิดอะไรขึ้น)

#### Lists

* ตั้งค่า default ให้ list เสมอถ้าเป็นไปได้ โดยเลือก option ที่ใช้บ่อยที่สุด
* เรียง option ใน list ตามตัวอักษร
* ใส่คำอธิบาย option ได้ถ้ามีประโยชน์
* ถ้ามี option แบบ **All** ให้ใช้คำว่า **All** หลีกเลี่ยง ***** หรือคำย่ออื่น

#### Trigger node inputs

ถ้า trigger node มี parameter สำหรับเลือก event ที่จะ trigger:

* ตั้งชื่อ parameter ว่า **Trigger on**
* ไม่ต้องใส่ tooltip

#### Subtitles

ตั้ง subtitle ตามค่าของ parameter หลัก เช่น:

```js
subtitle: '={{$parameter["operation"] + ": " + $parameter["resource"]}}',
```

#### IDs

เวลาทำ operation กับ record เฉพาะ เช่น "update a task comment" ต้องให้ user ระบุ record ที่ต้องการ

* ถ้าเป็นไปได้ ให้ user เลือก record ได้ 2 วิธี:
    * เลือกจาก list ที่ดึงมา (ใช้ `loadOptions` parameter ดู [Base files](/integrations/creating-nodes/build/reference/node-base-files/index.md))
    * กรอก ID เอง
* ตั้งชื่อ field ว่า `<Record name> name or ID` เช่น **Workspace Name or ID** ใส่ tooltip ว่า "Choose a name from the list, or specify an ID using an expression." พร้อมลิงก์ไป [Expressions](/code/expressions.md) ของ n8n
* สร้าง node ให้รองรับข้อมูลที่ user ใส่มากกว่าที่ต้องการ เช่น:
    * ถ้าต้องการ relative path ให้รองรับกรณี user วาง absolute path
    * ถ้าต้องการ ID จาก URL ให้รองรับกรณี user วางทั้ง URL

#### Dates and timestamps

n8n ใช้ [ISO timestamp strings](https://en.wikipedia.org/wiki/ISO_8601){:target=_blank class=.external-link} สำหรับวันที่และเวลา ให้แน่ใจว่า field ที่เกี่ยวข้องรองรับ format นี้

#### JSON

ควรให้ user กรอก JSON ได้ 2 แบบ:

* พิมพ์ JSON ตรงๆ ใน text input: ต้อง parse string เป็น JSON object
* ใช้ expression ที่ return JSON

#### Node icons

--8<-- "_snippets/integrations/node-icons.md"

### Common patterns and exceptions

ส่วนนี้ให้แนวทางสำหรับ pattern ที่พบบ่อย รวมถึงกรณี edge case และข้อยกเว้น

#### Simplify responses

API มักจะคืนข้อมูลเยอะเกินจำเป็น ลองเพิ่ม toggle ให้ user เลือกว่าจะ simplify response หรือไม่:

  * Name: **Simplify Response**
  * Description: **Whether to return a simplified version of the response instead of the raw data**

#### Upsert operations

ควรเป็น operation แยกต่างหากเสมอ โดยมี:

  * Name: **Create or Update**
  * Description: **Create a new record, or update the current one if it already exists (upsert)**

#### Boolean operators
<!-- vale off -->
n8n ยังไม่รองรับการ combine boolean operator (AND, OR) ใน GUI ได้ดีนัก ถ้าเป็นไปได้ ให้มี option สำหรับ AND ทั้งหมด หรือ OR ทั้งหมด
<!-- vale on -->

เช่น มี field ชื่อ **Must match** สำหรับเช็คค่าตรงกัน ให้มี option **Any** กับ **All** แยกกัน

#### Source keys or binary properties

Binary data คือไฟล์ เช่น spreadsheet หรือรูปภาพ ใน n8n ต้องมี key สำหรับอ้างอิงข้อมูลนี้ อย่าใช้คำว่า "binary data" หรือ "binary property" สำหรับ field นี้ ให้ใช้ชื่อที่อธิบายได้ชัดเจนกว่า เช่น **Input data field name** / **Output data field name**






