---
#https://www.notion.so/n8n/Frontmatter-432c2b8dff1f43d4b1c8d20075510fe4
title: Workflow Retriever node documentation
description: Learn how to use the Workflow Retriever node in n8n. Follow technical documentation to integrate Workflow Retriever node into your workflows.
contentType: [integration, reference]
priority: medium
---

# Workflow Retriever node

ใช้ Workflow Retriever node เพื่อดึงข้อมูลจาก workflow ของ n8n ไปใช้กับ Retrieval QA Chain หรือ Retriever node อื่นๆ

ในหน้านี้จะมี parameter ของ node Workflow Retriever และลิงก์ resource อื่นๆ ที่เกี่ยวข้อง

--8<-- "_snippets/integrations/builtin/cluster-nodes/sub-node-expression-resolution.md"

## Node parameters

### Source

บอก n8n ว่าจะเรียก workflow ไหน โดยเลือกได้ระหว่าง:

* **Database** แล้วใส่ workflow ID
* **Parameter** แล้วใส่ [workflow JSON](/workflows/export-import.md) ทั้งหมด

### Workflow values

--8<-- "_snippets/integrations/builtin/cluster-nodes/langchain-sub-nodes/workflow-values.md"

## Templates and examples

<!-- see https://www.notion.so/n8n/Pull-in-templates-for-the-integrations-pages-37c716837b804d30a33b47475f6e3780 -->
[[ templatesWidget(page.title, 'workflow-retriever') ]]

## Related resources

ดูข้อมูลเพิ่มเติมได้ที่ [LangChain's general retriever documentation](https://js.langchain.com/docs/concepts/retrievers/){:target=_blank .external-link}

--8<-- "_snippets/integrations/builtin/cluster-nodes/langchain-overview-link.md"
--8<-- "_glossary/ai-glossary.md"
