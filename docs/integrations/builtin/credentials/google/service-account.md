---
#https://www.notion.so/n8n/Frontmatter-432c2b8dff1f43d4b1c8d20075510fe4
title: Google Service Account
description: เอกสารสำหรับ Google credentials ประเภท Service Account ใช้ credential นี้เพื่อยืนยันตัวตน Google ใน n8n แพลตฟอร์ม workflow automation
contentType: [integration, reference]
---

# Google: Service Account

การใช้ Service Account มีความซับซ้อนกว่า OAuth2 ก่อนที่คุณจะเริ่ม:

* ตรวจสอบว่า node ของคุณ [เข้ากันได้](/integrations/builtin/credentials/google/index.md#compatible-nodes) กับ Service Account หรือไม่
* ตรวจสอบให้แน่ใจว่าคุณจำเป็นต้องใช้ Service Account จริงๆ สำหรับกรณีการใช้งานส่วนใหญ่ [OAuth2](/integrations/builtin/credentials/google/oauth-single-service.md) เป็นตัวเลือกที่ดีกว่า
* อ่านเอกสารของ Google เกี่ยวกับ [Creating and managing service accounts](https://cloud.google.com/iam/docs/creating-managing-service-accounts){:target=_blank .external-link}

## Prerequisites

* สร้างบัญชี [Google Cloud](https://cloud.google.com/){:targe=_blank .external-link}

## Set up Service Account

มีสี่ขั้นตอนในการเชื่อมต่อ credential ของ n8n กับ Google Service Account:

- [Google: Service Account](#google-service-account)
	- [Prerequisites](#prerequisites)
	- [Set up Service Account](#set-up-service-account)
		- [Create a Google Cloud Console project](#create-a-google-cloud-console-project)
		- [Enable APIs](#enable-apis)
		- [Set up Google Cloud Service Account](#set-up-google-cloud-service-account)
		- [Finish your n8n credential](#finish-your-n8n-credential)
	- [Video](#video)
	- [Troubleshooting](#troubleshooting)
		- [Service Account can't access Google Drive files](#service-account-cant-access-google-drive-files)
		- [Enable domain-wide delegation](#enable-domain-wide-delegation)

### Create a Google Cloud Console project

ขั้นแรก สร้างโปรเจกต์ Google Cloud Console หากคุณมีโปรเจกต์อยู่แล้ว ข้ามไปที่ส่วนถัดไป:

--8<-- "_snippets/integrations/builtin/credentials/google/create-google-cloud-project.md"

### Enable APIs

เมื่อสร้างโปรเจกต์ของคุณแล้ว เปิดใช้งาน APIs ที่คุณต้องการเข้าถึง:

--8<-- "_snippets/integrations/builtin/credentials/google/enable-apis.md"

### Set up Google Cloud Service Account

1. เข้าถึง [Google Cloud Console - Library](https://console.cloud.google.com/apis/library){:target=_blank .external-link} ของคุณ ตรวจสอบให้แน่ใจว่าคุณอยู่ในโปรเจกต์ที่ถูกต้อง

	<figure markdown="span">
	![The project dropdown in the Google Cloud top navigation](/_images/integrations/builtin/credentials/google/google-cloud-project-dropdown.png)
	<figcaption>ตรวจสอบ dropdown ของโปรเจกต์ในแถบนำทางด้านบนของ Google Cloud</figcaption>
	</figure>

1. เลือกเมนูแฮมเบอร์เกอร์ **> APIs & Services > Credentials** Google จะนำคุณไปยังหน้า **Credentials** ของคุณ
2. เลือก **+ CREATE CREDENTIALS > Service account**
3. ป้อนชื่อใน **Service account name** และ ID ใน **Service account ID** อ้างอิง [Creating a service account](https://cloud.google.com/iam/docs/creating-managing-service-accounts?hl=en#creating){:target=_blank .external-link} สำหรับข้อมูลเพิ่มเติม
4. เลือก **CREATE AND CONTINUE**
5. ขึ้นอยู่กับกรณีการใช้งานของคุณ คุณอาจต้องการ **Select a role** และ **Grant users access to this service account** โดยใช้ส่วนที่เกี่ยวข้อง
6. เลือก **DONE**
7. เลือก Service Account ที่คุณเพิ่งสร้างขึ้นภายใต้ส่วน **Service Accounts** เปิดแท็บ **KEYS**
8. เลือก **ADD KEY > Create new key**
9. ใน modal ที่ปรากฏขึ้น เลือก **JSON** จากนั้นเลือก **CREATE** Google จะบันทึกไฟล์ลงในคอมพิวเตอร์ของคุณ

### Finish your n8n credential

เมื่อโปรเจกต์และ credentials ของ Google ได้รับการกำหนดค่าอย่างสมบูรณ์แล้ว ให้ดำเนินการ credential ของ n8n ให้เสร็จสิ้น:

1. เปิดไฟล์ JSON ที่ดาวน์โหลดมา
2. คัดลอก `client_email` และป้อนลงใน credential ของ n8n ของคุณเป็น **Service Account Email**
3. คัดลอก `private_key` ไม่ต้องรวมเครื่องหมาย `"` ที่อยู่รอบๆ ป้อนค่านี้เป็น **Private Key** ใน credential ของ n8n ของคุณ

	///warning | Older versions of n8n
	หากคุณใช้ n8n เวอร์ชันเก่ากว่า 0.156.0 ให้แทนที่ `\n` ทั้งหมดในไฟล์ JSON ด้วยการขึ้นบรรทัดใหม่
	///

4. **Optional**: เลือกว่าคุณต้องการ [**Impersonate a User**](https://developers.google.com/identity/protocols/oauth2/service-account#delegatingauthority){:target=_blank .external-link} (เปิดใช้งาน) หรือไม่
    1. หากต้องการใช้ตัวเลือกนี้ คุณต้อง [Enable domain-wide delegation](#enable-domain-wide-delegation) สำหรับ Service Account ในฐานะ super admin ของ Google Workspace
	1. ป้อน **Email** ของผู้ใช้ที่คุณต้องการ impersonate
5. หากคุณวางแผนที่จะใช้ credential นี้กับโหนด [HTTP Request](/integrations/builtin/core-nodes/n8n-nodes-base.httprequest/index.md) ให้เปิด **Set up for use in HTTP Request node**
	1. เมื่อเปิดการตั้งค่านี้ คุณจะต้องเพิ่ม **Scope(s)** สำหรับโหนด n8n จะเติม scope บางส่วนไว้ล่วงหน้า อ้างอิง [OAuth 2.0 Scopes for Google APIs](https://developers.google.com/identity/protocols/oauth2/scopes){:target=_blank .external-link} สำหรับข้อมูลเพิ่มเติม
6. **Save** credentials ของคุณ

## Video

วิดีโอต่อไปนี้สาธิตขั้นตอนที่อธิบายไว้ข้างต้น

<div class="video-container">
<iframe width="840" height="472.5" src="https://www.youtube.com/embed/ArXVlpo3y1k" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
</div>

## Troubleshooting

### Service Account can't access Google Drive files

Service Account ไม่สามารถเข้าถึงไฟล์และโฟลเดอร์ Google Drive ที่ไม่ได้แชร์กับอีเมลผู้ใช้ที่เกี่ยวข้อง

1. เข้าถึง [Google Cloud Console](https://console.cloud.google.com){:target=_blank .external-link} ของคุณและคัดลอกอีเมล Service Account ของคุณ
2. เข้าถึง [Google Drive](https://drive.google.com){:target=_blank .external-link} ของคุณและไปที่ไฟล์หรือโฟลเดอร์ที่กำหนด
3. คลิกขวาที่ไฟล์หรือโฟลเดอร์แล้วเลือก **Share**
4. วางอีเมล Service Account ของคุณลงใน **Add People and groups**
5. เลือก **Editor** สำหรับการเข้าถึงแบบอ่าน-เขียน หรือ **Viewer** สำหรับการเข้าถึงแบบอ่านอย่างเดียว

### Enable domain-wide delegation

ในการ impersonate ผู้ใช้ด้วย Service Account คุณต้องเปิดใช้งาน domain-wide delegation สำหรับ Service Account นั้น

/// warning | Not recommended
Google แนะนำให้คุณ [หลีกเลี่ยงการใช้ domain-wide delegation](https://cloud.google.com/iam/docs/best-practices-service-accounts#domain-wide-delegation){:target=_blank .external-link} เนื่องจากอนุญาตให้ impersonate ผู้ใช้คนใดก็ได้ (รวมถึง super admins) และอาจก่อให้เกิดความเสี่ยงด้านความปลอดภัย
///

ในการมอบสิทธิ์ domain-wide ให้กับ Service Account คุณต้องเป็น super administrator สำหรับโดเมน Google Workspace จากนั้น:

1. จาก [Admin console](https://admin.google.com/){:target=_blank .external-link} ของโดเมน Google Workspace ของคุณ เลือกเมนูแฮมเบอร์เกอร์ จากนั้นเลือก **Security > Access and data control > API Controls**
2. ในบานหน้าต่าง **Domain wide delegation** เลือก **Manage Domain Wide Delegation**
3. เลือก **Add new**
4. ในฟิลด์ **Client ID** ป้อน **Client ID** ของ Service Account หากต้องการรับ Client ID:
    * เปิดโปรเจกต์ Google Cloud Console ของคุณ จากนั้นเปิดหน้า [Service Accounts](https://console.cloud.google.com/iam-admin/serviceaccounts){:target=_blank .external-link}
    * คัดลอก **OAuth 2 Client ID** และใช้เป็น **Client ID** สำหรับ **Domain Wide Delegation**
5. ในฟิลด์ **OAuth scopes** ป้อนรายการ scope ที่คั่นด้วยเครื่องหมายจุลภาค เพื่อให้สิทธิ์แอปพลิเคชันของคุณเข้าถึง ตัวอย่างเช่น หากแอปพลิเคชันของคุณต้องการสิทธิ์เข้าถึง Google Drive API และ Google Calendar API แบบเต็มรูปแบบทั้งโดเมน ให้ป้อน: `https://www.googleapis.com/auth/drive, https://www.googleapis.com/auth/calendar`
6. เลือก **Authorize**

อาจใช้เวลาตั้งแต่ 5 นาทีถึง 24 ชั่วโมง ก่อนที่คุณจะสามารถ impersonate ผู้ใช้ทั้งหมดใน Workspace ของคุณได้
