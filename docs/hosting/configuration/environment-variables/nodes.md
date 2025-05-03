---
#https://www.notion.so/n8n/Frontmatter-432c2b8dff1f43d4b1c8d20075510fe4
title: Environment Variables สำหรับ Nodes
description: Environment Variable สำหรับตั้งค่าการจัดการ Nodes ใน n8n Self-hosted
contentType: reference
tags:
  - environment variables
hide:
  - toc
  - tags
---

# Nodes environment variables

--8<-- "_snippets/self-hosting/file-based-configuration.md"

หน้านี้จะสรุป environment variables สำหรับจัดการ [nodes](/glossary.md#node-n8n) ใน n8n เช่น เลือก node ที่จะโหลด/ไม่โหลด, import module ใน Code node, และเปิด community nodes

| Variable | Type  | Default  | Description |
| :------- | :---- | :------- | :---------- |
| `NODES_INCLUDE` | Array of strings | - | ระบุ node ที่จะโหลด |
| `NODES_EXCLUDE` | Array of strings | - | ระบุ node ที่ไม่ต้องโหลด เช่น ถ้าอยาก block node ที่เสี่ยงกับ security: `NODES_EXCLUDE: "[\"n8n-nodes-base.executeCommand\", \"n8n-nodes-base.readWriteFile\"]"` |
| `NODE_FUNCTION_ALLOW_BUILTIN` | String | - | อนุญาตให้ import built-in module ใน Code node (ใส่ * เพื่อเปิดหมด) ปกติจะปิดหมด |
| `NODE_FUNCTION_ALLOW_EXTERNAL` | String | - | อนุญาตให้ import external module (จาก `n8n/node_modules`) ใน Code node ปกติจะปิดหมด |
| `NODES_ERROR_TRIGGER_TYPE` | String | `n8n-nodes-base.errorTrigger` | ระบุ node type ที่ใช้เป็น Error Trigger |
| `N8N_CUSTOM_EXTENSIONS` | String | - | path ไปยังโฟลเดอร์ custom nodes |
| `N8N_COMMUNITY_PACKAGES_ENABLED` | Boolean | `true` | เปิด/ปิด community nodes |
| `N8N_COMMUNITY_PACKAGES_REGISTRY` | String | `https://registry.npmjs.org` | NPM registry URL สำหรับ community packages (ต้องมี license) |
