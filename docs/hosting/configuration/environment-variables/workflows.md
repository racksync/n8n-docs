---
#https://www.notion.so/n8n/Frontmatter-432c2b8dff1f43d4b1c8d20075510fe4
title: Environment Variables สำหรับ Workflows
description: Environment Variables สำหรับตั้งค่า Workflows ใน n8n เช่น ชื่อ Default การตั้งค่า Onboarding การจัดการ Tag และ Caller Policy
contentType: reference
tags:
  - environment variables
hide:
  - toc
  - tags
---

# Workflows environment variables

--8<-- "_snippets/self-hosting/file-based-configuration.md"

| Variable | Type  | Default  | Description |
| :------- | :---- | :------- | :---------- |
| `N8N_ONBOARDING_FLOW_DISABLED` | Boolean | `false` | ปิด onboarding tips ตอนสร้าง workflow ใหม่ (true = ปิด, false = เปิด) |
| `N8N_WORKFLOW_ACTIVATION_BATCH_SIZE` | Number | `1` | จำนวน workflow ที่จะ activate พร้อมกันตอน startup |
| `N8N_WORKFLOW_CALLER_POLICY_DEFAULT_OPTION` | String | `workflowsFromSameOwner` | กำหนดว่า workflow ไหนเรียก workflow นี้ได้บ้าง ตัวเลือก: `any`, `none`, `workflowsFromAList`, `workflowsFromSameOwner` ฟีเจอร์นี้ต้องเปิด [Workflow sharing](/workflows/sharing.md) |
| `N8N_WORKFLOW_TAGS_DISABLED` | Boolean | `false` | ปิด workflow tags (true = ปิด, false = เปิด) |
| `WORKFLOWS_DEFAULT_NAME` | String | `My workflow` | ชื่อ default สำหรับ workflow ใหม่ |
