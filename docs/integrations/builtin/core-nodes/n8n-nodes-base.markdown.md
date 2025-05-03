---
#https://www.notion.so/n8n/Frontmatter-432c2b8dff1f43d4b1c8d20075510fe4
title: มาร์กดาวน์ (Markdown)
description: คู่มือ Markdown node สำหรับแปลงข้อมูล Markdown และ HTML ใน n8n
contentType: [integration, reference]
priority: medium
---

# Markdown

Markdown node ใช้สำหรับแปลงข้อมูลระหว่างรูปแบบ Markdown และ HTML

## Operations

การทำงานของ node นี้เรียกว่า **Modes**:

*   **Markdown to HTML**: ใช้โหมดนี้เพื่อแปลง Markdown เป็น HTML
*   **HTML to Markdown**: ใช้โหมดนี้เพื่อแปลง HTML เป็น Markdown

## Node parameters

*   **HTML** หรือ **Markdown**: ใส่ข้อมูลที่ต้องการแปลง ชื่อฟิลด์จะเปลี่ยนไปตาม **Mode** ที่เลือก
*   **Destination Key**: ใส่ชื่อฟิลด์ที่ต้องการเก็บผลลัพธ์ สามารถระบุฟิลด์ซ้อนกันโดยใช้จุด เช่น `level1.level2.newKey`

## Node options

**Options** ของ node จะขึ้นอยู่กับ **Mode** ที่เลือก

/// note | ทดลองใช้ตัวเลือกต่างๆ
ตัวเลือกบางอย่างขึ้นอยู่กับตัวเลือกอื่นหรืออาจมีผลต่อกัน แนะนำให้ทดลองใช้แต่ละ option เพื่อดูว่าผลลัพธ์ตรงกับที่ต้องการหรือไม่
///

### Markdown to HTML options

| Option                       | Description


