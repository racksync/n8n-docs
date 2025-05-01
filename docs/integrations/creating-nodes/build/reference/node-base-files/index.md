---
#https://www.notion.so/n8n/Frontmatter-432c2b8dff1f43d4b1c8d20075510fe4
contentType: overview
---

# Node base file

node base file คือไฟล์หลักที่เก็บโค้ด core ของ node ทุก node ต้องมี base file โดยเนื้อหาของไฟล์นี้จะแตกต่างกันไปตามว่าเป็น declarative-style หรือ programmatic-style ถ้าต้องการเลือกว่าจะใช้แบบไหน ดูที่ [Choose your node building approach](/integrations/creating-nodes/plan/choose-node-method.md)

เอกสารนี้จะมีโค้ดตัวอย่างสั้น ๆ เพื่อช่วยให้เข้าใจโครงสร้างและแนวคิด ถ้าต้องการดูตัวอย่างจริงแบบเต็ม ๆ ดูที่ [Build a declarative-style node](/integrations/creating-nodes/build/declarative-style-node.md) หรือ [Build a programmatic-style node](/integrations/creating-nodes/build/programmatic-style-node.md)

คุณยังสามารถดูตัวอย่างเพิ่มเติมได้ที่ [n8n-nodes-starter](https://github.com/n8n-io/n8n-nodes-starter){:target=_blank .external-link} และ [nodes ของ n8n](https://github.com/n8n-io/n8n/tree/master/packages/nodes-base/nodes){:target=_blank .external-link} ตัว starter จะมีตัวอย่างพื้นฐานที่นำไปต่อยอดได้ ส่วน [Mattermost node ของ n8n](https://github.com/n8n-io/n8n/tree/master/packages/nodes-base/nodes/Mattermost) เป็นตัวอย่าง node แบบ programmatic-style ที่ซับซ้อนขึ้นและมีการ versioning

สำหรับ node ทุกประเภท ดูที่:

* [Structure of the node base file](/integrations/creating-nodes/build/reference/node-base-files/structure.md)
* [Standard parameters](/integrations/creating-nodes/build/reference/node-base-files/standard-parameters.md)

สำหรับ declarative-style nodes ดูที่:

* [Declarative-style parameters](/integrations/creating-nodes/build/reference/node-base-files/declarative-style-parameters.md)

สำหรับ programmatic-style nodes ดูที่:

* [Programmatic-style parameters](/integrations/creating-nodes/build/reference/node-base-files/programmatic-style-parameters.md)
* [Programmatic-style execute() method](/integrations/creating-nodes/build/reference/node-base-files/programmatic-style-execute-method.md)