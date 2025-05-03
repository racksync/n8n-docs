---
title: ข้อมูลเข้าสู่ระบบ Strapi
description: คู่มือการตั้งค่า Strapi credentials สำหรับเชื่อมต่อ Strapi กับ n8n
contentType: [integration, reference]
---

# Strapi credentials

คุณสามารถใช้ credentials นี้เพื่อยืนยันตัวตนกับ node ต่อไปนี้ได้:

- [Strapi](/integrations/builtin/app-nodes/n8n-nodes-base.strapi.md)

## Prerequisites

สร้างบัญชี admin [Strapi](https://strapi.io/){:target=_blank .external-link} ที่:

- มีสิทธิ์เข้าถึงโปรเจกต์ Strapi ที่มีอยู่แล้ว
- มี collection type อย่างน้อยหนึ่งอันในโปรเจกต์นั้น
- มีข้อมูลที่ publish แล้วใน collection type นั้น

ดูคู่มือเริ่มต้นสำหรับนักพัฒนาได้ที่ [Quick Start Guide](https://docs.strapi.io/dev-docs/quick-start){:target=_blank .external-link}

## Supported authentication methods

- API user account: ต้องใช้บัญชีผู้ใช้ที่มี permission สำหรับ content ที่เหมาะสม
- API token: ต้องใช้บัญชี admin

## Related resources

ดูข้อมูลเพิ่มเติมเกี่ยวกับบริการนี้ได้ที่ [Strapi's documentation](https://docs.strapi.io/dev-docs/api/rest){:target=_blank .external-link}

## Using API user account

ในการตั้งค่า credentials นี้ คุณจะต้องมี:

- **Email** ของ user: ต้องเป็นบัญชีผู้ใช้ (user account) ไม่ใช่ admin account ดูรายละเอียดเพิ่มเติมด้านล่าง
- **Password** ของ user: ต้องเป็นบัญชีผู้ใช้ (user account) ไม่ใช่ admin account ดูรายละเอียดเพิ่มเติมด้านล่าง
- **URL**: ใช้ public URL ของ Strapi server ของคุณ ซึ่งกำหนดไว้ใน `./config/server.js` ใน parameter `url` แนะนำให้ใช้ absolute URL
    - ถ้าเป็น Strapi Cloud ให้ใช้ URL ของโปรเจกต์ Cloud เช่น `https://my-strapi-project-name.strapiapp.com`
- **API Version**: เลือกเวอร์ชัน API ที่ต้องการใช้งาน มีให้เลือก:
    - **Version 3**
    - **Version 4**

ใน Strapi ต้องตั้งค่าสองขั้นตอน:

1. [Configure a role](#configure-a-role)
2. [Create a user account](#create-a-user-account)

ดูรายละเอียดแต่ละขั้นตอนด้านล่าง

### Configure a role

สำหรับการเข้าถึง API ให้ใช้ Users & Permissions Plugin ที่ **Settings > Users & Permissions Plugin**

ดูข้อมูลเพิ่มเติมเกี่ยวกับปลั๊กอินนี้ได้ที่ [Configuring Users & Permissions Plugin](https://docs.strapi.io/user-docs/settings/configuring-users-permissions-plugin-settings){:target=_blank .external-link} และดูข้อมูลเกี่ยวกับ roles ได้ที่ [Configuring end-user roles](https://docs.strapi.io/user-docs/users-roles-permissions/configuring-end-users-roles){:target=_blank .external-link}

สำหรับ credentials ใน n8n ผู้ใช้ต้องมี role ที่ให้ permission สำหรับ API ใน collection type ที่ต้องการ โดยสามารถเลือกได้ว่าจะ:

* อัปเดต role **Authenticated** ที่มีอยู่ให้มี permission ที่ต้องการ แล้วกำหนด user ให้ใช้ role นี้ ดูรายละเอียดที่ [Configuring role's permissions](https://docs.strapi.io/user-docs/users-roles-permissions/configuring-end-users-roles#configuring-roles-permissions){:target=_blank .external-link}
* สร้าง role ใหม่ที่มี permission ที่ต้องการ แล้วกำหนด user ให้ใช้ role นี้ ดูรายละเอียดที่ [Creating a new role](https://docs.strapi.io/user-docs/users-roles-permissions/configuring-end-users-roles#creating-a-new-role){:target=_blank .external-link}

เมื่อเปิด role แล้ว:

1. ไปที่ส่วน **Permissions**
2. เปิดส่วนของ collection type ที่เกี่ยวข้อง
3. เลือก permission ที่ต้องการให้ role นี้ เช่น:
    - `create` (POST)
    - `find` และ `findone` (GET)
    - `update` (PUT)
    - `delete` (DELETE)
4. ทำซ้ำสำหรับ collection type อื่น ๆ ที่เกี่ยวข้อง
5. กดบันทึก role

ดูข้อมูลเพิ่มเติมเกี่ยวกับ endpoints ได้ที่ [Endpoints](https://docs.strapi.io/dev-docs/api/rest#endpoints){:target=_blank .external-link}

### Create a user account

หลังจากตั้งค่า role แล้ว ให้สร้าง end-user account และกำหนด role ที่ตั้งค่าไว้ให้กับ user:

1. ไปที่ **Content Manager > Collection Types > User**
2. เลือก **Add new entry**
3. กรอกข้อมูล user โดย credentials ใน n8n ต้องใช้ข้อมูลเหล่านี้ (แต่โปรเจกต์ Strapi ของคุณอาจมี field อื่น ๆ เพิ่มเติม):
    - **Username**: จำเป็นสำหรับผู้ใช้ Strapi ทุกคน
    - **Email**: กรอกใน Strapi และใช้เป็น **Email** ใน credentials ของ n8n
    - **Password**: กรอกใน Strapi และใช้เป็น **Password** ใน credentials ของ n8n
    - **Role**: เลือก role ที่ตั้งค่าไว้ในขั้นตอนก่อนหน้า

ดูข้อมูลเพิ่มเติมเกี่ยวกับการจัดการบัญชีผู้ใช้ได้ที่ [Managing end-user accounts](https://docs.strapi.io/user-docs/users-roles-permissions/managing-end-users){:target=_blank .external-link}

## Using API token

ในการตั้งค่า credentials นี้ คุณจะต้องมี:

- **API Token**: สร้าง API token ได้ที่ **Settings > Global Settings > API Tokens** ดูวิธีสร้าง token และข้อมูลเพิ่มเติมได้ที่ [Creating a new API token documentation](https://docs.strapi.io/user-docs/settings/API-tokens#creating-a-new-api-token){:target=_blank .external-link}
    
    /// note | API tokens permission
    ถ้าไม่เห็นตัวเลือก **API tokens** ใน **Global settings** แสดงว่าบัญชีของคุณไม่มี permission **API tokens > Read**
    ///
    
- **URL**: ใช้ public URL ของ Strapi server ของคุณ ซึ่งกำหนดไว้ใน `./config/server.js` ใน parameter `url` แนะนำให้ใช้ absolute URL
    - ถ้าเป็น Strapi Cloud ให้ใช้ URL ของโปรเจกต์ Cloud เช่น `https://my-strapi-project-name.strapiapp.com`
- **API Version**: เลือกเวอร์ชัน API ที่ต้องการใช้งาน มีให้เลือก:
    - **Version 3**
    - **Version 4**
