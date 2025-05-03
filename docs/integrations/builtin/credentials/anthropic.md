---
#https://www.notion.so/n8n/Frontmatter-432c2b8dff1f43d4b1c8d20075510fe4
title: ข้อมูลรับรอง Anthropic
description: เอกสารข้อมูลรับรอง Anthropic ใช้ข้อมูลนี้เพื่อยืนยันตัวตน Anthropic ใน n8n
contentType: [integration, reference]
priority: medium
---

# Anthropic credentials

คุณสามารถใช้ credentials นี้เพื่อเชื่อมต่อกับ node เหล่านี้:

- [Anthropic Chat Model](/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.lmchatanthropic.md)

## Supported authentication methods

- API key

## Related resources

ดูข้อมูลเพิ่มเติมเกี่ยวกับบริการได้ที่ [Anthropic's documentation](https://docs.anthropic.com/claude/reference/getting-started-with-the-api){:target=_blank .external-link}

--8<-- "_snippets/integrations/builtin/cluster-nodes/langchain-overview-link.md"

## Using API key

ถ้าจะตั้งค่า credentials นี้ คุณต้องมีบัญชี [Anthropic Console account](https://console.anthropic.com){:target=_blank .external-link} ที่มีสิทธิ์เข้าถึง Claude

จากนั้น:

1. ใน Anthropic Console เปิด **Settings >** [**API Keys**](https://console.anthropic.com/settings/keys){:target=_blank .external-link}
2. เลือก **+ Create Key**
3. ตั้ง **Name** ให้กับ key ของคุณ เช่น `n8n-integration`
4. เลือก **Copy Key** เพื่อคัดลอก key
5. ป้อน key นี้เป็น **API Key** ใน n8n credential ของคุณ

ดูข้อมูลเพิ่มเติมได้ที่ [Intro to Claude](https://docs.anthropic.com/en/docs/intro-to-claude){:target=_blank .external-link} และ [Quickstart](https://docs.anthropic.com/en/docs/quickstart){:target=_blank .external-link} ของ Anthropic
