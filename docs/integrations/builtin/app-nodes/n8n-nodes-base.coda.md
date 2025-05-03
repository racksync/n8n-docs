---
#https://www.notion.so/n8n/Frontmatter-432c2b8dff1f43d4b1c8d20075510fe4
title: เอกสารคู่มือ Coda node
description: เรียนรู้วิธีใช้ Coda node ใน n8n และดูเอกสารทางเทคนิคเพื่อเชื่อมต่อ Coda node เข้ากับ workflows ของคุณ
contentType: [integration, reference]
---

# Coda node

ใช้ Coda node เพื่อทำงานอัตโนมัติใน Coda และ integrate Coda กับแอปพลิเคชันอื่นๆ n8n มีการรองรับในตัวสำหรับฟีเจอร์ต่างๆ ของ Coda รวมถึงการสร้าง, ดึง, และลบ controls, formulas, tables, และ views

ในหน้านี้ คุณจะพบรายการ operations ที่ Coda node รองรับ และลิงก์ไปยังแหล่งข้อมูลเพิ่มเติม

/// note | Credentials
อ้างอิง [Coda credentials](/integrations/builtin/credentials/coda.md) สำหรับคำแนะนำในการตั้งค่า authentication
///

## Operations

* Control
    * Get a control
    * Get all controls
* Formula
    * Get a formula
    * Get all formulas
* Table
    * Create/Insert a row
    * Delete one or multiple rows
    * Get all columns
    * Get all the rows
    * Get a column
    * Get a row
    * Pushes a button
* View
    * Delete view row
    * Get a view
    * Get all views
    * Get all views columns
    * Get all views rows
    * Update row
    * Push view button

## Templates and examples

<!-- see https://www.notion.so/n8n/Pull-in-templates-for-the-integrations-pages-37c716837b804d30a33b47475f6e3780 -->
[[ templatesWidget(page.title, 'coda') ]]
