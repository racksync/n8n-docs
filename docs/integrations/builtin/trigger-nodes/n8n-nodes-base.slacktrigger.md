---
#https://www.notion.so/n8n/Frontmatter-432c2b8dff1f43d4b1c8d20075510fe4
title: Slack Trigger node documentation
description: Learn how to use the Slack Trigger node in n8n. Follow technical documentation to integrate Slack Trigger node into your workflows.
contentType: [integration, reference]
priority: medium
---

# Slack Trigger node

ใช้ Slack Trigger node เพื่อรับเหตุการณ์ต่าง ๆ ที่เกิดขึ้นใน [Slack](https://slack.com/){:target=_blank .external-link} และเชื่อมต่อ Slack กับแอปอื่น ๆ ได้แบบอัตโนมัติ n8n รองรับ event หลากหลาย เช่น ข้อความใหม่, การกด reaction, หรือการสร้าง channel ใหม่

ในหน้านี้จะมีรายการ event ที่ Slack Trigger node สามารถตอบสนองได้ พร้อมลิงก์ไปยังแหล่งข้อมูลเพิ่มเติม

///  note  | Credentials
คุณสามารถดูข้อมูลการตั้งค่า authentication สำหรับ node นี้ได้ [ที่นี่](/integrations/builtin/credentials/slack.md)
///
///  note  | Examples and templates
ถ้าต้องการดูตัวอย่างการใช้งานและ template สำหรับเริ่มต้นใช้งาน ลองดูที่หน้า [Slack integrations](https://n8n.io/integrations/slack-trigger/){:target=_blank .external-link} ของ n8n ได้เลย
///

## Events

* **Any Event**: node จะ trigger เมื่อมี event ใด ๆ ใน Slack
* **Bot / App Mention**: node จะ trigger เมื่อ bot หรือ app ของคุณถูก [mention](https://slack.com/help/articles/205240127-Use-mentions-in-Slack){:target=_blank .external-link} ใน channel ที่ app อยู่
* **File Made Public**: node จะ trigger เมื่อมีการ [แชร์ไฟล์เป็นสาธารณะ](https://slack.com/help/articles/4412651915539-Manage-public-file-sharing){:target=_blank .external-link}
* **File Shared**: node จะ trigger เมื่อมีการ [แชร์ไฟล์](https://slack.com/help/articles/201330736-Add-files-to-Slack){:target=_blank .external-link} ใน channel ที่ app อยู่
* **New Message Posted to Channel**: node จะ trigger เมื่อมีข้อความใหม่ใน channel ที่ app อยู่
* **New Public Channel Created**: node จะ trigger เมื่อมีการสร้าง [public channel](https://slack.com/help/articles/360017938993-What-is-a-channel){:target=_blank .external-link} ใหม่
* **New User**: node จะ trigger เมื่อมีการเพิ่มผู้ใช้ใหม่ใน Slack
* **Reaction Added**: node จะ trigger เมื่อมีการเพิ่ม [reaction](https://slack.com/help/articles/202931348-Use-emoji-and-reactions){:target=_blank .external-link} ในข้อความที่ app อยู่

## Parameters

เมื่อคุณตั้งค่า event ที่ต้องการ trigger แล้ว คุณสามารถใช้ parameter ที่เหลือเพื่อกำหนดพฤติกรรมของ node ได้เพิ่มเติม:

* **Watch Whole Workspace**: กำหนดว่า node ควรดู event ที่เลือกในทุก channel ใน workspace (เปิดใช้งาน) หรือไม่ (ปิดใช้งาน, ค่าเริ่มต้น)

    ///warning | Caution
    การตั้งค่านี้จะใช้การประมวลผลหนึ่งครั้งสำหรับทุก event ในทุก channel ที่ bot หรือ app ของคุณอยู่ ใช้อย่างระมัดระวัง!
    ///

* **Channel to Watch**: เลือก channel ที่ node ควรดู event ที่เลือก Parameter นี้จะปรากฏเฉพาะเมื่อคุณไม่เปิดใช้งาน **Watch Whole Workspace** คุณสามารถเลือก channel ได้ดังนี้:
    * **From list**: node จะใช้ credential ของคุณเพื่อค้นหารายการ channel ใน workspace เพื่อให้คุณเลือก channel ที่ต้องการ
    * **By ID**: ป้อน ID ของ channel ที่คุณต้องการดู Slack จะแสดง ID ของ channel ที่ด้านล่างของรายละเอียด channel พร้อมปุ่มคัดลอก
    * **By URL**: ป้อน URL ของ channel ที่คุณต้องการดู โดยใช้รูปแบบ `https://app.slack.com/client/<channel-address>`
* **Download Files**: กำหนดว่าจะดาวน์โหลดไฟล์และใช้ใน output ของ node (เปิดใช้งาน) หรือไม่ (ปิดใช้งาน, ค่าเริ่มต้น) ใช้ parameter นี้ร่วมกับ event **File Made Public** และ **File Shared**

## Options

คุณสามารถปรับแต่งพฤติกรรมของ node ได้เพิ่มเติมเมื่อคุณ **Add Option**:

* **Resolve IDs**: กำหนดว่าจะเปลี่ยน ID ให้เป็นชื่อที่เกี่ยวข้องและส่งคืน (เปิดใช้งาน) หรือไม่ (ปิดใช้งาน, ค่าเริ่มต้น)
* **Usernames or IDs to ignore**: เลือกชื่อผู้ใช้หรือป้อน string ของ user ID ที่เข้ารหัสคั่นด้วยเครื่องหมายจุลภาคเพื่อไม่ให้รับ event จากผู้ใช้เหล่านั้น เลือกจากรายการ หรือระบุ ID โดยใช้ [expression](/code/expressions.md)

## Related resources

n8n มี app node สำหรับ Slack คุณสามารถดูเอกสาร node ได้ [ที่นี่](/integrations/builtin/app-nodes/n8n-nodes-base.slack.md)

ดู [ตัวอย่าง workflow และเนื้อหาที่เกี่ยวข้อง](https://n8n.io/integrations/slack-trigger/){:target=_blank .external-link} บนเว็บไซต์ของ n8n

ดูเอกสาร [Slack's documentation](https://api.slack.com/apis/connections/events-api){:target=_blank .external-link} สำหรับรายละเอียดเกี่ยวกับ API ของพวกเขา

## Required scopes

ในการใช้ node นี้ คุณต้องสร้างแอปพลิเคชันใน Slack และเปิดใช้งาน event subscriptions ดูข้อมูลเพิ่มเติมได้ที่ [Slack credentials | Slack Trigger configuration](/integrations/builtin/credentials/slack.md#slack-trigger-configuration)

คุณต้องเพิ่ม scope ที่เหมาะสมให้กับ Slack app ของคุณเพื่อให้ trigger node นี้ทำงานได้

node ต้องการ scope สำหรับ [conversations.list](https://api.slack.com/methods/conversations.list){:target=blank .external-link} และ [users.list](https://api.slack.com/methods/users.list){:target=blank .external-link} อย่างน้อยที่สุด ดู [Scopes | Slack credentials](/integrations/builtin/credentials/slack.md#scopes) สำหรับรายการ scope ที่สมบูรณ์ยิ่งขึ้น

## Common issues

นี่คือข้อผิดพลาดและปัญหาทั่วไปที่เกิดขึ้นกับ Slack Trigger node และขั้นตอนในการแก้ไขหรือแก้ปัญหา

### Workflow only works in testing or production

Slack อนุญาตให้คุณลงทะเบียน webhook เพียงอันเดียวต่อแอป ซึ่งหมายความว่าคุณไม่สามารถสลับจากการใช้ URL ทดสอบไปยัง URL การผลิต (และในทางกลับกัน) โดยไม่ต้องกำหนดค่า URL webhook ที่ลงทะเบียนใหม่

คุณอาจมีปัญหากับสิ่งนี้หากคุณพยายามทดสอบ workflow ที่ใช้งานอยู่ใน production Slack จะส่ง event ไปยังหนึ่งในสอง URL webhook เท่านั้น ดังนั้นอีกอันจะไม่ได้รับการแจ้งเตือน event

เพื่อแก้ปัญหานี้ คุณสามารถปิดใช้งาน workflow ของคุณเมื่อทดสอบ:

/// warning | Halts production traffic
การดำเนินการนี้จะปิดใช้งาน workflow การผลิตของคุณชั่วคราวสำหรับการทดสอบ workflow ของคุณจะไม่ได้รับ traffic การผลิตในขณะที่ถูกปิดใช้งาน
///

1. ไปที่หน้า workflow ของคุณ
2. สลับสวิตช์ **Active** ในแผงด้านบนเพื่อปิดใช้งาน workflow ชั่วคราว
3. แก้ไข **Request URL** ใน [Slack Trigger configuration](/integrations/builtin/credentials/slack.md#slack-trigger-configuration) ของคุณเพื่อใช้ URL webhook ทดสอบแทน URL webhook การผลิต
4. ทดสอบ workflow ของคุณโดยใช้ URL webhook ทดสอบ
5. เมื่อคุณทดสอบเสร็จแล้ว ให้แก้ไข **Request URL** ใน [Slack Trigger configuration](/integrations/builtin/credentials/slack.md#slack-trigger-configuration) ของคุณเพื่อใช้ URL webhook การผลิตแทน URL webhook ทดสอบ
6. สลับสวิตช์ **Inactive** เพื่อเปิดใช้งาน workflow อีกครั้ง URL webhook การผลิตควรกลับมาทำงานได้

### Token expired

--8<-- "_snippets/integrations/builtin/credentials/slack/token-rotation.md"
