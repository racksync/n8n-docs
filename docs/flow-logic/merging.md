---
#https://www.notion.so/n8n/Frontmatter-432c2b8dff1f43d4b1c8d20075510fe4
contentType: howto
description: Merge data streams in you n8n workflows.
---

# Merging data

Merging คือการนำ data หลาย stream มารวมกัน คุณสามารถใช้ node ต่างๆ ตามความต้องการของ workflow

- รวมข้อมูลจาก data stream หรือ node ต่างๆ: ใช้ [Merge](/integrations/builtin/core-nodes/n8n-nodes-base.merge.md) node เพื่อรวมข้อมูลจากหลายแหล่งให้เป็นหนึ่งเดียว
- รวมข้อมูลจากการ execute node หลายครั้ง: ใช้ [Code](/integrations/builtin/core-nodes/n8n-nodes-base.code/index.md) node ถ้าต้องการ merge ข้อมูลจากการ execute หลายรอบหรือหลาย node
- เปรียบเทียบและ merge ข้อมูล: ใช้ [Compare Datasets](/integrations/builtin/core-nodes/n8n-nodes-base.comparedatasets.md) node เพื่อเปรียบเทียบ, รวม และแยกข้อมูลตามผลการเปรียบเทียบ

ดูรายละเอียดแต่ละวิธีในหัวข้อด้านล่าง

## Merge data from different data streams

ถ้า workflow ของคุณมีการ [splitting](/flow-logic/splitting.md) คุณสามารถรวม stream ที่แยกออกมาให้กลับมาเป็น stream เดียว

ดู [ตัวอย่าง workflow](https://n8n.io/workflows/1747-joining-different-datasets/) ที่แสดงวิธี merging แบบต่างๆ เช่น append, เก็บเฉพาะข้อมูลใหม่, หรือเก็บเฉพาะข้อมูลเดิม ดูรายละเอียดแต่ละ operation ได้ที่ [Merge node](/integrations/builtin/core-nodes/n8n-nodes-base.merge.md)

[[ workflowDemo("https://api.n8n.io/workflows/templates/1747") ]]

## Merge data from different nodes

คุณสามารถใช้ Merge node เพื่อรวมข้อมูลจากสอง node ก่อนหน้า แม้ว่า workflow จะไม่ได้ split เป็นหลาย stream ก็ได้ เหมาะกับกรณีที่ต้องการรวมข้อมูลจากหลาย node ให้เป็น dataset เดียว

<figure markdown="span">
![Merging data from two previous nodes. The diagram shows three nodes lined up sequentially. The first node is labeled Fetch data, the second is labeled Modify data, and the third is labeled Merge: append both data sets. Arrows connect nodes 1 to 2, 2 to 3, and 1 to 3.](/_images/flow-logic/merging/merge-node-data.png)
<figcaption>Merging data from two previous nodes</figcaption>
</figure>

## Merge data from multiple node executions

ใช้ Code node เพื่อ merge ข้อมูลจากการ execute node หลายรอบ เหมาะกับบางกรณี [Looping](/flow-logic/looping.md)

/// note | Node executions and workflow executions
หัวข้อนี้พูดถึงการ merge ข้อมูลจากการ execute node หลายรอบใน workflow เดียว
///
ดู [ตัวอย่าง workflow](https://n8n.io/workflows/1814-merge-multiple-runs-into-one/){:target=_blank .external-link} ที่ใช้ Loop Over Items และ Wait เพื่อสร้างการ execute หลายรอบ

[[ workflowDemo("https://api.n8n.io/workflows/templates/1814") ]]

## Compare, merge, and split again

[Compare Datasets](/integrations/builtin/core-nodes/n8n-nodes-base.comparedatasets.md) node ใช้เปรียบเทียบข้อมูลก่อน merge และสามารถแยก output ได้สูงสุด 4 stream

ดู [ตัวอย่าง workflow](https://n8n.io/workflows/1943-comparing-data-with-the-compare-datasets-node/){:target=_blank .external-link} สำหรับตัวอย่างการใช้งาน

[[ workflowDemo("https://api.n8n.io/workflows/templates/1943") ]]