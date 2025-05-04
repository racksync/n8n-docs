/// info | 0.236.0 และต่ำกว่า
n8n ได้ลบพฤติกรรมการ execution นี้ในเวอร์ชัน 1.0 ส่วนนี้ใช้กับ workflows ที่ใช้ลำดับการ execution แบบ **v0 (legacy)** โดยค่าเริ่มต้น นี่คือ workflows ทั้งหมดที่สร้างก่อนเวอร์ชัน 1.0 คุณสามารถเปลี่ยนลำดับการ execution ได้ใน [workflow settings](/workflows/settings.md)
///
หากคุณเพิ่ม Merge node ไปยัง workflow ที่มี If node อาจส่งผลให้ data streams ทั้งสองของ If node ทำงาน

Data stream หนึ่งจะ trigger Merge node ซึ่งจากนั้นจะไป execute data stream อีกอัน

ตัวอย่างเช่น ในภาพหน้าจอด้านล่าง มี workflow ที่มี Edit Fields node, If node และ Merge node พฤติกรรมมาตรฐานของ If node คือการ execute data stream เดียว (ในภาพหน้าจอคือ output **true**) อย่างไรก็ตาม เนื่องจากมี Merge node ทำให้ data streams ทั้งสองทำงาน แม้ว่า If node จะไม่ได้ส่งข้อมูลใดๆ ไปยัง data stream **false** ก็ตาม

![Screenshot of a workflow. The workflow has an Edit Fields node, followed by an If node. It ends with a Merge node.](/_images/integrations/builtin/core-nodes/merge/if-merge-node.png)

<!-- TODO: remove once v1 is mature -->
