---
#https://www.notion.so/n8n/Frontmatter-432c2b8dff1f43d4b1c8d20075510fe4
title: เอกสาร Supabase node
description: เรียนรู้วิธีใช้ Supabase node ใน n8n ดูเอกสารทางเทคนิคเพื่อเชื่อม Supabase node เข้ากับ workflow ของคุณ
contentType: [integration, reference]
priority: high
---

# Supabase node

Use the Supabase node to automate work in Supabase, and integrate Supabase with other applications. n8n has built-in support for a wide range of Supabase features, including creating, deleting, and getting rows. 
{ 
ใช้ Supabase node เพื่อทำงานอัตโนมัติกับ Supabase และเชื่อม Supabase เข้ากับแอปอื่นๆ n8n รองรับฟีเจอร์ของ Supabase หลากหลาย ตั้งแต่การสร้าง ลบ และดึงข้อมูลแถว 
}

On this page, you'll find a list of operations the Supabase node supports and links to more resources.
{ 
ในหน้านี้จะมีรายการของ Operations ที่ Supabase node รองรับ พร้อมลิงก์ไปยัง resources เพิ่มเติม 
}

/// note | Credentials
Refer to [Supabase credentials](/integrations/builtin/credentials/supabase.md) for guidance on setting up authentication. 
{ 
ดูที่ [Supabase credentials](/integrations/builtin/credentials/supabase.md) เพื่อดูแนวทางการตั้งค่า authentication 
}

///

--8<-- "_snippets/integrations/builtin/app-nodes/ai-tools.md"

## Operations

* Row
    * Create a new row
    * Delete a row
    * Get a row
    * Get all rows
    * Update a row

## Templates and examples

<!-- see https://www.notion.so/n8n/Pull-in-templates-for-the-integrations-pages-37c716837b804d30a33b47475f6e3780 -->
[[ templatesWidget(page.title, 'supabase') ]]

--8<-- "_snippets/integrations/builtin/app-nodes/operation-not-supported.md"

## Common issues

For common errors or issues and suggested resolution steps, refer to [Common issues](/integrations/builtin/app-nodes/n8n-nodes-base.supabase/common-issues.md).
{ 
สำหรับข้อผิดพลาดหรือปัญหาที่พบบ่อยพร้อมแนวทางแก้ไข ให้ดูที่ [Common issues](/integrations/builtin/app-nodes/n8n-nodes-base.supabase/common-issues.md) 
}
