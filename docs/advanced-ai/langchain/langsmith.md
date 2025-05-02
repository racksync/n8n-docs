---
#https://www.notion.so/n8n/Frontmatter-432c2b8dff1f43d4b1c8d20075510fe4
contentType: howto
title: Use LangSmith with n8n
description: How to enable LangSmith for your self-hosted n8n instance.
---

# Use LangSmith with n8n

[LangSmith](https://www.langchain.com/langsmith){:target=_blank .external-link} คือแพลตฟอร์มสำหรับนักพัฒนาที่สร้างโดยทีม LangChain คุณสามารถเชื่อมต่อ n8n instance ของคุณกับ LangSmith เพื่อบันทึกและตรวจสอบ runs ใน n8n ได้ เหมือนกับที่ทำในแอป LangChain

/// info | Feature availability
เฉพาะ self-hosted n8n เท่านั้น
///

## Connect your n8n instance to LangSmith

1. [Log in to LangSmith](https://smith.langchain.com/settings){:target=_blank .external-link} แล้วรับ API key ของคุณ
1. ตั้งค่า LangSmith environment variables:

	| Variable | Value |
	| -------- | ----- |
	| LANGCHAIN_ENDPOINT | `"https://api.smith.langchain.com"` |
	| LANGCHAIN_TRACING_V2 | `true` |
	| LANGCHAIN_API_KEY | ตั้งค่านี้เป็น API key ของคุณ |

	ตั้งค่า variables เหล่านี้ให้ใช้งานได้ทั่วทั้ง environment ที่คุณ host n8n instance ของคุณ สามารถตั้งค่าแบบเดียวกับการ config อื่นๆ ทั่วไป พวกนี้ไม่ใช่ n8n environment variables ดังนั้นอย่าพยายามตั้งค่าผ่าน [n8n configuration file](/hosting/configuration/configuration-methods.md#set-environment-variables-using-a-file)

1. รีสตาร์ท n8n

สำหรับข้อมูลเกี่ยวกับการใช้ LangSmith ดูที่ [LangSmith's documentation](https://docs.smith.langchain.com/){:target=_blank .external-link}
