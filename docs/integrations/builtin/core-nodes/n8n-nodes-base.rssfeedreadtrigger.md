---
#https://www.notion.so/n8n/Frontmatter-432c2b8dff1f43d4b1c8d20075510fe4
title: RSS Feed Trigger node documentation
description: Learn how to use the RSS Feed Trigger node in n8n. Follow technical documentation to integrate RSS Feed Trigger node into your workflows.
contentType: [integration, reference]
priority: medium
---

# RSS Feed Trigger node

RSS Feed Trigger node ช่วยให้ workflow ของ n8n เริ่มทำงานเมื่อมี item ใหม่ใน RSS feed ถูกเผยแพร่

ในหน้านี้ คุณจะพบรายการ operation ที่ RSS Feed Trigger node รองรับ และลิงก์ไปยัง resource อื่น ๆ

## Node parameters

* **Poll Times**: เลือก poll **Mode** เพื่อกำหนดความถี่ในการตรวจสอบ feed ว่ามีข้อมูลใหม่หรือไม่ การเลือก **Mode** จะเพิ่มหรือลด field ที่เกี่ยวข้อง ดูรายละเอียดแต่ละ mode ได้ในหัวข้อด้านล่าง
* **Feed URL**: กรอก URL ของ RSS feed ที่ต้องการตรวจสอบ

--8<-- "_snippets/integrations/builtin/poll-modes.md"

## Templates and examples

<!-- see https://www.notion.so/n8n/Pull-in-templates-for-the-integrations-pages-37c716837b804d30a33b47475f6e3780 -->
[[ templatesWidget(page.title, 'rss-feed-trigger') ]]

## Related resources

n8n มี app node สำหรับ RSS Feeds ด้วย ดูเอกสาร node ได้ที่ [here](/integrations/builtin/core-nodes/n8n-nodes-base.rssfeedread.md)
