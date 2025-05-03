---
#https://www.notion.so/n8n/Frontmatter-432c2b8dff1f43d4b1c8d20075510fe4
title: เอกสารคู่มือ Facebook Graph API node
description: เรียนรู้วิธีใช้ Facebook Graph API node ใน n8n และดูเอกสารทางเทคนิคเพื่อเชื่อมต่อ Facebook Graph API node เข้ากับ workflows ของคุณ
contentType: [integration, reference]
priority: medium
---

# Facebook Graph API node

ใช้ Facebook Graph API node เพื่อทำงานอัตโนมัติใน Facebook Graph API และเชื่อมต่อ Facebook Graph API กับแอปอื่นๆ ได้เลย n8n รองรับฟีเจอร์ของ Facebook Graph API หลายอย่าง เช่น การใช้ queries GET POST DELETE สำหรับ parameters หลายอย่าง เช่น host URL, request methods และอื่นๆ อีกมากมาย

ในหน้านี้จะมีรายการ operations ที่ Facebook Graph API node รองรับ พร้อมลิงก์ไปยังแหล่งข้อมูลอื่นๆ

/// note | Credentials
โปรดดู [Facebook Graph API credentials](/integrations/builtin/credentials/facebookgraph.md) สำหรับคำแนะนำการตั้งค่าการยืนยันตัวตน
///

## Operations

* **Default**
    * GET
    * POST
    * DELETE 
* **Video Uploads**
    * GET
    * POST
    * DELETE 


### Parameters

--8<-- "_snippets/integrations/builtin/app-nodes/ai-tools.md"

* **Host URL**: Host URL สำหรับ request มีตัวเลือกดังนี้:
    * **Default**: Requests จะถูกส่งไปยัง `graph.facebook.com` host URL ใช้สำหรับ requests ส่วนใหญ่
    * **Video**: Requests จะถูกส่งไปยัง `graph-video.facebook.com` host URL ใช้สำหรับ video upload requests เท่านั้น
* **HTTP Request Method**: Method ที่จะใช้สำหรับ request นี้ จากตัวเลือกต่อไปนี้:
    * **GET**
    * **POST**
    * **DELETE**
* **Graph API Version**: เวอร์ชันของ [Facebook Graph API](https://developers.facebook.com/docs/graph-api/changelog) ที่จะใช้สำหรับ request นี้
* **Node**: Node ที่จะดำเนินการ เช่น `/<page-id>/feed` อ่านเพิ่มเติมได้ใน [official Facebook Developer documentation](https://developers.facebook.com/docs/graph-api/using-graph-api)
* **Edge**: Edge ของ node ที่จะดำเนินการ Edges แทน collections ของ objects ที่แนบอยู่กับ node
* **Ignore SSL Issues**: สลับเพื่อยังคงดาวน์โหลด response แม้ว่าจะไม่สามารถตรวจสอบ SSL certificate ได้
* **Send Binary File**: ใช้ได้สำหรับ `POST` operations หากเปิดใช้งาน ข้อมูล binary จะถูกส่งเป็น body ต้องตั้งค่าต่อไปนี้:
    * **Input Binary Field**: ชื่อของ binary property ที่มีข้อมูลสำหรับ file ที่จะอัปโหลด

## Templates and examples

<!-- see https://www.notion.so/n8n/Pull-in-templates-for-the-integrations-pages-37c716837b804d30a33b47475f6e3780 -->
[[ templatesWidget(page.title, 'facebook-graph-api') ]]
