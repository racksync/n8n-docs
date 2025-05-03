---
#https://www.notion.so/n8n/Frontmatter-432c2b8dff1f43d4b1c8d20075510fe4
title: การจัดการ binary data ใน n8n
description: วิธีจัดการไฟล์ขนาดใหญ่โดยไม่กระทบประสิทธิภาพ n8n
contentType: howto
---

# Binary data

Binary data คือข้อมูลประเภทไฟล์ เช่น รูปภาพหรือเอกสารที่ workflow สร้างหรือประมวลผลระหว่าง execution

## Enable filesystem mode

โดยปกติ n8n จะเก็บ binary data ใน memory ซึ่งอาจทำให้ crash ถ้าทำงานกับไฟล์ใหญ่

เพื่อป้องกันปัญหานี้ ให้เปลี่ยน [environment variable](/hosting/configuration/environment-variables/binary-data.md) `N8N_DEFAULT_BINARY_DATA_MODE` เป็น `filesystem` เพื่อให้ n8n เก็บข้อมูลลง disk แทน memory

ถ้าใช้ queue mode ให้คงค่าเป็น `default` เพราะ n8n ยังไม่รองรับ filesystem mode กับ queue mode

## Binary data pruning

n8n จะลบ binary data ตามการลบ execution data ดูรายละเอียดที่ [Execution data | Enable data pruning](/hosting/scaling/execution-data.md#enable-data-pruning)

ถ้าตั้ง binary data mode หลายแบบ การลบ binary data จะทำกับ mode ที่ active เช่น ถ้าเคยเก็บใน S3 แล้วเปลี่ยนเป็น filesystem n8n จะลบเฉพาะ binary data ใน filesystem ดูรายละเอียดที่ [External storage](/hosting/scaling/external-storage.md#usage)
