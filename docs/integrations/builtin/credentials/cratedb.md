---
#https://www.notion.so/n8n/Frontmatter-432c2b8dff1f43d4b1c8d20075510fe4
title: CrateDB credentials
description: Documentation for CrateDB credentials. Use these credentials to authenticate CrateDB in n8n, a workflow automation platform.
contentType: [integration, reference]
---

# CrateDB credentials

คุณสามารถใช้ credentials นี้เพื่อเชื่อมต่อกับ node เหล่านี้:

- [CrateDB](/integrations/builtin/app-nodes/n8n-nodes-base.cratedb.md)

## Prerequisites

instance ของ CrateDB ที่พร้อมใช้งาน

## Supported authentication methods

- account connection

## Related resources

ดูข้อมูลเพิ่มเติมเกี่ยวกับบริการได้ที่ [CrateDB's documentation](https://cratedb.com/docs/crate/reference/en/latest/){:target=_blank .external-link}

## Using account connection

ถ้าจะตั้งค่า credentials นี้ คุณต้องมี:

- ชื่อ **Host** ของคุณ
- ชื่อ **Database** ของคุณ
- ชื่อ **User**
- **Password** ของผู้ใช้
- ตั้งค่าพารามิเตอร์ **SSL** ดูข้อมูลเพิ่มเติมได้ที่ [CrateDB Secured Communications (SSL/TLS) documentation](https://cratedb.com/docs/crate/reference/en/5.7/admin/ssl.html#admin-ssl){:target=_blank .external-link} ตัวเลือกที่ n8n รองรับคือ:
    - Allow
    - Disable
    - Require
- หมายเลข **Port**

ดูคำแนะนำโดยละเอียดเกี่ยวกับฟิลด์เหล่านี้และค่าเริ่มต้นได้ที่ [Connect to a CrateDB cluster documentation](https://cratedb.com/docs/crate/clients-tools/en/latest/connect/){:target=_blank .external-link}

