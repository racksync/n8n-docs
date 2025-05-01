---
#https://www.notion.so/n8n/Frontmatter-432c2b8dff1f43d4b1c8d20075510fe4
title: GitHub credentials
description: Documentation for GitHub credentials. Use these credentials to authenticate GitHub in n8n, a workflow automation platform.
contentType: [integration, reference]
priority: medium
---

# GitHub credentials

คุณสามารถใช้ credentials เหล่านี้เพื่อยืนยันตัวตนกับ node ต่อไปนี้:

- [GitHub](/integrations/builtin/app-nodes/n8n-nodes-base.github.md)
- [GitHub Trigger](/integrations/builtin/trigger-nodes/n8n-nodes-base.githubtrigger.md)
- [GitHub Document Loader](/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.documentgithubloader.md): node นี้ไม่รองรับ OAuth

## Prerequisites

สร้างบัญชี [GitHub](https://github.com/){:target=_blank .external-link}

## Supported authentication methods

- API access token: ใช้วิธีนี้กับ GitHub nodes ใดก็ได้
- OAuth2: ใช้วิธีนี้กับ node [GitHub](/integrations/builtin/app-nodes/n8n-nodes-base.github.md) และ [GitHub Trigger](/integrations/builtin/trigger-nodes/n8n-nodes-base.githubtrigger.md) เท่านั้น; ห้ามใช้กับ [GitHub Document Loader](/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.documentgithubloader.md)

## Related resources

ดูข้อมูลเพิ่มเติมเกี่ยวกับบริการนี้ได้ที่ [GitHub's API documentation](https://docs.github.com/en/rest){:target=_blank .external-link}

## Using API access token

ในการกำหนดค่า credential นี้ คุณจะต้องมีบัญชี [GitHub](https://github.com/){:target=_blank .external-link}

มีสองขั้นตอนในการตั้งค่า credential นี้:

1. [สร้าง GitHub personal access token](#generate-personal-access-token)
2. [ตั้งค่า credential](#set-up-the-credential)

ดูคำแนะนำโดยละเอียดในส่วนด้านล่าง

### Generate personal access token

/// note | Recommended access token type
n8n แนะนำให้ใช้ personal access token (classic) GitHub's fine-grained personal access tokens ยังอยู่ในช่วงเบต้าและไม่สามารถเข้าถึง endpoints ทั้งหมดได้
///

วิธีสร้าง personal access token ของคุณ:

1. หากคุณยังไม่ได้ทำ ให้ยืนยันที่อยู่อีเมลของคุณกับ GitHub ดูข้อมูลเพิ่มเติมได้ที่ [Verifying your email address](https://docs.github.com/en/account-and-profile/setting-up-and-managing-your-personal-account-on-github/managing-email-preferences/verifying-your-email-address){:target=_blank .external-link}
2. เปิด [Settings](https://github.com/settings/profile){:target=_blank .external-link} ของโปรไฟล์ GitHub ของคุณ
3. ในการนำทางด้านซ้าย เลือก [**Developer settings**](https://github.com/settings/apps){:target=_blank .external-link}
4. ในการนำทางด้านซ้าย ใต้ **Personal access tokens** เลือก **Tokens (classic)**
5. เลือก **Generate new token > Generate new token (classic)**
6. ป้อนชื่อที่สื่อความหมายสำหรับ token ของคุณในช่อง **Note** เช่น `n8n integration`
7. เลือก **Expiration** ที่คุณต้องการสำหรับ token หรือเลือก **No expiration**
8. เลือก **Scopes** สำหรับ token ของคุณ สำหรับ n8n GitHub nodes ส่วนใหญ่ ให้เพิ่ม scope `repo`
    - token ที่ไม่มี scopes ที่กำหนดไว้สามารถเข้าถึงข้อมูลสาธารณะได้เท่านั้น
    - ดูข้อมูลเพิ่มเติมได้ที่
9. เลือก **Generate token**
10. คัดลอก token

ดูข้อมูลเพิ่มเติมได้ที่ [Creating a personal access token (classic)](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/managing-your-personal-access-tokens#creating-a-personal-access-token-classic){:target=_blank .external-link} ดูข้อมูลเพิ่มเติมเกี่ยวกับ GitHub scopes ได้ที่ [Scopes for OAuth apps](https://docs.github.com/en/apps/oauth-apps/building-oauth-apps/scopes-for-oauth-apps#available-scopes){:target=_blank .external-link}

### Set up the credential

จากนั้น ใน credential ของ n8n:

1. หากคุณไม่ได้ใช้ GitHub Enterprise Server ไม่ต้องเปลี่ยน URL ของ **GitHub server**
    - หากคุณใช้ [GitHub Enterprise Server](https://docs.github.com/en/enterprise-server@3.9/admin/overview/about-github-enterprise-server){:target=_blank .external-link} ให้อัปเดต **GitHub server** ให้ตรงกับ URL สำหรับเซิร์ฟเวอร์ของคุณ
2. ป้อนชื่อ **User** ของคุณตามที่ปรากฏในโปรไฟล์ GitHub ของคุณ
3. ป้อน **Access Token** ที่คุณสร้างขึ้นด้านบน

## Using OAuth2

--8<-- "_snippets/integrations/builtin/credentials/cloud-oauth-button.md"

หากคุณ [self-hosting n8n](/hosting/index.md) ให้สร้าง [OAuth app](https://docs.github.com/en/apps/oauth-apps){:target=_blank .external-link} ใหม่ของ GitHub:

1. เปิด [Settings](https://github.com/settings/profile){:target=_blank .external-link} ของโปรไฟล์ GitHub ของคุณ
2. ในการนำทางด้านซ้าย เลือก [**Developer settings**](https://github.com/settings/apps){:target=_blank .external-link}
3. ในการนำทางด้านซ้าย เลือก **OAuth apps**
4. เลือก **New OAuth App**
    - หากคุณไม่เคยสร้างแอปมาก่อน คุณอาจเห็น **Register a new application** แทน ให้เลือกตัวเลือกนั้น
5. ป้อน **Application name** เช่น `n8n integration`
6. ป้อน **Homepage URL** สำหรับเว็บไซต์ของแอปของคุณ
7. หากต้องการ ให้เพิ่ม **Application description** ซึ่งเป็นทางเลือก GitHub จะแสดงให้ผู้ใช้ปลายทางเห็น
8. จาก n8n คัดลอก **OAuth Redirect URL** และวางลงใน **Authorization callback URL** ของ GitHub
9. เลือก **Register application**
10. คัดลอก **Client ID** และ **Client Secret** ที่สร้างขึ้นนี้และเพิ่มลงใน credential ของ n8n

ดูข้อมูลเพิ่มเติมเกี่ยวกับกระบวนการ authorization ได้ที่ [GitHub Authorizing OAuth apps documentation](https://docs.github.com/en/apps/oauth-apps/using-oauth-apps/authorizing-oauth-apps){:target=_blank .external-link}
