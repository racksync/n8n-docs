---
#https://www.notion.so/n8n/Frontmatter-432c2b8dff1f43d4b1c8d20075510fe4
title: PostBin node documentation
description: เรียนรู้วิธีการใช้ PostBin node ใน n8n. ติดตามเอกสารทางเทคนิคเพื่อรวม PostBin node เข้ากับ workflows ของคุณ.
contentType: [integration, reference]
priority: high
---

# PostBin node

PostBin เป็นบริการที่ช่วยให้คุณทดสอบ API clients และ webhooks ได้อย่างง่ายดาย. ใช้ PostBin node เพื่อช่วยทำงานใน PostBin แบบอัตโนมัติและเชื่อมต่อกับแอปพลิเคชันอื่น ๆ. n8n มีการสนับสนุนคุณสมบัติของ PostBin หลากหลาย เช่น การสร้างและลบ bins รวมถึงการดึงและส่ง requests.

ในหน้านี้ คุณจะพบรายการของ operations ที่ PostBin node รองรับและลิงก์สำหรับข้อมูลเพิ่มเติม.

## Operations

* Bin
	* Create
	* Get
	* Delete
* Request
	* Get
	* Remove First
	* Send

## Templates and examples

<!-- see https://www.notion.so/n8n/Pull-in-templates-for-the-integrations-pages-37c716837b804d30a33b47475f6e3780 -->
[[ templatesWidget(page.title, 'postbin') ]]

## Send requests

การส่ง requests ไปที่ PostBin bin:

1. ไปที่ [PostBin](https://www.toptal.com/developers/postbin/){:target=_blank .external-link} แล้วทำตามขั้นตอนเพื่อสร้าง bin ใหม่. PostBin จะให้ URL ที่ไม่ซ้ำกัน รวมถึง bin ID.
2. ใน PostBin node ให้เลือก **Request** resource.
3. เลือกประเภทของ **Operation** ที่คุณต้องการดำเนินการ.
4. ป้อน bin ID ของคุณใน **Bin ID**.

## Create and manage bins

คุณสามารถสร้างและจัดการ PostBin bins โดยใช้ PostBin node.

1. ใน **Resource** ให้เลือก **Bin**.
2. เลือก **Operation** คุณสามารถสร้าง, ลบ หรือดึงข้อมูล bin.
