---
#https://www.notion.so/n8n/Frontmatter-432c2b8dff1f43d4b1c8d20075510fe4
title: Google credentials
description: เอกสารสำหรับ Google credentials ใช้ credential นี้เพื่อยืนยันตัวตน Google ใน n8n แพลตฟอร์ม workflow automation
contentType: overview
---

# Google credentials

ส่วนนี้ประกอบด้วย:

* [OAuth2 single service](/integrations/builtin/credentials/google/oauth-single-service.md): สร้าง OAuth2 credential สำหรับ node บริการเฉพาะ เช่น node Gmail
* [OAuth2 generic](/integrations/builtin/credentials/google/oauth-generic.md): สร้าง OAuth2 credential สำหรับใช้กับ [custom operations](/integrations/custom-operations.md)
* [Service Account](/integrations/builtin/credentials/google/service-account.md): สร้าง [Service Account](https://cloud.google.com/iam/docs/service-account-overview){:target=_blank .external-link} credential สำหรับ node บริการเฉพาะบางตัว
* [Google PaLM and Gemini](/integrations/builtin/credentials/googleai.md): รับ Google Gemini/Google PaLM API key


## OAuth2 and Service Account

มีวิธีการยืนยันตัวตนสองวิธีสำหรับ node บริการของ Google:

* [OAuth2](https://developers.google.com/identity/protocols/oauth2){:target=_blank .external-link}: แนะนำเนื่องจากมีการใช้งานที่กว้างขวางกว่าและตั้งค่าได้ง่ายกว่า
* [Service Account](https://cloud.google.com/iam/docs/understanding-service-accounts){:target=_blank .external-link}: อ้างอิงเอกสาร [Google documentation: Understanding service accounts](https://cloud.google.com/iam/docs/understanding-service-accounts){:target=_blank .external-link} สำหรับคำแนะนำเกี่ยวกับเวลาที่คุณต้องการ Service Account

--8<-- "_snippets/integrations/managed-google-oauth.md"

## Compatible nodes

เมื่อกำหนดค่าแล้ว คุณสามารถใช้ credentials ของคุณเพื่อยืนยันตัวตน node ต่อไปนี้ Node ส่วนใหญ่เข้ากันได้กับการยืนยันตัวตนแบบ OAuth2 การรองรับการยืนยันตัวตนแบบ Service Account มีจำกัด


| Node | OAuth | Service Account |
| :--- | :---: | :-------------: |
| [Google Ads](/integrations/builtin/app-nodes/n8n-nodes-base.googleads.md) | :white_check_mark: | :x: |
| [Gmail](/integrations/builtin/app-nodes/n8n-nodes-base.gmail/index.md) | :white_check_mark: | :warning: |
| [Google Analytics](/integrations/builtin/app-nodes/n8n-nodes-base.googleanalytics.md) | :white_check_mark: | :x: |
| [Google BigQuery](/integrations/builtin/app-nodes/n8n-nodes-base.googlebigquery.md) | :white_check_mark: | :white_check_mark: |
| [Google Books](/integrations/builtin/app-nodes/n8n-nodes-base.googlebooks.md) | :white_check_mark: | :white_check_mark: |
| [Google Calendar](/integrations/builtin/app-nodes/n8n-nodes-base.googlecalendar/index.md) | :white_check_mark: | :x: |
| [Google Chat](/integrations/builtin/app-nodes/n8n-nodes-base.googlechat.md) | :x: | :white_check_mark: |
| [Google Cloud Storage](/integrations/builtin/app-nodes/n8n-nodes-base.googlecloudstorage.md) | :white_check_mark: | :x: |
| [Google Contacts](/integrations/builtin/app-nodes/n8n-nodes-base.googlecontacts.md) | :white_check_mark: | :x: |
| [Google Cloud Firestore](/integrations/builtin/app-nodes/n8n-nodes-base.googlecloudfirestore.md) | :white_check_mark: | :white_check_mark: |
| [Google Cloud Natural Language](/integrations/builtin/app-nodes/n8n-nodes-base.googlecloudnaturallanguage.md) | :white_check_mark: | :x: |
| [Google Cloud Realtime Database](/integrations/builtin/app-nodes/n8n-nodes-base.googlecloudrealtimedatabase.md) | :white_check_mark: | :x: |
| [Google Docs](/integrations/builtin/app-nodes/n8n-nodes-base.googledocs.md) | :white_check_mark: | :white_check_mark: |
| [Google Drive](/integrations/builtin/app-nodes/n8n-nodes-base.googledrive/index.md) | :white_check_mark: | :white_check_mark: |
| [Google Drive Trigger](/integrations/builtin/trigger-nodes/n8n-nodes-base.googledrivetrigger/index.md) | :white_check_mark: | :white_check_mark: |
| [Google Perspective](/integrations/builtin/app-nodes/n8n-nodes-base.googleperspective.md) | :white_check_mark: | :x: |
| [Google Sheets](/integrations/builtin/app-nodes/n8n-nodes-base.googlesheets/index.md) | :white_check_mark: | :white_check_mark: |
| [Google Slides](/integrations/builtin/app-nodes/n8n-nodes-base.googleslides.md) | :white_check_mark: | :white_check_mark: |
| [Google Tasks](/integrations/builtin/app-nodes/n8n-nodes-base.googletasks.md) | :white_check_mark: | :x: |
| [Google Translate](/integrations/builtin/app-nodes/n8n-nodes-base.googletranslate.md) | :white_check_mark: | :white_check_mark: |
| [Google Workspace Admin](/integrations/builtin/app-nodes/n8n-nodes-base.gsuiteadmin.md) | :white_check_mark: | :x: |
| [YouTube](/integrations/builtin/app-nodes/n8n-nodes-base.youtube.md) | :white_check_mark: | :x: |

/// warning | Gmail and Service Accounts
ทางเทคนิคแล้ว Google รองรับ Service Accounts สำหรับใช้กับ Gmail แต่ต้องเปิดใช้งาน domain-wide delegation ซึ่ง Google ไม่แนะนำ และพฤติกรรมอาจไม่สอดคล้องกัน

n8n แนะนำให้ใช้ OAuth2 กับ node Gmail
///
