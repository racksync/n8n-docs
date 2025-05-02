---
#https://www.notion.so/n8n/Frontmatter-432c2b8dff1f43d4b1c8d20075510fe4
title: Self-hosted AI Starter Kit
description: ใช้ Self-hosted AI Starter Kit ที่คัดสรรโดย n8n เพื่อเริ่มต้นสร้าง workflow AI แบบ self-hosted ได้อย่างรวดเร็ว
contentType: howto
---

# Self-hosted AI Starter Kit

Self-hosted AI Starter Kit คือ docker compose template ที่รวมเครื่องมือ Local AI และ Low Code development environment ไว้ให้พร้อมใช้งาน

คัดสรรโดย [n8n](https://github.com/n8n-io) รวม self-hosted n8n platform กับ AI products และ components ที่ใช้งานร่วมกันได้ ให้คุณเริ่มสร้าง workflow AI แบบ self-hosted ได้ทันที

## What’s included

✅ [**Self-hosted n8n**](/hosting/index.md): Low-code platform ที่มี integration กว่า 400 ตัว และ component AI ขั้นสูง

✅ [**Ollama**](https://ollama.com/){:target=_blank .external-link}: LLM platform ข้ามแพลตฟอร์มสำหรับติดตั้งและรัน LLMs ล่าสุดแบบ local

✅ [**Qdrant**](https://qdrant.tech/){:target=_blank .external-link}: vector store แบบ open-source ประสิทธิภาพสูง พร้อม API ครบถ้วน

✅ [**PostgreSQL**](https://www.postgresql.org/){:target=_blank .external-link}: database ยอดนิยมสำหรับงาน Data Engineering จัดการข้อมูลขนาดใหญ่ได้ดี

## What you can build

⭐️ [AI Agents](/glossary.md#ai-agent){ data-preview} ที่ช่วยนัดหมาย

⭐️ สรุปเนื้อหา PDF ของบริษัทโดยไม่ต้องส่งข้อมูลออกนอก

⭐️ Slackbot อัจฉริยะสำหรับสื่อสารในบริษัทและ IT-ops

⭐️ วิเคราะห์เอกสารการเงินแบบ private และประหยัดค่าใช้จ่าย

## Get the kit

<!-- vale off -->
ไปที่ [the GitHub repository](https://github.com/n8n-io/self-hosted-ai-starter-kit){:target=_blank .external-link} เพื่อ clone repo และเริ่มต้นใช้งานได้เลย!
<!-- vale on -->

/// note | For testing only
n8n ออกแบบ kit นี้เพื่อให้คุณเริ่มต้นสร้าง workflow AI แบบ self-hosted ได้ง่ายๆ ยังไม่เหมาะกับ production เต็มรูปแบบ แต่รวม component ที่ทำงานร่วมกันได้ดีสำหรับ proof-of-concept สามารถปรับแต่งได้ตามต้องการ อย่าลืม secure และ harden ก่อนนำไปใช้จริง
///
