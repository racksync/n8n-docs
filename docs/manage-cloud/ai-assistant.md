---
#https://www.notion.so/n8n/Frontmatter-432c2b8dff1f43d4b1c8d20075510fe4
contentType: explanation
---

# AI Assistant

n8n AI Assistant ช่วยให้คุณสร้าง, debug, และปรับแต่ง workflow ได้อย่างง่ายดาย ไม่ว่าจะเป็นการตอบคำถามเกี่ยวกับ n8n หรือช่วยเหลือเรื่องการเขียนโค้ดและ [expressions](/glossary.md#expression-n8n) AI Assistant จะช่วยให้การสร้าง workflow ของคุณเป็นเรื่องง่ายขึ้น และช่วยซัพพอร์ตคุณขณะใช้งานความสามารถต่างๆ ของ n8n

## Current capabilities

AI Assistant มีเครื่องมือหลากหลายเพื่อช่วยเหลือคุณ:

- **Debug helper**: ช่วยหาสาเหตุและแก้ปัญหาเวลามีปัญหาในการรัน node ใน workflow ของคุณ เพื่อให้ workflow ทำงานได้ต่อเนื่อง
- **Answer n8n questions**: ตอบคำถามเกี่ยวกับ n8n ได้ทันที ไม่ว่าจะเป็นฟีเจอร์เฉพาะหรือการใช้งานทั่วไป
- **Coding support**: ให้คำแนะนำเกี่ยวกับการเขียนโค้ด เช่น SQL และ JSON เพื่อให้ node และการประมวลผลข้อมูลของคุณมีประสิทธิภาพมากขึ้น
- **Expression assistance**: สอนวิธีสร้างและปรับแต่ง [expressions](/code/expressions.md) เพื่อให้ workflow ของคุณทำงานได้เต็มที่
- **Credential setup tips**: แนะนำวิธีตั้งค่าและจัดการ node [credentials](/integrations/builtin/credentials/index.md) อย่างปลอดภัยและมีประสิทธิภาพ

## Tips for getting the most out of the Assistant

1. **Engage in a conversation**: AI Assistant สามารถคุยกับคุณแบบ step-by-step ได้ ถ้าคำแนะนำไม่ตรงใจ บอกได้เลย! ยิ่งให้ข้อมูลมากเท่าไหร่ คำแนะนำก็จะยิ่งตรงจุดมากขึ้น
<!-- vale from-microsoft.FirstPerson = NO -->
2. **Ask specific questions**: ถามคำถามแบบเจาะจงจะได้ผลลัพธ์ดีที่สุด (เช่น "How do I set up credentials for Google Sheets?") Assistant จะตอบได้ดีที่สุดถ้าคำถามชัดเจน
3. **Iterate on suggestions**: อย่ากลัวที่จะต่อยอดจากคำตอบของ Assistant ลองวิธีต่างๆ และปรับแต่งตาม feedback เพื่อให้ได้ผลลัพธ์ที่ต้องการ
4. **Things to try out**:
    - Debug ข้อผิดพลาดที่คุณเจอ
    - ถามวิธี setup credentials
    - "Explain what this workflow does."
    - "I need your help to write code: [Explain your code here]"
    - "How can I build X in n8n?"
<!-- vale from-microsoft.FirstPerson = YES -->

## FAQs

<!-- vale from-microsoft.HeadingPunctuation = NO -->
### What context does the Assistant have?

AI Assistant จะเข้าถึงทุก element ที่แสดงบนหน้าจอ n8n ของคุณ ยกเว้นค่าข้อมูล input และ output จริง (เช่น ข้อมูลลูกค้า) ถ้าอยากรู้ว่า n8n แชร์ข้อมูลอะไรกับ Assistant บ้าง ดูได้ที่ [AI in n8n](https://docs.n8n.io/privacy-security/privacy/#ai-in-n8n)

<!-- vale from-microsoft.FirstPerson = NO -->
### Who can use the Assistant?
<!-- vale from-microsoft.FirstPerson = YES -->

ผู้ใช้ทุกคนที่อยู่บน Cloud plan สามารถใช้ assistant ได้

### How does the Assistant work?

เบื้องหลังของ assistant ถูกสร้างขึ้นด้วย AI ขั้นสูงของ n8n โดยใช้การผสมผสานของ [agents](/glossary.md#ai-agent) ที่เชี่ยวชาญแต่ละด้านของ n8n, RAG เพื่อดึงข้อมูลจาก docs และ community forum รวมถึง custom prompts, [memory](/glossary.md#ai-memory) และ context
<!-- vale from-microsoft.HeadingPunctuation = YES -->
