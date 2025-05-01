---
#https://www.notion.so/n8n/Frontmatter-432c2b8dff1f43d4b1c8d20075510fe4
title: LinkedIn credentials
description: Documentation for LinkedIn credentials. Use these credentials to authenticate LinkedIn in n8n, a workflow automation platform.
contentType: [integration, reference]
priority: medium
---

# LinkedIn credentials

คุณสามารถใช้ credentials เหล่านี้เพื่อยืนยันตัวตนกับ node ต่อไปนี้ได้:

- [LinkedIn](/integrations/builtin/app-nodes/n8n-nodes-base.linkedin.md)


## Prerequisites

*   สร้างบัญชี [LinkedIn](https://www.linkedin.com/){:target=_blank .external-link}
*   สร้าง [Company Page](https://www.linkedin.com/help/linkedin/answer/a543852){:target=_blank .external-link} บน LinkedIn

## Supported authentication methods

- **Community Management OAuth2**: ใช้วิธีนี้หากคุณเป็นผู้ใช้ LinkedIn ใหม่ หรือกำลังสร้างแอป LinkedIn ใหม่
- **OAuth2**: ใช้วิธีนี้สำหรับแอป LinkedIn และบัญชีผู้ใช้ที่เก่ากว่า

## Related Resources

ดูข้อมูลเพิ่มเติมเกี่ยวกับบริการนี้ได้ที่ [LinkedIn's Community Management API documentation](https://learn.microsoft.com/en-us/linkedin/marketing/community-management/community-management-overview?view=li-lms-2024-04){:target=_blank .external-link}

credential นี้ทำงานร่วมกับ API version `202404`

## Using Community Management OAuth2

ใช้วิธีนี้หากคุณเป็นผู้ใช้ LinkedIn ใหม่ หรือกำลังสร้างแอป LinkedIn ใหม่

ในการตั้งค่า credential นี้ คุณจะต้องมีบัญชี [LinkedIn](https://www.linkedin.com/){:target=_blank .external-link}, [Company Page](https://www.linkedin.com/help/linkedin/answer/a543852){:target=_blank .external-link} บน LinkedIn และ:

- **Client ID**: สร้างขึ้นหลังจากที่คุณสร้าง developer app ใหม่
- **Client Secret**: สร้างขึ้นหลังจากที่คุณสร้าง developer app ใหม่

วิธีสร้าง developer app ใหม่และตั้งค่า credential:

1.  เข้าสู่ระบบ LinkedIn และเลือก link นี้เพื่อ [create a new developer app](https://www.linkedin.com/developers/apps/new){:target=_blank .external-link}
2.  ป้อน **App name** สำหรับแอปของคุณ เช่น `n8n integration`
3.  สำหรับ **LinkedIn Page** ให้ป้อน [Company Page](https://www.linkedin.com/help/linkedin/answer/a543852){:target=_blank .external-link} ของ LinkedIn หรือใช้ link **Create a new LinkedIn Page** เพื่อสร้างหน้าใหม่ทันที ดูข้อมูลเพิ่มเติมได้ที่ [Associate an App with a LinkedIn Page](https://www.linkedin.com/help/linkedin/answer/a548360){:target=_blank .external-link}
4.  เพิ่ม **App logo**
5.  ทำเครื่องหมายในช่องเพื่อยอมรับ **Legal agreement**
6.  เลือก **Create app**
7.  ขั้นตอนนี้ควรเปิดแท็บ **Products** เลือก products/APIs ที่คุณต้องการเปิดใช้งานสำหรับแอปของคุณ เพื่อให้ LinkedIn node ทำงานได้อย่างถูกต้อง คุณต้องรวม:
    *   **Share on LinkedIn**
    *   **Sign In with LinkedIn using OpenID Connect**
8.  เมื่อคุณขอเข้าถึง products ที่ต้องการแล้ว ให้เปิดแท็บ **Auth**
9.  คัดลอก **Client ID** และป้อนลงใน n8n credential ของคุณ
10. เลือกไอคอนเพื่อ **Copy** **Primary Client Secret** ป้อนข้อมูลนี้ลงใน n8n credential ของคุณเป็น **Client Secret**

/// note | Posting from organization accounts
หากต้องการโพสต์ในฐานะองค์กร คุณต้องส่งแอปของคุณผ่านกระบวนการ [Community Management App Review](https://learn.microsoft.com/en-us/linkedin/marketing/community-management-app-review){:target=_blank .external-link} ของ LinkedIn
///

ดูข้อมูลเพิ่มเติมเกี่ยวกับ scopes และ permissions ได้ที่ [Getting Access to LinkedIn APIs](https://learn.microsoft.com/en-us/linkedin/shared/authentication/getting-access){:target=_blank .external-link}

## Using OAuth2

ใช้วิธีนี้สำหรับแอป LinkedIn และบัญชีผู้ใช้ที่เก่ากว่าเท่านั้น

--8<-- "_snippets/integrations/builtin/credentials/cloud-oauth-button.md"

ผู้ใช้ทุกคนต้องเลือก:

- **Organization Support**: หากเปิดใช้งาน credential จะขออนุญาตโพสต์ในฐานะองค์กรโดยใช้ scope `w_organization_social`
    - หากต้องการใช้ตัวเลือกนี้ คุณต้องส่งแอปของคุณผ่านกระบวนการ [Community Management App Review](https://learn.microsoft.com/en-us/linkedin/marketing/community-management-app-review){:target=_blank .external-link} ของ LinkedIn
- **Legacy**: หากเปิดใช้งาน credential จะใช้ legacy scopes สำหรับ `r_liteprofile` และ `r_emailaddress` แทน scopes ใหม่ `profile` และ `email`

หากคุณ [self-hosting](/hosting/index.md) n8n คุณจะต้องตั้งค่า OAuth2 ตั้งแต่ต้นโดยสร้าง developer app ใหม่:

1.  เข้าสู่ระบบ LinkedIn และเลือก link นี้เพื่อ [create a new developer app](https://www.linkedin.com/developers/apps/new){:target=_blank .external-link}
2.  ป้อน **App name** สำหรับแอปของคุณ เช่น `n8n integration`
3.  สำหรับ **LinkedIn Page** ให้ป้อน [Company Page](https://www.linkedin.com/help/linkedin/answer/a543852){:target=_blank .external-link} ของ LinkedIn หรือใช้ link **Create a new LinkedIn Page** เพื่อสร้างหน้าใหม่ทันที ดูข้อมูลเพิ่มเติมได้ที่ [Associate an App with a LinkedIn Page](https://www.linkedin.com/help/linkedin/answer/a548360){:target=_blank .external-link}
4.  เพิ่ม **App logo**
5.  ทำเครื่องหมายในช่องเพื่อยอมรับ **Legal agreement**
6.  เลือก **Create app**
7.  ขั้นตอนนี้ควรเปิดแท็บ **Products** เลือก products/APIs ที่คุณต้องการเปิดใช้งานสำหรับแอปของคุณ เพื่อให้ LinkedIn node ทำงานได้อย่างถูกต้อง คุณต้องรวม:
    *   **Share on LinkedIn**
    *   **Sign In with LinkedIn using OpenID Connect**
8.  เมื่อคุณขอเข้าถึง products ที่ต้องการแล้ว ให้เปิดแท็บ **Auth**
9.  คัดลอก **Client ID** และป้อนลงใน n8n credential ของคุณ
10. เลือกไอคอนเพื่อ **Copy** **Primary Client Secret** ป้อนข้อมูลนี้ลงใน n8n credential ของคุณเป็น **Client Secret**

/// note | Posting from organization accounts
หากต้องการโพสต์ในฐานะองค์กร คุณต้องส่งแอปของคุณผ่านกระบวนการ [Community Management App Review](https://learn.microsoft.com/en-us/linkedin/marketing/community-management-app-review){:target=_blank .external-link} ของ LinkedIn
///

ดูข้อมูลเพิ่มเติมเกี่ยวกับ scopes และ permissions ได้ที่ [Getting Access to LinkedIn APIs](https://learn.microsoft.com/en-us/linkedin/shared/authentication/getting-access){:target=_blank .external-link}
