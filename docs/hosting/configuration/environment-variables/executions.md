---
#https://www.notion.so/n8n/Frontmatter-432c2b8dff1f43d4b1c8d20075510fe4
title: Executions environment variables
description: Environment variables to configure settings related to workflow executions. 
contentType: reference
tags:
  - environment variables
hide:
  - toc
  - tags
---

# Executions environment variables

--8<-- "_snippets/self-hosting/file-based-configuration.md"

หน้านี้จะสรุป environment variables สำหรับตั้งค่าการรัน workflow

| Variable | Type  | Default  | Description |
| :------- | :---- | :------- | :---------- |
| `EXECUTIONS_MODE` | Enum string: `regular`, `queue` | `regular` | เลือกว่าจะรัน execution ตรง ๆ หรือใช้ queue<br><br>ดู [Queue mode](/hosting/scaling/queue-mode.md) |
| `EXECUTIONS_TIMEOUT` | Number | `-1` | timeout (วินาที) default สำหรับ workflow ถ้าเกินนี้ n8n จะหยุด execution ผู้ใช้ override ได้ในแต่ละ workflow (แต่ไม่เกิน `EXECUTIONS_TIMEOUT_MAX`) ถ้าตั้ง `-1` จะปิด timeout |
| `EXECUTIONS_TIMEOUT_MAX` | Number | `3600` | execution time สูงสุด (วินาที) ที่ผู้ใช้ตั้งได้ในแต่ละ workflow |
| `EXECUTIONS_DATA_SAVE_ON_ERROR` | Enum string: `all`, `none` | `all` | จะ save execution data ตอน error หรือไม่ |
| `EXECUTIONS_DATA_SAVE_ON_SUCCESS` | Enum string: `all`, `none` | `all` | จะ save execution data ตอนสำเร็จหรือไม่ |
| `EXECUTIONS_DATA_SAVE_ON_PROGRESS` | Boolean | `false` | save progress ทุก node ที่รันหรือไม่ |
| `EXECUTIONS_DATA_SAVE_MANUAL_EXECUTIONS` | Boolean | `true` | save data ของ execution ที่รัน manual หรือไม่ |
| `EXECUTIONS_DATA_PRUNE` | Boolean | `true` | ลบ execution เก่า ๆ อัตโนมัติหรือไม่ |
| `EXECUTIONS_DATA_MAX_AGE` | Number | `336` | อายุ execution (ชั่วโมง) ก่อนจะถูกลบ |
| `EXECUTIONS_DATA_PRUNE_MAX_COUNT` | Number | `10000` | จำนวน execution สูงสุดที่เก็บใน database 0 = ไม่จำกัด |
| `EXECUTIONS_DATA_HARD_DELETE_BUFFER` | Number | `1` | execution ที่จบแล้วต้องเก่าแค่ไหน (ชั่วโมง) ถึงจะ hard-delete (กันไม่ให้ execution ล่าสุดโดนลบขณะ dev) |
| `EXECUTIONS_DATA_PRUNE_HARD_DELETE_INTERVAL` | Number | `15` | ความถี่ (นาที) ในการ hard-delete execution |
| `EXECUTIONS_DATA_PRUNE_SOFT_DELETE_INTERVAL` | Number | `60` | ความถี่ (นาที) ในการ soft-delete execution |
| `N8N_CONCURRENCY_PRODUCTION_LIMIT` | Number | `-1` | จำกัดจำนวน execution production ที่รันพร้อมกัน (ทั้ง regular/queue) `-1` = ไม่จำกัดใน regular mode |
