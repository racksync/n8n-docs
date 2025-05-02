---
#https://www.notion.so/n8n/Frontmatter-432c2b8dff1f43d4b1c8d20075510fe4
title: AWS S3 node documentation
description: Learn how to use the AWS S3 node in n8n. Follow technical documentation to integrate AWS S3 node into your workflows.
contentType: [integration, reference]
priority: medium
---

# AWS S3 node

ใช้ AWS S3 node เพื่อทำงานอัตโนมัติใน AWS S3 และผสานรวม AWS S3 กับแอปพลิเคชันอื่นๆ n8n มีการรองรับฟีเจอร์หลากหลายของ AWS S3 ในตัว รวมถึงการสร้างและลบ buckets, การคัดลอกและดาวน์โหลดไฟล์, รวมถึงการดึงข้อมูลโฟลเดอร์

ในหน้านี้ คุณจะพบรายการ operations ที่ AWS S3 node รองรับ และลิงก์ไปยังแหล่งข้อมูลเพิ่มเติม

/// note | Credentials
อ้างอิง [AWS credentials](/integrations/builtin/credentials/aws.md) สำหรับคำแนะนำในการตั้งค่าการยืนยันตัวตน
///

--8<-- "_snippets/integrations/builtin/app-nodes/ai-tools.md"

## Operations

* Bucket
    * Create a bucket
    * Delete a bucket
    * Get all buckets
    * Search within a bucket
* File
    * Copy a file
    * Delete a file
    * Download a file
    * Get all files
    * Upload a file
* Folder
    * Create a folder
    * Delete a folder
    * Get all folders

## Templates and examples

<!-- see https://www.notion.so/n8n/Pull-in-templates-for-the-integrations-pages-37c716837b804d30a33b47475f6e3780 -->
[[ templatesWidget(page.title, 'aws-s3') ]]

--8<-- "_snippets/integrations/builtin/app-nodes/operation-not-supported.md"

