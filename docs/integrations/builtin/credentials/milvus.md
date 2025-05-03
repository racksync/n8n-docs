---
#https://www.notion.so/n8n/Frontmatter-432c2b8dff1f43d4b1c8d20075510fe4
title: ข้อมูลยืนยันตัวตน Milvus
description: เอกสารสำหรับ Milvus credentials ใช้เพื่อเชื่อมต่อ Milvus ใน n8n
contentType: [integration, reference]
priority: high
---

# Milvus credentials

คุณสามารถใช้ credentials เหล่านี้เพื่อยืนยันตัวตนใน nodes ต่อไปนี้:

* [Milvus Vector Store](/integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.vectorstoremilvus.md)

## Prerequisites

สร้างและรัน instance ของ [Milvus](https://milvus.io/) อ้างอิง [Install Milvus](https://milvus.io/docs/install-overview.md) สำหรับข้อมูลเพิ่มเติม

## Supported authentication methods

- Basic auth

## Related resources

อ้างอิง [Milvus's Authentication documentation](https://milvus.io/docs/authenticate.md?tab=docker#Authenticate-User-Access) สำหรับข้อมูลเพิ่มเติมเกี่ยวกับการตั้งค่าการยืนยันตัวตน

--8<-- "_snippets/integrations/builtin/cluster-nodes/langchain-overview-link.md"

## Using basic auth

ในการกำหนดค่า credential นี้ คุณจะต้องมี:

* **Base URL**: Base URL ของ instance Milvus ของคุณ ค่าเริ่มต้นคือ `http://localhost:19530`
* **Username**: ชื่อผู้ใช้เพื่อยืนยันตัวตนกับ instance Milvus ของคุณ ค่าเริ่มต้นคือ `root`
* **Password**: รหัสผ่านเพื่อยืนยันตัวตนกับ instance Milvus ของคุณ ค่าเริ่มต้นคือ `Milvus`
