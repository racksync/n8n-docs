---
#https://www.notion.so/n8n/Frontmatter-432c2b8dff1f43d4b1c8d20075510fe4
title: Vector databases คืออะไร
description: ทำความเข้าใจ vector databases เรียนรู้วิธีที่ n8n ให้บริการ vector databases พร้อมส่วนประกอบสำคัญ เช่น embeddings retrievers และ document loaders
contentType: explanation
---

# What are vector databases?

Vector database คือฐานข้อมูลที่เก็บข้อมูลเป็นตัวเลข:

> Vector database คือฐานข้อมูลที่เก็บข้อมูลเป็นเวกเตอร์มิติสูง (high-dimensional vectors) ซึ่งเป็นตัวแทนเชิงคณิตศาสตร์ของคุณสมบัติหรือ attribute ต่างๆ ([source](https://learn.microsoft.com/en-us/semantic-kernel/memories/vector-db){:target=_blank .external-link})

ข้อดีคือสามารถค้นหาข้อมูลที่คล้ายกันได้อย่างรวดเร็วและแม่นยำ ด้วย vector database คุณจะค้นหาข้อมูลที่เกี่ยวข้องจากความหมายหรือ context แทนที่จะใช้ query แบบดั้งเดิม

## A simplified example

สมมติว่า vector database เก็บประโยค "n8n is a source-available automation tool that you can self-host" แทนที่จะเก็บเป็นข้อความ จะเก็บเป็น array ของตัวเลข (แต่ละตัวเลขอยู่ระหว่าง 0 ถึง 1) ที่แทนคุณสมบัติต่างๆ ของประโยคนี้ ไม่ใช่การแปลงแต่ละตัวอักษรเป็นตัวเลข แต่เวกเตอร์จะอธิบายเนื้อหาของประโยค

เช่น ใน vector store ถ้า `0.1` แทน `automation tool`, `0.2` แทน `source available`, `0.3` แทน `can be self-hosted` จะได้เวกเตอร์แบบนี้:

| Sentence | Vector (array of dimensions) |
| -------- | ------ |
| n8n is a source-available automation tool that you can self-host | [0.1, 0.2, 0.3] |
| Zapier is an automation tool | [0.1] |
| Make is an automation tool | [0.1] |
| Confluence is a wiki tool that you can self-host | [0.3] |

/// note | ตัวอย่างนี้ง่ายมาก
ในความเป็นจริง เวกเตอร์จะซับซ้อนกว่านี้มาก ขนาดของเวกเตอร์อาจมีตั้งแต่หลักสิบถึงหลักพันมิติ และแต่ละมิติไม่ได้แทน feature เดียวแบบตรงๆ ตัวอย่างนี้แค่ช่วยให้เห็นภาพรวม ไม่ใช่ความเข้าใจเชิงเทคนิคจริงๆ ///

## Demonstrating the power of similarity search

Qdrant มี [vector search demos](https://qdrant.tech/demo/){:target=_blank .external-link} ให้ลองเล่นเพื่อเข้าใจพลังของ vector database เช่น [food discovery demo](https://food-discovery.qdrant.tech/){:target=_blank .external-link} ที่โชว์การจับคู่รูปอาหารจากความคล้ายกันของภาพ

> เดโมนี้ใช้ข้อมูลจาก Delivery Service ผู้ใช้สามารถกด like/dislike รูปอาหาร แล้วแอปจะแนะนำเมนูที่คล้ายกันตามหน้าตา หรือเลือกดูเฉพาะร้านในระยะส่งได้ ([source](https://qdrant.tech/demo/){:target=_blank .external-link})

ดูรายละเอียดเทคนิคเต็มๆ ได้ที่ [Qdrant demo-food-discovery GitHub repository](https://github.com/qdrant/demo-food-discovery){:target=_blank .external-link}

## Embeddings, retrievers, text splitters, and document loaders

Vector database ต้องใช้เครื่องมืออื่นร่วมด้วย:

- Document loaders และ text splitters: document loader จะดึงข้อมูลหรือเอกสารเข้ามาและเตรียมไว้สำหรับ [embedding](/glossary.md#ai-embedding) โดยอาจใช้ text splitter แบ่งเอกสารเป็นชิ้นๆ
- Embeddings: เป็นเครื่องมือที่แปลงข้อมูล (ข้อความ, รูปภาพ ฯลฯ) เป็นเวกเตอร์ และแปลงกลับเป็นข้อมูลดิบ n8n รองรับเฉพาะ text embedding
- Retrievers: ใช้ดึงข้อมูลจาก vector database ต้องใช้ร่วมกับ embedding เพื่อแปลงเวกเตอร์กลับเป็นข้อมูล





