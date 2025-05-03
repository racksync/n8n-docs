---
#https://www.notion.so/n8n/Frontmatter-432c2b8dff1f43d4b1c8d20075510fe4
description: การใช้งาน LDAP กับ n8n
contentType: howto
---

# Lightweight Directory Access Protocol (LDAP)

/// info | Feature availability
* มีให้ใช้งานบน Self-hosted Enterprise และ Cloud Enterprise plans
* คุณต้องมีสิทธิ์เข้าถึง n8n instance owner account
///

หน้านี้จะบอกวิธีเปิดใช้งาน LDAP ใน n8n โดยสมมติว่าคุณคุ้นเคยกับ LDAP และมี LDAP server ที่ตั้งค่าไว้แล้ว

LDAP ช่วยให้ผู้ใช้สามารถ sign in เข้าสู่ n8n ด้วยข้อมูลประจำตัวขององค์กร แทนที่จะใช้ login ของ n8n

## Enable LDAP

1. Login เข้าสู่ n8n ในฐานะ instance owner
2. เลือก **Settings** <span class="inline-image">![Settings icon](/_images/common-icons/settings.png){.off-glb}</span> > **LDAP**
3. สลับเปิด **Enable LDAP Login**
4. กรอกข้อมูลในช่องต่างๆ ด้วยรายละเอียดจาก LDAP server ของคุณ
5. เลือก **Test connection** เพื่อตรวจสอบการตั้งค่าการเชื่อมต่อของคุณ หรือ **Save connection** เพื่อสร้างการเชื่อมต่อ

หลังจากเปิดใช้งาน LDAP แล้ว ทุกคนบน LDAP server ของคุณจะสามารถ sign in เข้าสู่ n8n instance ได้ เว้นแต่คุณจะยกเว้นพวกเขาโดยใช้การตั้งค่า **User Filter**

คุณยังคงสามารถสร้างผู้ใช้ที่ไม่ใช่ LDAP (email users) ได้ในหน้า **Settings** > **Users**

## Merging n8n and LDAP accounts

หาก n8n พบ account ที่ตรงกัน (email ตรงกัน) สำหรับ email users และ LDAP users ผู้ใช้นั้นจะต้อง sign in ด้วย LDAP account ของตน n8n instance owner accounts จะถูกยกเว้นจากกรณีนี้: n8n จะไม่แปลง owner accounts เป็น LDAP users โดยเด็ดขาด

## LDAP user accounts in n8n

ในการ sign in ครั้งแรก n8n จะสร้าง user account ใน n8n สำหรับ LDAP user นั้น

คุณต้องจัดการรายละเอียดผู้ใช้บน LDAP server ไม่ใช่ใน n8n หากคุณอัปเดตหรือลบผู้ใช้บน LDAP server ของคุณ บัญชี n8n จะอัปเดตในการ sync ตามกำหนดเวลาครั้งถัดไป หรือเมื่อผู้ใช้พยายาม login ครั้งถัดไป แล้วแต่ว่าเหตุการณ์ใดเกิดขึ้นก่อน

/// note | User deletion
หากคุณลบผู้ใช้ออกจาก LDAP server ของคุณ พวกเขาจะสูญเสียสิทธิ์การเข้าถึง n8n ในการ sync ครั้งถัดไป
///
## Turn LDAP off

วิธีปิด LDAP:

1. Login เข้าสู่ n8n ในฐานะ instance owner
2. เลือก **Settings** <span class="inline-image">![Settings icon](/_images/common-icons/settings.png){.off-glb}</span> > **LDAP**
3. สลับปิด **Enable LDAP Login**

หากคุณปิด LDAP n8n จะแปลง LDAP users ที่มีอยู่เป็น email users ในการ login ครั้งถัดไปของพวกเขา ผู้ใช้จะต้อง reset password ของตนเอง
