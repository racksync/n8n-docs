---
#https://www.notion.so/n8n/Frontmatter-432c2b8dff1f43d4b1c8d20075510fe4
title: AWS Bedrock Chat Model node documentation
description: Learn how to use the AWS Bedrock Chat Model node in n8n. Follow technical documentation to integrate AWS Bedrock Chat Model node into your workflows.
contentType: [integration, reference]
---

# AWS Bedrock Chat Model node

AWS Bedrock Chat Model node ช่วยให้คุณใช้งาน LLM models ผ่านแพลตฟอร์ม AWS Bedrock ได้ง่ายๆ

ในหน้านี้จะมีพารามิเตอร์ของ node AWS Bedrock Chat Model และลิงก์ไปยังแหล่งข้อมูลเพิ่มเติม

/// note | Credentials
คุณสามารถดูข้อมูลการเชื่อมต่อสำหรับ node นี้ได้ [ที่นี่](/integrations/builtin/credentials/aws.md)
///

--8<-- "_snippets/integrations/builtin/cluster-nodes/sub-node-expression-resolution.md"
	
## Node parameters

* **Model**: เลือกโมเดลที่ต้องการให้สร้างข้อความตอบกลับ

ดูรายละเอียดโมเดลที่รองรับได้ที่ [Amazon Bedrock model documentation](https://docs.aws.amazon.com/bedrock/latest/userguide/models-supported.html){:target=_blank .external-link}

## Node options

* **Maximum Number of Tokens**: กำหนดจำนวน tokens สูงสุดที่ใช้ ซึ่งจะเป็นการกำหนดความยาวของข้อความที่โมเดลจะตอบกลับ
* **Sampling Temperature**: ปรับความสุ่มของการสร้างข้อความ ค่า temperature สูงจะทำให้โมเดลตอบหลากหลายมากขึ้น แต่ก็เสี่ยงต่อการตอบแบบหลุดประเด็น

## Templates and examples

[[ templatesWidget(page.title, 'aws-bedrock-chat-model') ]]

## Related resources

ดูข้อมูลเพิ่มเติมได้ที่ [LangChains's AWS Bedrock Chat Model documentation](https://js.langchain.com/docs/integrations/chat/bedrock/){:target=_blank .external-link}

--8<-- "_snippets/integrations/builtin/cluster-nodes/langchain-overview-link.md"
--8<-- "_glossary/ai-glossary.md"
