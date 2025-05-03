---
#https://www.notion.so/n8n/Frontmatter-432c2b8dff1f43d4b1c8d20075510fe4
title: ข้อมูลยืนยันตัวตน LDAP
description: เอกสารสำหรับ LDAP credentials ใช้เพื่อเชื่อมต่อ LDAP ใน n8n
contentType: [integration, reference]
---

# LDAP credentials

คุณสามารถใช้ credentials เหล่านี้เพื่อยืนยันตัวตนกับ node ต่อไปนี้ได้:

* [LDAP](/integrations/builtin/core-nodes/n8n-nodes-base.ldap.md)

## Prerequisites

สร้าง server directory โดยใช้ Lightweight Directory Access Protocol (LDAP)

ผู้ให้บริการ LDAP ทั่วไปบางราย ได้แก่:

* [Jumpcloud](https://jumpcloud.com/blog/how-to-connect-your-application-to-ldap){:target=_blank .external-link}
* [Azure ADDS](https://learn.microsoft.com/en-us/azure/active-directory-domain-services/tutorial-configure-ldaps){:target=_blank .external-link}
* [Okta](https://help.okta.com/en-us/Content/Topics/Directory/LDAP-interface-connection-settings.htm){:target=_blank .external-link}

## Supported authentication methods

- LDAP server details

## Related resources

ดูข้อมูลโดยละเอียดได้จากเอกสารของผู้ให้บริการ LDAP ของคุณ

สำหรับข้อมูล LDAP ทั่วไป โปรดดู [Basic LDAP concepts](https://ldap.com/basic-ldap-concepts/){:target=_blank .external-link} สำหรับภาพรวมพื้นฐาน และ [The LDAP Bind Operation](https://ldap.com/the-ldap-bind-operation/){:target=_blank .external-link} สำหรับข้อมูลเกี่ยวกับวิธีการทำงานของการดำเนินการ bind และการยืนยันตัวตน

## Using LDAP server details

ในการตั้งค่า credential นี้ คุณจะต้องมี:

- **LDAP Server Address**: ใช้ IP address หรือ domain ของ LDAP server ของคุณ
- **LDAP Server Port**: ใช้หมายเลข port ที่ใช้เชื่อมต่อกับ LDAP server
- **Binding DN**: ใช้ Binding Distinguished Name (Bind DN) สำหรับ LDAP server ของคุณ นี่คือบัญชีผู้ใช้ที่ credential ควรเข้าสู่ระบบ หากคุณใช้ Active Directory อาจมีลักษณะคล้าย `cn=administrator, cn=Users, dc=n8n, dc=io` ดูข้อมูลเพิ่มเติมเกี่ยวกับวิธีระบุ DN นี้และรหัสผ่านที่เกี่ยวข้องได้จากเอกสารของผู้ให้บริการ LDAP ของคุณ
- **Binding Password**: ใช้รหัสผ่านสำหรับผู้ใช้ **Binding DN**
- เลือก **Connection Security**: ตัวเลือกได้แก่:
    - `None`
    - `TLS`
    - `STARTTLS`
- _Optional:_ ป้อนค่าตัวเลขเป็นวินาทีเพื่อตั้งค่า **Connection Timeout**

