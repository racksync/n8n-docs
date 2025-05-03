---
#https://www.notion.so/n8n/Frontmatter-432c2b8dff1f43d4b1c8d20075510fe4
title: คีย์ License
description: วิธี activate คีย์ License ของคุณ
contentType: howto
---

# License Key

เพื่อเปิดใช้งานฟีเจอร์ที่ต้องใช้ license บางอย่าง คุณต้อง activate license ของคุณก่อน คุณสามารถทำได้ผ่าน UI หรือโดยการตั้งค่า environment variables

## Add a license key using the UI

ใน n8n instance ของคุณ:

1. ล็อกอินในฐานะ **Admin** หรือ **Owner**
1. เลือก **Settings** > **Usage and plan**
1. เลือก **Enter activation key**
1. วาง license key ของคุณ
1. เลือก **Activate**

## Add a license key using an environment variables

ในการกำหนดค่า n8n ของคุณ ให้ตั้งค่า `N8N_LICENSE_ACTIVATION_KEY` เป็น license key ของคุณ หาก instance มี license ที่ activate แล้ว ตัวแปรนี้จะไม่มีผล

โปรดดู [Environment variables](/hosting/configuration/configuration-methods.md) เพื่อเรียนรู้เพิ่มเติมเกี่ยวกับการกำหนดค่า n8n

## Allowlist the license server IP addresses

n8n ใช้ Cloudflare เพื่อ host license server เนื่องจาก IP addresses เฉพาะอาจมีการเปลี่ยนแปลง คุณจำเป็นต้อง allowlist [ช่วง IP addresses ทั้งหมดของ Cloudflare](https://www.cloudflare.com/ips/) เพื่อให้แน่ใจว่า n8n สามารถเข้าถึง license server ได้เสมอ
