---
#https://www.notion.so/n8n/Frontmatter-432c2b8dff1f43d4b1c8d20075510fe4
contentType: tutorial
---

# Workflow 1: Merging data

บริษัทของ Nathan เก็บข้อมูลลูกค้าไว้ใน Airtable ข้อมูลนี้ประกอบด้วยข้อมูลเกี่ยวกับ ID, ประเทศ, อีเมล, และวันที่เข้าร่วมของลูกค้า แต่ขาดข้อมูลเกี่ยวกับ region และ subregion ของลูกค้า คุณต้องกรอกข้อมูลในสอง fields สุดท้ายนี้เพื่อสร้างรายงานสำหรับยอดขายตามภูมิภาค

เพื่อให้งานนี้สำเร็จ คุณต้องคัดลอกตารางนี้ไปยังบัญชี Airtable ของคุณก่อน:

<iframe class="airtable-embed" src="https://airtable.com/embed/shrNX9tjPkVLABbNz?backgroundColor=orange&viewControls=on" frameborder="0" onmousewheel="" width="100%" height="533" style="background: transparent; border: 1px solid #ccc;"></iframe>

ถัดไป สร้าง workflow เล็กๆ ที่รวมข้อมูลจาก Airtable และ REST Countries API:

1. ใช้ [**Airtable node**](/integrations/builtin/app-nodes/n8n-nodes-base.airtable/index.md) เพื่อ list ข้อมูลในตาราง Airtable ชื่อ `customers`
2. ใช้ [**HTTP Request node**](/integrations/builtin/core-nodes/n8n-nodes-base.httprequest/index.md) เพื่อรับข้อมูลจาก REST Countries API: `https://restcountries.com/v3.1/all` การดำเนินการนี้จะคืนค่าข้อมูลเกี่ยวกับประเทศต่างๆ ทั่วโลก โดยแบ่งออกเป็น items แยกกัน
3. ใช้ [**Merge node**](/integrations/builtin/core-nodes/n8n-nodes-base.merge.md) เพื่อรวมข้อมูลจาก Airtable และ Countries API ตามชื่อประเทศ ซึ่งแสดงเป็น `customerCountry` ใน Airtable และ `name.common` ใน Countries API ตามลำดับ
4. ใช้ Airtable node อีกอันเพื่ออัปเดต fields `region` และ `subregion` ใน Airtable ด้วยข้อมูลจาก Countries API

workflow ควรมีลักษณะดังนี้:

<figure><img src="/_images/courses/level-two/chapter-five/workflow1.png" alt="Workflow 1 for merging data from Airtable and the Countries API" style="width:100%"><figcaption align = "center"><i>Workflow 1 for merging data from Airtable and the Countries API</i></figcaption></figure>


/// question | Quiz questions
* **HTTP Request node** คืนค่ากี่ items?
* **Merge node** คืนค่ากี่ items?
* มีกี่ unique regions ที่ถูกกำหนดในตาราง customers?
* subregion ที่กำหนดให้กับ customerID 10 คืออะไร?
///
