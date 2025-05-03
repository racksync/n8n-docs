---
#https://www.notion.so/n8n/Frontmatter-432c2b8dff1f43d4b1c8d20075510fe4
title: เอกสารคู่มือ BambooHR node
description: เรียนรู้วิธีใช้ BambooHR node ใน n8n และดูเอกสารทางเทคนิคเพื่อเชื่อมต่อ BambooHR node เข้ากับ workflows ของคุณ
contentType: [integration, reference]
---

# BambooHR node

ใช้ BambooHR node เพื่อทำงานอัตโนมัติใน BambooHR และ integrate BambooHR กับแอปพลิเคชันอื่นๆ n8n มีการรองรับในตัวสำหรับฟีเจอร์ต่างๆ ของ BambooHR รวมถึงการสร้าง, ลบ, ดาวน์โหลด, และดึง company reports, employee documents, และ files

ในหน้านี้ คุณจะพบรายการ operations ที่ BambooHR node รองรับ และลิงก์ไปยังแหล่งข้อมูลเพิ่มเติม

/// note | Credentials
อ้างอิง [BambooHR credentials](/integrations/builtin/credentials/bamboohr.md) สำหรับคำแนะนำในการตั้งค่า authentication
///

## Operations

* Company Report
    * Get a company report
* Employee
    * Create an employee
    * Get an employee
    * Get all employees
    * Update an employee
* Employee Document
    * Delete an employee document
    * Download an employee document
    * Get all employee document
    * Update an employee document
    * Upload an employee document
* File
    * Delete a company file
    * Download a company file
    * Get all company files
    * Update a company file
    * Upload a company file

## Templates and examples

<!-- see https://www.notion.so/n8n/Pull-in-templates-for-the-integrations-pages-37c716837b804d30a33b47475f6e3780 -->
[[ templatesWidget(page.title, 'bamboohr') ]]
