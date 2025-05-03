---
#https://www.notion.so/n8n/Frontmatter-432c2b8dff1f43d4b1c8d20075510fe4
title: เอกสาร Email Trigger (IMAP) node
description: เรียนรู้วิธีใช้ Email Trigger (IMAP) node ใน n8n ทำตามเอกสารเพื่อนำ Email Trigger (IMAP) node ไปใช้ใน workflow ของคุณ
contentType: [integration, reference]
priority: high
---

# Email Trigger (IMAP) node

ใช้ IMAP Email node เพื่อรับอีเมลผ่าน IMAP email server node นี้เป็น trigger node

/// note | Credential
ดูข้อมูลการตั้งค่า authentication สำหรับ node นี้ได้ที่ [IMAP credential](/integrations/builtin/credentials/imap/index.md)
///

## Operations

- รับอีเมล

## Node parameters

ตั้งค่า node นี้โดยใช้ parameter เหล่านี้

### Credential to connect with

เลือกหรือสร้าง [IMAP credential](/integrations/builtin/credentials/imap/index.md) เพื่อเชื่อมต่อกับ server

### Mailbox Name

ใส่ชื่อ mailbox ที่ต้องการรับอีเมลจาก

### Action

เลือกว่าจะให้อีเมลถูก mark ว่าอ่านแล้วเมื่อ n8n รับหรือไม่ **None** คือยังไม่อ่าน **Mark as Read** คือ mark ว่าอ่านแล้ว

### Download Attachments

toggle นี้ควบคุมว่าจะดาวน์โหลดไฟล์แนบอีเมลหรือไม่ (เปิด/ปิด) ถ้าไม่จำเป็นอย่าเปิด เพราะจะใช้ resource เพิ่ม

### Format

เลือก format ที่จะคืนค่า message ได้จาก:

* **RAW**: คืนข้อมูลอีเมลทั้งหมดใน field raw เป็น base64url encoded string ไม่มี field payload
* **Resolved**: คืนข้อมูลอีเมลทั้งหมดแบบ resolve แล้ว และแนบไฟล์เป็น binary
* **Simple**: คืนข้อมูลอีเมลทั้งหมด ไม่เหมาะถ้าต้องการ inline attachments

## Node options

ตั้งค่าเพิ่มเติมได้ใน **Options**

### Custom Email Rules

ใส่ rule สำหรับดึงอีเมลแบบ custom ได้

ดู [node-imap's search function criteria](https://github.com/mscdex/node-imap) สำหรับรายละเอียด

### Force Reconnect Every Minutes

ตั้ง interval (นาที) สำหรับ reconnect ใหม่

## Templates and examples

<!-- see https://www.notion.so/n8n/Pull-in-templates-for-the-integrations-pages-37c716837b804d30a33b47475f6e3780 -->
[[ templatesWidget(page.title, 'email-trigger-imap') ]]
