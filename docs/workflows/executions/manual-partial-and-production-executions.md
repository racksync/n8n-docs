---
#https://www.notion.so/n8n/Frontmatter-432c2b8dff1f43d4b1c8d20075510fe4
title: Manual, partial, and production executions
description: How manual, partial, and automatic workflow executions differ.
contentType: explanation
---

# Manual, partial, and production executions

มีความแตกต่างที่สำคัญบางประการในวิธีที่ n8n execute workflows แบบ manual (โดยการคลิกปุ่ม **Test Workflow**) และแบบอัตโนมัติ (เมื่อ workflow เป็น **Active** และถูก trigger โดย event หรือ schedule)

## Manual executions

Manual executions ช่วยให้คุณสามารถรัน workflows ได้โดยตรงจาก [canvas](/glossary.md#canvas-n8n) เพื่อทดสอบ logic ของ workflow ของคุณ executions เหล่านี้เป็นแบบ "ad-hoc" — จะรันเฉพาะเมื่อคุณเลือกปุ่ม **Test workflow** ด้วยตนเองเท่านั้น

Manual executions ทำให้การสร้าง workflows ง่ายขึ้นโดยช่วยให้คุณสามารถทดสอบซ้ำๆ ไปพร้อมๆ กับการสร้าง ตาม flow logic และดูการแปลงข้อมูล คุณสามารถทดสอบ conditional branching, การเปลี่ยนแปลงการจัดรูปแบบข้อมูล และพฤติกรรม loop โดยการให้ input items ที่แตกต่างกันและแก้ไข node options

/// note | Pinning execution data
เมื่อทำการ manual executions คุณสามารถใช้ [data pinning](/data/data-pinning.md) เพื่อ "pin" หรือ "freeze" ข้อมูล output ของ node ได้ คุณยังสามารถ [edit the pinned data](https://docs.n8n.io/data/data-editing/) ได้อีกด้วย (เป็นทางเลือก)

ในการรันครั้งต่อไป แทนที่จะ execute node ที่ถูก pin, n8n จะแทนที่ด้วยข้อมูลที่ถูก pin และดำเนินการตาม flow logic ต่อไป ซึ่งช่วยให้คุณสามารถทำซ้ำได้โดยไม่ต้องดำเนินการกับข้อมูลที่เปลี่ยนแปลงได้ หรือทำการ query ซ้ำไปยังบริการภายนอก Production executions จะไม่สนใจข้อมูลที่ถูก pin ทั้งหมด
///

## Partial executions

การคลิกปุ่ม **Test workflow** ที่ด้านล่างของ workflow ในแท็บ **Editor** จะรัน workflow ทั้งหมดด้วยตนเอง คุณยังสามารถทำการ partial executions เพื่อรันขั้นตอนเฉพาะใน workflow ของคุณได้ Partial executions คือ manual executions ที่รันเฉพาะชุดย่อยของ nodes ใน workflow ของคุณ

ในการทำ partial execution ให้เลือก node เปิด detail view ของมัน แล้วเลือก **Test step** การทำเช่นนี้จะ execute node ที่ระบุและ nodes ก่อนหน้าที่จำเป็นในการป้อนข้อมูล input ของมัน คุณยังสามารถปิดการใช้งาน nodes เฉพาะใน workflow chain ชั่วคราวเพื่อหลีกเลี่ยงการโต้ตอบกับบริการเหล่านั้นในขณะที่สร้างได้

โดยเฉพาะอย่างยิ่ง partial executions มีประโยชน์เมื่ออัปเดต logic ของ node เฉพาะ เนื่องจากช่วยให้คุณสามารถ re-execute node ด้วยข้อมูล input เดิมได้

### Troubleshooting partial executions

ปัญหาทั่วไปบางอย่างที่คุณอาจพบเมื่อรัน partial executions มีดังนี้:

<!-- vale from-microsoft.Contractions = NO -->
> The destination node is not connected to any trigger. Partial executions need a trigger.
<!-- vale from-microsoft.Contractions = YES -->

ข้อความแสดงข้อผิดพลาดนี้จะปรากฏขึ้นเมื่อคุณพยายามทำ partial execution โดยไม่ได้เชื่อมต่อ workflow กับ trigger Manual executions รวมถึง partial executions พยายามเลียนแบบ production executions เมื่อเป็นไปได้ ส่วนหนึ่งของสิ่งนี้รวมถึงการต้องการ trigger node เพื่ออธิบายว่าเมื่อใดที่ logic ของ workflow ควร execute

ในการแก้ไขปัญหานี้ ให้เชื่อมต่อ trigger node กับ workflow ด้วย node ที่คุณพยายามจะ execute บ่อยครั้งที่สุด [manual trigger](/integrations/builtin/core-nodes/n8n-nodes-base.manualworkflowtrigger.md) เป็นตัวเลือกที่ง่ายที่สุด

> Please execute the whole workflow, rather than just the node. (Existing execution data is too large.)

ข้อผิดพลาดนี้อาจปรากฏขึ้นเมื่อทำการ partial executions ใน workflows ที่มี branches จำนวนมาก Partial executions เกี่ยวข้องกับการส่งข้อมูลและ workflow logic ไปยัง n8n backend ในลักษณะที่ไม่จำเป็นสำหรับ full executions ข้อผิดพลาดนี้เกิดขึ้นเมื่อ workflow ของคุณมีขนาดเกินขนาดสูงสุดที่อนุญาตสำหรับข้อความเหล่านี้

ในการแก้ไขปัญหานี้ ให้พิจารณาใช้ [limit node](/integrations/builtin/core-nodes/n8n-nodes-base.limit.md) เพื่อจำกัด output ของ node ในขณะที่รัน partial executions เมื่อ workflow ทำงานตามที่ต้องการแล้ว คุณสามารถปิดการใช้งานหรือลบ limit node ก่อนที่จะเปิดใช้งาน production execution ได้

## Production executions

Production executions เกิดขึ้นเมื่อ triggering event หรือ schedule รัน workflow โดยอัตโนมัติ

ในการกำหนดค่า production executions คุณต้องแนบ [trigger node](/glossary.md#trigger-node-n8n) (trigger ใดๆ นอกเหนือจาก [manual trigger](/integrations/builtin/core-nodes/n8n-nodes-base.manualworkflowtrigger.md) ก็ใช้ได้) และสลับ toggle ของ workflow เป็น **Active** เมื่อเปิดใช้งานแล้ว workflow จะ execute โดยอัตโนมัติเมื่อใดก็ตามที่เงื่อนไข trigger เกิดขึ้น

Execution flow สำหรับ production executions จะไม่แสดงในแท็บ Editor ของ workflow เหมือนกับ manual executions แต่คุณสามารถดู executions ได้ในแท็บ **Executions** ของ workflow ตาม [workflow settings](/workflows/settings.md) ของคุณ จากตรงนั้น คุณสามารถสำรวจและแก้ไขปัญหาโดยใช้ [debug in editor feature](/workflows/executions/debug.md) ได้
