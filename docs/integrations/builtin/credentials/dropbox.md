---
#https://www.notion.so/n8n/Frontmatter-432c2b8dff1f43d4b1c8d20075510fe4
title: Dropbox credentials
description: Documentation for Dropbox credentials. Use these credentials to authenticate Dropbox in n8n, a workflow automation platform.
contentType: [integration, reference]
priority: medium
---

# Dropbox credentials

คุณสามารถใช้ credentials นี้เพื่อเชื่อมต่อกับ node เหล่านี้:

- [Dropbox](/integrations/builtin/app-nodes/n8n-nodes-base.dropbox.md)

## Supported authentication methods

- API access token: Dropbox แนะนำวิธีนี้สำหรับการทดสอบกับบัญชีผู้ใช้ของคุณ และให้สิทธิ์การเข้าถึงแก่ผู้ใช้จำนวนจำกัด
- OAuth2: Dropbox แนะนำวิธีนี้สำหรับ production หรือสำหรับการทดสอบกับผู้ใช้มากกว่า 50 คน

/// note | App reuse
คุณสามารถเปลี่ยน app จาก API access token ไปเป็น OAuth2 ได้โดยการสร้าง credential ใหม่ใน n8n สำหรับ OAuth2 โดยใช้ app เดิม
///

## Related resources

ดูรายละเอียดเพิ่มเติมเกี่ยวกับการใช้งาน API ได้ที่ [Dropbox's Developer documentation](https://www.dropbox.com/developers/documentation){:target=_blank .external-link}

## Using access token

ถ้าจะตั้งค่า credentials นี้ คุณต้องมีบัญชี [Dropbox](https://www.dropbox.com/developers){:target=_blank .external-link} developer และ:

- **Access Token**: สร้างขึ้นเมื่อคุณสร้าง Dropbox app
- **App Access Type**

วิธีตั้งค่า credential โดยสร้าง Dropbox app:

1. เปิด [App Console](https://www.dropbox.com/developers/apps){:target=_blank .external-link} ใน Dropbox developer portal
2. เลือก **Create app**
3. ใน **Choose an API** เลือก **Scoped access**
4. ใน **Choose the type of access you need** เลือกตัวเลือกที่เหมาะสมกับการใช้งาน [Dropbox](/integrations/builtin/app-nodes/n8n-nodes-base.dropbox.md) node ของคุณมากที่สุด:
    - **App folder**: ให้สิทธิ์เข้าถึงเฉพาะ folder ที่สร้างขึ้นสำหรับ app ของคุณเท่านั้น
    - **Full Dropbox**: ให้สิทธิ์เข้าถึงไฟล์ทั้งหมดในบัญชี Dropbox ของผู้ใช้
5. ตั้งชื่อ app ของคุณ เช่น `n8n integration`
6. เลือก **Create app** รายละเอียด app จะเปิดขึ้น
7. ในแท็บ **Permissions** เลือก permission ที่ต้องการสำหรับ app ของคุณ n8n แนะนำให้เลือก permission เหล่านี้สำหรับ [Dropbox](/integrations/builtin/app-nodes/n8n-nodes-base.dropbox.md) node:
    - `files.metadata.write`
    - `files.metadata.read`
    - `files.content.write`
    - `files.content.read`
    - `sharing.write`
    - `sharing.read`
    - `file_requests.write`
    - `file_requests.read`
8. เลือก **Submit** เพื่อบันทึกการเปลี่ยนแปลง permission
9. ในแท็บ **Settings** คัดลอก **App key** และ **App secret** ไปใส่ใน n8n credential ของคุณ
10. ในส่วน **Generated access token** เลือก **Generate** เพื่อสร้าง access token
11. คัดลอก access token ที่สร้างขึ้นแล้วนำไปใส่ใน n8n credential ของคุณ

ดูข้อมูลเพิ่มเติมได้ที่ [Dropbox Building an App documentation](https://www.dropbox.com/developers/reference/getting-started#app){:target=_blank .external-link}

## Using OAuth2

--8<-- "_snippets/integrations/builtin/credentials/cloud-oauth-button.md"

หากคุณต้องการตั้งค่า OAuth2 ด้วยตัวเอง หรือต้องการรายละเอียดเพิ่มเติมเกี่ยวกับขั้นตอน OAuth web flow คุณจะต้องสร้าง Dropbox app:

1. ทำตามขั้นตอน 1-9 ในส่วน [Using access token](#using-access-token) ด้านบน
2. ใน n8n คัดลอก **OAuth Callback URL**
3. ใน Dropbox app ของคุณ ไปที่แท็บ **Settings**
4. ในส่วน **OAuth 2** เพิ่ม **Redirect URIs** โดยใส่ URL ที่คัดลอกมาจาก n8n
5. เลือก **Add**
6. เลือก **Connect my account** ใน n8n และทำตามคำแนะนำบนหน้าจอเพื่อเชื่อมต่อ credential ให้เสร็จสิ้น

ดูข้อมูลเพิ่มเติมได้ที่ [Dropbox OAuth Guide](https://www.dropbox.com/developers/reference/oauth-guide){:target=_blank .external-link}
