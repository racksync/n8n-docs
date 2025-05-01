---
#https://www.notion.so/n8n/Frontmatter-432c2b8dff1f43d4b1c8d20075510fe4
title: Ollama credentials
description: Documentation for the Ollama credentials. Use these credentials to authenticate Ollama in n8n, a workflow automation platform.
contentType: [integration, reference]
priority: high
---

# Ollama credentials

คุณสามารถใช้ credentials เหล่านี้เพื่อยืนยันตัวตนใน nodes ต่อไปนี้:

* [Ollama](/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.lmollama/index.md)
* [Chat Ollama](/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.lmchatollama/index.md)
* [Embeddings Ollama](/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.embeddingsollama.md)

## Prerequisites

สร้างและรัน instance ของ [Ollama](https://ollama.com/){:target=_blank .external-link} ด้วยผู้ใช้หนึ่งคน อ้างอิง Ollama [Quick Start](https://github.com/ollama/ollama/blob/main/README.md#quickstart){:target=_blank .external-link} สำหรับข้อมูลเพิ่มเติม

## Supported authentication methods

- Instance URL

## Related resources

อ้างอิง [Ollama's API documentation](https://github.com/ollama/ollama/blob/main/docs/api.md){:target=_blank .external-link} สำหรับข้อมูลเพิ่มเติมเกี่ยวกับบริการนี้

--8<-- "_snippets/integrations/builtin/cluster-nodes/langchain-overview-link.md"

## Using instance URL

ในการกำหนดค่า credential นี้ คุณจะต้องมี:

- **Base URL** ของ instance Ollama ของคุณ

**Base URL** เริ่มต้นคือ `http://localhost:11434` แต่ถ้าคุณได้ตั้งค่าตัวแปรสภาพแวดล้อม `OLLAMA_HOST` ให้ป้อนค่านั้น หากคุณมีปัญหาในการเชื่อมต่อกับเซิร์ฟเวอร์ n8n ในเครื่อง ให้ลองใช้ `127.0.0.1` แทน `localhost`

อ้างอิง [How do I configure Ollama server?](https://github.com/ollama/ollama/blob/main/docs/faq.md#how-do-i-configure-ollama-server){:target=_blank .external-link} สำหรับข้อมูลเพิ่มเติม

### Ollama and self-hosted n8n

หากคุณ self-host n8n บนเครื่องเดียวกับ Ollama คุณอาจประสบปัญหาหากทำงานใน containers ที่แตกต่างกัน

สำหรับการตั้งค่านี้ ให้เปิด port เฉพาะสำหรับ n8n เพื่อสื่อสารกับ Ollama โดยตั้งค่าตัวแปร `OLLAMA_ORIGINS` หรือปรับ `OLLAMA_HOST` เป็นที่อยู่ที่ container อื่นสามารถเข้าถึงได้

อ้างอิง Ollama's [How can I allow additional web origins to access Ollama?](https://github.com/ollama/ollama/blob/main/docs/faq.md#how-can-i-allow-additional-web-origins-to-access-ollama){:target=_blank .external-link} สำหรับข้อมูลเพิ่มเติม
