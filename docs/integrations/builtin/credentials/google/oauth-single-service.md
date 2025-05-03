---
#https://www.notion.so/n8n/Frontmatter-432c2b8dff1f43d4b1c8d20075510fe4
title: Google OAuth2 สำหรับบริการเดียว
description: เอกสารสำหรับ Google credentials ประเภท OAuth2 สำหรับบริการเดียว ใช้ credential นี้เพื่อยืนยันตัวตน Google ใน n8n แพลตฟอร์ม workflow automation
contentType: [integration, reference]
priority: critical
---

# Google: OAuth2 single service

เอกสารนี้มีคำแนะนำในการสร้าง Google credential สำหรับบริการเดียว นอกจากนี้ยังมีในรูปแบบ [video](#video)

--8<-- "_snippets/integrations/managed-google-oauth.md"

## Prerequisites

* สร้างบัญชี [Google Cloud](https://cloud.google.com/){:target=_blank .external-link}

## Set up OAuth

มีห้าขั้นตอนในการเชื่อมต่อ credential ของ n8n กับบริการของ Google:

1. [Create a Google Cloud Console project](#create-a-google-cloud-console-project)
1. [Enable APIs](#enable-apis)
1. [Configure your OAuth consent screen](#configure-your-oauth-consent-screen)
1. [Create your Google OAuth client credentials](#create-your-google-oauth-client-credentials)
1. [Finish your n8n credential](#finish-your-n8n-credential)

### Create a Google Cloud Console project

ขั้นแรก สร้างโปรเจกต์ Google Cloud Console หากคุณมีโปรเจกต์อยู่แล้ว ข้ามไปที่ส่วนถัดไป:

--8<-- "_snippets/integrations/builtin/credentials/google/create-google-cloud-project.md"

### Enable APIs

เมื่อสร้างโปรเจกต์ของคุณแล้ว เปิดใช้งาน APIs ที่คุณต้องการเข้าถึง:

--8<-- "_snippets/integrations/builtin/credentials/google/enable-apis.md"

### Configure your OAuth consent screen

หากคุณไม่เคยใช้ OAuth ในโปรเจกต์ Google Cloud ของคุณมาก่อน คุณจะต้อง [configure the OAuth consent screen](https://developers.google.com/workspace/guides/configure-oauth-consent){:target=_blank .external-link}:

1. เข้าถึง [Google Cloud Console - Library](https://console.cloud.google.com/apis/library){:target=_blank .external-link} ของคุณ ตรวจสอบให้แน่ใจว่าคุณอยู่ในโปรเจกต์ที่ถูกต้อง
	<figure markdown="span">
	![The project dropdown in the Google Cloud top navigation](/_images/integrations/builtin/credentials/google/google-cloud-project-dropdown.png)
	<figcaption>ตรวจสอบ dropdown ของโปรเจกต์ในแถบนำทางด้านบนของ Google Cloud</figcaption>
	</figure>
1. เปิดเมนูนำทางด้านซ้ายและไปที่ **APIs & Services > OAuth consent screen**
2. สำหรับ **User Type** เลือก **Internal** สำหรับการเข้าถึงของผู้ใช้ภายใน Google Workspace ขององค์กรของคุณ หรือ **External** สำหรับผู้ใช้ใดๆ ที่มีบัญชี Google อ้างอิงเอกสาร [User type documentation](https://support.google.com/cloud/answer/10311615#user-type&zippy=%2Cexternal%2Cinternal){:target=_blank .external-link} ของ Google สำหรับข้อมูลเพิ่มเติมเกี่ยวกับประเภทผู้ใช้
3. เลือก **Create**
4. ป้อนข้อมูลที่จำเป็น:
	- **App name**
	- **User support email**
	- ฟิลด์ **Email addresses** ใน **Developer contact information**
5. ในส่วน **Authorized domains** เพิ่ม `n8n.cloud` หากใช้บริการ Cloud ของ n8n หากคุณ [self-hosting](/hosting/index.md) ให้เพิ่มโดเมนของ instance n8n ของคุณ
7. เลือก **SAVE AND CONTINUE** เพื่อไปยังหน้า **Scopes**
8. คุณไม่จำเป็นต้องตั้งค่า scope ใดๆ เลือก **SAVE AND CONTINUE** อีกครั้งเพื่อไปยังหน้า **Summary**
9. ในหน้า **Summary** ตรวจสอบข้อมูลเพื่อความถูกต้อง

### Create your Google OAuth client credentials

ถัดไป สร้าง OAuth client credentials ใน Google:

1. ในส่วน **APIs & Services** เลือก **Credentials**
2. เลือก **+ CREATE CREDENTIALS > OAuth client ID**
3. ใน dropdown **Application type** เลือก **Web application**
4. Google จะสร้าง **Name** โดยอัตโนมัติ อัปเดต **Name** เป็นชื่อที่คุณจะจำได้ใน console ของคุณ
5. จาก credential ของ n8n ของคุณ คัดลอก **OAuth Redirect URL** วางลงใน **Authorized redirect URIs** ใน Google Console
6. เลือก **CREATE**

### Finish your n8n credential

เมื่อโปรเจกต์และ credentials ของ Google ได้รับการกำหนดค่าอย่างสมบูรณ์แล้ว ให้ดำเนินการ credential ของ n8n ให้เสร็จสิ้น:

1. จาก modal **OAuth client created** ของ Google คัดลอก **Client ID** ป้อนค่านี้ใน credential ของ n8n ของคุณ
2. จาก modal เดียวกันของ Google คัดลอก **Client Secret** ป้อนค่านี้ใน credential ของ n8n ของคุณ
2. ใน n8n เลือก **Sign in with Google** เพื่อทำการยืนยันตัวตน Google ของคุณให้เสร็จสมบูรณ์
3. **Save** credentials ใหม่ของคุณ

## Video

<div class="video-container">
<iframe width="840" height="472.5" src="https://www.youtube.com/embed/gZ6N2H3_vys" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
</div>

## Troubleshooting

### Google hasn't verified this app

--8<-- "_snippets/integrations/builtin/credentials/google/unverified-app.md"

### Google Cloud app becoming unauthorized

--8<-- "_snippets/integrations/builtin/credentials/google/app-becoming-unauthorized.md"

