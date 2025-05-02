---
#https://www.notion.so/n8n/Frontmatter-432c2b8dff1f43d4b1c8d20075510fe4
title: Code node common issues 
description: Documentation for common issues and questions in the Code node in n8n, a workflow automation platform. Includes details of the issue and suggested solutions.
contentType: [integration, reference]
priority: high
---

# Code node common issues

นี่คือข้อผิดพลาดและปัญหาที่พบบ่อยกับ [Code node](/integrations/builtin/core-nodes/n8n-nodes-base.code/index.md) พร้อมวิธีแก้ไขหรือแนวทางตรวจสอบ

<!-- vale off -->
## Code doesn't return items properly
<!-- vale on -->

ข้อผิดพลาดนี้เกิดขึ้นเมื่อโค้ดใน Code node ของคุณไม่ได้ return ข้อมูลในรูปแบบที่ n8n คาดหวัง

ใน n8n ข้อมูลที่ส่งต่อระหว่าง node จะเป็น array ของ object โดยแต่ละ object จะมี key ชื่อ `json` ครอบข้อมูลอีกที

```javascript
[
  {
    "json": {
	  // ข้อมูลของคุณใส่ตรงนี้
	}
  }
]
```

วิธีตรวจสอบปัญหานี้:

* อ่าน [data structure](/data/data-structure.md) เพื่อเข้าใจโครงสร้างข้อมูลที่ Code node ได้รับและข้อกำหนดสำหรับการ return ข้อมูลออกจาก node
* ทำความเข้าใจการทำงานของ data item และการเชื่อมโยงข้อมูลจาก node ก่อนหน้าด้วย [item linking](/data/data-mapping/data-item-linking/index.md)

<!-- vale off -->
## A 'json' property isn't an object
<!-- vale on -->

ข้อผิดพลาดนี้เกิดขึ้นเมื่อ Code node return ข้อมูลที่ key `json` ไม่ได้ชี้ไปที่ object

เช่น ถ้าคุณตั้งค่า `json` ให้เป็น array แทน object:

```javascript
[
  {
    "json": [
	  // ตั้ง json เป็น array แบบนี้จะ error
	]
  }
]
```

วิธีแก้ไข: ให้แน่ใจว่า key `json` อ้างอิง object เสมอ

```javascript
[
  {
    "json": {
	  // ตั้ง json เป็น object ตามที่ระบบต้องการ
	}
  }
]
```

## Code doesn't return an object

ข้อผิดพลาดนี้อาจเกิดขึ้นเมื่อ Code node ของคุณไม่ได้ return อะไรเลย หรือ return ผลลัพธ์ที่ไม่ถูกต้อง

วิธีแก้ไข: ให้แน่ใจว่า Code node ของคุณ return [expected data structure](/data/data-structure.md):

```javascript
[
  {
    "json": {
	  // ข้อมูลของคุณใส่ตรงนี้
	}
  }
]
```

ข้อผิดพลาดนี้อาจเกิดขึ้นถ้าโค้ดของคุณ return `'undefined'` แทนผลลัพธ์ที่ต้องการ กรณีนี้ให้ตรวจสอบว่าข้อมูลที่คุณอ้างอิงใน Code node มีอยู่จริงในทุก execution และมีโครงสร้างตรงกับที่โค้ดของคุณคาดหวัง

## 'import' and 'export' may only appear at the top level

ข้อผิดพลาดนี้เกิดขึ้นถ้าคุณพยายามใช้ `import` หรือ `export` ใน Code node ซึ่ง n8n ไม่รองรับใน JavaScript sandbox ให้ใช้ `require` แทน

วิธีแก้ไข: เปลี่ยนจาก `import` เป็น `require` เช่น

```javascript
// โค้ดเดิม:
// import express from "express";
// โค้ดใหม่:
const express = require("express");
```

<!-- vale off -->
## Cannot find module '&lt;module&gt;'
<!-- vale on -->

ข้อผิดพลาดนี้เกิดขึ้นเมื่อคุณใช้ `require` ใน Code node แล้ว n8n หา module ไม่เจอ

/// warning | Only for self-hosted
n8n ไม่รองรับการ import module ใน [Cloud](/manage-cloud/overview.md) version
///

ถ้าคุณ [self-hosting](/hosting/index.md) n8n ให้ทำตามขั้นตอนนี้:

* ติดตั้ง module ลงใน environment เดียวกับที่รัน n8n
	* ถ้าใช้ [npm](/hosting/installation/npm.md) ให้ติดตั้ง module ใน environment เดียวกับ n8n
	* ถ้าใช้ [Docker](/hosting/installation/docker.md) ต้อง extend image n8n ด้วย [custom image](https://docs.docker.com/build/building/base-images/){:target=_blank .external-link} ที่มี module ที่ต้องการ
* ตั้งค่า environment variable `NODE_FUNCTION_ALLOW_BUILTIN` และ `NODE_FUNCTION_ALLOW_EXTERNAL` [ดูตัวอย่าง](/hosting/configuration/configuration-examples/modules-in-code-node.md) เพื่ออนุญาต import module

## Using global variables

บางครั้งคุณอาจอยากเก็บหรือดึงข้อมูลแบบ global ที่เกี่ยวกับ workflow ข้าม execution หรือในแต่ละ execution เช่น อยากเก็บวันที่ของ report ก่อนหน้าไว้ใช้ใน report รอบถัดไป

ให้ใช้ [static data](/code/cookbook/builtin/get-workflow-static-data.md) ในโค้ดของคุณเพื่อ set, update, และดึงข้อมูล workflow-level สามารถจัดการข้อมูลแบบ global หรือผูกกับ node เฉพาะก็ได้

/// info | Use Remove Duplicates when possible
ถ้าคุณอยากใช้ตัวแปรเพื่อป้องกันการประมวลผลข้อมูลซ้ำ ลองใช้ [Remove Duplicates node](/integrations/builtin/core-nodes/n8n-nodes-base.removeduplicates/index.md) แทน Remove Duplicates node จะช่วยเก็บข้อมูลข้าม execution เพื่อป้องกันการประมวลผลซ้ำ
///
