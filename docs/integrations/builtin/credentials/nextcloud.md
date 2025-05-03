---
title: ข้อมูลยืนยันตัวตน Nextcloud
description: เอกสารสำหรับการยืนยันตัวตน Nextcloud. ใช้ข้อมูลเหล่านี้เพื่อยืนยันตัวตน Nextcloud ใน n8n.
contentType: [integration, reference]
priority: medium
---

# Nextcloud credentials

คุณสามารถใช้ credentials เหล่านี้เพื่อยืนยันตัวตนใน nodes ต่อไปนี้:

- [Nextcloud](/integrations/builtin/app-nodes/n8n-nodes-base.nextcloud.md)

## Supported authentication methods

- Basic auth
- OAuth2

## Related resources

อ้างอิง [Nextcloud's API documentation](https://nextcloud-server.netlify.app/){:target=_blank .external-link} สำหรับข้อมูลเพิ่มเติมเกี่ยวกับบริการนี้

อ้างอิง [Nextcloud's user manual](https://docs.nextcloud.com/server/stable/user_manual/en/contents.html){:target=_blank .external-link} สำหรับข้อมูลเพิ่มเติมเกี่ยวกับการติดตั้งและกำหนดค่า Nextcloud

## Using basic auth

ในการกำหนดค่า credential นี้ คุณจะต้องมีบัญชี [Nextcloud](https://nextcloud.com/){:target=_blank .external-link} และ:

- **Web DAV URL** ของคุณ
- ชื่อ **User** ของคุณ
- **Password** ของคุณ หรือ app password

วิธีตั้งค่า:

1. วิธีสร้าง **Web DAV URL** ของคุณ: หาก Nextcloud อยู่ใน root ของ domain ของคุณ: ป้อน URL ที่คุณใช้เข้าถึง Nextcloud และเพิ่ม `/remote.php/webdav/` ตัวอย่างเช่น หากคุณเข้าถึง Nextcloud ที่ `https://cloud.n8n.com` WebDAV URL ของคุณคือ `https://cloud.n8n.com/remote.php/webdav`
    - หากคุณติดตั้ง Nextcloud ใน subdirectory ให้ป้อน URL ที่คุณใช้เข้าถึง Nextcloud และเพิ่ม `/<subdirectory>/remote.php/webdav/` แทนที่ `<subdirectory>` ด้วย subdirectory ที่ติดตั้ง Nextcloud
    - อ้างอิงเอกสาร [Third-party WebDAV clients](https://docs.nextcloud.com/server/stable/user_manual/en/files/access_webdav.html#third-party-webdav-clients){:target=_blank .external-link} ของ Nextcloud สำหรับข้อมูลเพิ่มเติมเกี่ยวกับการสร้าง WebDAV URL ของคุณ
2. ป้อนชื่อ **User** ของคุณ
3. สำหรับ **Password** Nextcloud แนะนำให้ใช้ app password แทนรหัสผ่านผู้ใช้ของคุณ วิธีสร้าง app password:
    1. ใน Nextcloud Web interface เลือก avatar ของคุณที่มุมขวาบนและเลือก **Personal settings**
    2. ในเมนูด้านซ้าย เลือก **Security**
    3. เลื่อนไปที่ด้านล่างสุดไปยังส่วน **App Password** และสร้าง app password ใหม่
    4. คัดลอก app password นั้นและป้อนลงใน n8n เป็น **Password** ของคุณ

## Using OAuth2

ในการกำหนดค่า credential นี้ คุณจะต้องมีบัญชี [Nextcloud](https://nextcloud.com/){:target=_blank .external-link} และ:

- **Authorization URL** และ **Access Token URL**: สิ่งเหล่านี้ขึ้นอยู่กับ URL ที่คุณใช้เข้าถึง Nextcloud
- **Client ID**: สร้างขึ้นเมื่อคุณเพิ่มแอปพลิเคชันไคลเอ็นต์ OAuth2 ใน **Administrator Security Settings**
- **Client Secret**: สร้างขึ้นเมื่อคุณเพิ่มแอปพลิเคชันไคลเอ็นต์ OAuth2 ใน **Administrator Security Settings**
- **Web DAV URL**: สิ่งนี้ขึ้นอยู่กับ URL ที่คุณใช้เข้าถึง Nextcloud

วิธีตั้งค่า:

1. ใน Nextcloud เปิด **Administrator Security Settings** ของคุณ
2. ค้นหาส่วน **Add client** ใต้ **OAuth 2.0 clients**
3. ป้อน **Name** สำหรับไคลเอ็นต์ของคุณ เช่น `n8n integration`
4. คัดลอก **OAuth Callback URL** จาก n8n และป้อนเป็น **Redirection URI**
5. จากนั้นเลือก **Add** ใน Nextcloud
6. ใน n8n อัปเดต **Authorization URL** เพื่อแทนที่ `https://nextcloud.example.com` ด้วย URL ที่คุณใช้เข้าถึง Nextcloud ตัวอย่างเช่น หากคุณเข้าถึง Nextcloud ที่ `https://cloud.n8n.com` Authorization URL คือ `https://cloud.n8n.com/apps/oauth2/authorize`
7. ใน n8n อัปเดต **Access Token URL** เพื่อแทนที่ `https://nextcloud.example.com` ด้วย URL ที่คุณใช้เข้าถึง Nextcloud ตัวอย่างเช่น หากคุณเข้าถึง Nextcloud ที่ `https://cloud.n8n.com` Access Token URL คือ `https://cloud.n8n.com/apps/oauth2/api/v1/token`

    /// note | Pretty URL configuration
    **Authorization URL** และ **Access Token URL** สันนิษฐานว่าคุณได้กำหนดค่า Nextcloud ให้ใช้ [Pretty URLs](https://docs.nextcloud.com/server/latest/admin_manual/installation/source_installation.html#pretty-urls){:target=_blank .external-link} หากคุณยังไม่ได้ทำ คุณต้องเพิ่ม `/index.php/` ระหว่าง URL Nextcloud ของคุณและส่วน `/apps/oauth2` ตัวอย่างเช่น: `https://cloud.n8n.com/index.php/apps/oauth2/api/v1/token`
    ///
    
8. คัดลอก **Client Identifier** ของ Nextcloud สำหรับไคลเอ็นต์ OAuth2 ของคุณและป้อนเป็น **Client ID** ใน n8n
9. คัดลอก **Secret** ของ Nextcloud และป้อนเป็น **Client Secret** ใน n8n
10. ใน n8n วิธีสร้าง **Web DAV URL** ของคุณ: หาก Nextcloud อยู่ใน root ของ domain ของคุณ ให้ป้อน URL ที่คุณใช้เข้าถึง Nextcloud และเพิ่ม `/remote.php/webdav/` ตัวอย่างเช่น หากคุณเข้าถึง Nextcloud ที่ `https://cloud.n8n.com` WebDAV URL ของคุณคือ `https://cloud.n8n.com/remote.php/webdav`
    - หากคุณติดตั้ง Nextcloud ใน subdirectory ให้ป้อน URL ที่คุณใช้เข้าถึง Nextcloud และเพิ่ม `/<subdirectory>/remote.php/webdav/` แทนที่ `<subdirectory>` ด้วย subdirectory ที่ติดตั้ง Nextcloud
    - อ้างอิงเอกสาร [Third-party WebDAV clients](https://docs.nextcloud.com/server/stable/user_manual/en/files/access_webdav.html#third-party-webdav-clients){:target=_blank .external-link} ของ Nextcloud สำหรับข้อมูลเพิ่มเติมเกี่ยวกับการสร้าง WebDAV URL ของคุณ

อ้างอิงเอกสาร Nextcloud [OAuth2 Configuration documentation](https://docs.nextcloud.com/server/latest/admin_manual/configuration_server/oauth2.html){:target=_blank .external-link} สำหรับคำแนะนำโดยละเอียดเพิ่มเติม
