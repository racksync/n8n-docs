---
#https://www.notion.so/n8n/Frontmatter-432c2b8dff1f43d4b1c8d20075510fe4
contentType: overview
---

# Data

Data คือข้อมูลที่ n8n nodes รับและประมวลผล สำหรับการใช้งาน n8n ขั้นพื้นฐาน คุณไม่จำเป็นต้องเข้าใจโครงสร้างข้อมูลและการจัดการข้อมูล อย่างไรก็ตาม มันจะมีความสำคัญหากคุณต้องการ:

 - สร้าง node ของคุณเอง
 - เขียน [expressions](/glossary.md#expression-n8n) แบบกำหนดเอง
 - ใช้ Function หรือ Function Item node

ส่วนนี้ครอบคลุม:

* [Data structure](/data/data-structure.md)
* [Data flow within nodes](/data/data-flow-nodes.md)
* [Transforming data](/data/transforming-data.md)
* [Process data using code](/data/code.md)
* [Pinning](/data/data-pinning.md) และ [editing](/data/data-editing.md) data ระหว่างการพัฒนา workflow
* [Data mapping](/data/data-mapping/index.md) และ [Item linking](/data/data-mapping/data-item-linking/index.md): วิธีที่ data items เชื่อมโยงถึงกัน

## Related resources

### Data transformation nodes

n8n มีชุดของ nodes สำหรับแปลงข้อมูล:

* [Aggregate](/integrations/builtin/core-nodes/n8n-nodes-base.aggregate.md): นำรายการแยกกัน หรือบางส่วนของรายการ มารวมกลุ่มกันเป็นรายการเดี่ยว
* [Limit](/integrations/builtin/core-nodes/n8n-nodes-base.aggregate.md): ลบรายการที่เกินจำนวนสูงสุดที่กำหนด
* [Remove Duplicates](/integrations/builtin/core-nodes/n8n-nodes-base.removeduplicates/index.md): ระบุและลบรายการที่เหมือนกันทุกประการในทุก field หรือในชุดของ field ที่กำหนด
* [Sort](/integrations/builtin/core-nodes/n8n-nodes-base.sort.md): จัดระเบียบรายการตามลำดับที่ต้องการ หรือสร้างการสุ่มเลือก
* [Split Out](/integrations/builtin/core-nodes/n8n-nodes-base.splitout.md): แยกรายการข้อมูลเดียวที่มี list ออกเป็นหลายรายการ
* [Summarize](/integrations/builtin/core-nodes/n8n-nodes-base.summarize.md): รวบรวมรายการเข้าด้วยกัน คล้ายกับ pivot tables ใน Excel
