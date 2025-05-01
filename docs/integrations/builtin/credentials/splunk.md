---
#https://www.notion.so/n8n/Frontmatter-432c2b8dff1f43d4b1c8d20075510fe4
title: Splunk credentials
description: Documentation for Splunk credentials. Use these credentials to authenticate Splunk in n8n, a workflow automation platform.
contentType: [integration, reference]
---

# Splunk credentials

คุณสามารถใช้ credentials เหล่านี้เพื่อยืนยันตัวตนกับ node ต่อไปนี้:

- [Splunk](/integrations/builtin/app-nodes/n8n-nodes-base.splunk.md)

## Prerequisites

- [Download and install](https://www.splunk.com/en_us/download/splunk-enterprise.html){:target=_blank .external-link} Splunk Enterprise
- [Enable token authentication](https://docs.splunk.com/Documentation/Splunk/9.2.1/Security/EnableTokenAuth){:target=_blank .external-link} ที่ **Settings > Tokens**

/// note | Free trial Splunk Cloud Platform accounts can't access the REST API
บัญชี Splunk Cloud Platform แบบทดลองใช้งานฟรีจะไม่สามารถใช้ REST API ได้ ต้องมีสิทธิ์ที่เหมาะสม ดูรายละเอียดที่ [Access requirements and limitations for the Splunk Cloud Platform REST API](https://docs.splunk.com/Documentation/SplunkCloud/8.2.2203/RESTTUT/RESTandCloud){:target=_blank .external-link}
///

## Supported authentication methods

- API auth token

## Related resources

ดูรายละเอียดเพิ่มเติมได้ที่ [Splunk's Enterprise API documentation](https://docs.splunk.com/Documentation/Splunk/latest/RESTREF/RESTprolog){:target=_blank .external-link}

## Using API auth token

ในการตั้งค่า credential นี้ คุณจะต้องมี:

- **Auth Token**: หลังจากเปิดใช้งาน token authentication แล้ว ให้สร้าง auth token ที่ **Settings > Tokens** ดูวิธีที่ [Creating authentication tokens](https://docs.splunk.com/Documentation/Splunk/9.2.1/Security/CreateAuthTokens){:target=_blank .external-link}
- **Base URL**: URL ของ Splunk instance ของคุณ ต้องรวม protocol, domain และ port เช่น `https://localhost:8089`
- **Allow Self-Signed Certificates**: ถ้าเปิดใช้งาน n8n จะเชื่อมต่อแม้ SSL validation จะล้มเหลว

## Required capabilities

บัญชีและ role ของคุณใน Splunk platform ต้องมีความสามารถบางอย่างเพื่อสร้าง authentication tokens:

- `edit_tokens_own`: ถ้าต้องการสร้าง token สำหรับตัวเอง
- `edit_tokens_all`: ถ้าต้องการสร้าง token ให้ user อื่นใน instance

ดูรายละเอียดเพิ่มเติมที่ [Define roles on the Splunk platform with capabilities](https://docs.splunk.com/Documentation/Splunk/9.2.1/Security/Rolesandcapabilities){:target=_blank .external-link}
