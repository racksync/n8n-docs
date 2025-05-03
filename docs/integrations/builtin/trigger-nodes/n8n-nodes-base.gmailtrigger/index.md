---
#https://www.notion.so/n8n/Frontmatter-432c2b8dff1f43d4b1c8d20075510fe4
title: คู่มือ Gmail Trigger node
description: เรียนรู้วิธีใช้ Gmail Trigger node ใน n8n พร้อมวิธีเชื่อม Gmail กับ workflow ของคุณ
contentType: [integration, reference]
priority: high
---

# Gmail Trigger node

[Gmail](https://www.gmail.com){:target=_blank .external-link} คือบริการอีเมลที่พัฒนาโดย Google โดย Gmail Trigger node สามารถเริ่ม workflow ได้เมื่อเกิด event ต่างๆ ใน Gmail

/// note | Credentials
คุณสามารถดูข้อมูลเกี่ยวกับการตั้งค่า credentials สำหรับ node นี้ได้ [ที่นี่](/integrations/builtin/credentials/google/index.md)
///

///  note  | Examples and templates
สำหรับตัวอย่างการใช้งานและ template ที่จะช่วยให้คุณเริ่มต้นได้ง่ายขึ้น ดูได้ที่หน้า [Gmail Trigger integrations](https://n8n.io/integrations/gmail-trigger/){:target=_blank .external-link} ของ n8n
///

## Events

* **Message Received**: node จะ trigger เมื่อมีข้อความใหม่ตาม **Poll Time** ที่เลือก

## Node parameters

ตั้งค่า node นี้ด้วย parameter เหล่านี้:

* **Credential to connect with**: เลือกหรือสร้าง Google credential ใหม่เพื่อใช้กับ trigger ดูรายละเอียดการตั้งค่า credential ได้ที่ [Google credentials](/integrations/builtin/credentials/google/index.md)
* **Poll Times**: เลือก poll **Mode** เพื่อกำหนดความถี่ในการ trigger poll การเลือก **Mode** จะเพิ่มหรือลด field ที่เกี่ยวข้อง ดูวิธีตั้งค่า parameter สำหรับแต่ละ mode ได้ที่ [Poll Mode options](/integrations/builtin/trigger-nodes/n8n-nodes-base.gmailtrigger/poll-mode-options.md)
* **Simplify**: เลือกว่าจะให้ node ส่งข้อมูลแบบ simplified (เปิดไว้เป็นค่า default) หรือส่ง raw data (ปิด)
    * แบบ simplified จะส่งเฉพาะ email message ID, labels และ email headers เช่น From, To, CC, BCC, Subject

## Node filters

ใช้ filter เหล่านี้เพื่อปรับแต่งการทำงานของ node:

* **Include Spam and Trash**: เลือกว่าจะให้ node trigger กับข้อความใหม่ในโฟลเดอร์ Spam และ Trash ด้วยหรือไม่ (เปิด/ปิด)
* **Label Names or IDs**: trigger เฉพาะข้อความที่มี label ที่เลือก สามารถเลือกชื่อ label หรือใส่ expression เพื่อระบุ ID dropdown จะเปลี่ยนตาม **Credential** ที่เลือก
* **Search**: ใส่ Gmail search filter เช่น `from:` เพื่อให้ node trigger เฉพาะเงื่อนไขที่กรองไว้ ดูตัวอย่าง filter ได้ที่ [Refine searches in Gmail](https://support.google.com/mail/answer/7190?hl=en){:target=_blank .external-link}
* **Read Status**: เลือกว่าจะรับอีเมล **Unread and read emails**, **Unread emails only** (default) หรือ **Read emails only**
* **Sender**: ใส่อีเมลหรือบางส่วนของชื่อผู้ส่งเพื่อ trigger เฉพาะข้อความจาก sender นั้น

## Related resources

n8n มี app node สำหรับ Gmail ด้วย ดูเอกสาร node ได้ [ที่นี่](/integrations/builtin/app-nodes/n8n-nodes-base.gmail/index.md)

ดู [ตัวอย่าง workflow และเนื้อหาที่เกี่ยวข้อง](https://n8n.io/integrations/gmail-trigger/){:target=_blank .external-link} บนเว็บไซต์ n8n

ดูรายละเอียดเพิ่มเติมเกี่ยวกับ API ได้ที่ [Google's Gmail API documentation](https://developers.google.com/gmail/api/guides){:target=_blank .external-link}

## Common issues

สำหรับคำถามหรือปัญหาที่พบบ่อยและวิธีแก้ไข ดูได้ที่ [Common issues](/integrations/builtin/trigger-nodes/n8n-nodes-base.gmailtrigger/common-issues.md)
