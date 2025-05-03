---
#https://www.notion.so/n8n/Frontmatter-432c2b8dff1f43d4b1c8d20075510fe4
title: คู่มือ Sentiment Analysis node
description: วิธีใช้งาน Sentiment Analysis node ใน n8n สำหรับวิเคราะห์ความรู้สึกของข้อความ
contentType: [integration, reference]
---

# Sentiment Analysis node

ใช้ Sentiment Analysis node เพื่อวิเคราะห์ sentiment (ความรู้สึก) ของข้อมูลข้อความที่เข้ามา

Language model ใช้ [**Sentiment Categories**](#node-options) ใน node options เพื่อกำหนด sentiment ของแต่ละ item

## Node parameters

*   **Text to Analyze** กำหนดข้อความ input สำหรับการวิเคราะห์ sentiment นี่คือ expression ที่อ้างอิงถึง field จาก input items ตัวอย่างเช่น อาจเป็น
    `{{ $json.chatInput }}` หาก input มาจากแหล่ง chat หรือ message โดยค่าเริ่มต้น คาดว่าจะเป็น field `text`

## Node options

*   **Sentiment Categories**: กำหนด categories ที่คุณต้องการจำแนก input ของคุณ
    *   โดยค่าเริ่มต้นคือ `Positive, Neutral, Negative` คุณสามารถปรับแต่ง categories เหล่านี้ให้เหมาะกับ use case เฉพาะของคุณได้ เช่น `Very Positive, Positive, Neutral, Negative, Very Negative` สำหรับการวิเคราะห์ที่ละเอียดมากขึ้น
*   **Include Detailed Results**: เมื่อเปิดใช้งาน ตัวเลือกนี้จะรวมคะแนนความแรงของ sentiment และ confidence scores ไว้ใน output โปรดทราบว่าคะแนนเหล่านี้เป็นค่าประมาณที่สร้างโดย language model และเป็นตัวบ่งชี้คร่าวๆ ไม่ใช่การวัดที่แม่นยำ
*   **System Prompt Template**: ใช้ตัวเลือกนี้เพื่อเปลี่ยน system prompt ที่ใช้สำหรับการวิเคราะห์ sentiment มันใช้ placeholder `{categories}` สำหรับ categories
*   **Enable Auto-Fixing**: เมื่อเปิดใช้งาน node จะแก้ไข outputs ของ model โดยอัตโนมัติเพื่อให้แน่ใจว่าตรงกับ format ที่คาดหวัง ทำได้โดยส่ง schema parsing error ไปยัง LLM และขอให้แก้ไข

## Usage Notes

### Model Temperature Setting

ขอแนะนำอย่างยิ่งให้ตั้งค่า temperature ของ language model ที่เชื่อมต่อเป็น 0 หรือค่าใกล้เคียง 0 ซึ่งจะช่วยให้มั่นใจได้ว่าผลลัพธ์จะมีความแน่นอน (deterministic) มากที่สุดเท่าที่จะเป็นไปได้ ทำให้การวิเคราะห์ sentiment มีความสอดคล้องและน่าเชื่อถือมากขึ้นในการรันหลายครั้ง

### Language Considerations

ประสิทธิภาพของ node อาจแตกต่างกันไปขึ้นอยู่กับภาษาของข้อความ input

เพื่อให้ได้ผลลัพธ์ที่ดีที่สุด ตรวจสอบให้แน่ใจว่า language model ที่คุณเลือก รองรับภาษาของ input

### Processing Large Volumes

เมื่อวิเคราะห์ข้อความจำนวนมาก ให้พิจารณาแบ่ง input ออกเป็นส่วนเล็กๆ (chunks) เพื่อเพิ่มประสิทธิภาพเวลาในการประมวลผลและการใช้ทรัพยากร

### Iterative Refinement

สำหรับงานวิเคราะห์ sentiment ที่ซับซ้อน คุณอาจต้องปรับแต่ง system prompt และ categories ซ้ำๆ เพื่อให้ได้ผลลัพธ์ที่ต้องการ

## Example Usage

### Basic Sentiment Analysis

1.  เชื่อมต่อ data source (เช่น RSS Feed, HTTP Request) เข้ากับ Sentiment Analysis node
2.  ตั้งค่า field "Text to Analyze" เป็น property ของ item ที่เกี่ยวข้อง (เช่น `{{ $json.content }}` สำหรับเนื้อหา blog post)
3.  คงค่า sentiment categories เริ่มต้นไว้
4.  เชื่อมต่อ outputs ของ node ไปยัง path แยกต่างหากสำหรับการประมวลผล sentiments เชิงบวก กลาง และลบ ที่แตกต่างกัน

### Custom Category Analysis

1.  เปลี่ยน **Sentiment Categories** เป็น `Excited, Happy, Neutral, Disappointed, Angry`
2.  ปรับ workflow ของคุณเพื่อจัดการกับ output categories ทั้งห้านี้
3.  ใช้การตั้งค่านี้เพื่อวิเคราะห์ความคิดเห็นของลูกค้าด้วย categories ทางอารมณ์ที่ละเอียดอ่อนยิ่งขึ้น

## Related resources

--8<-- "_snippets/integrations/builtin/cluster-nodes/langchain-overview-link.md"
--8<-- "_glossary/ai-glossary.md"
