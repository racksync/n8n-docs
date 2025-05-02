---
#https://www.notion.so/n8n/Frontmatter-432c2b8dff1f43d4b1c8d20075510fe4
title: Google Business Profile node documentation
description: Learn how to use the Google Business Profile node in n8n. Follow technical documentation to integrate Google Business Profile node into your workflows.
contentType: [integration, reference]
---

# Google Business Profile node

ใช้ Google Business Profile node เพื่อทำงานอัตโนมัติใน Google Business Profile และเชื่อมต่อ Google Business Profile กับแอปอื่นๆ ได้เลย n8n รองรับฟีเจอร์ของ Google Business Profile หลายอย่าง เช่น การสร้าง อัปเดต และลบ posts และ reviews

ในหน้านี้จะมีรายการ operations ที่ Google Business Profile node รองรับ พร้อมลิงก์ไปยังแหล่งข้อมูลอื่นๆ

///  note  | Credentials
คุณสามารถค้นหาข้อมูลการยืนยันตัวตนสำหรับ node นี้ได้ [ที่นี่](/integrations/builtin/credentials/google/index.md)
///


## Operations

* Post
	* Create
	* Delete
	* Get
	* Get Many
	* Update
* Review
	* Delete Reply
	* Get
	* Get Many
	* Reply

## Templates and examples

<!-- see https://www.notion.so/n8n/Pull-in-templates-for-the-integrations-pages-37c716837b804d30a33b47475f6e3780 -->
[[ templatesWidget(page.title, 'google-business-profile') ]]

## Related resources

n8n มี trigger node สำหรับ Google Business Profile คุณสามารถค้นหาเอกสาร trigger node ได้ [ที่นี่](/integrations/builtin/trigger-nodes/n8n-nodes-base.googlebusinessprofiletrigger.md)

โปรดดู [Google Business Profile's documentation](https://developers.google.com/my-business/reference/rest){:target=_blank .external-link} สำหรับข้อมูลเพิ่มเติมเกี่ยวกับบริการนี้

--8<-- "_snippets/integrations/builtin/app-nodes/operation-not-supported.md"
