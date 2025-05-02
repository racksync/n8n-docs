---
#https://www.notion.so/n8n/Frontmatter-432c2b8dff1f43d4b1c8d20075510fe4
title: Data mocking
description: Ways to mock data in your n8n workflow.
contentType: howto
---

# Data mocking

Data mocking คือการจำลองหรือสร้างข้อมูลปลอมขึ้นมา มีประโยชน์เมื่อพัฒนา workflow โดยการ mock data คุณสามารถ:

- หลีกเลี่ยงการเรียกซ้ำไปยังแหล่งข้อมูลของคุณ ซึ่งช่วยประหยัดเวลาและค่าใช้จ่าย
- ทำงานกับชุดข้อมูลขนาดเล็กที่คาดเดาได้ในระหว่างการพัฒนาเบื้องต้น
- หลีกเลี่ยงความเสี่ยงในการเขียนทับข้อมูลจริง (live data): ในช่วงแรกของการสร้าง workflow คุณไม่จำเป็นต้องเชื่อมต่อกับแหล่งข้อมูลจริงของคุณ


## Mocking with real data using data pinning

การใช้ [data pinning](/data/data-pinning.md) คุณโหลดข้อมูลจริงเข้ามาใน workflow ของคุณ จากนั้น pin ข้อมูลนั้นใน output panel ของ node การใช้วิธีนี้ทำให้คุณมีข้อมูลที่สมจริง โดยมีการเรียกไปยังแหล่งข้อมูลของคุณเพียงครั้งเดียว คุณสามารถ [edit pinned data](/data/data-editing.md) ได้

ใช้วิธีนี้เมื่อคุณต้องการกำหนดค่า workflow ของคุณเพื่อจัดการกับโครงสร้างข้อมูลและ parameters ที่แน่นอนที่มาจากแหล่งข้อมูลของคุณ

--8<-- "_snippets/data/how-to-pin-data.md"


## Generate custom data using the Code or Edit Fields nodes

คุณสามารถสร้างชุดข้อมูลแบบกำหนดเองใน workflow ของคุณโดยใช้ [Code node](/integrations/builtin/core-nodes/n8n-nodes-base.code/index.md) หรือ [Edit Fields (Set) node](/integrations/builtin/core-nodes/n8n-nodes-base.set.md)

ใน Code node คุณสามารถสร้างชุดข้อมูลใดก็ได้ที่คุณต้องการ และส่งคืนเป็น output ของ node ใน Edit Fields node เลือก **Add fields** เพื่อเพิ่มข้อมูลที่คุณกำหนดเอง

Edit Fields node เป็นตัวเลือกที่ดีสำหรับการทดสอบเล็กๆ หากต้องการสร้างชุดข้อมูลที่ซับซ้อนมากขึ้น ให้ใช้ Code node

## Output a sample data set from the Customer Datastore node

Customer Datastore node มีชุดข้อมูลปลอมให้ใช้งาน เพิ่มและ execute node เพื่อสำรวจข้อมูล

ใช้วิธีนี้หากคุณต้องการข้อมูลทดสอบบางอย่างเมื่อสำรวจ n8n และคุณยังไม่มี use-case จริงที่จะทำงานด้วย
