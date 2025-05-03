---
#https://www.notion.so/n8n/Frontmatter-432c2b8dff1f43d4b1c8d20075510fe4
description: ใส่คำอธิบายประกอบ workflows ของคุณโดยใช้ sticky notes
contentType: howto
---

# Sticky Notes

Sticky Notes ช่วยให้คุณสามารถใส่คำอธิบายประกอบและแสดงความคิดเห็นใน workflows ของคุณได้

n8n แนะนำให้ใช้ Sticky Notes อย่างสม่ำเสมอ โดยเฉพาะอย่างยิ่งใน [template workflows](/glossary.md#template-n8n) เพื่อช่วยให้ผู้ใช้คนอื่นเข้าใจ workflow ของคุณ

![Screenshot of a basic workflow with an example sticky note](/_images/workflows/components/stickies/example-sticky-note.png)

## Create a Sticky Note

Sticky Notes เป็น core node วิธีเพิ่ม Sticky Note ใหม่:

1. เปิด nodes panel
2. ค้นหา `note`
3. คลิกที่ **Sticky Note** node n8n จะเพิ่ม Sticky Note ใหม่ลงบน canvas

## Edit a Sticky Note

1. ดับเบิลคลิกที่ Sticky Note ที่คุณต้องการแก้ไข
2. เขียนบันทึกของคุณ [คู่มือนี้](https://commonmark.org/help/) อธิบายวิธีการจัดรูปแบบข้อความของคุณด้วย Markdown n8n ใช้ [markdown-it](https://github.com/markdown-it/markdown-it) ซึ่งใช้ข้อกำหนด CommonMark
3. คลิกออกห่างจาก note หรือกด `Esc` เพื่อหยุดแก้ไข

## Change the color

วิธีเปลี่ยนสี Sticky Note:

1. วางเมาส์เหนือ Sticky Note
1. เลือก **Change color** <span class="inline-image">![Change Sticky Note color icon](/_images/common-icons/change-color.png){.off-glb}</span>

## Sticky Note positioning

คุณสามารถ:

* ลาก Sticky Note ไปวางที่ใดก็ได้บน canvas
* ลาก Sticky Notes ไปไว้ด้านหลัง nodes คุณสามารถใช้สิ่งนี้เพื่อจัดกลุ่ม nodes ด้วยสายตา
* ปรับขนาด Sticky Notes โดยวางเมาส์เหนือขอบของ note แล้วลากเพื่อปรับขนาด
* เปลี่ยนสี: เลือก **Options** <span class="inline-image">![Options icon](/_images/common-icons/three-dot-options-menu.png){.off-glb}</span> เพื่อเปิดตัวเลือกสี

## Writing in Markdown

Sticky Notes รองรับการจัดรูปแบบ Markdown ส่วนนี้อธิบายตัวเลือกทั่วไปบางส่วน

```
The text in double asterisks will be **bold**

The text in single asterisks will be *italic*

Use # to indicate headings:
# This is a top-level heading
## This is a sub-heading
### This is a smaller sub-heading

You can add links:
[Example](https://example.com/)

Create lists with asterisks:

* Item one
* Item two

Or created ordered lists with numbers:

1. Item one
2. Item two
```

สำหรับคำแนะนำโดยละเอียดเพิ่มเติม โปรดดูที่ [CommonMark's help](https://commonmark.org/help/) n8n ใช้ [markdown-it](https://github.com/markdown-it/markdown-it) ซึ่งใช้ข้อกำหนด CommonMark

## Make images full width

คุณสามารถบังคับให้รูปภาพมีความกว้าง 100% ของ sticky note ได้โดยการเพิ่ม `#full-width` ต่อท้ายชื่อไฟล์:

```markdown
![Source example](https://<IMAGE-URL>/<IMAGE-NAME>.png#full-width)
```
