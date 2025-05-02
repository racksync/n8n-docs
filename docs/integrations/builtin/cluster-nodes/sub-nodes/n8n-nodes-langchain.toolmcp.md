---
#https://www.notion.so/n8n/Frontmatter-432c2b8dff1f43d4b1c8d20075510fe4
title: MCP Client Tool node documentation
description: เรียนรู้วิธีการใช้ MCP Client Tool node ใน n8n พร้อมคำแนะนำทางเทคนิคสำหรับการรวม MCP Client Tool node เข้ากับ workflow ของคุณ
contentType: [integration, reference]
---

# MCP Client Tool node

MCP Client Tool node คือ [Model Context Protocol (MCP)](https://modelcontextprotocol.io/introduction) client ที่ให้คุณใช้ tool ที่เปิดจาก MCP server ภายนอกได้ คุณสามารถเชื่อมต่อ MCP Client Tool node กับ model ของคุณเพื่อเรียกใช้ external tool ผ่าน n8n agent

///  note  | Credentials
MCP Client Tool node รองรับทั้ง [Bearer](/integrations/builtin/credentials/httprequest.md#using-bearer-auth) และ generic [header](/integrations/builtin/credentials/httprequest.md#using-header-auth) authentication
///

## Node parameters

ตั้งค่า node ด้วย parameter เหล่านี้

* **SSE Endpoint**: กรอก endpoint ของ MCP server ที่ต้องการเชื่อมต่อ
* **Authentication**: เลือกวิธี authentication สำหรับเชื่อมต่อ MCP server รองรับ [bearer](/integrations/builtin/credentials/httprequest.md#using-bearer-auth) และ generic [header](/integrations/builtin/credentials/httprequest.md#using-header-auth) หรือเลือก **None** ถ้าต้องการเชื่อมต่อแบบไม่ต้อง auth
* **Tools to Include**: เลือก tool ที่ต้องการเปิดให้ AI Agent ใช้งาน:
	* **All**: เปิดทุก tool ที่ MCP server มี
	* **Selected**: จะมี parameter **Tools to Include** ให้เลือก tool ที่ต้องการเปิดให้ AI Agent
	* **All Except**: จะมี parameter **Tools to Exclude** ให้เลือก tool ที่ไม่ต้องการให้ AI Agent ใช้ AI Agent จะเข้าถึง tool อื่นๆ ที่ไม่ได้เลือกเท่านั้น

## Templates and examples

<!-- see https://www.notion.so/n8n/Pull-in-templates-for-the-integrations-pages-37c716837b804d30a33b47475f6e3780 -->
[[ templatesWidget(page.title, 'mcp-client-tool') ]]

## Related resources

n8n ยังมี [MCP Server Trigger](/integrations/builtin/core-nodes/n8n-nodes-langchain.mcptrigger.md) node สำหรับเปิด tool ของ n8n ให้ external AI Agent ใช้งานด้วย

ดูรายละเอียด protocol, server, client เพิ่มเติมได้ที่ [MCP documentation](https://modelcontextprotocol.io/introduction) และ [MCP specification](https://modelcontextprotocol.io/specification/)

--8<-- "_snippets/integrations/builtin/cluster-nodes/tools-link.md"

--8<-- "_snippets/integrations/builtin/cluster-nodes/langchain-overview-link.md"
--8<-- "_glossary/ai-glossary.md"
