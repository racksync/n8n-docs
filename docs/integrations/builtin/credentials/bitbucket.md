---
#https://www.notion.so/n8n/Frontmatter-432c2b8dff1f43d4b1c8d20075510fe4
title: Bitbucket credentials
description: Documentation for Bitbucket credentials. Use these credentials to authenticate Bitbucket in n8n, a workflow automation platform.
contentType: [integration, reference]
---

# Bitbucket credentials

คุณสามารถใช้ credentials นี้เพื่อเชื่อมต่อกับ node เหล่านี้:

- [Bitbucket Trigger](/integrations/builtin/trigger-nodes/n8n-nodes-base.bitbuckettrigger.md)

## Prerequisites

สมัคร [Bitbucket](https://www.bitbucket.com/){:target=_blank .external-link} ให้เรียบร้อยก่อน

## Supported authentication methods

- API username and app password

## Related resources

ดูข้อมูลเพิ่มเติมเกี่ยวกับบริการได้ที่ [Bitbucket's API documentation](https://developer.atlassian.com/cloud/bitbucket/rest/intro/#authentication){:target=_blank .external-link}

## Using API username/app password

ถ้าจะตั้งค่า credentials นี้ คุณต้องมี:

- **Username**: ดูได้ใน Bitbucket profile settings **Personal settings > Account settings**
- **App Password**: ดูคำแนะนำของ Bitbucket เพื่อ [Create an app password](https://support.atlassian.com/bitbucket-cloud/docs/create-an-app-password/){:target=_blank .external-link}

## App password permissions

Bitbucket API credentials จะทำงานได้ก็ต่อเมื่อบัญชีผู้ใช้ที่คุณสร้าง app password ให้มี privilege scopes ที่เหมาะสมสำหรับ app password permissions ที่เลือกไว้ กล่องโต้ตอบ n8n credentials จะแสดงข้อผิดพลาดหากบัญชีผู้ใช้ไม่มี permissions ที่เหมาะสมสำหรับ scope ที่เลือก เช่น `Your credentials lack one or more required privilege scopes`

ดูข้อมูลเพิ่มเติมเกี่ยวกับการทำงานกับ permissions เหล่านี้ได้ที่ [Bitbucket App password permissions documentation](https://support.atlassian.com/bitbucket-cloud/docs/app-password-permissions/){:target=_blank .external-link}

