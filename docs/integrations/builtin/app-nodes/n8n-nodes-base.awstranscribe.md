---
#https://www.notion.so/n8n/Frontmatter-432c2b8dff1f43d4b1c8d20075510fe4
title: เอกสารคู่มือ AWS Transcribe node
description: เรียนรู้วิธีใช้ AWS Transcribe node ใน n8n และดูเอกสารทางเทคนิคเพื่อเชื่อมต่อ AWS Transcribe node เข้ากับ workflows ของคุณ
contentType: [integration, reference]
---

# AWS Transcribe node

ใช้ AWS Transcribe node เพื่อทำงานอัตโนมัติใน AWS Transcribe และผสานรวม AWS Transcribe กับแอปพลิเคชันอื่นๆ n8n มีการรองรับฟีเจอร์หลากหลายของ AWS Transcribe ในตัว รวมถึงการสร้าง, การลบ, และการดึงข้อมูล transcription jobs

ในหน้านี้ คุณจะพบรายการ operations ที่ AWS Transcribe node รองรับ และลิงก์ไปยังแหล่งข้อมูลเพิ่มเติม

/// note | Credentials
อ้างอิง [AWS Transcribe credentials](/integrations/builtin/credentials/aws.md) สำหรับคำแนะนำในการตั้งค่าการยืนยันตัวตน
///

--8<-- "_snippets/integrations/builtin/app-nodes/ai-tools.md"

## Operations

**Transcription Job**

- Create a transcription job
- Delete a transcription job
- Get a transcription job
- Get all transcriptions job

## Templates and examples

<!-- see https://www.notion.so/n8n/Pull-in-templates-for-the-integrations-pages-37c716837b804d30a33b47475f6e3780 -->
[[ templatesWidget(page.title, 'aws-transcribe') ]]

--8<-- "_snippets/integrations/builtin/app-nodes/operation-not-supported.md"

