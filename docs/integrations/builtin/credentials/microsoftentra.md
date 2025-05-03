---
#https://www.notion.so/n8n/Frontmatter-432c2b8dff1f43d4b1c8d20075510fe4
title: ข้อมูลยืนยันตัวตน Microsoft Entra ID
description: เอกสารสำหรับ Microsoft Entra ID credentials ใช้เพื่อเชื่อมต่อ Microsoft Entra ID ใน n8n
contentType: [integration, reference]
priority: medium
---

# Microsoft Entra ID credentials

คุณสามารถใช้ credentials เหล่านี้เพื่อยืนยันตัวตนใน nodes ต่อไปนี้:

* [Microsoft Entra ID](/integrations/builtin/app-nodes/n8n-nodes-base.microsoftentra.md)

## Prerequisites

- สร้างบัญชีหรือสมัครสมาชิก Microsoft Entra ID
- หากบัญชีผู้ใช้ถูกจัดการโดยบัญชี Microsoft Entra ขององค์กร บัญชีผู้ดูแลระบบได้เปิดใช้งานตัวเลือก “User can consent to apps accessing company data on their behalf” สำหรับผู้ใช้นี้ (ดู [Microsoft Entra documentation](https://learn.microsoft.com/en-us/entra/identity/enterprise-apps/grant-admin-consent))

Microsoft รวมแผน Entra ID ฟรีเมื่อคุณสร้างบัญชี [Microsoft Azure](https://azure.microsoft.com/){:target=_blank .external-link}

## Supported authentication methods

- OAuth2

## Related resources

อ้างอิง [Microsoft Entra ID's documentation](https://www.microsoft.com/en-us/security/business/identity-access/azure-active-directory){:target=_blank .external-link} สำหรับข้อมูลเพิ่มเติมเกี่ยวกับบริการนี้

## Using OAuth2

--8<-- "_snippets/integrations/builtin/credentials/cloud-oauth-button.md"

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
1. เลือก **Connect my account** ใน n8n เพื่อสิ้นสุดการตั้งค่าการเชื่อมต่อ
1. เข้าสู่ระบบบัญชี Microsoft ของคุณและอนุญาตให้แอปเข้าถึงข้อมูลของคุณ

อ้างอิง Microsoft's [Add credentials](https://learn.microsoft.com/en-us/graph/auth-register-app-v2#add-credentials){:target=_blank .external-link} สำหรับข้อมูลเพิ่มเติมเกี่ยวกับการเพิ่ม client secret

## Common issues

นี่คือข้อผิดพลาดและปัญหาทั่วไปที่ทราบเกี่ยวกับ Microsoft Entra credentials

--8<-- "_snippets/integrations/builtin/credentials/microsoft-need-admin-approval.md"
