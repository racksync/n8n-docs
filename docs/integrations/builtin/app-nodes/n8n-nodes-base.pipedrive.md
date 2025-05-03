---
#https://www.notion.so/n8n/Frontmatter-432c2b8dff1f43d4b1c8d20075510fe4
title: เอกสารคู่มือ Pipedrive node
description: เรียนรู้วิธีใช้ Pipedrive node ใน n8n และดูเอกสารทางเทคนิคเพื่อเชื่อมต่อ Pipedrive node เข้ากับ workflow ของคุณ
contentType: [integration, reference]
priority: medium
---

# Pipedrive node

ใช้ Pipedrive node เพื่อช่วยทำงานใน Pipedrive แบบอัตโนมัติและเชื่อมต่อกับแอปพลิเคชันอื่น ๆ. n8n มีการสนับสนุนคุณสมบัติของ Pipedrive หลากหลาย เช่น การสร้าง, อัปเดต, ลบ และดึงข้อมูล activity, files, notes, organizations และ leads.

ในหน้านี้ คุณจะพบรายการของ operations ที่ Pipedrive node รองรับและลิงก์สำหรับข้อมูลเพิ่มเติม.

/// note | Credentials
ดูรายละเอียดเพิ่มเติมได้ที่ [Pipedrive credentials](/integrations/builtin/credentials/pipedrive.md) สำหรับคำแนะนำในการตั้งค่า authentication. 
///

--8<-- "_snippets/integrations/builtin/app-nodes/ai-tools.md"

## Operations

* Activity
    * Create an activity
    * Delete an activity
    * Get data of an activity
    * Get data of all activities
    * Update an activity
* Deal
    * Create a deal
    * Delete a deal
    * Duplicate a deal
    * Get data of a deal
    * Get data of all deals
    * Search a deal
    * Update a deal
* Deal Activity
    * Get all activities of a deal
* Deal Product
    * Add a product to a deal
    * Get all products in a deal
    * Remove a product from a deal
    * Update a product in a deal
* File
    * Create a file
    * Delete a file
    * Download a file
    * Get data of a file
* Lead
    * Create a lead
    * Delete a lead
    * Get data of a lead
    * Get data of all leads
    * Update a lead
* Note
    * Create a note
    * Delete a note
    * Get data of a note
    * Get data of all notes
    * Update a note
* Organization
    * Create an organization
    * Delete an organization
    * Get data of an organization
    * Get data of all organizations
    * Update an organization
    * Search organizations
* Person
    * Create a person
    * Delete a person
    * Get data of a person
    * Get data of all persons
    * Search all persons
    * Update a person
* Product
    * Get data of all products

## Templates and examples

<!-- see https://www.notion.so/n8n/Pull-in-templates-for-the-integrations-pages-37c716837b804d30a33b47475f6e3780 -->
[[ templatesWidget(page.title, 'pipedrive') ]]

--8<-- "_snippets/integrations/builtin/app-nodes/operation-not-supported.md"
