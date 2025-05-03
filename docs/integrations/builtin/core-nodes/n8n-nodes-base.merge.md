---
title: รวมข้อมูล (Merge)
description: คู่มือ Merge node สำหรับรวมข้อมูลจากหลายแหล่งใน n8n
contentType: [integration, reference]
priority: critical
---

# Merge

ใช้ Merge node เพื่อรวมข้อมูลจากหลายสตรีม เมื่อข้อมูลของทุกสตรีมพร้อมใช้งาน

/// note | การเปลี่ยนแปลงที่สำคัญในเวอร์ชัน 0.194.0
ทีม n8n ได้ปรับปรุง node นี้ครั้งใหญ่ใน n8n เวอร์ชัน 0.194.0 เอกสารนี้อธิบาย node เวอร์ชันล่าสุด หากคุณใช้ n8n เวอร์ชันเก่า คุณสามารถดูเอกสารเวอร์ชันก่อนหน้าได้ [ที่นี่](https://github.com/n8n-io/n8n-docs/blob/4ff688642cc9ee7ca7d00987847bf4e4515da59d/docs/integrations/builtin/core-nodes/n8n-nodes-base.merge.md){:target=_blank .external-link}
///

/// note | การเปลี่ยนแปลงเล็กน้อยในเวอร์ชัน 1.49.0
n8n เวอร์ชัน 1.49.0 ได้เพิ่มตัวเลือกในการเพิ่มอินพุตมากกว่าสองอินพุต เวอร์ชันเก่ารองรับได้สูงสุดเพียงสองอินพุต หากคุณใช้เวอร์ชันเก่าและต้องการรวมอินพุตหลายรายการในเวอร์ชันเหล่านั้น ให้ใช้ [Code node](https://deploy-preview-2225--n8n-docs.netlify.app/code/code-node/)

ฟีเจอร์ **Mode > SQL Query** ถูกเพิ่มเข้ามาใน n8n เวอร์ชัน 1.49.0 และไม่มีในเวอร์ชันเก่า
///

## Node parameters

คุณสามารถระบุวิธีที่ Merge node ควรจะรวมข้อมูลจากสตรีมข้อมูลต่างๆ โดยเลือก **Mode**:

### Append

เก็บข้อมูลจากอินพุตทั้งหมด เลือก **Number of Inputs** เพื่อส่งออกรายการของแต่ละอินพุตทีละรายการ node จะรอการดำเนินการของอินพุตที่เชื่อมต่อทั้งหมด

<figure markdown="span">
![Sample Append mode inputs and output. Two separate data sources are on the left, one with items A, B, C and one with items D, E, F. The final data source combines both and lists A, B, C, D, E, F.](/_images/integrations/builtin/core-nodes/merge/append-diagram.png)
<figcaption>อินพุตและเอาต์พุตของโหมด Append</figcaption>
</figure>

### Combine

รวมข้อมูลจากสองอินพุต เลือกตัวเลือกใน **Combine By** เพื่อกำหนดวิธีที่คุณต้องการรวมข้อมูลอินพุต

#### Matching Fields

เปรียบเทียบรายการตามค่าฟิลด์ ป้อนฟิลด์ที่คุณต้องการเปรียบเทียบใน **Fields to Match**

พฤติกรรมเริ่มต้นของ n8n คือการเก็บรายการที่ตรงกัน คุณสามารถเปลี่ยนสิ่งนี้ได้โดยใช้การตั้งค่า **Output Type**:

*   **Keep Matches**: รวมรายการที่ตรงกัน เหมือนกับการทำ inner join
*   **Keep Non-Matches**: รวมรายการที่ไม่ตรงกัน
*   **Keep Everything**: รวมรายการที่ตรงกันเข้าด้วยกันและรวมรายการที่ไม่ตรงกันด้วย เหมือนกับการทำ outer join
*   **Enrich Input 1**: เก็บข้อมูลทั้งหมดจาก Input 1 และเพิ่มข้อมูลที่ตรงกันจาก Input 2 เหมือนกับการทำ left join
*   **Enrich Input 2**: เก็บข้อมูลทั้งหมดจาก Input 2 และเพิ่มข้อมูลที่ตรงกันจาก Input 1 เหมือนกับการทำ right join

<figure markdown="span">
![Sample Combine mode inputs and output. Two separate data sources are on the left. The final data source combines these data sources by matching fields.](/_images/integrations/builtin/core-nodes/merge/merge-by-field-diagram.png)
<figcaption>อินพุตและเอาต์พุตของโหมด Combine by Matching Fields</figcaption>
</figure>


#### Position

รวมรายการตามลำดับ รายการที่ index 0 ใน Input 1 จะรวมกับรายการที่ index 0 ใน Input 2 และต่อไปเรื่อยๆ

<figure markdown="span">
![Sample Combine mode inputs and output. Two separate data sources are on the left. The final data source combines these data sources by index position.](/_images/integrations/builtin/core-nodes/merge/merge-by-position-diagram.png)
<figcaption>อินพุตและเอาต์พุตของโหมด Combine by Position</figcaption>
</figure>


#### All Possible Combinations

ส่งออกชุดค่าผสมที่เป็นไปได้ทั้งหมดของรายการ ในขณะที่รวมฟิลด์ที่มีชื่อเดียวกัน

<figure markdown="span">
![Sample Combine mode inputs and output. Two separate data sources are on the left. The final data source combines these data sources by all possible combinations.](/_images/integrations/builtin/core-nodes/merge/multiplex-diagram.png)
<figcaption>อินพุตและเอาต์พุตของโหมด Combine by All Possible Combinations</figcaption>
</figure>

#### Combine mode options

เมื่อรวมข้อมูลโดยใช้ **Mode > Combine** คุณสามารถตั้งค่า **Options** เหล่านี้ได้:

* **Clash Handling**: เลือกวิธีรวมเมื่อสตรีมข้อมูลขัดแย้งกัน หรือเมื่อมีฟิลด์ย่อย อ้างอิงถึง [Clash handling](#clash-handling) สำหรับรายละเอียด
* **Fuzzy Compare**: เลือกว่าจะยอมรับความแตกต่างของประเภทเมื่อเปรียบเทียบฟิลด์หรือไม่ (เปิดใช้งาน) หรือไม่ (ปิดใช้งาน, ค่าเริ่มต้น) ตัวอย่างเช่น เมื่อคุณเปิดใช้งานสิ่งนี้ n8n จะถือว่า `"3"` และ `3` เหมือนกัน
* **Disable Dot Notation**: ป้องกันการเข้าถึงฟิลด์ลูกโดยใช้ `parent.child` ในชื่อฟิลด์
* **Multiple Matches**: เลือกวิธีที่ n8n จัดการกับการจับคู่หลายรายการเมื่อเปรียบเทียบสตรีมข้อมูล
    * **Include All Matches**: ส่งออกหลายรายการหากมีการจับคู่หลายรายการ หนึ่งรายการสำหรับการจับคู่แต่ละครั้ง
    * **Include First Match Only**: เก็บรายการแรกต่อการจับคู่และทิ้งการจับคู่หลายรายการที่เหลือ
* **Include Any Unpaired Items**: เลือกว่าจะเก็บหรือทิ้งรายการที่ไม่มีคู่เมื่อรวมตามตำแหน่ง พฤติกรรมเริ่มต้นคือการละเว้นรายการที่ไม่มีการจับคู่

##### Clash Handling

--8<-- "_snippets/integrations/builtin/core-nodes/merge/field-value-clash.md"

### SQL Query

เขียน SQL Query แบบกำหนดเองเพื่อรวมข้อมูล

ตัวอย่าง:
```sql
SELECT * FROM input1 LEFT JOIN input2 ON input1.name = input2.id
```

ข้อมูลจาก node ก่อนหน้ามีให้ใช้งานเป็นตาราง และคุณสามารถใช้ใน SQL query เป็น input1, input2, input3 และอื่นๆ ตามลำดับ อ้างอิงถึง [AlaSQL GitHub page](https://github.com/alasql/alasql/wiki/Supported-SQL-statements){:target=_blank .external-link} สำหรับรายการคำสั่ง SQL ที่รองรับทั้งหมด

### Choose Branch

เลือกอินพุตที่จะเก็บ ตัวเลือกนี้จะรอจนกว่าข้อมูลจากอินพุตทั้งสองจะพร้อมใช้งานเสมอ คุณสามารถเลือกที่จะ **Output**:

* **Input 1 Data**
* **Input 2 Data**
* **A Single, Empty Item**

node จะส่งออกข้อมูลจากอินพุตที่เลือก โดยไม่มีการเปลี่ยนแปลง

## Templates and examples

<!-- see https://www.notion.so/n8n/Pull-in-templates-for-the-integrations-pages-37c716837b804d30a33b47475f6e3780 -->
[[ templatesWidget(page.title, 'merge') ]]

## Merging data streams with uneven numbers of items

รายการที่ส่งไปยัง Input 1 ของ Merge node จะมีความสำคัญกว่า ตัวอย่างเช่น หาก Merge node ได้รับห้ารายการใน Input 1 และ 10 รายการใน Input 2 มันจะประมวลผลเพียงห้ารายการเท่านั้น รายการที่เหลืออีกห้ารายการจาก Input 2 จะไม่ถูกประมวลผล

## Branch execution with If and Merge nodes

--8<-- "_snippets/integrations/builtin/core-nodes/merge/if-merge-branch-execution.md"


## Try it out: A step by step example

สร้าง workflow พร้อมข้อมูลอินพุตตัวอย่างเพื่อลองใช้ Merge node

### Set up sample data using the Code nodes

1. เพิ่ม Code node ลงใน canvas และเชื่อมต่อกับ Start node
2. วางโค้ด JavaScript ต่อไปนี้ในฟิลด์ **JavaScript Code**:
```js
return [
  {
    json: {
      name: 'Stefan',
      language: 'de',
    }
  },
  {
    json: {
      name: 'Jim',
      language: 'en',
    }
  },
  {
    json: {
      name: 'Hans',
      language: 'de',
    }
  }
];
```
3. เพิ่ม Code node ที่สอง และเชื่อมต่อกับ Start node
4. วางโค้ด JavaScript ต่อไปนี้ในฟิลด์ **JavaScript Code**:
```js
return [
	  {
    json: {
      greeting: 'Hello',
      language: 'en',
    }
  },
  {
    json: {
      greeting: 'Hallo',
      language: 'de',
    }
  }
];
```

### Try out different merge modes

เพิ่ม Merge node เชื่อมต่อ Code node แรกกับ **Input 1** และ Code node ที่สองกับ **Input 2** รัน workflow เพื่อโหลดข้อมูลลงใน Merge node

workflow สุดท้ายควรมีลักษณะดังนี้:

[[ workflowDemo("https://api.n8n.io/workflows/templates/655") ]]

ตอนนี้ลองใช้ตัวเลือกต่างๆ ใน **Mode** เพื่อดูว่ามีผลต่อข้อมูลเอาต์พุตอย่างไร

#### Append

เลือก **Mode** > **Append** จากนั้นเลือก **Test step**

เอาต์พุตของคุณในมุมมองตารางควรมีลักษณะดังนี้:
<!-- vale off -->
| **name** | **language** | **greeting** |
| --- | --- | --- |
| Stefan | de |  |
| Jim | en |  |
| Hans | de |  |
|   | en | Hello |
|   | de | Hallo |
<!-- vale on -->

#### Combine by Matching Fields

คุณสามารถรวมข้อมูลอินพุตทั้งสองนี้เพื่อให้แต่ละคนได้รับคำทักทายที่ถูกต้องสำหรับภาษาของพวกเขา

1. เลือก **Mode** > **Combine**
2. เลือก **Combine by** > **Matching Fields**
3. ในทั้ง **Input 1 Field** และ **Input 2 Field** ป้อน `language` สิ่งนี้จะบอก n8n ให้รวมข้อมูลโดยการจับคู่ค่าในฟิลด์ `language` ในแต่ละชุดข้อมูล
4. เลือก **Test step**

เอาต์พุตของคุณในมุมมองตารางควรมีลักษณะดังนี้:
<!-- vale off -->

| **name** | **language** | **greeting** |
| --- | --- | --- |
| Stefan | de | Hallo |
| Jim | en | Hello  |
| Hans | de | Hallo |
<!-- vale on -->

#### Combine by Position

เลือก **Mode** > **Combine**, **Combine by** > **Position** จากนั้นเลือก **Test step**

เอาต์พุตของคุณในมุมมองตารางควรมีลักษณะดังนี้:
<!-- vale off -->
| **name** | **language** | **greeting** |
| --- | --- | --- |
| Stefan | en | Hello |
| Jim | de | Hallo  |
<!-- vale on -->

##### Keep unpaired items

หากคุณต้องการเก็บรายการทั้งหมด ให้เลือก **Add Option** > **Include Any Unpaired Items** จากนั้นเปิด **Include Any Unpaired Items**

เอาต์พุตของคุณในมุมมองตารางควรมีลักษณะดังนี้:
<!-- vale off -->
| **name** | **language** | **greeting** |
| --- | --- | --- |
| Stefan | en | Hello |
| Jim | de | Hallo  |
| Hans | de |  |
<!-- vale on -->

#### Combine by All Possible Combinations

เลือก **Mode** > **Combine**, **Combine by** > **All Possible Combinations** จากนั้นเลือก **Test step**

เอาต์พุตของคุณในมุมมองตารางควรมีลักษณะดังนี้:
<!-- vale off -->
| **name** | **language** | **greeting** |
| --- | --- | --- |
| Stefan | en | Hello |
| Stefan | de | Hallo |
| Jim | en | Hello  |
| Jim | de | Hallo |
| Hans | en | Hello |
| Hans | de | Hallo |
<!-- vale on -->
