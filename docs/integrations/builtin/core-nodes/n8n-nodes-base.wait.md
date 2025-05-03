---
#https://www.notion.so/n8n/Frontmatter-432c2b8dff1f43d4b1c8d20075510fe4
title: Wait
description: เอกสารสำหรับ Wait node ใน n8n แพลตฟอร์ม workflow automation พร้อมคำแนะนำการใช้งานและตัวอย่าง
contentType: [integration, reference]
priority: critical
---

# Wait

ใช้ Wait node เพื่อหยุดการทำงานของ workflow ชั่วคราว เมื่อ workflow หยุดชั่วคราว ข้อมูล execution จะถูก offload ไปที่ database และเมื่อเงื่อนไข resume ตรงตามที่ตั้งไว้ workflow จะโหลดข้อมูลกลับมาแล้วทำงานต่อ

## Operations

Wait node สามารถ **Resume** ได้ตามเงื่อนไขเหล่านี้:

* [**After Time Interval**](#after-time-interval): รอเป็นระยะเวลาที่กำหนด
* [**At Specified Time**](#at-specified-time): รอจนถึงเวลาที่กำหนด
* [**On Webhook Call**](#on-webhook-call): รอจนกว่าจะได้รับ HTTP call
* [**On Form Submitted**](#on-form-submitted): รอจนกว่าจะได้รับการส่งฟอร์ม

ดูรายละเอียดแต่ละแบบได้ในหัวข้อด้านล่าง

### After Time Interval

รอเป็นระยะเวลาที่กำหนด

parameter นี้จะมี 2 field เพิ่มเติม:

* **Wait Amount**: ใส่จำนวนเวลาที่ต้องการรอ
* **Wait Unit**: เลือกหน่วยของ **Wait Amount** มีให้เลือก:
	* **Seconds**
	* **Minutes**
	* **Hours**
	* **Days**

ดูรายละเอียดเพิ่มเติมเกี่ยวกับ [Time-based operations](#time-based-operations) ว่า interval ทำงานอย่างไรและใช้ timezone อะไร

### At Specified Time

รอจนถึงวันที่และเวลาที่กำหนด ใช้ date และ time picker เพื่อเลือก **Date and Time**

ดูรายละเอียดเพิ่มเติมเกี่ยวกับ timezone ได้ที่ [Time-based operations](#time-based-operations)

### On Webhook Call

parameter นี้ช่วยให้ workflow resume ได้เมื่อ Wait node ได้รับ HTTP call

Webhook URL ที่จะ resume execution จะถูกสร้างขึ้นตอน runtime Wait node จะให้ตัวแปร `$execution.resumeUrl` เพื่อให้คุณนำไปใช้หรือส่งต่อ URL ที่จะถูกสร้างนี้ไปยังที่อื่น เช่น ส่งให้ third-party หรือในอีเมล

เมื่อ workflow ทำงาน Wait node จะสร้าง resume URL และ webhook ใน workflow โดยใช้ `$execution.resumeUrl` URL ที่สร้างนี้จะ unique สำหรับแต่ละ execution ดังนั้น workflow สามารถมี Wait node หลายตัว และเมื่อ webhook ถูกเรียกแต่ละตัวก็จะ resume ตามลำดับ

สำหรับ **Resume** แบบนี้ ให้ตั้งค่า parameters เพิ่มเติมดังนี้

#### Authentication

เลือกว่าจะให้ request ที่เข้ามา resume webhook ที่ `$execution.resumeUrl` ต้อง authenticate หรือไม่ ตัวเลือกมี:

* **Basic Auth**: ใช้ basic authentication เลือกหรือสร้าง **Credential for Basic Auth**
* **Header Auth**: ใช้ header authentication เลือกหรือสร้าง **Credential for Header Auth**
* **JWT Auth**: ใช้ JWT authentication เลือกหรือสร้าง **Credential for JWT Auth**
* **None**: ไม่ต้องใช้ authentication

/// note | Auth reference
ดูรายละเอียดแต่ละ auth type ได้ที่ [Webhook node | Authentication documentation](/integrations/builtin/core-nodes/n8n-nodes-base.webhook/index.md#supported-authentication-methods)
///

#### HTTP Method

เลือก HTTP method ที่ webhook จะใช้ ดูรายละเอียดได้ที่ [Webhook node | HTTP Method documentation](/integrations/builtin/core-nodes/n8n-nodes-base.webhook/index.md#http-method)

#### Response Code

ใส่ Response Code ที่ webhook จะ return สามารถใช้ code ทั่วไปหรือกำหนดเองก็ได้

#### Respond

ตั้งค่าว่าจะตอบกลับ webhook เมื่อไหร่และอย่างไร มีตัวเลือกดังนี้:

* **Immediately**: ตอบกลับทันทีที่ node ทำงาน
* **When Last Node Finishes**: ตอบกลับด้วย response code และข้อมูล output ของ node สุดท้ายใน workflow ถ้าเลือกตัวเลือกนี้ ให้ตั้งค่าเพิ่ม:
	* **Response Data**: เลือกข้อมูลและรูปแบบที่จะ return มีตัวเลือก:
		* **All Entries**: ส่งข้อมูลทั้งหมดของ node สุดท้ายใน array
		* **First Entry JSON**: ส่งข้อมูล JSON ของ entry แรกของ node สุดท้ายในรูปแบบ object
		* **First Entry Binary**: ส่งข้อมูล binary ของ entry แรกของ node สุดท้ายเป็นไฟล์
		* **No Response Body**: ตอบกลับโดยไม่มี body
* **Using 'Respond to Webhook' Node**: ตอบกลับตามที่ตั้งค่าไว้ใน [Respond to Webhook](/integrations/builtin/core-nodes/n8n-nodes-base.respondtowebhook.md) node

#### Limit Wait Time

ตั้งค่าว่า workflow จะ resume อัตโนมัติหลังจากถึง limit ที่กำหนดหรือไม่ (เปิด/ปิด) ถ้าเปิด ให้ตั้งค่าเพิ่ม:

* **Limit Type**: เลือกประเภท limit ที่ต้องการ มีตัวเลือก:
	* **After Time Interval**: รอเป็นระยะเวลาที่กำหนด
		* ใส่ **Amount** ของเวลาที่ต้องการ
		* เลือก **Unit** ของเวลา
	* **At Specified Time**: รอจนถึงวันที่และเวลาที่กำหนด
		* **Max Date and Time**: ใช้ date และ time picker เพื่อเลือกเวลาที่ node จะ resume

#### On Webhook Call options

* **Binary Property**: ใส่ชื่อ property ที่จะเก็บข้อมูล binary ที่ได้รับมา ใช้เฉพาะกรณีรับ binary data
* **Ignore Bots**: ตั้งค่าว่าจะ ignore request จาก bot เช่น link previewer หรือ web crawler หรือไม่ (เปิด/ปิด)
* **IP(s) Whitelist**: ใส่ IP address ที่อนุญาตให้เรียก webhook ได้ ใส่หลาย IP คั่นด้วย comma ถ้าเว้นว่างไว้ ทุก IP จะเรียกได้ ถ้า IP ไม่อยู่ใน whitelist จะได้ error 403
* **No Response Body**: ตั้งค่าว่า n8n จะส่ง body ใน response หรือไม่ (ปิด = ส่ง, เปิด = ไม่ส่ง)
* **Raw Body**: ตั้งค่าว่าจะ return body ในรูปแบบ raw เช่น JSON หรือ XML หรือไม่ (เปิด/ปิด)
* **Response Data**: ใส่ข้อมูล custom ที่ต้องการส่งกลับใน response
* **Response Headers**: ใส่ header เพิ่มเติมใน webhook response ดูรายละเอียด header ได้ที่ [MDN Web Docs | Response header](https://developer.mozilla.org/en-US/docs/Glossary/Response_header){:target=_blank .external-link}
* **Webhook Suffix**: ใส่ suffix ที่จะต่อท้าย resume URL ใช้สำหรับสร้าง webhook URL ที่ unique สำหรับแต่ละ Wait node ใน workflow ที่มีหลาย Wait node หมายเหตุ: `$resumeWebhookUrl` ที่สร้างจะยังไม่รวม suffix นี้ ต้องต่อเองก่อนนำไปใช้

#### On Webhook Call limitations

ข้อจำกัดที่ควรทราบเมื่อใช้ On Webhook Call:

* ถ้า workflow ถูก execute แบบ partial ค่า `$resumeWebhookUrl` จะเปลี่ยน ดังนั้นต้องแน่ใจว่า node ที่ส่ง URL นี้ไปยัง third-party ต้องทำงานใน execution เดียวกับ Wait node

### On Form Submitted

รอจนกว่าจะมีการส่งฟอร์มก่อนจะทำงานต่อ ตั้งค่าดังนี้:

#### Form Title

ใส่หัวข้อที่จะแสดงด้านบนของฟอร์ม

#### Form Description

ใส่คำอธิบายฟอร์มที่จะแสดงใต้หัวข้อ ใช้เพื่ออธิบายหรือแนะนำการกรอกฟอร์ม

#### Form Fields

ตั้งค่าฟิลด์แต่ละอันที่จะให้แสดงในฟอร์มโดยใช้ parameters เหล่านี้:

* **Field Label**: ใส่ label ที่ต้องการให้แสดงในฟอร์ม
* **Field Type**: เลือกประเภทฟิลด์ที่ต้องการ มีให้เลือก:
	* **Date**
	* **Dropdown List**: ใส่ตัวเลือก dropdown ใน **Field Options**
		* **Multiple Choice**: เลือกว่าจะให้เลือกได้หลายตัว (เปิด) หรือเลือกได้ตัวเดียว (ปิด)
	* **Number**
	* **Password**
	* **Text**
	* **Textarea**
* **Required Field**: ตั้งค่าว่าต้องกรอกฟิลด์นี้ก่อนส่งฟอร์มหรือไม่ (เปิด/ปิด)

#### Respond When

ตั้งค่าว่าจะตอบกลับเมื่อไหร่ มีตัวเลือก:

* **Form Is Submitted**: ตอบกลับทันทีที่ได้รับการส่งฟอร์ม
* **Workflow Finishes**: ตอบกลับเมื่อ node สุดท้ายของ workflow ทำงานเสร็จ
* **Using 'Respond to Webhook' Node**: ตอบกลับเมื่อ [Respond to Webhook](/integrations/builtin/core-nodes/n8n-nodes-base.respondtowebhook.md) node ทำงาน

#### Limit Wait Time

ตั้งค่าว่า workflow จะ resume อัตโนมัติหลังจากถึง limit ที่กำหนดหรือไม่ (เปิด/ปิด)

ถ้าเปิด ให้ตั้งค่าเพิ่ม:
* **Limit Type**: เลือกประเภท limit ที่ต้องการ มีตัวเลือก:
	* **After Time Interval**: รอเป็นระยะเวลาที่กำหนด
		* ใส่ **Amount** ของเวลาที่ต้องการ
		* เลือก **Unit** ของเวลา
	* **At Specified Time**: รอจนถึงวันที่และเวลาที่กำหนด
		* **Max Date and Time**: ใช้ date และ time picker เพื่อเลือกเวลาที่ node จะ resume

#### On Form Response options

* **Form Response**: เลือกวิธีและสิ่งที่ต้องการให้ฟอร์มตอบกลับ มีตัวเลือก:
	* **Form Submitted Text**: ฟอร์มจะแสดงข้อความที่ใส่ใน **Text to Show** หลังจากผู้ใช้ส่งฟอร์ม ใช้สำหรับแสดงข้อความยืนยัน
	* **Redirect URL**: ฟอร์มจะ redirect ผู้ใช้ไปยัง **URL to Redirect to** หลังจากส่งฟอร์ม ต้องเป็น URL ที่ถูกต้อง
* **Webhook Suffix**: ใส่ suffix ที่จะต่อท้าย resume URL ใช้สำหรับสร้าง webhook URL ที่ unique สำหรับแต่ละ Wait node ใน workflow ที่มีหลาย Wait node หมายเหตุ: `$resumeWebhookUrl` ที่สร้างจะยังไม่รวม suffix นี้ ต้องต่อเองก่อนนำไปใช้

## Templates and examples

<!-- see https://www.notion.so/n8n/Pull-in-templates-for-the-integrations-pages-37c716837b804d30a33b47475f6e3780 -->
[[ templatesWidget(page.title, 'wait') ]]

## Time-based operations

สำหรับการ resume แบบใช้เวลา ให้ทราบว่า:

* ถ้าระยะเวลารอไม่ถึง 65 วินาที workflow จะไม่ offload ข้อมูล execution ไปที่ database แต่ process จะยังรันอยู่และ resume หลังจากครบเวลาที่กำหนด
* n8n จะใช้เวลาของ server เสมอ ไม่ว่าจะตั้ง timezone workflow ไว้อย่างไร หรือเปลี่ยน timezone ก็ไม่มีผลกับ Wait node
