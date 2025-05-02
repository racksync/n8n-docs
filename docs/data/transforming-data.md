---
#https://www.notion.so/n8n/Frontmatter-432c2b8dff1f43d4b1c8d20075510fe4
contentType: explanation
---

# Transforming data

n8n ใช้ [โครงสร้างข้อมูล](/data/data-structure.md) ที่กำหนดไว้ล่วงหน้า ซึ่งช่วยให้ node ทั้งหมดสามารถประมวลผลข้อมูลขาเข้าได้อย่างถูกต้อง

ข้อมูลขาเข้าของคุณอาจมีโครงสร้างข้อมูลที่แตกต่างกัน ซึ่งในกรณีนี้คุณจะต้องแปลงข้อมูลเพื่อให้แต่ละรายการสามารถประมวลผลแยกกันได้

ตัวอย่างเช่น ภาพด้านล่างแสดงผลลัพธ์ของ [HTTP Request](/integrations/builtin/core-nodes/n8n-nodes-base.httprequest/index.md) node ที่ส่งคืนข้อมูลที่ไม่เข้ากันกับโครงสร้างข้อมูลของ n8n node จะส่งคืนข้อมูลและแสดงว่ามีการส่งคืนเพียงรายการเดียว

![HTTP Request node output](/_images/data/transforming-data/HTTPRequest_output.png)

ในการแปลงโครงสร้างประเภทนี้ให้เป็นโครงสร้างข้อมูล n8n คุณสามารถใช้ node การแปลงข้อมูล (data transformation nodes) ได้:

* [Aggregate](/integrations/builtin/core-nodes/n8n-nodes-base.aggregate.md): นำรายการแยกกัน หรือบางส่วนของรายการ มารวมกลุ่มกันเป็นรายการเดี่ยว
* [Limit](/integrations/builtin/core-nodes/n8n-nodes-base.limit.md): ลบรายการที่เกินจำนวนสูงสุดที่กำหนด
* [Remove Duplicates](/integrations/builtin/core-nodes/n8n-nodes-base.removeduplicates/index.md): ระบุและลบรายการที่เหมือนกันทุกประการในทุก field หรือในชุดของ field ที่กำหนด
* [Sort](/integrations/builtin/core-nodes/n8n-nodes-base.sort.md): จัดระเบียบรายการตามลำดับที่ต้องการ หรือสร้างการสุ่มเลือก
* [Split Out](/integrations/builtin/core-nodes/n8n-nodes-base.splitout.md): แยกรายการข้อมูลเดียวที่มี list ออกเป็นหลายรายการ
* [Summarize](/integrations/builtin/core-nodes/n8n-nodes-base.summarize.md): รวบรวมรายการเข้าด้วยกัน คล้ายกับ pivot tables ใน Excel


