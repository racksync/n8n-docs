---
#https://www.notion.so/n8n/Frontmatter-432c2b8dff1f43d4b1c8d20075510fe4
title: การใช้ Code ในเอกสารและคู่มือ n8n
description: เข้าถึงเอกสารและคู่มือการใช้ code และ expressions ใน n8n รวมถึงแหล่งข้อมูลสำหรับนักพัฒนาอื่นๆ
contentType: overview
---

# Code in n8n

n8n เป็นเครื่องมือ low-code ซึ่งหมายความว่าคุณสามารถทำอะไรได้มากมายโดยไม่ต้องเขียน code แล้วค่อยเพิ่ม code เข้าไปเมื่อจำเป็น

## Code in your workflows

มีสองที่ใน workflows ของคุณที่คุณสามารถใช้ code ได้:

<div class="grid-cards-vertical cards" markdown>

- __Expressions__

	ใช้ [expressions](/glossary.md#expression-n8n) เพื่อแปลง [data](/data/index.md) ใน nodes ของคุณ คุณสามารถใช้ JavaScript ใน expressions รวมถึง [Built-in methods and variables](/code/builtin/overview.md) และ [Data transformation functions](/code/builtin/data-transformation-functions/index.md) ของ n8n

	[:octicons-arrow-right-24: Expressions](/code/expressions.md)

- __Code node__

	ใช้ Code node เพื่อเพิ่ม JavaScript หรือ Python ลงใน workflow ของคุณ

	[:octicons-arrow-right-24: Code node](/code/code-node.md)

</div>


## Other technical resources

นี่คือ features ที่เกี่ยวข้องกับผู้ใช้ทางเทคนิค

### Technical nodes

n8n มี core nodes ซึ่งช่วยให้การเพิ่มฟังก์ชันการทำงานหลัก เช่น การร้องขอ API, webhooks, การตั้งเวลา และการจัดการไฟล์ง่ายขึ้น

<div class="grid-cards-vertical cards" markdown>

- __Write a backend__

	[HTTP Request](/integrations/builtin/core-nodes/n8n-nodes-base.httprequest/index.md), [Webhook](/integrations/builtin/core-nodes/n8n-nodes-base.webhook/index.md), และ [Code](/code/code-node.md) nodes ช่วยให้คุณทำการเรียก API, ตอบสนองต่อ webhooks, และเขียน JavaScript ใดๆ ใน workflow ของคุณ

	ใช้สิ่งนี้เพื่อทำสิ่งต่างๆ เช่น [Create an API endpoint](https://n8n.io/workflows/1750-creating-an-api-endpoint/){:target=_blank .external-link}

	[:octicons-arrow-right-24: Core nodes](/integrations/builtin/core-nodes/index.md)

- __Represent complex logic__

	คุณสามารถสร้าง flows ที่ซับซ้อนได้ โดยใช้ nodes เช่น [If](/integrations/builtin/core-nodes/n8n-nodes-base.if.md), [Switch](/integrations/builtin/core-nodes/n8n-nodes-base.switch.md), และ [Merge](/integrations/builtin/core-nodes/n8n-nodes-base.merge.md) nodes

	[:octicons-arrow-right-24: Flow logic](/flow-logic/index.md)

</div>

### Other developer resources

<div class="grid-cards-vertical cards" markdown>

- __The n8n API__

	n8n มี API ที่คุณสามารถทำงานหลายอย่างแบบเดียวกับที่คุณทำใน GUI ผ่านการเขียนโปรแกรมได้ มี [n8n API node](/integrations/builtin/core-nodes/n8n-nodes-base.n8n.md) เพื่อเข้าถึง API ใน workflows ของคุณ

	[:octicons-arrow-right-24: API](/api/index.md)

- __Self-host__

	คุณสามารถ self-host n8n ได้ ซึ่งจะช่วยเก็บข้อมูลของคุณไว้ในโครงสร้างพื้นฐานของคุณเอง

	[:octicons-arrow-right-24: Hosting](/hosting/index.md)

- __Build your own nodes__

	คุณสามารถสร้าง custom nodes, ติดตั้งบน n8n instance ของคุณ, และเผยแพร่ไปยัง [npm](https://www.npmjs.com/){:target=_blank .external-link}

	[:octicons-arrow-right-24: Creating nodes](/integrations/creating-nodes/overview.md)

</div>
