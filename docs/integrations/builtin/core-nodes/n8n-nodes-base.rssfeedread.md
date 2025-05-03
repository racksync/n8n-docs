---
#https://www.notion.so/n8n/Frontmatter-432c2b8dff1f43d4b1c8d20075510fe4
title: RSS Read
description: เอกสารสำหรับ RSS Read node ใน n8n แพลตฟอร์ม workflow automation พร้อมคำแนะนำการใช้งานและตัวอย่าง
contentType: [integration, reference]
priority: medium
---

# RSS Read

ใช้ RSS Read node เพื่ออ่านข้อมูลจาก RSS feed ที่เผยแพร่บนอินเทอร์เน็ต

## Node parameters

- **URL**: กรอก URL ของ RSS publication ที่ต้องการอ่าน

## Node options

* **Ignore SSL Issues**: เลือกว่าจะให้ n8n ข้ามการตรวจสอบ SSL/TLS (เปิด) หรือไม่ (ปิด)

## Templates and examples

<!-- see https://www.notion.so/n8n/Pull-in-templates-for-the-integrations-pages-37c716837b804d30a33b47475f6e3780 -->
[[ templatesWidget(page.title, 'rss-read') ]]

## Related resources

n8n มี trigger node สำหรับ RSS Read ด้วย ดูเอกสาร trigger node ได้ที่ [here](/integrations/builtin/core-nodes/n8n-nodes-base.rssfeedreadtrigger.md)

