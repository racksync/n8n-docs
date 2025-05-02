---
#https://www.notion.so/n8n/Frontmatter-432c2b8dff1f43d4b1c8d20075510fe4
title: Configure workflow timeout settings
description: Set execution timeouts to determine how long workflows can run.  
contentType: howto
---

# Configure workflow timeout settings

workflow จะ timeout และถูก cancel หลังจากเวลาที่กำหนด (หน่วยเป็นวินาที) ถ้า workflow รันใน main process จะเป็น soft timeout (รอให้ node ปัจจุบันจบก่อน) ถ้ารันใน process แยก n8n จะพยายาม soft timeout ก่อน แล้ว kill process หลังจากรอ 1/5 ของเวลาที่ตั้งไว้

ค่า default ของ `EXECUTIONS_TIMEOUT` คือ `-1` ตัวอย่างเช่น ถ้าอยากให้ timeout เป็น 1 ชั่วโมง:

```bash
export EXECUTIONS_TIMEOUT=3600
```

คุณสามารถตั้งเวลาสูงสุด (วินาที) สำหรับแต่ละ workflow แยกกันได้ เช่น ถ้าอยากให้ workflow ใด ๆ รันได้นานสุด 2 ชั่วโมง:

```bash
export EXECUTIONS_TIMEOUT_MAX=7200
```
ดูรายละเอียดตัวแปรนี้เพิ่มเติมได้ที่ [Environment variables reference](/hosting/configuration/environment-variables/executions.md)
