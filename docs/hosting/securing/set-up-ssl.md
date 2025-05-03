---
#https://www.notion.so/n8n/Frontmatter-432c2b8dff1f43d4b1c8d20075510fe4
title: ตั้งค่า SSL
description: "ตั้งค่า SSL สำหรับ n8n instance ที่คุณโฮสต์เอง"
contentType: howto
---

# Set up SSL

มี 2 วิธีในการตั้งค่า TLS/SSL ให้กับ n8n

## Use a reverse proxy (recommended)

แนะนำให้ใช้ reverse proxy เช่น [Traefik](https://doc.traefik.io/traefik/){:target=_blank .external-link} หรือ Network Load Balancer (NLB) ไว้หน้าตัว n8n instance ซึ่งจะช่วยจัดการเรื่อง certificate renewals ให้ด้วย

ดูข้อมูลเพิ่มเติมได้ที่ [Security | Data encryption](https://n8n.io/legal/#security){:target=_blank .external-link}

## Pass certificates into n8n directly

อีกวิธีคือส่ง certificate เข้าไปที่ n8n โดยตรง โดยตั้งค่า environment variables `N8N_SSL_CERT` และ `N8N_SSL_KEY` ให้ชี้ไปที่ไฟล์ certificate และ key ที่สร้างไว้

อย่าลืมดูแล certificate ให้ต่ออายุและอัปเดตอยู่เสมอ

ดูรายละเอียด environment variables เหล่านี้ได้ที่ [Deployment environment variables](/hosting/configuration/environment-variables/deployment.md) และดูวิธีตั้งค่า environment variables ได้ที่ [Configuration](/hosting/configuration/configuration-methods.md)
