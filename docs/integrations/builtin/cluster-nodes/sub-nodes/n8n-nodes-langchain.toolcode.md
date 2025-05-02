---
#https://www.notion.so/n8n/Frontmatter-432c2b8dff1f43d4b1c8d20075510fe4
title: Custom Code Tool node documentation
description: Learn how to use the Custom Code Tool node in n8n. Follow technical documentation to integrate Custom Code Tool node into your workflows.
contentType: [integration, reference]
priority: high
---

# Custom Code Tool node

ใช้ Custom Code Tool node เพื่อเขียนโค้ดที่ [agent](/glossary.md#ai-agent) สามารถรันได้

ในหน้านี้จะมี parameter ของ node Custom Code Tool และลิงก์ไปยัง resource อื่นๆ ที่เกี่ยวข้อง

--8<-- "_snippets/integrations/builtin/cluster-nodes/sub-node-expression-resolution.md"

## Node parameters

### Description

ใส่คำอธิบายสำหรับ custom code ของคุณ ตรงนี้จะช่วยบอก agent ว่าควรใช้ tool นี้เมื่อไหร่ เช่น

> Call this tool to get a random color. The input should be a string with comma separated names of colors to exclude.

### Language

เลือกได้ว่าจะใช้ JavaScript หรือ Python

### JavaScript / Python box

เขียนโค้ดของคุณตรงนี้

คุณสามารถเข้าถึง input ของ tool ได้ด้วย `query` เช่น ถ้าต้องการรับ string แล้วแปลงเป็นตัวพิมพ์เล็กทั้งหมด:

```js
let myString = query;
return myString.toLowerCase();
```

## Templates and examples

<!-- see https://www.notion.so/n8n/Pull-in-templates-for-the-integrations-pages-37c716837b804d30a33b47475f6e3780 -->
[[ templatesWidget(page.title, 'code-tool') ]]

## Related resources

--8<-- "_snippets/integrations/builtin/cluster-nodes/tools-link.md"

--8<-- "_snippets/integrations/builtin/cluster-nodes/langchain-overview-link.md"

--8<-- "_glossary/ai-glossary.md"
