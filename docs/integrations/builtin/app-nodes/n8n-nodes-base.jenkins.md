---
#https://www.notion.so/n8n/Frontmatter-432c2b8dff1f43d4b1c8d20075510fe4
title: เอกสารคู่มือ Jenkins node
description: เรียนรู้วิธีใช้ Jenkins node ใน n8n และดูเอกสารทางเทคนิคเพื่อเชื่อมต่อ Jenkins node เข้ากับ workflows ของคุณ
contentType: [integration, reference]
---

# Jenkins node

ใช้ Jenkins node เพื่อทำงานอัตโนมัติใน Jenkins และเชื่อมต่อ Jenkins กับแอปอื่นๆ ได้เลย n8n รองรับฟีเจอร์ของ Jenkins หลายอย่าง เช่น การแสดงรายการ builds, จัดการ instances, และการสร้างหรือคัดลอก jobs

ในหน้านี้จะมีรายการ operations ที่ Jenkins node รองรับ พร้อมลิงก์ไปยังแหล่งข้อมูลอื่นๆ

/// note | Credentials
โปรดดู [Jenkins credentials](/integrations/builtin/credentials/jenkins.md) สำหรับคำแนะนำการตั้งค่าการยืนยันตัวตน
///

--8<-- "_snippets/integrations/builtin/app-nodes/ai-tools.md"

## Operations

* Build
    * List Builds
* Instance
    * Cancel quiet down state
    * Put Jenkins in quiet mode, no builds can be started, Jenkins is ready for shutdown
    * Restart Jenkins immediately on environments where it's possible
    * Restart Jenkins once no jobs are running on environments where it's possible
    * Shutdown once no jobs are running
    * Shutdown Jenkins immediately
* Job
    * Copy a specific job
    * Create a new job
    * Trigger a specific job
    * Trigger a specific job

## Templates and examples

<!-- see https://www.notion.so/n8n/Pull-in-templates-for-the-integrations-pages-37c716837b804d30a33b47475f6e3780 -->
[[ templatesWidget(page.title, 'jenkins') ]]
