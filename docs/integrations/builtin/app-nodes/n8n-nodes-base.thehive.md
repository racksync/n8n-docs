---
#https://www.notion.so/n8n/Frontmatter-432c2b8dff1f43d4b1c8d20075510fe4
title: TheHive node documentation
description: Learn how to use the TheHive node in n8n. Follow technical documentation to integrate TheHive node into your workflows.
contentType: [integration, reference]
---

# TheHive node

ใช้ TheHive node เพื่อช่วยให้งานใน TheHive เป็นอัตโนมัติและเชื่อมต่อกับแอปพลิเคชันอื่น ๆ โดย n8n รองรับฟีเจอร์ของ TheHive หลากหลาย เช่น การสร้าง alerts, การนับ log ของ tasks, cases และ observables

ในหน้านี้ คุณจะพบรายการ operations ที่ TheHive node รองรับ พร้อมทั้งลิงก์ไปยังแหล่งข้อมูลเพิ่มเติม

/// note | TheHive and TheHive 5
n8n provides two nodes for TheHive. Use this node (TheHive) if you want to use TheHive's version 3 or 4 API. If you want to use version 5, use [TheHive 5](/integrations/builtin/app-nodes/n8n-nodes-base.thehive5.md).
///
/// note | Credentials
ดู [TheHive credentials](/integrations/builtin/credentials/thehive.md) สำหรับคำแนะนำในการตั้งค่า authentication.
///

## Operations

The available operations depend on your API version. To see the operations list, create your credentials, including selecting your API version. Then return to the node, select the resource you want to use, and n8n displays the available operations for your API version. 

* Alert
* Case
* Log
* Observable
* Task

## Templates and examples

<!-- see https://www.notion.so/n8n/Pull-in-templates-for-the-integrations-pages-37c716837b804d30a33b47475f6e3780 -->
[[ templatesWidget(page.title, 'thehive') ]]

--8<-- "_snippets/integrations/builtin/app-nodes/operation-not-supported.md"

## Related resources

n8n มี trigger node สำหรับ TheHive คุณสามารถดูเอกสารเกี่ยวกับ trigger node ได้ที่ [here](/integrations/builtin/trigger-nodes/n8n-nodes-base.thehivetrigger.md).

ดูเอกสารของ TheHive สำหรับข้อมูลเพิ่มเติมเกี่ยวกับบริการ:
* [Version 3](https://docs.thehive-project.org/thehive/legacy/thehive3/api/){:target=_blank .external-link}
* [Version 4](https://docs.thehive-project.org/cortex/api/api-guide/){:target=_blank .external-link}
