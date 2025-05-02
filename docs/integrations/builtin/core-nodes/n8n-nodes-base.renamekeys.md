---
#https://www.notion.so/n8n/Frontmatter-432c2b8dff1f43d4b1c8d20075510fe4
title: Rename Keys
description: Documentation for the Rename Keys node in n8n, a workflow automation platform. Includes guidance on usage, and links to examples.
contentType: [integration, reference]
priority: medium
---

# Rename Keys

ใช้ Rename Keys node เพื่อเปลี่ยนชื่อ key ของ key-value pair ใน n8n

## Node parameters

คุณสามารถเปลี่ยนชื่อ key ได้หนึ่งหรือหลาย key โดยใช้ Rename Keys node กดปุ่ม **Add new key** เพื่อเพิ่ม key ที่ต้องการเปลี่ยนชื่อ

สำหรับแต่ละ key ให้กรอก:

- **Current Key Name**: ชื่อปัจจุบันของ key ที่ต้องการเปลี่ยนชื่อ
- **New Key Name**: ชื่อใหม่ที่ต้องการตั้งให้ key นั้น

## Node options

เลือกว่าจะใช้ **Regex** (regular expression) เพื่อระบุ key ที่ต้องการเปลี่ยนชื่อหรือไม่ ถ้าใช้ option นี้ ต้องกรอกข้อมูลดังนี้:

* **Regular Expression**: กรอก regular expression ที่ต้องการใช้
* **Replace With**: กรอกชื่อใหม่ที่ต้องการตั้งให้ key ที่ตรงกับ regular expression
* สามารถเลือก option เฉพาะของ Regex ได้ดังนี้:
    * **Case Insensitive**: เลือกว่าจะให้ regular expression ไม่สนใจตัวพิมพ์ใหญ่/เล็ก (เปิด) หรือสนใจ (ปิด)
    * **Max Depth**: กำหนดความลึกสูงสุดในการเปลี่ยนชื่อ key โดย `-1` คือไม่จำกัด, `0` คือเฉพาะระดับบนสุด

/// warning | Regex impacts
การใช้ regular expression อาจมีผลกับ key ใด ๆ ที่ตรงกับ expression รวมถึง key ที่คุณเปลี่ยนชื่อไปแล้วด้วย
///

## Templates and examples

<!-- see https://www.notion.so/n8n/Pull-in-templates-for-the-integrations-pages-37c716837b804d30a33b47475f6e3780 -->
[[ templatesWidget(page.title, 'rename-keys') ]]
