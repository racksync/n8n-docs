---
#https://www.notion.so/n8n/Frontmatter-432c2b8dff1f43d4b1c8d20075510fe4
title: JWT
description: เอกสารสำหรับ JWT node ใน n8n แพลตฟอร์ม workflow automation พร้อมคำแนะนำการใช้งานและตัวอย่าง
contentType: [integration, reference]
priority: medium
---

# JWT

ใช้งาน JSON web tokens ใน workflow ของ n8n ของคุณ

/// note | Credentials
คุณสามารถดูข้อมูลการยืนยันตัวตนสำหรับ node นี้ได้ [ที่นี่](/integrations/builtin/credentials/jwt.md).
///

## Operations

* Decode
* Sign
* Verify

## Node parameters

--8<-- "_snippets/integrations/builtin/app-nodes/ai-tools.md"

* **Credential to connect with**: เลือกหรือสร้าง [JWT credential](/integrations/builtin/credentials/jwt.md) เพื่อเชื่อมต่อ
* **Token**: ใส่ token ที่ต้องการ **Verify** หรือ **Decode**
* ถ้าเลือก operation **Sign** จะมี parameter เพิ่มเติมดังนี้:
    * **Use JSON to Build Payload**: ถ้าเปิดใช้งาน node จะใช้ JSON ในการสร้าง claims การเลือกตรงนี้จะมีผลกับสิ่งที่แสดงในส่วน Payload Claims

## Payload Claims

node จะแสดง payload claims เฉพาะเมื่อเลือก operation **Sign** สิ่งที่เห็นจะขึ้นอยู่กับการเลือก **Use JSON to Build Payload**:

* ถ้าเลือก **Use JSON to Build Payload** จะมี editor สำหรับใส่ claims แบบ JSON
* ถ้าไม่เลือก จะมีปุ่ม **Add Claim** ให้เพิ่ม claims ทีละตัว

คุณสามารถเพิ่ม claims ต่อไปนี้ได้

### Audience

**Audience** หรือ `aud` claim ใช้ระบุผู้รับที่ JWT นี้ตั้งใจจะส่งถึง

ดูข้อมูลเพิ่มเติมที่ ["aud" (Audience) Claim](https://datatracker.ietf.org/doc/html/rfc7519#section-4.1.3){:target=_blank .external-link}

### Expires In

**Expires In** หรือ `exp` claim ใช้ระบุเวลาหลังจากนั้น JWT จะหมดอายุและไม่ควรใช้งานต่อ

ดูข้อมูลเพิ่มเติมที่ ["exp" (Expiration Time) Claim](https://datatracker.ietf.org/doc/html/rfc7519#section-4.1.4){:target=_blank .external-link}

### Issuer

**Issuer** หรือ `iss` claim ใช้ระบุว่าใครเป็นผู้ออก JWT นี้

ดูข้อมูลเพิ่มเติมที่ ["iss" (Issuer) Claim](https://datatracker.ietf.org/doc/html/rfc7519#section-4.1.1){:target=_blank .external-link}

### JWT ID

**JWT ID** หรือ `jti` claim ใช้ระบุรหัสเฉพาะของ JWT

ดูข้อมูลเพิ่มเติมที่ ["jti" (JWT ID) Claim](https://datatracker.ietf.org/doc/html/rfc7519#section-4.1.7){:target=_blank .external-link}

### Not Before

**Not Before** หรือ `nbf` claim ใช้ระบุเวลาก่อนหน้านี้ที่ JWT จะยังไม่สามารถใช้งานได้

ดูข้อมูลเพิ่มเติมที่ ["nbf" (Not Before) Claim](https://datatracker.ietf.org/doc/html/rfc7519#section-4.1.5){:target=_blank .external-link}

### Subject

**Subject** หรือ `sub` claim ใช้ระบุ subject ของ JWT นี้

ดูข้อมูลเพิ่มเติมที่ ["sub" (Subject) Claim](https://datatracker.ietf.org/doc/html/rfc7519#section-4.1.2){:target=_blank .external-link}

## Node options

### Decode node options

**Return Additional Info** toggle จะควบคุมว่าข้อมูลที่ node คืนค่าจะละเอียดแค่ไหน

ถ้าเปิด node จะคืนค่าข้อมูล token ที่ decode แล้วทั้งหมด รวมถึง header และ signature ถ้าปิด node จะคืนค่าเฉพาะ payload

### Sign node options

ใช้ **Override Algorithm** เพื่อเลือก algorithm ที่จะใช้ในการ verify token ซึ่งจะ override algorithm ที่ตั้งไว้ใน credentials

### Verify node options

operation นี้มี options หลายตัว:

* **Return Additional Info**: toggle นี้ควบคุมว่าข้อมูลที่ node คืนค่าจะละเอียดแค่ไหน ถ้าเปิด node จะคืนค่าข้อมูล token ที่ decode แล้วทั้งหมด รวมถึง header และ signature ถ้าปิด node จะคืนค่าเฉพาะ payload
* **Ignore Expiration**: toggle นี้ควบคุมว่า node จะละเลย claim หมดอายุ (`exp`) หรือไม่ ดูข้อมูลเพิ่มเติมที่ ["exp" (Expiration Time) Claim](https://datatracker.ietf.org/doc/html/rfc7519#section-4.1.4){:target=_blank .external-link}
* **Ignore Not Before Claim**: toggle นี้ควบคุมว่าจะละเลย claim `nbf` หรือไม่ ดูข้อมูลเพิ่มเติมที่ ["nbf" (Not Before) Claim](https://datatracker.ietf.org/doc/html/rfc7519#section-4.1.5){:target=_blank .external-link}
* **Clock Tolerance**: ใส่จำนวนวินาทีที่ยอมให้ต่างกันได้ตอนตรวจสอบ `nbf` และ `exp` เพื่อรองรับความคลาดเคลื่อนของเวลาระหว่าง server ดูข้อมูลเพิ่มเติมที่ ["exp" (Expiration Time) Claim](https://datatracker.ietf.org/doc/html/rfc7519#section-4.1.4){:target=_blank .external-link}
* **Override Algorithm**: เลือก algorithm ที่จะใช้ในการ verify token ซึ่งจะ override algorithm ที่ตั้งไว้ใน credentials

## Templates and examples

<!-- see https://www.notion.so/n8n/Pull-in-templates-for-the-integrations-pages-37c716837b804d30a33b47475f6e3780 -->
[[ templatesWidget(page.title, 'jwt') ]]
