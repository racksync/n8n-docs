---
#https://www.notion.so/n8n/Frontmatter-432c2b8dff1f43d4b1c8d20075510fe4
title: Loop Over Items (Split in Batches)
description: Documentation for the Loop Over Items node in n8n, a workflow automation platform. Includes guidance on usage, and links to examples.
contentType: [integration, reference]
priority: critical
---

# Loop Over Items

Loop Over Items node ช่วยให้คุณวนลูปผ่านข้อมูลได้ตามต้องการ

node นี้จะบันทึกข้อมูล input ดั้งเดิมไว้ และในแต่ละรอบของการวนลูป จะคืนค่าข้อมูลตามจำนวนที่กำหนดไว้ผ่าน output **loop**

เมื่อ node ทำงานเสร็จ จะรวมข้อมูลที่ประมวลผลทั้งหมดและคืนค่าผ่าน output **done**

## When to use the Loop Over Items node

โดยปกติแล้ว node ใน n8n จะถูกออกแบบมาให้ประมวลผลรายการข้อมูลเป็น list อยู่แล้ว (ยกเว้นบาง node ที่ระบุไว้ด้านล่าง) ขึ้นอยู่กับสิ่งที่คุณต้องการทำ คุณอาจไม่จำเป็นต้องใช้ Loop Over Items node ใน workflow ของคุณ สามารถอ่านเพิ่มเติมเกี่ยวกับการประมวลผลหลายรายการใน n8n ได้ที่ [looping in n8n](/flow-logic/looping.md)

ลิงก์เหล่านี้แสดงตัวอย่างกรณีที่ควรใช้ Loop Over Items node:

* [Loop until all items are processed](/flow-logic/looping.md#loop-until-all-items-are-processed): อธิบายความแตกต่างของ Loop Over Items node กับการประมวลผลรายการปกติ และเมื่อไหร่ควรใช้ node นี้
* [Node exceptions](/flow-logic/looping.md#node-exceptions): สรุปกรณีและ node ที่อาจต้องใช้ Loop Over Items node เพื่อสร้าง logic การวนลูปเอง
* [Avoiding rate limiting](/integrations/builtin/rate-limits.md): ตัวอย่างการ batch API requests เพื่อหลีกเลี่ยง rate limit จากบริการอื่น

## Node parameters

### Batch Size

ใส่จำนวนรายการที่ต้องการคืนค่าทุกครั้งที่เรียกใช้งาน

## Node options

### Reset

ถ้าเปิด option นี้ node จะ reset ข้อมูล input ปัจจุบันใหม่ทุกครั้งที่วนลูป ใช้ในกรณีที่ต้องการให้ Loop Over Items node มองข้อมูลที่เข้ามาแต่ละรอบเป็นชุดข้อมูลใหม่ ไม่ใช่ต่อเนื่องจากรอบก่อน

ตัวอย่างเช่น สามารถใช้ Loop Over Items node พร้อม reset option และ [If node](/integrations/builtin/core-nodes/n8n-nodes-base.if.md) เพื่อดึงข้อมูลแบบ paginated เมื่อไม่รู้จำนวนหน้าล่วงหน้า โดย loop จะดึงข้อมูลทีละหน้า ประมวลผล และเพิ่มหมายเลขหน้า การ reset loop จะช่วยให้แต่ละรอบเป็นข้อมูลใหม่ If node จะเช็คเงื่อนไขเพื่อหยุดหรือวนลูปต่อ

/// warning | Include a valid termination condition
สำหรับ workflow แบบนี้ ต้องมีเงื่อนไขหยุด loop ที่ถูกต้อง ถ้าเงื่อนไขไม่ตรงตามที่กำหนด workflow อาจวนลูปไม่รู้จบ
///

เมื่อเปิดใช้งาน สามารถปรับแต่งเงื่อนไข reset ได้โดยเปลี่ยน parameter จาก **Fixed** เป็น **Expression** ผลลัพธ์ของ expression จะเป็นตัวกำหนดว่า node จะ reset การประมวลผลรายการเมื่อไหร่

## Templates and examples

<!-- see https://www.notion.so/n8n/Pull-in-templates-for-the-integrations-pages-37c716837b804d30a33b47475f6e3780 -->
[[ templatesWidget(page.title, 'split-in-batches') ]]

### Read RSS feed from two different sources

workflow นี้ช่วยให้คุณอ่าน RSS feed จากสองแหล่งโดยใช้ Loop Over Items node จำเป็นต้องใช้ node นี้เพราะ RSS Feed Read node จะประมวลผลแค่รายการแรกที่ได้รับ สามารถดู [workflow](https://n8n.io/workflows/687-read-rss-feed-from-two-different-sources/){:target=_blank .external-link} ได้ที่ n8n.io

ตัวอย่างนี้จะอธิบายการสร้าง workflow โดยสมมติว่าคุณคุ้นเคยกับ n8n แล้ว ถ้ายังไม่เคยใช้งานมาก่อน ดูวิธีสร้าง workflow แรกได้ที่ [Try it out](/try-it-out/index.md)

workflow สุดท้ายจะหน้าตาแบบนี้:

[[ workflowDemo("file:///integrations/builtin/core-nodes/n8n-nodes-base.splitinbatches/rss-feed-example.json") ]]

คัดลอก workflow ข้างบนไปวางใน instance ของคุณ หรือสร้างเองตามขั้นตอนนี้:

1. เพิ่ม manual trigger
2. เพิ่ม Code node
3. คัดลอก code นี้ไปใส่ใน Code node:
	```js
	return [
		{
			json: {
				url: 'https://medium.com/feed/n8n-io',
			}
		},
		{
			json: {
				url: 'https://dev.to/feed/n8n',
			}
		}
	];
	```
4. เพิ่ม Loop Over Items node
5. ตั้งค่า Loop Over Items: ใส่ batch size เป็น `1` ใน **Batch Size**
6. เพิ่ม RSS Feed Read node
7. เลือก **Test Workflow** เพื่อรัน workflow และโหลดข้อมูลเข้า RSS Feed Read node
8. ตั้งค่า RSS Feed Read: map `url` จาก input ไปที่ **URL** สามารถลากจาก **INPUT** panel หรือใช้ expression: `{{ $json.url }}`
9. เลือก **Test Workflow** เพื่อดูผลลัพธ์

### Check that the node has processed all items

ถ้าอยากเช็คว่า node ประมวลผลข้อมูลครบหรือยัง ใช้ expression นี้: `{{$node["Loop Over Items"].context["noItemsLeft"]}}` expression นี้จะคืนค่าเป็น boolean ถ้ายังมีข้อมูลเหลือจะได้ `false` ถ้าหมดแล้วจะได้ `true`

### Get the current running index of the node

ถ้าอยากรู้ว่า node กำลังประมวลผลรอบที่เท่าไหร่ ใช้ expression นี้: `{{$node["Loop Over Items"].context["currentRunIndex"];}}`

