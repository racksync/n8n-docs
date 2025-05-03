---
#https://www.notion.so/n8n/Frontmatter-432c2b8dff1f43d4b1c8d20075510fe4
title: OpenAI Text operations
description: เอกสารสำหรับ Text operations ใน OpenAI node ของ n8n. รวมรายละเอียด operations, การตั้งค่า, และลิงก์.
contentType: [integration, reference]
priority: critical
---

# OpenAI Text operations

ใช้ operation นี้เพื่อส่งข้อความหรือ prompt ไปยัง OpenAI model และรับคำตอบกลับ. ดูข้อมูลเพิ่มเติมที่ [OpenAI](/integrations/builtin/app-nodes/n8n-nodes-langchain.openai/index.md).

## Message a Model

ใช้ operation นี้เพื่อส่งข้อความหรือ prompt ไปยัง OpenAI model และรับผลลัพธ์ตอบกลับ.

Enter these parameters:

- **Credential to connect with**: สร้างหรือเลือก [OpenAI credential](/integrations/builtin/credentials/openai.md) ที่มีอยู่แล้ว.
- **Resource**: เลือก **Text**.
- **Operation**: เลือก **Message a Model**.
- **Model**: เลือก Model ที่ต้องการใช้. หากไม่แน่ใจ ให้ลองใช้ `gpt-4o` สำหรับความฉลาดสูง หรือ `gpt-4o-mini` สำหรับความเร็วและต้นทุนต่ำสุด. ดูรายละเอียดเพิ่มเติมได้ที่ [Models overview | OpenAI Platform](https://platform.openai.com/docs/models){:target=_blank .external-link}.
- **Messages**: ระบุ prompt แบบ **Text** และกำหนด **Role** ที่ model ควรใช้ในการตอบกลับ. ดูรายละเอียดเพิ่มเติมได้ที่ [Prompt engineering | OpenAI](https://platform.openai.com/docs/guides/prompt-engineering){:target=_blank .external-link} สำหรับวิธีการเขียน prompt โดยใช้ roles. ให้เลือกหนึ่งในบทบาทดังนี้:
    - **User**: ส่งข้อความในฐานะผู้ใช้และรับคำตอบจาก model.
    - **Assistant**: บอกให้ model ใช้น้ำเสียงหรือบุคลิกเฉพาะ.
    - **System**: ค่าเริ่มต้นคือ `"You are a helpful assistant"`. สามารถกำหนดคำแนะนำในข้อความ user ได้ แต่คำสั่งใน system message มีประสิทธิภาพมากกว่า. สามารถตั้งได้เพียงหนึ่งข้อความ system ต่อการสนทนา.
- **Simplify Output**: เปิดเพื่อคืนผลลัพธ์แบบย่อแทนข้อมูลดิบ.
- **Output Content as JSON**: เปิดเพื่อพยายามคืนผลลัพธ์ในรูปแบบ JSON. ใช้งานกับ `GPT-4 Turbo` และทุก model ใหม่ของ `GPT-3.5 Turbo` ที่ใหม่กว่า `gpt-3.5-turbo-1106`.

### Options

- **Frequency Penalty**: ใช้ลดแนวโน้มที่ model จะทำซ้ำคำในลักษณะเดียวกัน. ระหว่าง `0.0` ถึง `2.0`.
- **Maximum Number of Tokens**: กำหนดจำนวน tokens สูงสุดสำหรับคำตอบ (token หนึ่งประมาณ 4 ตัวอักษรภาษาอังกฤษ).
- **Number of Completions**: ค่าเริ่มต้นคือ 1. กำหนดจำนวน completions ที่ต้องการสร้างต่อ prompt.
- **Presence Penalty**: ใช้กระตุ้นให้ model นำเสนอหัวข้อใหม่. ช่วง `0.0` ถึง `2.0`.
- **Output Randomness (Temperature)**: ปรับความสุ่มของคำตอบในช่วง `0.0` ถึง `1.0`. แนะนำเริ่มประมาณ `0.7`.
- **Output Randomness (Top P)**: ปรับค่า Top P เพื่อควบคุมความหลากหลายของคำตอบ. เช่น `0.5` หมายถึงใช้ครึ่งหนึ่งของตัวเลือกที่มีน้ำหนักความน่าจะเป็น.

ดูรายละเอียดเพิ่มเติมที่ [Message a Model | OpenAI](https://platform.openai.com/docs/api-reference/text-completion/create){:target=_blank .external-link}.

## Classify Text for Violations

ใช้ operation นี้เพื่อตรวจจับและทำเครื่องหมายข้อความที่อาจเป็นอันตราย. OpenAI model จะวิเคราะห์ข้อความและคืนผลลัพธ์ประกอบด้วย:

- `flagged`: ฟิลด์ boolean ระบุว่าข้อความอาจเป็นอันตราย.
- `categories`: รายการของการแจ้งเตือนประเภทความผิด.
- `category_scores`: คะแนนสำหรับแต่ละประเภท.

Enter these parameters:

- **Credential to connect with**: สร้างหรือเลือก [OpenAI credential](/integrations/builtin/credentials/openai.md) ที่มีอยู่แล้ว.
- **Resource**: เลือก **Text**.
- **Operation**: เลือก **Classify Text for Violations**.
- **Text Input**: ระบุข้อความที่ต้องการตรวจสอบหากละเมิดนโยบาย moderation.
- **Simplify Output**: เปิดเพื่อคืนผลลัพธ์แบบย่อแทนข้อมูลดิบ.

### Options

- **Use Stable Model**: เปิดเพื่อใช้ model เวอร์ชันที่เสถียรแทนเวอร์ชันล่าสุด แม้อาจมีความแม่นยำน้อยลง.

ดูรายละเอียดเพิ่มเติมที่ [Moderations | OpenAI](https://platform.openai.com/docs/api-reference/moderations){:target=_blank .external-link}.

## Common issues

For common errors or issues and suggested resolution steps, refer to [Common Issues](/integrations/builtin/app-nodes/n8n-nodes-langchain.openai/common-issues.md).
