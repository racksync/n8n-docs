---
#https://www.notion.so/n8n/Frontmatter-432c2b8dff1f43d4b1c8d20075510fe4
title: Pushcut Trigger node documentation
description: Learn how to use the Pushcut Trigger node in n8n. Follow technical documentation to integrate Pushcut Trigger node into your workflows.
contentType: [integration, reference]
---

# Pushcut Trigger node

[Pushcut](https://pushcut.io){:target=_blank .external-link} คือแอปสำหรับ iOS ที่ให้คุณสร้าง smart notification เพื่อเรียกใช้งาน shortcut, URL หรือ automation อื่นๆ ได้

/// note | Credentials
คุณสามารถดูข้อมูลเกี่ยวกับการเชื่อมต่อบัญชี (authentication) สำหรับ node นี้ได้ [ที่นี่](/integrations/builtin/credentials/pushcut.md)
///

///  note  | Examples and templates
ถ้าอยากดูตัวอย่างการใช้งานหรือ template สำหรับเริ่มต้น ลองดูที่หน้า [Pushcut Trigger integrations](https://n8n.io/integrations/pushcut-trigger/){:target=_blank .external-link} ของ n8n ได้เลย
///

## Configure a Pushcut action

ทำตามขั้นตอนนี้เพื่อเชื่อมต่อ Pushcut Trigger node กับแอป Pushcut ของคุณ

1. ในแอป Pushcut ให้เลือก notification ที่ต้องการจากหน้าจอ **Notifications**
2. กดปุ่ม **Add Action**
3. ใส่ชื่อ action ในช่อง **Label**
4. เลือกแท็บ **Server**
5. เลือกแท็บ **Integration**
6. เลือก **Integration Trigger**
7. ที่ n8n ให้ตั้งชื่อ action แล้วเลือก **Test step**
8. เลือก action นี้ในหน้าจอ **Select Integration Trigger** ในแอป Pushcut
9. กด **Done** ที่มุมขวาบนเพื่อบันทึก action
