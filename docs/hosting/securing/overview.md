---
#https://www.notion.so/n8n/Frontmatter-432c2b8dff1f43d4b1c8d20075510fe4
title: การรักษาความปลอดภัย n8n
contentType: overview
---

# Securing n8n

การดูแลความปลอดภัยให้ n8n instance ของคุณมีได้หลายแบบ

โดยรวมแล้ว คุณสามารถ:

* ทำ [security audit](/hosting/securing/security-audit.md) เพื่อเช็คความเสี่ยงด้านความปลอดภัย
* [Set up SSL](/hosting/securing/set-up-ssl.md) เพื่อบังคับให้เชื่อมต่อแบบปลอดภัย
* [Set up Single Sign-On](/hosting/securing/set-up-sso.md) เพื่อจัดการบัญชีผู้ใช้
* ใช้ [two-factor authentication (2FA)](/user-management/two-factor-auth.md) สำหรับผู้ใช้ของคุณ

ถ้าอยากควบคุมรายละเอียดมากขึ้น ลองปิดหรือ opt-out ฟีเจอร์หรือการเก็บข้อมูลที่ไม่ต้องการ:

* [Disable the public API](/hosting/securing/disable-public-api.md) ถ้าไม่ได้ใช้งาน
* [Opt out of data collection](/hosting/securing/telemetry-opt-out.md) สำหรับข้อมูล anonymous ที่ n8n เก็บอัตโนมัติ
* [Block certain nodes](/hosting/securing/blocking-nodes.md) ไม่ให้ผู้ใช้เข้าถึง nodes บางตัว