---
#https://www.notion.so/n8n/Frontmatter-432c2b8dff1f43d4b1c8d20075510fe4
title: MCP Server Trigger node documentation
description: เรียนรู้วิธีการใช้ MCP Server Trigger node ใน n8n อ่านเอกสารทางเทคนิคเพื่อรวม MCP Server Trigger node เข้ากับ workflows ของคุณ
contentType: [integration, reference]
---

# MCP Server Trigger node

ใช้ MCP Server Trigger node เพื่อให้นn8n ทำหน้าที่เป็น [Model Context Protocol (MCP)](https://modelcontextprotocol.io/introduction) server ทำให้ tools และ workflow ของ n8n สามารถถูกเรียกใช้งานโดย MCP clients ได้

///  note  | Credentials
ดูข้อมูลการตั้งค่า authentication สำหรับ node นี้ได้ที่ [ที่นี่](/integrations/builtin/credentials/httprequest.md)
///

## How the MCP Server Trigger node works

MCP Server Trigger node จะเป็นจุดเริ่มต้นให้ MCP clients เข้ามาใช้งาน n8n โดย node นี้จะเปิด URL ให้ MCP clients เข้ามาเรียกใช้งาน tools ของ n8n ได้

ต่างจาก [trigger nodes](/glossary.md#trigger-node-n8n) แบบปกติ ที่จะตอบสนอง event แล้วส่ง output ไปยัง [connected node](/workflows/components/connections.md) ตัวถัดไป MCP Server Trigger node จะเชื่อมต่อและ execute เฉพาะ [tool](/advanced-ai/examples/understand-tools.md) node เท่านั้น Clients สามารถ list tools ที่มีอยู่และเรียกใช้แต่ละ tool เพื่อให้ทำงานได้

คุณสามารถเปิด workflow ของ n8n ให้ client ใช้งานได้โดยเชื่อม workflow กับ [Custom n8n Workflow Tool](/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.toolworkflow.md) node

/// note | Server-Sent Events (SSE) support
MCP Server Trigger node รองรับ [Server-Sent Events (SSE)](https://modelcontextprotocol.io/docs/concepts/transports#server-sent-events-sse) ซึ่งเป็น transport แบบ long-lived บน HTTP สำหรับเชื่อมต่อระหว่าง client กับ server ตอนนี้ยังไม่รองรับ [standard input/output (stdio)](https://modelcontextprotocol.io/docs/concepts/transports#standard-input%2Foutput-stdio)
///

## Node parameters

ใช้ parameters เหล่านี้เพื่อปรับแต่ง node

### MCP URL

MCP Server Trigger node จะมี **MCP URLs** สองแบบ: test และ production n8n จะแสดง URL เหล่านี้ที่ด้านบนของ panel node

เลือก **Test URL** หรือ **Production URL** เพื่อสลับดู URL ที่ต้องการ

* **Test**: n8n จะ register test MCP URL เมื่อเลือก **Listen for Test Event** หรือ **Test workflow** ถ้า workflow ยังไม่ active เมื่อเรียก MCP URL นี้ n8n จะแสดงข้อมูลใน workflow
* **Production**: n8n จะ register production MCP URL เมื่อ activate workflow เมื่อใช้ production URL n8n จะไม่แสดงข้อมูลใน workflow แต่ยังสามารถดูข้อมูล execution ได้โดยไปที่ tab **Executions** แล้วเลือก execution ที่ต้องการดู

### Authentication

คุณสามารถบังคับให้ client ที่เชื่อมต่อกับ MCP URL ต้อง authenticate ได้ เลือกวิธี authentication ได้จาก:

- Bearer auth
- Header auth

ดูรายละเอียดการตั้งค่าแต่ละ credential ได้ที่ [HTTP request credentials](/integrations/builtin/credentials/httprequest.md)

### Path

โดย default field นี้จะมี path ของ MCP URL ที่สุ่มขึ้นมาเพื่อป้องกันชนกับ MCP Server Trigger node ตัวอื่น

คุณสามารถกำหนด path เองได้ รวมถึงใส่ route parameters เช่น ถ้าต้องการใช้ n8n สร้าง prototype API และอยากได้ endpoint URL ที่คงที่

**Path** field สามารถใช้รูปแบบเหล่านี้ได้:

- `/:variable`
- `/path/:variable`
- `/:variable/path`
- `/:variable1/path/:variable2`
- `/:variable1/:variable2`

## Templates and examples

<!-- see https://www.notion.so/n8n/Pull-in-templates-for-the-integrations-pages-37c716837b804d30a33b47475f6e3780 -->
[[ templatesWidget(page.title, 'mcp-server-trigger') ]]

### Integrating with Claude Desktop

คุณสามารถเชื่อมต่อ MCP Server Trigger node กับ [Claude Desktop](https://claude.ai/download) ได้โดยรัน gateway เพื่อ proxy ข้อความ SSE ไปยัง server ที่ใช้ stdio

ให้เพิ่ม config นี้ใน Claude Desktop:

```json
{
  "mcpServers": {
    "n8n": {
      "command": "npx",
      "args": [
        "-y",
        "supergateway",
        "--sse",
        "<MCP_URL>",
        "--header",
        "Authorization: Bearer <MCP_BEARER_TOKEN>"
      ]
    }
  }
}
```

อย่าลืมแทนที่ `<MCP_URL>` และ `<MCP_BEARER_TOKEN>` ด้วยค่าจาก MCP Server Trigger node ของคุณ

## Limitations

### Configuring the MCP Server Trigger node with webhook replicas

MCP Server Trigger node ใช้ Server-Sent Events (SSE) ซึ่งต้องให้ server instance เดียวกันรับ connection ตลอดเวลา ถ้าใช้ n8n แบบ [queue mode](/hosting/scaling/queue-mode.md) อาจมีปัญหาขึ้นอยู่กับ [webhook processor](/hosting/scaling/queue-mode.md#webhook-processors) ที่ตั้งไว้:

* ถ้าใช้ queue mode กับ **single webhook replica** MCP Server Trigger node จะทำงานปกติ
* ถ้าใช้ **multiple webhook replicas** ต้อง route request `/mcp*` ทั้งหมดไปที่ webhook replica เดียวเท่านั้น ให้สร้าง replica set แยกที่มี webhook container เดียวสำหรับ MCP แล้วปรับ ingress หรือ load balancer ให้ส่ง `/mcp*` ไปที่ instance นั้น

/// warning | Caution when running with multiple webhook replicas
ถ้าใช้ MCP Server Trigger node กับ multiple webhook replicas แล้วไม่ได้ route `/mcp*` ไปที่ webhook replica เดียว connection SSE จะหลุดหรือส่ง event ไม่เสถียร
///

## Related resources

n8n ยังมี [MCP Client Tool](/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.toolmcp.md) node สำหรับเชื่อมต่อ AI agent ของ n8n กับ external tools

ดูรายละเอียดเพิ่มเติมเกี่ยวกับ protocol, server, client ได้ที่ [MCP documentation](https://modelcontextprotocol.io/introduction) และ [MCP specification](https://modelcontextprotocol.io/specification/)

## Common issues

รวม error และปัญหาที่พบบ่อยของ MCP Server Trigger node พร้อมวิธีแก้ไขหรือแนวทางตรวจสอบ

### Running the MCP Server Trigger node with a reverse proxy

ถ้าใช้งาน n8n หลัง reverse proxy เช่น nginx อาจเจอปัญหาถ้า endpoint MCP ไม่ได้ตั้งค่าสำหรับ SSE

ต้องปิด proxy buffering สำหรับ endpoint นี้ และอาจต้องปิด gzip compression (n8n จัดการเอง), ปิด chunked transfer encoding และตั้ง `Connection` เป็นค่าว่างเพื่อไม่ให้ header นี้ถูก forward ไปยัง backend แนะนำให้ตั้งค่าเหล่านี้ใน location block ของ nginx สำหรับ MCP traffic เช่น:

```
location /mcp/ {
    proxy_http_version          1.1;
    proxy_buffering             off;
    gzip                        off;
    chunked_transfer_encoding   off;

    proxy_set_header            Connection '';

    # The rest of your proxy headers and settings
    # . . .
}
```
