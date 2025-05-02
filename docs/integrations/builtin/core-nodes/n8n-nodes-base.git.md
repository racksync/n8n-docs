---
#https://www.notion.so/n8n/Frontmatter-432c2b8dff1f43d4b1c8d20075510fe4
title: Git
description: Documentation for the Git node in n8n, a workflow automation platform. Includes guidance on usage, and links to examples.
contentType: [integration, reference]
---

# Git

[Git](https://git-scm.com/) คือระบบ distributed version control แบบ open-source ที่ออกแบบมาให้รองรับทั้งโปรเจ็กต์ขนาดเล็กและใหญ่ได้อย่างรวดเร็วและมีประสิทธิภาพ

/// note | Credentials
คุณสามารถดูข้อมูลการตั้งค่า authentication สำหรับ node นี้ได้ที่ [Git credential](/integrations/builtin/credentials/git.md)
///

## Operations

* [**Add**](#add) เพิ่มไฟล์หรือโฟลเดอร์เข้า commit (เหมือน [git add](https://git-scm.com/docs/git-add){:target=_blank .external-link})
* [**Add Config**](#add-config): เพิ่ม property ใน config (เหมือน [git config](https://git-scm.com/docs/git-config){:target=_blank .external-link})
* [**Clone**](#clone) โคลน repository (เหมือน [git clone](https://git-scm.com/docs/git-clone){:target=_blank .external-link})
* [**Commit**](#commit) commit ไฟล์หรือโฟลเดอร์ (เหมือน [git commit](https://git-scm.com/docs/git-commit){:target=_blank .external-link})
* [**Fetch**](#fetch) ดึงข้อมูลจาก remote repository (เหมือน [git fetch](https://git-scm.com/docs/git-fetch){:target=_blank .external-link})
* [**List Config**](#list-config): ดู config ปัจจุบัน (เหมือน [git config](https://git-scm.com/docs/git-config){:target=_blank .external-link})
* [**Log**](#log): ดูประวัติ commit (เหมือน [git log](https://git-scm.com/docs/git-log){:target=_blank .external-link})
* [**Pull**](#pull) ดึงข้อมูลจาก remote repository (เหมือน [git pull](https://git-scm.com/docs/git-pull){:target=_blank .external-link})
* [**Push**](#push) ส่งข้อมูลไป remote repository (เหมือน [git push](https://git-scm.com/docs/git-push){:target=_blank .external-link})
* [**Push Tags**](#push-tags) ส่ง tag ไป remote repository (เหมือน [git push --tags](https://git-scm.com/docs/git-push#Documentation/git-push.txt---tags){:target=_blank .external-link})
* ดู [**Status**](#status) ของ repository ปัจจุบัน (เหมือน [git status](https://git-scm.com/docs/git-status){:target=_blank .external-link})
* สร้าง [**Tag**](#tag) ใหม่ (เหมือน [git tag](https://git-scm.com/docs/git-tag){:target=_blank .external-link})
* [**User Setup**](#user-setup): ตั้งค่าผู้ใช้

ดูรายละเอียด parameter และ options ของแต่ละ operation ได้ในหัวข้อด้านล่าง

## Add

ตั้งค่า operation นี้ด้วย parameter เหล่านี้:

* **Repository Path**: กรอก path ของ git repository ในเครื่อง
* **Paths to Add**: กรอก path ของไฟล์หรือโฟลเดอร์ที่ต้องการ add (คั่นด้วย comma) จะใช้ path แบบ absolute หรือ relative จาก **Repository Path** ก็ได้

<!--Vale doesn't like "Config"-->
<!-- vale off -->
## Add Config

ตั้งค่า operation นี้ด้วย parameter เหล่านี้:

* **Repository Path**: กรอก path ของ git repository ในเครื่อง
* **Key**: กรอกชื่อ key ที่ต้องการตั้งค่า
* **Value**: กรอกค่าของ key

### Add Config options

add config operation จะมี option **Mode** ให้เลือกว่าจะ **Set** หรือ **Append** ค่าใน local config
<!-- vale on -->

## Clone

ตั้งค่า operation นี้ด้วย parameter เหล่านี้:

* **Repository Path**: กรอก path ของ git repository ในเครื่อง
* **Authentication**: เลือก **Authenticate** เพื่อใช้ credentials หรือ **None** ถ้าไม่ต้องการใช้ authentication
    * ถ้าเลือก **Authenticate** ต้องเลือกหรือสร้าง credentials สำหรับ node นี้ ดูรายละเอียดที่ [Git credential](/integrations/builtin/credentials/git.md)
* **New Repository Path**: กรอก path ที่ต้องการเก็บ repository ที่โคลนมา
* **Source Repository**: กรอก URL หรือ path ของ repository ที่ต้องการโคลน

## Commit

ตั้งค่า operation นี้ด้วย parameter เหล่านี้:

* **Repository Path**: กรอก path ของ git repository ในเครื่อง
* **Message**: กรอกข้อความ commit

### Commit options

commit operation จะมี option **Paths to Add** ถ้าต้องการ commit ไฟล์หรือโฟลเดอร์ที่ "add" ไว้ทั้งหมด ให้เว้นว่างไว้ ถ้าต้องการ commit เฉพาะไฟล์หรือโฟลเดอร์ที่ระบุ ให้กรอก path (คั่นด้วย comma)

จะใช้ path แบบ absolute หรือ relative จาก **Repository Path** ก็ได้

## Fetch

operation นี้มี parameter เดียวคือ **Repository Path** ให้กรอก path ของ git repository ในเครื่อง

<!--Vale doesn't like "Config"-->
<!-- vale off -->
## List Config

operation นี้มี parameter เดียวคือ **Repository Path** ให้กรอก path ของ git repository ในเครื่อง
<!-- vale on -->

## Log

ตั้งค่า operation นี้ด้วย parameter เหล่านี้:

* **Repository Path**: กรอก path ของ git repository ในเครื่อง
* **Return All**: เปิดเพื่อให้ node คืนค่าทั้งหมด ปิดเพื่อกำหนด **Limit**
* **Limit**: แสดงเมื่อปิด **Return All** กรอกจำนวนสูงสุดที่ต้องการคืนค่า

### Log options

log operation จะมี option **File** กรอก path ของไฟล์หรือโฟลเดอร์ที่ต้องการดูประวัติ

จะใช้ path แบบ absolute หรือ relative จาก **Repository Path** ก็ได้

## Pull

operation นี้มี parameter เดียวคือ **Repository Path** ให้กรอก path ของ git repository ในเครื่อง

## Push

ตั้งค่า operation นี้ด้วย parameter เหล่านี้:

* **Repository Path**: กรอก path ของ git repository ในเครื่อง
* **Authentication**: เลือก **Authenticate** เพื่อใช้ credentials หรือ **None** ถ้าไม่ต้องการใช้ authentication
    * ถ้าเลือก **Authenticate** ต้องเลือกหรือสร้าง **Credential for Git** สำหรับ node นี้ ดูรายละเอียดที่ [Git credential](/integrations/builtin/credentials/git.md)

### Push options

push operation จะมี option **Target Repository** กรอก URL หรือ path ของ repository ที่ต้องการ push

## Push Tags

operation นี้มี parameter เดียวคือ **Repository Path** ให้กรอก path ของ git repository ในเครื่อง

## Status

operation นี้มี parameter เดียวคือ **Repository Path** ให้กรอก path ของ git repository ในเครื่อง

## Tag

ตั้งค่า operation นี้ด้วย parameter เหล่านี้:

* **Repository Path**: กรอก path ของ git repository ในเครื่อง
* **Name**: กรอกชื่อ tag ที่ต้องการสร้าง

## User Setup

operation นี้มี parameter เดียวคือ **Repository Path** ให้กรอก path ของ git repository ในเครื่อง

## Templates and examples

<!-- see https://www.notion.so/n8n/Pull-in-templates-for-the-integrations-pages-37c716837b804d30a33b47475f6e3780 -->
[[ templatesWidget(page.title, 'git') ]]
