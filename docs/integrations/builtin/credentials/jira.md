---
#https://www.notion.so/n8n/Frontmatter-432c2b8dff1f43d4b1c8d20075510fe4
title: Jira credentials
description: Documentation for Jira credentials. Use these credentials to authenticate Jira in n8n, a workflow automation platform.
contentType: [integration, reference]
priority: medium
---

# Jira credentials

คุณสามารถใช้ credentials เหล่านี้เพื่อยืนยันตัวตนกับ node ต่อไปนี้ได้:

- [Jira](/integrations/builtin/app-nodes/n8n-nodes-base.jira.md)
- [Jira Trigger](/integrations/builtin/trigger-nodes/n8n-nodes-base.jiratrigger.md)

## Prerequisites

สร้างบัญชี [Jira](https://www.atlassian.com/software/jira){:target=_blank .external-link} Software Cloud หรือ Server

## Supported authentication methods

- [SW Cloud API token](#using-sw-cloud-api-token): ใช้วิธีนี้กับ [Jira Software Cloud](https://www.atlassian.com/software/jira){:target=_blank .external-link}
- [SW Server account](#using-sw-server-account): ใช้วิธีนี้กับ [Jira Software Server](https://www.atlassian.com/software/jira/download.){:target=_blank .external-link}

## Related resources

ดูข้อมูลเพิ่มเติมเกี่ยวกับบริการนี้ได้ที่ [Jira's API documentation](https://developer.atlassian.com/cloud/jira/platform/rest/v2/intro/#about){:target=_blank .external-link}

## Using SW Cloud API token

ในการตั้งค่า credential นี้ คุณจะต้องมีบัญชีบน [Jira Software Cloud](https://www.atlassian.com/software/jira){:target=_blank .external-link}

จากนั้น:

1.  เข้าสู่ระบบโปรไฟล์ Atlassian ของคุณ > หน้า **Security > API tokens** หรือไปที่นั่นโดยตรงโดยใช้ [link](https://id.atlassian.com/manage-profile/security/api-tokens){:target=_blank .external-link} นี้
2.  เลือก **Create API Token**
3.  ป้อน **Label** ที่ดีสำหรับ token ของคุณ เช่น `n8n integration`
4.  เลือก **Create**
5.  คัดลอก API token
6.  ใน n8n ป้อน **Email** address ที่เชื่อมโยงกับบัญชี Jira ของคุณ
7.  วาง API token ที่คุณคัดลอกมาเป็น **API Token** ของคุณ
8.  ป้อน **Domain** ที่คุณเข้าถึง Jira เช่น `https://example.atlassian.net`

ดูข้อมูลเพิ่มเติมได้ที่ [Manage API tokens for your Atlassian account](https://support.atlassian.com/atlassian-account/docs/manage-api-tokens-for-your-atlassian-account/){:target=_blank .external-link}

/// note | New tokens
token ใหม่อาจใช้เวลาถึงหนึ่งนาทีก่อนที่จะใช้งานได้ หากการยืนยัน credential ของคุณล้มเหลวในครั้งแรก ให้รอสักครู่ก่อนลองอีกครั้ง
///

## Using SW Server account

ในการตั้งค่า credential นี้ คุณจะต้องมีบัญชีบน [Jira Software Server](https://www.atlassian.com/software/jira/download.){:target=_blank .external-link}

จากนั้น:

1.  ป้อน **Email** address ที่เชื่อมโยงกับบัญชี Jira ของคุณ
2.  ป้อน **Password** บัญชี Jira ของคุณ
3.  ป้อน **Domain** ที่คุณเข้าถึง Jira

