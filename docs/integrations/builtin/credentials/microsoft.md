---
#https://www.notion.so/n8n/Frontmatter-432c2b8dff1f43d4b1c8d20075510fe4
title: ข้อมูลยืนยันตัวตน Microsoft
description: เอกสารสำหรับ Microsoft credentials ใช้เพื่อเชื่อมต่อ Microsoft บน n8n
contentType: [integration, reference]
priority: high
---

# Microsoft credentials

คุณสามารถใช้ credentials เหล่านี้เพื่อยืนยันตัวตนใน nodes ต่อไปนี้:

- [Microsoft Dynamics CRM](/integrations/builtin/app-nodes/n8n-nodes-base.microsoftdynamicscrm.md)
- [Microsoft Excel](/integrations/builtin/app-nodes/n8n-nodes-base.microsoftexcel.md)
- [Microsoft Graph Security](/integrations/builtin/app-nodes/n8n-nodes-base.microsoftgraphsecurity.md)
- [Microsoft OneDrive](/integrations/builtin/app-nodes/n8n-nodes-base.microsoftonedrive.md)
- [Microsoft Outlook](/integrations/builtin/app-nodes/n8n-nodes-base.microsoftoutlook.md)
- [Microsoft Teams](/integrations/builtin/app-nodes/n8n-nodes-base.microsoftteams.md)
- [Microsoft To Do](/integrations/builtin/app-nodes/n8n-nodes-base.microsofttodo.md)

## Prerequisites

- สร้างบัญชี [Microsoft Azure](https://azure.microsoft.com/){:target=_blank .external-link}
- สร้างบัญชีผู้ใช้อย่างน้อยหนึ่งบัญชีที่มีสิทธิ์เข้าถึงบริการที่เหมาะสม
- หากบัญชีผู้ใช้ถูกจัดการโดยบัญชี Microsoft Entra ขององค์กร บัญชีผู้ดูแลระบบได้เปิดใช้งานตัวเลือก “User can consent to apps accessing company data on their behalf” สำหรับผู้ใช้นี้ (ดู [Microsoft Entra documentation](https://learn.microsoft.com/en-us/entra/identity/enterprise-apps/grant-admin-consent))

## Supported authentication methods

- OAuth2

## Related resources

อ้างอิงเอกสาร Microsoft API ที่เชื่อมโยงด้านล่างสำหรับข้อมูลเพิ่มเติมเกี่ยวกับ API ของแต่ละบริการ:

- Dynamics CRM: [Web API](https://learn.microsoft.com/en-us/power-apps/developer/data-platform/webapi/overview){:target=_blank .external-link}
- Excel: [Graph API](https://learn.microsoft.com/en-us/graph/api/resources/excel){:target=_blank .external-link}
- Graph Security: [Graph API](https://learn.microsoft.com/en-us/graph/api/overview){:target=_blank .external-link}
- OneDrive: [Graph API](https://learn.microsoft.com/en-us/onedrive/developer/rest-api/){:target=_blank .external-link}
- Outlook: [Graph API](https://learn.microsoft.com/en-us/graph/api/resources/mail-api-overview){:target=_blank .external-link} และ [Outlook API](https://learn.microsoft.com/en-us/outlook/rest/reference){:target=_blank .external-link}
- Teams: [Graph API](https://learn.microsoft.com/en-us/graph/api/resources/teams-api-overview){:target=_blank .external-link}
- To Do: [Graph API](https://learn.microsoft.com/en-us/graph/todo-concept-overview){:target=_blank .external-link}

## Using OAuth2

--8<-- "_snippets/integrations/builtin/credentials/cloud-oauth-button.md"

บริการบางอย่างของ Microsoft ต้องการข้อมูลเพิ่มเติมสำหรับ OAuth2 อ้างอิง [Service-specific settings](#service-specific-settings) สำหรับคำแนะนำเพิ่มเติมเกี่ยวกับบริการเหล่านั้น

สำหรับผู้ใช้ self-hosted มีสองขั้นตอนหลักในการกำหนดค่า OAuth2 ตั้งแต่ต้น:

1. [ลงทะเบียนแอปพลิเคชัน](#register-an-application) กับ Microsoft Identity Platform
2. [สร้าง client secret](#generate-a-client-secret) สำหรับแอปพลิเคชันนั้น

ทำตามคำแนะนำโดยละเอียดสำหรับแต่ละขั้นตอนด้านล่าง สำหรับรายละเอียดเพิ่มเติมเกี่ยวกับ Microsoft OAuth2 web flow อ้างอิง [Microsoft authentication and authorization basics](https://learn.microsoft.com/en-us/graph/auth/auth-concepts){:target=_blank .external-link}

### Register an application

ลงทะเบียนแอปพลิเคชันกับ Microsoft Identity Platform:

1. เปิด [Microsoft Application Registration Portal](https://aka.ms/appregistrations){:target=_blank .external-link}
2. เลือก **Register an application**
3. ป้อน **Name** สำหรับแอปของคุณ
4. ใน **Supported account types** เลือก **Accounts in any organizational directory (Any Azure AD directory - Multi-tenant) and personal Microsoft accounts (for example, Skype, Xbox)**
5. ใน **Register an application**:
    1. คัดลอก **OAuth Callback URL** จาก credential ของ n8n
    2. วางลงในฟิลด์ **Redirect URI (optional)**
    3. เลือก **Select a platform** > **Web**
6. เลือก **Register** เพื่อสิ้นสุดการสร้างแอปพลิเคชันของคุณ
7. คัดลอก **Application (client) ID** และวางลงใน n8n เป็น **Client ID**

อ้างอิง [Register an application with the Microsoft Identity Platform](https://learn.microsoft.com/en-us/graph/auth-register-app-v2){:target=_blank .external-link} สำหรับข้อมูลเพิ่มเติม

### Generate a client secret

เมื่อสร้างแอปพลิเคชันของคุณแล้ว ให้สร้าง client secret สำหรับมัน:

1. บนหน้าแอปพลิเคชัน Microsoft ของคุณ เลือก **Certificates & secrets** ในการนำทางด้านซ้าย
1. ใน **Client secrets** เลือก **+ New client secret**
1. ป้อน **Description** สำหรับ client secret ของคุณ เช่น `n8n credential`
1. เลือก **Add**
1. คัดลอก **Secret** ในคอลัมน์ **Value**
1. วางลงใน n8n เป็น **Client Secret**
1. หากคุณเห็นฟิลด์อื่นๆ ใน credential ของ n8n อ้างอิง [Service-specific settings](#service-specific-settings) ด้านล่างสำหรับคำแนะนำในการกรอกฟิลด์เหล่านั้น
1. เลือก **Connect my account** ใน n8n เพื่อสิ้นสุดการตั้งค่าการเชื่อมต่อ
1. เข้าสู่ระบบบัญชี Microsoft ของคุณและอนุญาตให้แอปเข้าถึงข้อมูลของคุณ

อ้างอิง Microsoft's [Add credentials](https://learn.microsoft.com/en-us/graph/auth-register-app-v2#add-credentials){:target=_blank .external-link} สำหรับข้อมูลเพิ่มเติมเกี่ยวกับการเพิ่ม client secret

### Service-specific settings

บริการต่อไปนี้ต้องการข้อมูลเพิ่มเติมสำหรับ OAuth2:

#### Dynamics

Dynamics OAuth2 ต้องการข้อมูลเกี่ยวกับ domain และ region ของ Dynamics ของคุณ ทำตามขั้นตอนเพิ่มเติมเหล่านี้เพื่อกรอก credential:

1. ป้อน **Domain** ของ Dynamics ของคุณ
2. เลือก **Region** ของศูนย์ข้อมูล Dynamics ที่คุณอยู่

อ้างอิงเอกสาร [Microsoft Datacenter regions documentation](https://learn.microsoft.com/en-us/power-platform/admin/new-datacenter-regions){:target=_blank .external-link} สำหรับข้อมูลเพิ่มเติมเกี่ยวกับตัวเลือก region และ URL ที่สอดคล้องกัน

#### Microsoft (general)

Microsoft OAuth2 ทั่วไปยังต้องการให้คุณระบุรายการ **Scope** ที่คั่นด้วยช่องว่างสำหรับ credential นี้

อ้างอิง [Scopes and permissions in the Microsoft identity platform](https://learn.microsoft.com/en-us/entra/identity-platform/scopes-oidc){:target=_blank .external-link} สำหรับรายการ scopes ที่เป็นไปได้

#### Outlook

Outlook OAuth2 รองรับ credential ในการเข้าถึงกล่องจดหมายอีเมลหลักของผู้ใช้หรือกล่องจดหมายที่ใช้ร่วมกัน โดยค่าเริ่มต้น credential จะเข้าถึงกล่องจดหมายอีเมลหลักของผู้ใช้ หากต้องการเปลี่ยนพฤติกรรมนี้:

1. เปิดใช้งาน **Use Shared Inbox**
2. ป้อน UPN หรือ ID ของผู้ใช้เป้าหมายเป็น **User Principal Name**

#### SharePoint

SharePoint OAuth2 ต้องการข้อมูลเกี่ยวกับ **Subdomain** ของ SharePoint ของคุณ

ในการกรอก credential ให้ป้อนส่วน **Subdomain** ของ SharePoint URL ของคุณ ตัวอย่างเช่น หาก SharePoint URL ของคุณคือ `https://tenant123.sharepoint.com` subdomain คือ `tenant123`

## Common issues

นี่คือข้อผิดพลาดและปัญหาทั่วไปที่ทราบเกี่ยวกับ Microsoft OAuth2 credentials

--8<-- "_snippets/integrations/builtin/credentials/microsoft-need-admin-approval.md"
