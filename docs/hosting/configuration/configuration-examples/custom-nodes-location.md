---
#https://www.notion.so/n8n/Frontmatter-432c2b8dff1f43d4b1c8d20075510fe4
title: Specify location for your custom nodes
description: Add folders and specify paths for your custom nodes. 
contentType: howto
---

# Specify location for your custom nodes

ผู้ใช้แต่ละคนสามารถเพิ่ม custom node ของตัวเองได้ n8n จะโหลด node เหล่านี้ตอน startup โดย default จะอยู่ใน subfolder `.n8n/custom` ของ user ที่รัน n8n

ถ้าอยากเพิ่มโฟลเดอร์อื่น ๆ ให้ใช้ environment variable นี้:

```bash
export N8N_CUSTOM_EXTENSIONS="/home/jim/n8n/custom-nodes;/data/n8n/nodes"
```
ดูรายละเอียดตัวแปรนี้เพิ่มเติมได้ที่ [Environment variables reference](/hosting/configuration/environment-variables/nodes.md)
