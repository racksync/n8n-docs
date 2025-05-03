---
#https://www.notion.so/n8n/Frontmatter-432c2b8dff1f43d4b1c8d20075510fe4
title: คู่มือ Basic LLM Chain node
description: วิธีใช้งาน Basic LLM Chain node ใน n8n สำหรับตั้งค่า prompt และ parser ให้โมเดล AI
contentType: [integration, reference]
priority: critical
---

# Basic LLM Chain node

ใช้ Basic LLM Chain node เพื่อตั้งค่า prompt ที่โมเดลจะใช้ พร้อมกับการตั้งค่า parser เสริมสำหรับ response

ในหน้านี้ คุณจะพบพารามิเตอร์ของโหนด Basic LLM Chain และลิงก์ไปยังแหล่งข้อมูลเพิ่มเติม

/// note | Examples and templates
สำหรับตัวอย่างการใช้งานและ templates เพื่อช่วยให้คุณเริ่มต้น โปรดดูที่หน้า [Basic LLM Chain integrations](https://n8n.io/integrations/basic-llm-chain/){:target=_blank .external-link} ของ n8n
///

## Node parameters

### Prompt

--8<-- "_snippets/integrations/builtin/cluster-nodes/langchain-root-nodes/prompt.md"

### Require Specific Output Format

--8<-- "_snippets/integrations/builtin/cluster-nodes/langchain-root-nodes/output-format.md"

## Chat Messages

ใช้ **Chat Messages** เมื่อคุณกำลังใช้ chat model เพื่อตั้งค่าข้อความ

n8n จะไม่สนใจตัวเลือกเหล่านี้หากคุณไม่ได้เชื่อมต่อ chat model เลือก **Type Name or ID** ที่คุณต้องการให้โหนดใช้:

#### AI

ป้อนตัวอย่าง response ที่คาดหวังในช่อง **Message** โมเดลจะพยายามตอบกลับในลักษณะเดียวกันในข้อความของมัน

#### System

ป้อน **Message** ของระบบเพื่อรวมเข้ากับ input ของผู้ใช้ เพื่อช่วยแนะนำโมเดลว่าควรทำอะไร

ใช้ตัวเลือกนี้สำหรับสิ่งต่างๆ เช่น การกำหนดโทนเสียง ตัวอย่างเช่น: `Always respond talking like a pirate`

#### User

ป้อนตัวอย่าง input ของผู้ใช้ การใช้ตัวเลือกนี้ร่วมกับตัวเลือก AI สามารถช่วยปรับปรุง output ของ agent ได้ การใช้ทั้งสองอย่างร่วมกันเป็นการให้ตัวอย่างของ input และ response ที่คาดหวัง (คือ **AI Message**) เพื่อให้โมเดลปฏิบัติตาม

เลือกประเภท input อย่างใดอย่างหนึ่งต่อไปนี้:

*   **Text**: ป้อนตัวอย่าง input ของผู้ใช้เป็น **Message** แบบข้อความ
*   **Image (Binary)**: เลือก binary input จากโหนดก่อนหน้า ป้อน **Image Data Field Name** เพื่อระบุว่าฟิลด์ binary ใดจากโหนดก่อนหน้าที่มีข้อมูลรูปภาพ
*   **Image (URL)**: ใช้ตัวเลือกนี้เพื่อป้อนรูปภาพจาก URL ป้อน **Image URL**

สำหรับประเภท **Image** ทั้งสองแบบ ให้เลือก **Image Details** เพื่อควบคุมวิธีที่โมเดลประมวลผลรูปภาพและสร้างความเข้าใจเชิงข้อความ เลือกจาก:

*   **Auto**: โมเดลใช้การตั้งค่า auto ซึ่งจะดูขนาด input ของรูปภาพและตัดสินใจว่าจะใช้การตั้งค่า Low หรือ High
*   **Low**: โมเดลจะได้รับรูปภาพเวอร์ชันความละเอียดต่ำ 512px x 512px และแสดงรูปภาพด้วยงบประมาณ 65 tokens ซึ่งช่วยให้ API ตอบกลับได้เร็วขึ้นและใช้ input tokens น้อยลง ใช้ตัวเลือกนี้สำหรับกรณีการใช้งานที่ไม่ต้องการรายละเอียดสูง
*   **High**: โมเดลสามารถเข้าถึงรูปภาพความละเอียดต่ำ จากนั้นสร้างภาพ crop โดยละเอียดของ input images เป็นสี่เหลี่ยมจัตุรัส 512px ตามขนาด input image แต่ละภาพ crop โดยละเอียดจะใช้งบประมาณ token สองเท่า (65 tokens) รวมเป็น 129 tokens ใช้ตัวเลือกนี้สำหรับกรณีการใช้งานที่ต้องการรายละเอียดสูง

## Templates and examples

<!-- see https://www.notion.so/n8n/Pull-in-templates-for-the-integrations-pages-37c716837b804d30a33b47475f6e3780 -->
[[ templatesWidget(page.title, 'basic-llm-chain') ]]

## Related resources

อ้างอิง [เอกสารของ LangChain เกี่ยวกับ Basic LLM Chains](https://js.langchain.com/docs/tutorials/llm_chain/){:target=_blank .external-link} สำหรับข้อมูลเพิ่มเติมเกี่ยวกับบริการ

--8<-- "_snippets/integrations/builtin/cluster-nodes/langchain-overview-link.md"
--8<-- "_glossary/ai-glossary.md"

## Common issues

นี่คือข้อผิดพลาดและปัญหาทั่วไปบางประการเกี่ยวกับ Basic LLM Chain node และขั้นตอนในการแก้ไขหรือแก้ไขปัญหา

### No prompt specified error

ข้อผิดพลาดนี้จะแสดงขึ้นเมื่อ **Prompt** ว่างเปล่าหรือไม่ถูกต้อง

คุณอาจเห็นข้อผิดพลาดนี้ในสถานการณ์ใดสถานการณ์หนึ่งจากสองสถานการณ์:

1.  เมื่อคุณตั้งค่า **Prompt** เป็น **Define below** และไม่ได้ป้อนอะไรในช่อง **Text**
    *   ในการแก้ไข ให้ป้อน prompt ที่ถูกต้องในช่อง **Text**
2.  เมื่อคุณตั้งค่า **Prompt** เป็น **Connected Chat Trigger Node** และข้อมูลขาเข้าไม่มีฟิลด์ชื่อ `chatInput`
    *   โหนดคาดหวังฟิลด์ `chatInput` หากโหนดก่อนหน้าของคุณไม่มีฟิลด์นี้ ให้เพิ่มโหนด [Edit Fields (Set)](/integrations/builtin/core-nodes/n8n-nodes-base.set.md) เพื่อแก้ไขชื่อฟิลด์ขาเข้าเป็น `chatInput`
