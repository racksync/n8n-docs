---
#https://www.notion.so/n8n/Frontmatter-432c2b8dff1f43d4b1c8d20075510fe4
title: LDAP
description: เอกสารสำหรับ LDAP node ใน n8n แพลตฟอร์ม workflow automation พร้อมคำแนะนำการใช้งานและตัวอย่าง
contentType: [integration, reference]
---

# LDAP

node นี้ให้คุณเชื่อมต่อกับ LDAP server เพื่อสร้าง ค้นหา และอัปเดต object ต่างๆ

/// note | Credentials
คุณสามารถดูข้อมูลการยืนยันตัวตนสำหรับ node นี้ได้ [ที่นี่](/integrations/builtin/credentials/ldap.md).
///

## Operations

* [**Compare**](#compare) เปรียบเทียบ attribute
* [**Create**](#create) สร้าง entry ใหม่
* [**Delete**](#delete) ลบ entry
* [**Rename**](#rename) เปลี่ยน DN ของ entry ที่มีอยู่
* [**Search**](#search) LDAP
* [**Update**](#update) อัปเดต attributes

ดูรายละเอียดการตั้งค่าแต่ละ operation ได้ในหัวข้อด้านล่าง

--8<-- "_snippets/integrations/builtin/app-nodes/ai-tools.md"

## Compare

ตั้งค่า operation นี้โดยใช้ parameter เหล่านี้:

* **Credential to connect with**: เลือกหรือสร้าง [LDAP credential](/integrations/builtin/credentials/ldap.md) เพื่อเชื่อมต่อ
* **DN**: ใส่ Distinguished Name (DN) ของ entry ที่ต้องการเปรียบเทียบ
* **Attribute ID**: ใส่ ID ของ attribute ที่ต้องการเปรียบเทียบ
* **Value**: ใส่ค่าที่ต้องการเปรียบเทียบ

## Create

ตั้งค่า operation นี้โดยใช้ parameter เหล่านี้:

* **Credential to connect with**: เลือกหรือสร้าง [LDAP credential](/integrations/builtin/credentials/ldap.md) เพื่อเชื่อมต่อ
* **DN**: ใส่ Distinguished Name (DN) ของ entry ที่ต้องการสร้าง
* **Attributes**: เพิ่มคู่ **Attribute ID**/**Value** ที่ต้องการสร้าง

## Delete

ตั้งค่า operation นี้โดยใช้ parameter เหล่านี้:

* **Credential to connect with**: เลือกหรือสร้าง [LDAP credential](/integrations/builtin/credentials/ldap.md) เพื่อเชื่อมต่อ
* **DN**: ใส่ Distinguished Name (DN) ของ entry ที่ต้องการลบ

## Rename

ตั้งค่า operation นี้โดยใช้ parameter เหล่านี้:

* **Credential to connect with**: เลือกหรือสร้าง [LDAP credential](/integrations/builtin/credentials/ldap.md) เพื่อเชื่อมต่อ
* **DN**: ใส่ Distinguished Name (DN) ปัจจุบันของ entry ที่ต้องการเปลี่ยนชื่อ
* **New DN**: ใส่ Distinguished Name (DN) ใหม่สำหรับ entry นี้

## Search

ตั้งค่า operation นี้โดยใช้ parameter เหล่านี้:

* **Credential to connect with**: เลือกหรือสร้าง [LDAP credential](/integrations/builtin/credentials/ldap.md) เพื่อเชื่อมต่อ
* **Base DN**: ใส่ Distinguished Name (DN) ของ subtree ที่ต้องการค้นหา
* **Search For**: เลือก object class ที่ต้องการค้นหา
* **Attribute**: เลือก attribute ที่ต้องการค้นหา
* **Search Text**: ใส่ข้อความที่ต้องการค้นหา ใช้ `*` เป็น wildcard ได้
* **Return All**: ถ้าเปิด node จะคืนค่าทั้งหมด ถ้าปิดจะคืนค่าตาม **Limit** ที่ตั้งไว้
* **Limit**: ใช้ได้เมื่อปิด **Return All** ใส่จำนวนสูงสุดของผลลัพธ์ที่ต้องการ

### Search options

คุณสามารถตั้งค่า operation นี้เพิ่มเติมได้ด้วย options เหล่านี้:

* **Attribute Names or IDs**: ใส่ชื่อหรือ ID ของ attribute ที่ต้องการคืนค่า (คั่นด้วย comma) เลือกจาก list หรือใส่ ID ด้วย expression ก็ได้
* **Page Size**: ใส่จำนวนสูงสุดของผลลัพธ์ที่ต้องการในแต่ละครั้ง ใส่ 0 เพื่อปิดการแบ่งหน้า
* **Scopes**: กำหนดขอบเขตของ entry ที่จะค้นหาจาก **Base DN** เลือกได้จาก:
    * **Base Tree**: (subordinateSubtree) ค้นหาเฉพาะ subordinates ของ **Base DN** ไม่รวม **Base DN** เอง
    * **Single Level**: (one) ค้นหาเฉพาะลูกโดยตรงของ **Base DN**
    * **Whole Subtree**: (sub) ค้นหา **Base DN** และลูกทั้งหมดทุกระดับ

ดูข้อมูลเพิ่มเติมเกี่ยวกับ search scopes ได้ที่ [The LDAP Search Operation](https://ldap.com/the-ldap-search-operation/){:target="_blank" .external-link}

## Update

ตั้งค่า operation นี้โดยใช้ parameter เหล่านี้:

* **Credential to connect with**: เลือกหรือสร้าง [LDAP credential](/integrations/builtin/credentials/ldap.md) เพื่อเชื่อมต่อ
* **DN**: ใส่ Distinguished Name (DN) ของ entry ที่ต้องการอัปเดต
* ***Update Attributes**: เลือกว่าจะ **Add** (เพิ่ม), **Remove** (ลบ), หรือ **Replace** (แทนที่) attribute ที่มีอยู่
* จากนั้นใส่คู่ **Attribute ID**/**Value** ที่ต้องการอัปเดต

## Templates and examples

<!-- see https://www.notion.so/n8n/Pull-in-templates-for-the-integrations-pages-37c716837b804d30a33b47475f6e3780 -->
[[ templatesWidget(page.title, 'ldap') ]]
