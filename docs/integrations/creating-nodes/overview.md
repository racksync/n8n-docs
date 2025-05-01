---
#https://www.notion.so/n8n/Frontmatter-432c2b8dff1f43d4b1c8d20075510fe4
contentType: overview
---

# Creating nodes

เรียนรู้วิธีสร้าง [nodes](/glossary.md#node-n8n) ของคุณเองในแบบ custom

This section includes:

* คำแนะนำเกี่ยวกับการวางแผนการสร้าง node ของคุณ รวมถึง [เลือก style ที่จะใช้](/integrations/creating-nodes/plan/choose-node-method.md)
* [Tutorials](/integrations/creating-nodes/build/index.md) สำหรับแต่ละ style ของการสร้าง node
* วิธี [ทดสอบ node ของคุณ](/integrations/creating-nodes/test/index.md) รวมถึงวิธีใช้ n8n [node linter](/integrations/creating-nodes/test/node-linter.md) และ [troubleshooting](/integrations/creating-nodes/test/troubleshooting-node-development.md) เพื่อช่วยแก้ปัญหา
* วิธี [แชร์ node ของคุณ](/integrations/creating-nodes/deploy/submit-community-nodes.md) กับ community หรือใช้เป็น [private node](/integrations/creating-nodes/deploy/install-private-nodes.md)
* [Reference material](/integrations/creating-nodes/build/reference/index.md) รวมถึง UI elements และข้อมูลเกี่ยวกับไฟล์ต่างๆ ที่ประกอบเป็น node

## Prerequisites

This section assumes the following:

* คุณควรมีพื้นฐาน JavaScript และ TypeScript มาบ้าง
* สามารถจัดการ environment สำหรับพัฒนาเองได้ รวมถึงการใช้ git
* รู้จัก npm และการสร้าง/ส่ง package
* คุ้นเคยกับ n8n โดยเฉพาะ [data structures](/data/data-structure.md) และ [item linking](/data/data-mapping/data-item-linking/index.md)
