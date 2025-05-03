---
#https://www.notion.so/n8n/Frontmatter-432c2b8dff1f43d4b1c8d20075510fe4
title: Google OAuth2 แบบทั่วไป
description: เอกสารสำหรับ Google credentials ประเภท OAuth2 แบบทั่วไป ใช้ credential นี้เพื่อยืนยันตัวตนบริการ Google ใน n8n แพลตฟอร์ม workflow automation
contentType: [integration, reference]
---

# Google: OAuth2 generic

เอกสารนี้มีคำแนะนำในการสร้าง Google OAuth2 credential แบบทั่วไปสำหรับใช้กับ [custom operations](/integrations/custom-operations.md)

--8<-- "_snippets/integrations/managed-google-oauth.md"

## Prerequisites

* สร้างบัญชี [Google Cloud](https://cloud.google.com/){:targe=_blank .external-link}

## Set up OAuth

มีห้าขั้นตอนในการเชื่อมต่อ credential ของ n8n กับบริการของ Google:

- [Google: OAuth2 generic](#google-oauth2-generic)
	- [Prerequisites](#prerequisites)
	- [Set up OAuth](#set-up-oauth)
		- [Create a Google Cloud Console project](#create-a-google-cloud-console-project)
		- [Enable APIs](#enable-apis)
		- [Configure your OAuth consent screen](#configure-your-oauth-consent-screen)
		- [Create your Google OAuth client credentials](#create-your-google-oauth-client-credentials)
		- [Finish your n8n credential](#finish-your-n8n-credential)
	- [Video](#video)
	- [Scopes](#scopes)
	- [Troubleshooting](#troubleshooting)
		- [Google hasn't verified this app](#google-hasnt-verified-this-app)
		- [Google Cloud app becoming unauthorized](#google-cloud-app-becoming-unauthorized)

### Create a Google Cloud Console project

ขั้นแรก สร้างโปรเจกต์ Google Cloud Console หากคุณมีโปรเจกต์อยู่แล้ว ข้ามไปที่ส่วนถัดไป:

1. ล็อกอินเข้าสู่ [Google Cloud Console](https://console.cloud.google.com){:target=_blank .external-link} โดยใช้ข้อมูลประจำตัว Google ของคุณ
2. ในเมนูด้านบน เลือก dropdown ของโปรเจกต์ในแถบนำทางด้านบนและเลือก **New project** หรือไปที่หน้า [New Project](https://console.cloud.google.com/projectcreate){:target=_blank .external-link} โดยตรง
3. ป้อน **Project name** และเลือก **Location** สำหรับโปรเจกต์ของคุณ
4. เลือก **Create**
5. ตรวจสอบแถบนำทางด้านบนและตรวจสอบให้แน่ใจว่า dropdown **Select a project** ได้เลือกโปรเจกต์ของคุณแล้ว หากไม่ ให้เลือกโปรเจกต์ที่คุณเพิ่งสร้าง

	<figure markdown="span">
	![The project dropdown in the Google Cloud top navigation](/_images/integrations/builtin/credentials/google/google-cloud-project-dropdown.png)
	<figcaption>ตรวจสอบ dropdown ของโปรเจกต์ในแถบนำทางด้านบนของ Google Cloud</figcaption>
	</figure>

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
7. เลือก **SAVE AND CONTINUE** เพื่อไปยังหน้า **Data Access** และเปิด **Add or remove scopes**
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
3. คุณต้องระบุ scope สำหรับ credential นี้ อ้างอิง [Scopes](#scopes) สำหรับข้อมูลเพิ่มเติม ป้อนหลาย scope โดยคั่นด้วยช่องว่าง ตัวอย่างเช่น:
	```
	https://www.googleapis.com/auth/gmail.labels https://www.googleapis.com/auth/gmail.addons.current.action.compose
	```
4. ใน n8n เลือก **Sign in with Google** เพื่อทำการยืนยันตัวตน Google ของคุณให้เสร็จสมบูรณ์
5. **Save** credentials ใหม่ของคุณ

## Video

วิดีโอต่อไปนี้สาธิตขั้นตอนที่อธิบายไว้ข้างต้น:


<div class="video-container">
<iframe width="840" height="472.5" src="https://www.youtube.com/embed/gZ6N2H3_vys" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
</div>

## Scopes

บริการของ Google มี scope การเข้าถึงที่เป็นไปได้อย่างน้อยหนึ่งรายการ scope จะจำกัดสิ่งที่ผู้ใช้สามารถทำได้ อ้างอิง [OAuth 2.0 Scopes for Google APIs](https://developers.google.com/identity/protocols/oauth2/scopes){:target=_blank .external-link} สำหรับรายการ scope ของบริการทั้งหมด

n8n ไม่รองรับ scope ทั้งหมด เมื่อสร้าง Google OAuth2 API credential แบบทั่วไป คุณสามารถป้อน scope จากรายการ **Supported scopes** ด้านล่าง หากคุณป้อน scope ที่ n8n ยังไม่รองรับ มันจะไม่ทำงาน

??? Details "Supported scopes"
	| Service | Available scopes |
	| ------- | ---------------- |
	| Gmail | 	https://www.googleapis.com/auth/gmail.labels <br /> https://www.googleapis.com/auth/gmail.addons.current.action.compose <br />	https://www.googleapis.com/auth/gmail.addons.current.message.action <br /> https://mail.google.com/ <br /> https://www.googleapis.com/auth/gmail.modify <br />	https://www.googleapis.com/auth/gmail.compose |
	| Google Ads | https://www.googleapis.com/auth/adwords |
	| Google Analytics | https://www.googleapis.com/auth/analytics <br /> https://www.googleapis.com/auth/analytics.readonly |
	| Google BigQuery | https://www.googleapis.com/auth/bigquery |
	| Google Books | https://www.googleapis.com/auth/books |
	| Google Calendar | 	https://www.googleapis.com/auth/calendar <br /> https://www.googleapis.com/auth/calendar.events |
	| Google Cloud Natural Language | https://www.googleapis.com/auth/cloud-language <br /> https://www.googleapis.com/auth/cloud-platform |
	| Google Cloud Storage | https://www.googleapis.com/auth/cloud-platform <br /> https://www.googleapis.com/auth/cloud-platform.read-only <br /> https://www.googleapis.com/auth/devstorage.full_control <br /> https://www.googleapis.com/auth/devstorage.read_only <br /> https://www.googleapis.com/auth/devstorage.read_write |
	| Google Contacts | https://www.googleapis.com/auth/contacts |
	| Google Docs | https://www.googleapis.com/auth/documents <br /> https://www.googleapis.com/auth/drive <br /> https://www.googleapis.com/auth/drive.file |
	| Google Drive | https://www.googleapis.com/auth/drive <br /> https://www.googleapis.com/auth/drive.appdata <br /> https://www.googleapis.com/auth/drive.photos.readonly |
	| Google Firebase Cloud Firestore | https://www.googleapis.com/auth/datastore <br /> https://www.googleapis.com/auth/firebase |
	| Google Firebase Realtime Database | https://www.googleapis.com/auth/userinfo.email <br /> https://www.googleapis.com/auth/firebase.database <br /> https://www.googleapis.com/auth/firebase |
	| Google Perspective | https://www.googleapis.com/auth/userinfo.email |
	| Google Sheets | https://www.googleapis.com/auth/drive.file <br /> https://www.googleapis.com/auth/spreadsheets |
	| Google Slide | https://www.googleapis.com/auth/drive.file <br /> https://www.googleapis.com/auth/presentations |
	| Google Tasks | https://www.googleapis.com/auth/tasks |
	| Google Translate | https://www.googleapis.com/auth/cloud-translation |
	| GSuite Admin | https://www.googleapis.com/auth/admin.directory.group <br /> https://www.googleapis.com/auth/admin.directory.user <br /> https://www.googleapis.com/auth/admin.directory.domain.readonly <br /> https://www.googleapis.com/auth/admin.directory.userschema.readonly |

## Troubleshooting

### Google hasn't verified this app

--8<-- "_snippets/integrations/builtin/credentials/google/unverified-app.md"

### Google Cloud app becoming unauthorized

--8<-- "_snippets/integrations/builtin/credentials/google/app-becoming-unauthorized.md"