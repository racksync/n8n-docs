---
#https://www.notion.so/n8n/Frontmatter-432c2b8dff1f43d4b1c8d20075510fe4
title: Flow logic
description: วิธีแสดง logic ใน n8n workflow
contentType: overview
---

# Flow logic

n8n ช่วยให้คุณสามารถออกแบบ logic ที่ซับซ้อนใน workflow ของคุณได้

[[% import "_macros/section-toc.html" as sectionToc %]]

This section covers:

[[ sectionToc.sectionToc(page) ]]

## Related sections

คุณควรมีความเข้าใจพื้นฐานเกี่ยวกับ [Data](/data/index.md) ใน n8n รวมถึง [Data structure](/data/data-structure.md) และ [Data flow within nodes](/data/data-flow-nodes.md)

เวลาที่คุณสร้าง logic คุณจะได้ใช้ [Core nodes](/integrations/builtin/core-nodes/index.md) ของ n8n เช่น:

* Splitting: [IF](/integrations/builtin/core-nodes/n8n-nodes-base.if.md) และ [Switch](/integrations/builtin/core-nodes/n8n-nodes-base.switch.md)
* Merging: [Merge](/integrations/builtin/core-nodes/n8n-nodes-base.merge.md), [Compare Datasets](/integrations/builtin/core-nodes/n8n-nodes-base.comparedatasets.md), และ [Code](/integrations/builtin/core-nodes/n8n-nodes-base.code/index.md)
* Looping: [IF](/integrations/builtin/core-nodes/n8n-nodes-base.if.md) และ [Loop Over Items](/integrations/builtin/core-nodes/n8n-nodes-base.splitinbatches.md)
* Waiting: [Wait](/integrations/builtin/core-nodes/n8n-nodes-base.wait.md)
* Creating sub-workflows: [Execute Workflow](/integrations/builtin/core-nodes/n8n-nodes-base.executeworkflow.md) และ [Execute Workflow Trigger](/integrations/builtin/core-nodes/n8n-nodes-base.executeworkflowtrigger.md)
* Error handling: [Stop And Error](/integrations/builtin/core-nodes/n8n-nodes-base.stopanderror.md) และ [Error Trigger](/integrations/builtin/core-nodes/n8n-nodes-base.errortrigger.md)
