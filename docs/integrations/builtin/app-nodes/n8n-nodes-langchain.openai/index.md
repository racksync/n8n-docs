---
#https://www.notion.so/n8n/Frontmatter-432c2b8dff1f43d4b1c8d20075510fe4
title: OpenAI node
description: เรียนรู้วิธีใช้ OpenAI node ใน n8n เพื่อเชื่อมต่อกับเวิร์กโฟลว์ของคุณ.
contentType: [integration, reference]
priority: critical
search:
    boost: 3
---

# OpenAI node

ใช้ OpenAI node เพื่อทำงานอัตโนมัติใน OpenAI และเชื่อมต่อกับแอปพลิเคชันอื่นๆ. ในหน้านี้คุณจะพบรายการ operation ที่ OpenAI node รองรับและลิงก์ไปยังแหล่งข้อมูลเพิ่มเติม.

/// note | OpenAI Assistant node
OpenAI node แทนที่ OpenAI assistant node ตั้งแต่เวอร์ชัน 1.29.0 เป็นต้นไป.
///

/// note | Credentials
ดู [OpenAI credentials](/integrations/builtin/credentials/openai.md) สำหรับคำแนะนำการตั้งค่า authentication.
///

## Operations

- **Assistant** 
	- [**Create an Assistant**](/integrations/builtin/app-nodes/n8n-nodes-langchain.openai/assistant-operations.md#create-an-assistant)
	- [**Delete an Assistant**](/integrations/builtin/app-nodes/n8n-nodes-langchain.openai/assistant-operations.md#delete-an-assistant)
	- [**List Assistants**](/integrations/builtin/app-nodes/n8n-nodes-langchain.openai/assistant-operations.md#list-assistants)
	- [**Message an Assistant**](/integrations/builtin/app-nodes/n8n-nodes-langchain.openai/assistant-operations.md#message-an-assistant)
	- [**Update an Assistant**](/integrations/builtin/app-nodes/n8n-nodes-langchain.openai/assistant-operations.md#update-an-assistant)
- **Text**
	- [**Message a Model**](/integrations/builtin/app-nodes/n8n-nodes-langchain.openai/text-operations.md#message-a-model)
	- [**Classify Text for Violations**](/integrations/builtin/app-nodes/n8n-nodes-langchain.openai/text-operations.md#classify-text-for-violations)
- **Image**
	- [**Analyze Image**](/integrations/builtin/app-nodes/n8n-nodes-langchain.openai/image-operations.md#analyze-image)
	- [**Generate an Image**](/integrations/builtin/app-nodes/n8n-nodes-langchain.openai/image-operations.md#generate-an-image)
- **Audio**
	- [**Generate Audio**](/integrations/builtin/app-nodes/n8n-nodes-langchain.openai/audio-operations.md#generate-audio)
	- [**Transcribe a Recording**](/integrations/builtin/app-nodes/n8n-nodes-langchain.openai/audio-operations.md#transcribe-a-recording)
	- [**Translate a Recording**](/integrations/builtin/app-nodes/n8n-nodes-langchain.openai/audio-operations.md#translate-a-recording)
- **File**
	- [**Delete a File**](/integrations/builtin/app-nodes/n8n-nodes-langchain.openai/file-operations.md#delete-a-file)
	- [**List Files**](/integrations/builtin/app-nodes/n8n-nodes-langchain.openai/file-operations.md#list-files)
	- [**Upload a File**](/integrations/builtin/app-nodes/n8n-nodes-langchain.openai/file-operations.md#upload-a-file)

## Templates and examples

<!-- see https://www.notion.so/n8n/Pull-in-templates-for-the-integrations-pages-37c716837b804d30a33b47475f6e3780 -->
[[ templatesWidget(page.title, 'openai') ]]

## Related resources

ดู [OpenAI's documentation](https://beta.openai.com/docs/introduction){:target=_blank .external-link} สำหรับข้อมูลเพิ่มเติมเกี่ยวกับบริการ.

ดู [OpenAI's assistants documentation](https://platform.openai.com/docs/assistants/how-it-works/objects){:target=_blank .external-link} สำหรับข้อมูลเพิ่มเติมเกี่ยวกับการทำงานของ assistants.

สำหรับความช่วยเหลือเกี่ยวกับ rate limits, ดู [Handling rate limits](/integrations/builtin/rate-limits.md).

--8<-- "_snippets/integrations/builtin/app-nodes/operation-not-supported.md"

## Using tools with OpenAI assistants

บาง operation อนุญาตให้เชื่อมต่อ tools. [Tools](https://docs.n8n.io/advanced-ai/examples/understand-tools/) ทำหน้าที่เหมือน addons ที่ AI ของคุณใช้เพื่อเข้าถึง context หรือแหล่งข้อมูลเพิ่มเติม.

เลือก connector **Tools** เพื่อเรียกดูและเพิ่มเครื่องมือที่มีอยู่.

เมื่อมีการเพิ่มการเชื่อมต่อเครื่องมือ OpenAI node จะกลายเป็น [root node](/glossary.md#root-node-n8n) ซึ่งสามารถสร้าง [cluster node](/glossary.md#cluster-node-n8n) กับ [sub-nodes](/glossary.md#sub-node-n8n) ได้. ดู [Node types](/integrations/builtin/node-types.md#cluster-nodes) สำหรับข้อมูลเพิ่มเติมเกี่ยวกับ cluster nodes และ root nodes.

### Operations that support tool connectors

- **Assistant**
	- [**Message an Assistant**](/integrations/builtin/app-nodes/n8n-nodes-langchain.openai/assistant-operations.md#message-an-assistant)
- **Text**
	- [**Message a Model**](/integrations/builtin/app-nodes/n8n-nodes-langchain.openai/text-operations.md#message-a-model)

## Common issues

สำหรับคำถามหรือปัญหาทั่วไปและแนวทางแก้ไข ให้ดู [Common issues](/integrations/builtin/app-nodes/n8n-nodes-langchain.openai/common-issues.md).
