---
#https://www.notion.so/n8n/Frontmatter-432c2b8dff1f43d4b1c8d20075510fe4
description: ทำความเข้าใจโครงสร้างฐานข้อมูลของ n8n
contentType: explanation
---

# Database structure

หน้านี้จะอธิบายจุดประสงค์ของแต่ละ table ในฐานข้อมูลของ n8n

## Database and query technology

โดยปกติแล้ว n8n จะใช้ SQLite เป็นฐานข้อมูลหลัก ถ้าคุณใช้ฐานข้อมูลอื่น โครงสร้างจะคล้ายกัน แต่ data-types อาจแตกต่างกันไปตามแต่ละฐานข้อมูล

n8n ใช้ [TypeORM](https://github.com/typeorm/typeorm){:target=_blank .external-link} สำหรับ query และ migration ต่างๆ

ถ้าคุณอยากดูข้อมูลในฐานข้อมูล n8n สามารถใช้ [DBeaver](https://dbeaver.io){:target=_blank .external-link} ซึ่งเป็นเครื่องมือจัดการฐานข้อมูลแบบ open-source

## Tables

นี่คือตาราง (table) ที่ n8n สร้างขึ้นตอน setup
<!-- vale off -->
### auth_identity

เก็บรายละเอียดของ external authentication providers เวลาที่ใช้ [SAML](/user-management/saml/index.md)

### auth_provider_sync_history

เก็บประวัติการเชื่อมต่อ SAML

### credentials_entity

เก็บ [credentials](/glossary.md#credential-n8n) ที่ใช้สำหรับเชื่อมต่อกับ integration ต่างๆ

### event_destinations

เก็บ configuration ของปลายทางสำหรับ [Log streaming](/log-streaming.md)

### execution_data

เก็บ workflow ขณะที่รันอยู่ และ execution data

### execution_entity

เก็บ execution ของ workflow ทั้งหมดที่บันทึกไว้ การตั้งค่า workflow จะมีผลกับ execution ที่ n8n จะบันทึก

### execution_metadata

เก็บ [Custom executions data](/workflows/executions/custom-executions-data.md)

### installed_nodes

แสดงรายการ [community nodes](/integrations/community-nodes/installation/index.md) ที่ติดตั้งใน n8n instance ของคุณ

### installed_packages

รายละเอียด npm community nodes packages ที่ติดตั้งใน n8n instance ของคุณ [installed_nodes](#installed_nodes) จะเป็นรายชื่อ node แต่ละตัว ส่วน `installed_packages` จะเป็น npm package ซึ่งอาจมีหลาย node อยู่ใน package เดียว

### migrations

บันทึก log ของ database migration ทั้งหมด อ่านเพิ่มเติมเกี่ยวกับ [Migrations](https://github.com/typeorm/typeorm/blob/master/docs/migrations.md){:target=_blank .external-link} ในเอกสารของ TypeORM

### project

แสดงรายการ [projects](/user-management/rbac/projects.md) ใน instance ของคุณ

### project_relation

อธิบายความสัมพันธ์ระหว่าง user กับ [project](/user-management/rbac/projects.md) รวมถึง [role type](/user-management/rbac/role-types.md) ของ user ด้วย

### role

ตอนนี้ยังไม่ได้ใช้งาน จะใช้ในอนาคตสำหรับ custom roles

### settings

บันทึก custom instance settings ซึ่งเป็น setting ที่คุณไม่สามารถตั้งค่าผ่าน environment variable ได้ เช่น

* ตั้งค่า instance owner แล้วหรือยัง
* ผู้ใช้เลือกข้ามการตั้งค่า owner และ user management หรือไม่
* License key

### shared_credentials

เชื่อมโยง credentials กับ user

### shared_workflow

เชื่อมโยง workflow กับ user

### tag_entity

เก็บ tag ของ workflow ทั้งหมดที่สร้างใน n8n instance ตารางนี้จะเก็บรายละเอียด tag ส่วน [workflows_tags](#workflows_tags) จะบันทึกว่า workflow ไหนมี tag อะไรบ้าง

### user

เก็บข้อมูล user

### variables

เก็บ [variables](/code/variables.md)

### webhook_entity

บันทึก webhook ที่ active ใน workflow ของ n8n instance ของคุณ ไม่ได้จำกัดแค่ Webhook node แต่รวมถึง webhook ที่ใช้ใน trigger node อื่นๆ ด้วย

### workflow_entity

เก็บ workflow ที่บันทึกไว้ใน n8n instance ของคุณ

### workflow_history

เก็บเวอร์ชันก่อนหน้าของ workflow

### workflow_statistics

นับ workflow ID และสถานะของ workflow

### workflows_tags

เชื่อมโยง tag กับ workflow [tag_entity](#tag_entity) จะเก็บรายละเอียด tag

## Entity Relationship Diagram (ERD)

!["n8n ERD"](/_images/hosting/architecture/n8n-database-diagram.png)

<!-- vale on -->
