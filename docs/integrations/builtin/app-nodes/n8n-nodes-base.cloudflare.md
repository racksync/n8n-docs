---
#https://www.notion.so/n8n/Frontmatter-432c2b8dff1f43d4b1c8d20075510fe4
title: Cloudflare node documentation
description: Learn how to use the Cloudflare node in n8n. Follow technical documentation to integrate Cloudflare node into your workflows.
contentType: [integration, reference]
---

# Cloudflare node

ใช้ Cloudflare node เพื่อทำงานอัตโนมัติใน Cloudflare และ integrate Cloudflare กับแอปพลิเคชันอื่นๆ n8n มีการรองรับในตัวสำหรับฟีเจอร์ต่างๆ ของ Cloudflare รวมถึงการลบ, ดึง, และอัปโหลด zone certificates

ในหน้านี้ คุณจะพบรายการ operations ที่ Cloudflare node รองรับ และลิงก์ไปยังแหล่งข้อมูลเพิ่มเติม

/// note | Credentials
อ้างอิง [Cloudflare credentials](/integrations/builtin/credentials/cloudflare.md) สำหรับคำแนะนำในการตั้งค่า authentication
///

## Operations

* Zone Certificate
	* Delete
	* Get
	* Get Many
	* Upload

## Templates and examples

<!-- see https://www.notion.so/n8n/Pull-in-templates-for-the-integrations-pages-37c716837b804d30a33b47475f6e3780 -->
[[ templatesWidget(page.title, 'cloudflare') ]]

## Related resources

อ้างอิง [Cloudflare's API documentation on zone-level authentication](https://api.cloudflare.com/#zone-level-authenticated-origin-pulls-properties){:target=_blank .external-link} สำหรับข้อมูลเพิ่มเติมเกี่ยวกับ service นี้

--8<-- "_snippets/integrations/builtin/app-nodes/operation-not-supported.md"

