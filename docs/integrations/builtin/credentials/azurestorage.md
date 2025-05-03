---
#https://www.notion.so/n8n/Frontmatter-432c2b8dff1f43d4b1c8d20075510fe4
title: ข้อมูลรับรอง Azure Storage
description: เอกสารข้อมูลรับรอง Azure Storage ใช้ข้อมูลนี้เพื่อยืนยันตัวตน Azure Storage ใน n8n
contentType: [integration, reference]
---

# Azure Storage credentials

คุณสามารถใช้ credentials นี้เพื่อเชื่อมต่อกับ node เหล่านี้:

* [Azure Storage](/integrations/builtin/app-nodes/n8n-nodes-base.azurestorage.md)

## Prerequisites

* สมัคร [Azure](https://azure.microsoft.com) subscription
* สร้าง [Azure storage account](https://learn.microsoft.com/en-us/azure/storage/common/storage-account-create)

## Supported authentication methods

* OAuth2
* Shared Key

## Related resources

ดูข้อมูลเพิ่มเติมเกี่ยวกับบริการได้ที่ [Azure Storage's API documentation](https://learn.microsoft.com/en-us/rest/api/storageservices/)

## Using OAuth2

--8<-- "_snippets/integrations/builtin/credentials/cloud-oauth-button.md"

สำหรับผู้ใช้ self-hosted มีสองขั้นตอนหลักในการตั้งค่า OAuth2 ด้วยตัวเอง:

1. [ลงทะเบียน application](#register-an-application) กับ Microsoft Identity Platform
2. [สร้าง client secret](#generate-a-client-secret) สำหรับ application นั้น

ทำตามคำแนะนำโดยละเอียดสำหรับแต่ละขั้นตอนด้านล่าง สำหรับรายละเอียดเพิ่มเติมเกี่ยวกับ Microsoft OAuth2 web flow โปรดดูที่ [Microsoft authentication and authorization basics](https://learn.microsoft.com/en-us/graph/auth/auth-concepts)

### Register an application

ลงทะเบียน application กับ Microsoft Identity Platform:

1. เปิด [Microsoft Application Registration Portal](https://aka.ms/appregistrations)
2. เลือก **Register an application**
3. ป้อน **Name** สำหรับ app ของคุณ
4. ใน **Supported account types** เลือก **Accounts in any organizational directory (Any Azure AD directory - Multi-tenant) and personal Microsoft accounts (for example, Skype, Xbox)**
5. ใน **Register an application**:
    1. คัดลอก **OAuth Callback URL** จาก n8n credential ของคุณ
    2. วางลงในฟิลด์ **Redirect URI (optional)**
    3. เลือก **Select a platform** > **Web**
6. เลือก **Register** เพื่อสร้าง application ของคุณให้เสร็จสิ้น
7. คัดลอก **Application (client) ID** และวางลงใน n8n เป็น **Client ID**

ดูข้อมูลเพิ่มเติมได้ที่ [Register an application with the Microsoft Identity Platform](https://learn.microsoft.com/en-us/graph/auth-register-app-v2)

### Generate a client secret

เมื่อสร้าง application ของคุณแล้ว ให้สร้าง client secret สำหรับมัน:

1. บนหน้า Microsoft application ของคุณ เลือก **Certificates & secrets** ในการนำทางด้านซ้าย
1. ใน **Client secrets** เลือก **+ New client secret**
1. ป้อน **Description** สำหรับ client secret ของคุณ เช่น `n8n credential`
1. เลือก **Add**
1. คัดลอก **Secret** ในคอลัมน์ **Value**
1. วางลงใน n8n เป็น **Client Secret**
1. เลือก **Connect my account** ใน n8n เพื่อตั้งค่าการเชื่อมต่อให้เสร็จสิ้น
1. ล็อกอินเข้าบัญชี Microsoft ของคุณและอนุญาตให้ app เข้าถึงข้อมูลของคุณ

ดูข้อมูลเพิ่มเติมเกี่ยวกับการเพิ่ม client secret ได้ที่ [Add credentials](https://learn.microsoft.com/en-us/graph/auth-register-app-v2#add-credentials) ของ Microsoft

## Using Shared Key

ถ้าจะตั้งค่า credentials นี้ คุณต้องมี:

* **Account**: ชื่อของ Azure Storage account ของคุณ
* **Key**: shared key สำหรับ Azure Storage account ของคุณ เลือก **Security + networking** แล้วเลือก **Access keys** คุณสามารถใช้ key บัญชีใดก็ได้จากสอง key สำหรับวัตถุประสงค์นี้

ดูขั้นตอนโดยละเอียดเพิ่มเติมได้ที่ [Manage storage account access keys | Microsoft](https://learn.microsoft.com/en-us/azure/storage/common/storage-account-keys-manage)

## Common issues

นี่คือข้อผิดพลาดและปัญหาทั่วไปที่ทราบเกี่ยวกับ Azure Storage credentials

--8<-- "_snippets/integrations/builtin/credentials/microsoft-need-admin-approval.md"
