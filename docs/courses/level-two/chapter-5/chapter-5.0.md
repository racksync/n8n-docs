---
#https://www.notion.so/n8n/Frontmatter-432c2b8dff1f43d4b1c8d20075510fe4
contentType: tutorial
---

# Automating a business workflow

จำ [our friend Nathan](/courses/level-one/chapter-3.md) ได้ไหม?

**Nathan 🙋:** สวัสดีครับ ผมเองครับ ผู้จัดการของผมประทับใจกับโซลูชัน workflow automation แรกของผมมาก จนเธอมอบหมายความรับผิดชอบให้ผมมากขึ้น<br/>
**You 👩‍🔧:** งานและความรับผิดชอบมากขึ้น ยินดีด้วยนะคะ แล้วตอนนี้คุณต้องทำอะไรบ้าง?<br/>
**Nathan 🙋:** ผมเข้าถึงข้อมูลการขายทั้งหมดของเราได้แล้ว และตอนนี้ผมรับผิดชอบในการสร้างรายงานสองฉบับ: ฉบับหนึ่งสำหรับยอดขายตามภูมิภาค และอีกฉบับสำหรับราคา orders ข้อมูลมาจากแหล่งต่างๆ และอยู่ในรูปแบบที่แตกต่างกัน<br/>
**You 👩‍🔧:** ฟังดูเหมือนงาน manual เยอะเลย แต่เป็นประเภทที่สามารถทำ automation ได้ มาทำกันเถอะ!


## Workflow design

ตอนนี้เรารู้แล้วว่า Nathan ต้องการทำ automation อะไร มาลิสต์ขั้นตอนที่เขาต้องทำเพื่อให้บรรลุเป้าหมายนี้กัน:

1. รับและรวมข้อมูลจากแหล่งที่จำเป็นทั้งหมด
2. เรียงลำดับข้อมูลและจัดรูปแบบวันที่
3. เขียน binary files
4. ส่งการแจ้งเตือนโดยใช้อีเมลและ Discord

n8n มี [core nodes](/integrations/builtin/node-types.md#core-nodes) สำหรับขั้นตอนเหล่านี้ทั้งหมด use case นี้ค่อนข้างซับซ้อน เราควรสร้างจากสาม workflows แยกกัน:

1. workflow ที่รวมข้อมูลบริษัทกับข้อมูลภายนอก
2. workflow ที่สร้างรายงาน
3. workflow ที่ monitor errors ใน workflow ที่สอง

## Workflow prerequisites

ในการสร้าง workflows คุณจะต้องมีสิ่งต่อไปนี้:

* บัญชี [Airtable](https://airtable.com/){:target="_blank" .external-link} และ [credentials](/integrations/builtin/credentials/airtable.md)
* บัญชี [Google](https://www.google.com/account/about/){:target="_blank" .external-link} และ [credentials](/integrations/builtin/credentials/google/index.md) เพื่อเข้าถึง Gmail
* บัญชี [Discord](https://discord.com/){:target="_blank" .external-link} และ webhook URL (คุณได้รับสิ่งนี้ทางอีเมลเมื่อคุณลงทะเบียนสำหรับคอร์สนี้)

ถัดไป คุณจะสร้างสาม workflows เหล่านี้พร้อมคำแนะนำทีละขั้นตอน
