---
#https://www.notion.so/n8n/Frontmatter-432c2b8dff1f43d4b1c8d20075510fe4
title: OpenAI Assistant operations
description: เอกสารสำหรับ Assistant operations ใน OpenAI node ของ n8n. รวมรายละเอียด operations, การตั้งค่า, และลิงก์.
contentType: [integration, reference]
priority: critical
---

# OpenAI Assistant operations

ใช้ operation นี้เพื่อสร้าง, ลบ, แสดงรายการ, ส่งข้อความ หรืออัปเดต assistant ใน OpenAI. ดูข้อมูลเพิ่มเติมเกี่ยวกับ OpenAI node ได้ที่ [OpenAI](/integrations/builtin/app-nodes/n8n-nodes-langchain.openai/index.md).

## Create an Assistant

ใช้ operation นี้เพื่อสร้าง assistant ใหม่.

Enter these parameters:

- **Credential to connect with**: สร้างหรือเลือก [OpenAI credential](/integrations/builtin/credentials/openai.md) ที่มีอยู่แล้ว.
- **Resource**: เลือก **Assistant**.
- **Operation**: เลือก **Create an Assistant**.
- **Model**: เลือก Model ที่ assistant จะใช้. หากไม่แน่ใจ ให้ลองใช้ `gpt-4o` สำหรับความฉลาดสูง หรือ `gpt-4o-mini` สำหรับความเร็วและต้นทุนต่ำสุด. ดูรายละเอียดเพิ่มเติมได้ที่ [Models overview | OpenAI Platform](https://platform.openai.com/docs/models){:target=_blank .external-link}.
- **Name**: ระบุชื่อของ assistant. ความยาวสูงสุด 256 ตัวอักษร.
- **Description**: ระบุคำอธิบายของ assistant. ความยาวสูงสุด 512 ตัวอักษร.
  ```
  A virtual assistant that helps users with daily tasks, including setting reminders, answering general questions, and providing quick information.
  ```
- **Instructions**: ระบุ system instructions ที่ assistant ใช้. ความยาวสูงสุด 32,768 ตัวอักษร. ใช้เพื่อกำหนด persona ของโมเดล.
  ```
  Always respond in a friendly and engaging manner. When a user asks a question, provide a concise answer first, followed by a brief explanation or additional context if necessary. If the question is open-ended, offer a suggestion or ask a clarifying question to guide the conversation. Keep the tone positive and supportive, and avoid technical jargon unless specifically requested by the user.
  ```
- **Code Interpreter**: เปิดเพื่อใช้งาน code interpreter สำหรับ assistant ที่สามารถเขียนและรันโค้ดในสภาพแวดล้อม sandbox. ใช้สำหรับงานที่ต้องใช้การคำนวณ วิเคราะห์ข้อมูล หรือประมวลผลตรรกะ.
- **Knowledge Retrieval**: เปิดเพื่อใช้งานการดึงข้อมูลความรู้ให้ assistant เข้าถึงแหล่งข้อมูลภายนอกหรือฐานความรู้ที่เชื่อมต่อได้. ดูรายละเอียดเพิ่มเติมได้ที่ [File Search | OpenAI Platform](https://platform.openai.com/docs/assistants/tools/file-search){:target=_blank .external-link}.
  - **Files**: เลือกไฟล์ที่จะอัปโหลดเป็นแหล่งความรู้ภายนอก. ใช้ operation **Upload a File** เพื่อเพิ่มไฟล์เพิ่มเติม.

### Options

- **Output Randomness (Temperature)**: ปรับความสุ่มของผลลัพธ์ โดยมีช่วงค่าระหว่าง `0.0` (deterministic) ถึง `1.0` (สุ่มมากที่สุด). แนะนำให้ปรับค่า temperature หรือ **Output Randomness (Top P)** แต่ไม่ปรับทั้งคู่พร้อมกัน. เริ่มที่ค่าปานกลาง (ประมาณ 0.7) แล้วปรับตามผลที่สังเกต.
- **Output Randomness (Top P)**: ปรับค่า Top P เพื่อควบคุมความหลากหลายของคำตอบ. ตัวอย่าง `0.5` หมายถึงพิจารณาตัวเลือกที่มีน้ำหนักความน่าจะเป็นครึ่งหนึ่ง. แนะนำให้ปรับเพียงหนึ่งในค่า temperature หรือ Top P.
- **Fail if Assistant Already Exists**: ถ้าเปิดใช้งาน จะทำให้ operation ล้มเหลวหากมี assistant ที่มีชื่อเดียวกันอยู่แล้ว.

ดูรายละเอียดเพิ่มเติมที่ [Create assistant | OpenAI](https://platform.openai.com/docs/api-reference/assistants/createAssistant){:target=_blank .external-link}.

## Delete an Assistant

ใช้ operation นี้เพื่อลบ assistant ที่มีอยู่จากบัญชีของคุณ.

Enter these parameters:

- **Credential to connect with**: สร้างหรือเลือก [OpenAI credential](/integrations/builtin/credentials/openai.md) ที่มีอยู่แล้ว.
- **Resource**: เลือก **Assistant**.
- **Operation**: เลือก **Delete an Assistant**.
- **Assistant**: เลือก assistant ที่ต้องการลบ **From list** หรือ **By ID**.

ดูรายละเอียดเพิ่มเติมที่ [Delete assistant | OpenAI](https://platform.openai.com/docs/api-reference/assistants/deleteAssistant){:target=_blank .external-link}.

## List Assistants

ใช้ operation นี้เพื่อดึงรายการ assistant ในองค์กรของคุณ.

- **Credential to connect with**: สร้างหรือเลือก [OpenAI credential](/integrations/builtin/credentials/openai.md) ที่มีอยู่แล้ว.
- **Resource**: เลือก **Assistant**.
- **Operation**: เลือก **List Assistants**.

### Options

- **Simplify Output**: เปิดเพื่อคืนผลลัพธ์แบบย่อแทนข้อมูลดิบ. (ค่าเริ่มต้นเปิดใช้งาน)

ดูรายละเอียดเพิ่มเติมที่ [List assistants | OpenAI](https://platform.openai.com/docs/api-reference/assistants/listAssistants){:target=_blank .external-link}.

## Message an Assistant

ใช้ operation นี้เพื่อส่งข้อความไปยัง assistant และรับการตอบกลับ.

Enter these parameters:

- **Credential to connect with**: สร้างหรือเลือก [OpenAI credential](/integrations/builtin/credentials/openai.md) ที่มีอยู่แล้ว.
- **Resource**: เลือก **Assistant**.
- **Operation**: เลือก **Message an Assistant**.
- **Assistant**: เลือก assistant ที่ต้องการส่งข้อความ.
- **Prompt**: ระบุข้อความ prompt ที่ต้องการส่ง.
    - **Connected Chat Trigger Node**: ใช้ input จากฟิลด์ `chatInput` ของ node ก่อนหน้าโดยอัตโนมัติ.
    - **Define Below**: กำหนด prompt ด้วยตนเอง โดยระบุข้อความคงที่หรือใช้ expression จาก node ก่อนหน้า.

### Options

- **Base URL**: ระบุ base URL ที่ assistant ควรใช้สำหรับการร้องขอ API. ใช้สำหรับชี้ไปที่ endpoint ของ LLM ผู้ให้บริการอื่นๆ ที่รองรับ API แบบ OpenAI.
- **Max Retries**: กำหนดจำนวนครั้งที่ assistant ควรลองใหม่หากเกิดความล้มเหลว.
- **Timeout**: กำหนดเวลาสูงสุด (มิลลิวินาที) ที่ assistant รอคำตอบก่อนหมดเวลา.
- **Preserve Original Tools**: ปิดเพื่อเอาเครื่องมือเดิมของ assistant ออก. ใช้ถ้าต้องการเอาเครื่องมือออกชั่วคราวใน operation นี้.

ดูรายละเอียดที่ [Assistants | OpenAI](https://platform.openai.com/docs/api-reference/assistants){:target=_blank .external-link}.

## Update an Assistant

ใช้ operation นี้เพื่ออัปเดตรายละเอียดของ assistant ที่มีอยู่.

Enter these parameters:

- **Credential to connect with**: สร้างหรือเลือก [OpenAI credential](/integrations/builtin/credentials/openai.md) ที่มีอยู่แล้ว.
- **Resource**: เลือก **Assistant**.
- **Operation**: เลือก **Update an Assistant**.
- **Assistant**: เลือก assistant ที่ต้องการอัปเดต.

### Options

- **Code Interpreter**: เปิดเพื่อใช้งาน code interpreter สำหรับ assistant.
- **Description**: ระบุคำอธิบายของ assistant. ความยาวสูงสุด 512 ตัวอักษร.
  ```
  A virtual assistant that helps users with daily tasks, including setting reminders, answering general questions, and providing quick information.
  ```
- **Instructions**: ระบุ system instructions สำหรับ assistant. ความยาวสูงสุด 32,768 ตัวอักษร.
  ```
  Always respond in a friendly and engaging manner. When a user asks a question, provide a concise answer first, followed by a brief explanation or additional context if necessary. If the question is open-ended, offer a suggestion or ask a clarifying question to guide the conversation. Keep the tone positive and supportive, and avoid technical jargon unless specifically requested by the user.
  ```
- **Knowledge Retrieval**: เปิดเพื่อให้ assistant ดึงข้อมูลจากแหล่งข้อมูลภายนอกหรือฐานข้อมูล.
- **Files**: เลือกไฟล์สำหรับอัปโหลดเป็นแหล่งความรู้ (เฉพาะอัปเดต Code Interpreter เท่านั้น). ใช้ [**Upload a File**](/integrations/builtin/app-nodes/n8n-nodes-langchain.openai/file-operations.md#upload-a-file).
- **Model**: เลือก Model ที่ assistant จะใช้. หากไม่แน่ใจ ให้ลอง `gpt-4o` หรือ `gpt-4o-mini`. ดูรายละเอียดเพิ่มเติมได้ที่ [Models overview | OpenAI Platform](https://platform.openai.com/docs/models){:target=_blank .external-link}.
- **Name**: ระบุชื่อของ assistant. ความยาวสูงสุด 256 ตัวอักษร.
- **Remove All Custom Tools (Functions)**: เปิดเพื่อลบเครื่องมือ (functions) ที่กำหนดเองทั้งหมดออกจาก assistant.
- **Output Randomness (Temperature)**: ปรับความสุ่มของผลลัพธ์ในช่วง `0.0` ถึง `1.0`. แนะนำให้ปรับเพียงหนึ่งในค่า temperature หรือ Top P.
- **Output Randomness (Top P)**: ปรับค่า Top P เพื่อตั้งค่าความหลากหลายของคำตอบ. เช่น `0.5` หมายถึงพิจารณาตัวเลือกน้ำหนักความน่าจะเป็นครึ่งหนึ่ง.

ดูรายละเอียดเพิ่มเติมที่ [Modify assistant | OpenAI](https://platform.openai.com/docs/api-reference/assistants/modifyAssistant){:target=_blank .external-link}.

## Common issues

สำหรับข้อผิดพลาดและปัญหาทั่วไป พร้อมแนวทางแก้ไข ให้ดู [Common Issues](/integrations/builtin/app-nodes/n8n-nodes-langchain.openai/common-issues.md).
