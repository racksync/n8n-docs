---
#https://www.notion.so/n8n/Frontmatter-432c2b8dff1f43d4b1c8d20075510fe4
title: Block access to nodes
description: "Prevent your n8n users from accessing specific nodes."
contentType: howto
---

# Block access to nodes

ถ้าอยากเพิ่มความปลอดภัย อาจจะต้อง block ไม่ให้ผู้ใช้เข้าถึงหรือใช้งาน nodes บางตัวใน n8n โดยเฉพาะถ้าผู้ใช้อาจไม่น่าไว้ใจ

ใช้ environment variable `NODES_EXCLUDE` เพื่อป้องกันไม่ให้ผู้ใช้เข้าถึง nodes ที่ต้องการ

## Exclude nodes

ตั้งค่า `NODES_EXCLUDE` เป็น array ของ string ที่ระบุชื่อ nodes ที่ต้องการ block

ตัวอย่างเช่น ตั้งค่าตามนี้:

```
NODES_EXCLUDE: "[\"n8n-nodes-base.executeCommand\", \"n8n-nodes-base.readWriteFile\"]"
```

จะ block [Execute Command](/integrations/builtin/core-nodes/n8n-nodes-base.executecommand/index.md) และ [Read/Write Files from Disk](/integrations/builtin/core-nodes/n8n-nodes-base.readwritefile.md) nodes

ผู้ใช้ n8n จะไม่สามารถค้นหาหรือใช้งาน nodes เหล่านี้ได้

## Suggested nodes to block

nodes ที่เสี่ยงต่อความปลอดภัยขึ้นอยู่กับ use case และ profile ของผู้ใช้ ลองเริ่มต้น block nodes เหล่านี้ก่อน:

* [Execute Command](/integrations/builtin/core-nodes/n8n-nodes-base.executecommand/index.md)
* [Read/Write Files from Disk](/integrations/builtin/core-nodes/n8n-nodes-base.readwritefile.md)

## Related resources

ดูข้อมูลเพิ่มเติมเกี่ยวกับ environment variable นี้ได้ที่ [Nodes environment variables](/hosting/configuration/environment-variables/nodes.md)

ดูวิธีตั้งค่า environment variables ได้ที่ [Configuration](/hosting/configuration/configuration-methods.md)
