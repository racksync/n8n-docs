### Operation Mode (โหมดการทำงาน)

Vector Store node นี้มีสี่โหมด: **Get Many**, **Insert Documents**, **Retrieve Documents (As Vector Store for Chain/Tool)**, และ **Retrieve Documents (As Tool for AI Agent)** โหมดที่คุณเลือกจะกำหนดการดำเนินการที่คุณสามารถทำได้ด้วย node และ input/output ที่มีให้ใช้งาน

<!-- vale off -->
#### Get Many (ดึงข้อมูลหลายรายการ)

ในโหมดนี้ คุณสามารถดึงเอกสารหลายรายการจาก vector database ของคุณโดยการระบุ prompt ตัว prompt จะถูกแปลงเป็น embedding และใช้สำหรับการค้นหาความคล้ายคลึง (similarity search) node จะส่งคืนเอกสารที่คล้ายกับ prompt มากที่สุดพร้อมกับคะแนนความคล้ายคลึง (similarity score) ซึ่งมีประโยชน์หากคุณต้องการดึงรายการเอกสารที่คล้ายกันและส่งต่อไปยัง agent เพื่อใช้เป็น context เพิ่มเติม
<!-- vale on -->

#### Insert Documents (แทรกเอกสาร)

ใช้โหมด Insert Documents เพื่อแทรกเอกสารใหม่เข้าไปใน vector database ของคุณ

#### Retrieve Documents (As Vector Store for Chain/Tool) (ดึงเอกสาร - เป็น Vector Store สำหรับ Chain/Tool)

ใช้โหมด Retrieve Documents (As Vector Store for Chain/Tool) กับ vector-store retriever เพื่อดึงเอกสารจาก vector database และส่งต่อไปยัง retriever ที่เชื่อมต่อกับ chain ในโหมดนี้ คุณต้องเชื่อมต่อ node เข้ากับ retriever node หรือ root node

#### Retrieve Documents (As Tool for AI Agent) (ดึงเอกสาร - เป็น Tool สำหรับ AI Agent)

ใช้โหมด Retrieve Documents (As Tool for AI Agent) เพื่อใช้ vector store เป็น tool resource ในการตอบคำถาม เมื่อสร้างคำตอบ agent จะใช้ vector store เมื่อชื่อและคำอธิบายของ vector store ตรงกับรายละเอียดของคำถาม
