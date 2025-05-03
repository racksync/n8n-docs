---
#https://www.notion.so/n8n/Frontmatter-432c2b8dff1f43d4b1c8d20075510fe4
description: วิธีเปิดใช้งาน 2FA สำหรับบัญชี n8n ของคุณ
contentType: howto
---

# Two-factor authentication (2FA)

Two-factor authentication (2FA) เพิ่มวิธีการยืนยันตัวตนขั้นที่สองนอกเหนือจาก username และ password ซึ่งช่วยเพิ่มความปลอดภัยของบัญชี n8n รองรับ 2FA โดยใช้ authenticator app

## Enable 2FA

คุณต้องมี authenticator app บนโทรศัพท์ของคุณ

วิธีเปิดใช้งาน 2FA ใน n8n:

1. ไปที่ **Settings** > **Personal** ของคุณ
2. เลือก **Enable 2FA** n8n จะเปิด modal พร้อม QR code
3. สแกน QR code ใน authenticator app ของคุณ
4. ป้อนรหัสจากแอปของคุณในช่อง **Code from authenticator app**
5. เลือก **Continue** n8n จะแสดง recovery codes
6. บันทึก recovery codes เหล่านี้ คุณจะต้องใช้รหัสเหล่านี้เพื่อเข้าถึงบัญชีของคุณอีกครั้งหากคุณทำ authenticator หาย

## Disable 2FA for your instance

ผู้ใช้ Self-hosted สามารถกำหนดค่า n8n instance ของตนเพื่อปิดใช้งาน 2FA สำหรับผู้ใช้ทั้งหมดได้โดยตั้งค่า `N8N_MFA_ENABLED` เป็น false โปรดทราบว่า n8n จะไม่สนใจการตั้งค่านี้หากมีผู้ใช้เดิมที่เปิดใช้งาน 2FA อยู่แล้ว โปรดดู [Configuration methods](/hosting/configuration/configuration-methods.md) สำหรับข้อมูลเพิ่มเติมเกี่ยวกับการกำหนดค่า n8n instance ของคุณด้วย environment variables
