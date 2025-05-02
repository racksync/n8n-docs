---
#https://www.notion.so/n8n/Frontmatter-432c2b8dff1f43d4b1c8d20075510fe4
title: GitHub Document Loader node documentation
description: Learn how to use the GitHub Document Loader node in n8n. Follow technical documentation to integrate GitHub Document Loader node into your workflows.
contentType: [integration, reference]
---

# GitHub Document Loader node

ใช้ GitHub Document Loader node เพื่อโหลดข้อมูลจาก GitHub repository สำหรับ [vector stores](/glossary.md#ai-vector-store) หรือการสรุปผล (summarization)

ในหน้านี้ คุณจะพบพารามิเตอร์ของโหนดสำหรับ GitHub Document Loader node และลิงก์ไปยังแหล่งข้อมูลเพิ่มเติม

/// note | Credentials
คุณสามารถดูข้อมูลการยืนยันตัวตนสำหรับโหนดนี้ได้ [ที่นี่](/integrations/builtin/credentials/github.md) โหนดนี้ไม่รองรับ OAuth สำหรับการยืนยันตัวตน
///

--8<-- "_snippets/integrations/builtin/cluster-nodes/sub-node-expression-resolution.md"

## Node parameters

* **Repository Link**: ป้อน URL ของ GitHub repository ของคุณ
* **Branch**: ป้อนชื่อ branch ที่จะใช้

## Node options

* **Recursive**: เลือกว่าจะรวมโฟลเดอร์ย่อยและไฟล์ (เปิด) หรือไม่ (ปิด)
* **Ignore Paths**: ป้อนไดเรกทอรีที่จะละเว้น

## Templates and examples

<!-- see https://www.notion.so/n8n/Pull-in-templates-for-the-integrations-pages-37c716837b804d30a33b47475f6e3780 -->
[[ templatesWidget(page.title, 'github-document-loader') ]]

## Related resources

--8<-- "_snippets/integrations/builtin/cluster-nodes/langchain-doc-loaders-link.md"

--8<-- "_snippets/integrations/builtin/cluster-nodes/langchain-overview-link.md"
--8<-- "_glossary/ai-glossary.md"
