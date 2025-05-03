---
#https://www.notion.so/n8n/Frontmatter-432c2b8dff1f43d4b1c8d20075510fe4
title: เอกสารคู่มือ Okta node
description: เรียนรู้วิธีใช้ Okta node ใน n8n และดูเอกสารทางเทคนิคเพื่อเชื่อมต่อ Okta node เข้ากับ workflow ของคุณ
contentType: [integration, reference]
---

# Okta node

ใช้ Okta node เพื่อทำงานอัตโนมัติใน Okta และเชื่อมต่อกับแอปอื่น ๆ. n8n รองรับฟีเจอร์ต่าง ๆ ของ Okta เช่น การสร้าง, อัปเดต และการลบผู้ใช้

ในหน้านี้ คุณจะพบรายการ operations ที่ Okta node รองรับ พร้อมลิงก์สำหรับข้อมูลเพิ่มเติม

///  note  | Credentials
ดูข้อมูลการตั้งค่า authentication สำหรับ node นี้ได้ที่ [here](/integrations/builtin/credentials/okta.md).
///

## Operations

- User
    - Create a new user
    - Delete an existing user
    - Get details of a user
    - Get many users
    - Update an existing user

## Templates and examples

<!-- see https://www.notion.so/n8n/Pull-in-templates-for-the-integrations-pages-37c716837b804d30a33b47475f6e3780 -->
[[ templatesWidget(page.title, okta) ]]

## Related resources

<!-- add a link to the service's documentation. This should usually go direct to the API docs -->
ดู [Okta's documentation](https://developer.okta.com/docs/guides/){:target=_blank .external-link} เพื่อข้อมูลเพิ่มเติมเกี่ยวกับบริการ

--8<-- "_snippets/integrations/builtin/app-nodes/operation-not-supported.md"