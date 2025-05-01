---
#https://www.notion.so/n8n/Frontmatter-432c2b8dff1f43d4b1c8d20075510fe4
title: n8n Integrations Documentation and Guides
description: Access n8n integrations documentation and guides. Find comprehensive resources to help you master app integrations using different types of nodes to improve your automation workflows.
contentType: overview
---

# Integrations

n8n เรียก integrations ว่า nodes

Nodes คือส่วนประกอบหลักของ workflow ใน n8n โดย nodes จะเป็นจุดเริ่มต้นสำหรับดึงข้อมูล, ฟังก์ชันสำหรับประมวลผลข้อมูล หรือจุดสิ้นสุดสำหรับส่งข้อมูลออกไป การประมวลผลข้อมูลนี้รวมถึงการกรอง, การจัดรูปแบบใหม่ และการเปลี่ยนแปลงข้อมูล คุณสามารถมี node เดียวหรือหลาย node สำหรับ API, service หรือ app ของคุณก็ได้ และสามารถเชื่อมต่อ node หลายๆ ตัวเข้าด้วยกัน เพื่อสร้าง workflow ที่ซับซ้อนได้

## Built-in nodes

n8n มี built-in integrations ให้เลือกใช้งานมากมาย ดูรายละเอียดได้ที่ [Built-in nodes](/integrations/builtin/node-types.md) สำหรับเอกสารเกี่ยวกับ built-in nodes ทั้งหมดของ n8n

## Community nodes

นอกจาก built-in nodes แล้ว คุณยังสามารถติดตั้ง community-built nodes ได้ด้วย ดูรายละเอียดเพิ่มเติมที่ [Community nodes](/integrations/community-nodes/installation/index.md)

## Credential-only nodes and custom operations

--8<-- "_snippets/integrations/credential-only-intro.md"

ดูรายละเอียดเพิ่มเติมเกี่ยวกับ [Custom operations](/integrations/custom-operations.md)

## Generic integrations

ถ้าคุณต้องการเชื่อมต่อกับ service ที่ n8n ยังไม่มี node หรือมีแค่ credential-only node คุณก็ยังสามารถใช้ [HTTP Request](/integrations/builtin/core-nodes/n8n-nodes-base.httprequest/index.md) node ได้ ดูรายละเอียดวิธีตั้งค่าการ authentication และสร้าง API call ได้ที่หน้า node นี้

## Where to go next

* ถ้าคุณอยากสร้าง node ของตัวเอง ไปที่หัวข้อ [Creating Nodes](/integrations/creating-nodes/overview.md)
* ดู [Community nodes](/integrations/community-nodes/usage.md) เพื่อเรียนรู้วิธีติดตั้งและจัดการ community-built nodes
* ถ้าอยากรู้จัก nodes ต่างๆ ใน n8n, ฟังก์ชันการทำงาน และตัวอย่างการใช้งาน ดูได้ที่ node libraries ของ n8n: [Core nodes](/integrations/builtin/core-nodes/index.md), [Actions](/integrations/builtin/app-nodes/index.md), และ [Triggers](/integrations/builtin/trigger-nodes/index.md)
* ถ้าอยากรู้วิธีเพิ่ม credentials สำหรับแต่ละ node ไปที่หัวข้อ [Credentials](/integrations/builtin/credentials/index.md)
