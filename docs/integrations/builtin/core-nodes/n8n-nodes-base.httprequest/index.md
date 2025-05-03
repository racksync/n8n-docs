---
#https://www.notion.so/n8n/Frontmatter-432c2b8dff1f43d4b1c8d20075510fe4
title: คู่มือ HTTP Request node
description: เรียนรู้วิธีใช้ HTTP Request node ใน n8n พร้อมคำอธิบายและตัวอย่างการใช้งาน
contentType: [integration, reference]
priority: critical
---

# HTTP Request node

HTTP Request node เป็นหนึ่งใน node ที่ยืดหยุ่นที่สุดใน n8n เลยนะ มันช่วยให้คุณสามารถส่ง HTTP request เพื่อดึงข้อมูลจากแอปหรือบริการไหนก็ได้ที่มี REST API คุณสามารถใช้ HTTP Request node เป็น node ปกติ หรือจะต่อกับ [AI agent](/integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.agent/tools-agent.md) เพื่อใช้เป็น [tool](/advanced-ai/examples/understand-tools.md){ data-preview } ก็ได้

เวลาคุณใช้ node นี้ คุณกำลังสร้าง REST API call อยู่ ดังนั้นควรเข้าใจคำศัพท์และแนวคิดพื้นฐานของ API ด้วยนะ

มี 2 วิธีในการสร้าง HTTP request: ตั้งค่าผ่าน [node parameters](#node-parameters) หรือ [import curl command](#import-curl-command)

/// note | Credentials
ดูวิธีตั้งค่า authentication ได้ที่ [HTTP Request credentials](/integrations/builtin/credentials/httprequest.md)
///

## Node parameters

### Method

เลือก method ที่จะใช้กับ request นี้:

- DELETE
- GET
- HEAD
- OPTIONS
- PATCH
- POST
- PUT

### URL

ใส่ endpoint ที่คุณต้องการใช้

### Authentication

n8n แนะนำให้ใช้ **Predefined Credential Type** ถ้ามีให้เลือก เพราะจะตั้งค่าและจัดการ credentials ได้ง่ายกว่าการตั้งค่าแบบ generic

#### Predefined credentials

Credentials สำหรับ integration ที่ n8n รองรับอยู่แล้ว ทั้ง built-in และ community node ใช้ **Predefined Credential Type** สำหรับ custom operation ได้เลยโดยไม่ต้องตั้งค่าอะไรเพิ่ม ดูรายละเอียดที่ [Custom API operations](/integrations/custom-operations.md)

#### Generic credentials

Credentials สำหรับ integration ที่ n8n ยังไม่รองรับ คุณต้องตั้งค่าการ authentication เองทั้งหมด รวมถึงระบุ endpoint, parameter ที่ต้องใช้ และวิธี authentication

คุณสามารถเลือกวิธีเหล่านี้ได้:

* Basic auth
* Custom auth
* Digest auth
* Header auth
* OAuth1 API
* OAuth2 API
* Query auth

ดูวิธีตั้งค่าแต่ละ credential type ได้ที่ [HTTP request credentials](/integrations/builtin/credentials/httprequest.md)

### Send Query Parameters

Query parameter คือ filter สำหรับ HTTP request ถ้า API ที่คุณใช้รองรับ และ request ที่คุณจะส่งต้องใช้ filter ให้เปิด option นี้

**ระบุ query parameter** ได้ 2 แบบ:

* **Using Fields Below**: ใส่ **Name**/**Value** ของ **Query Parameters** ถ้าจะเพิ่มคู่ name/value ให้เลือก **Add Parameter** ชื่อคือ field ที่จะ filter และ value คือค่าที่จะ filter
* **Using JSON**: ใส่ **JSON** เพื่อกำหนด query parameter

ดูรายละเอียดในเอกสาร API ของบริการที่คุณใช้

### Send Headers

ใช้ option นี้ถ้าต้องการส่ง header ไปกับ request ด้วย Header จะเก็บ metadata หรือ context ของ request

**ระบุ Header** ได้ 2 แบบ:

* **Using Fields Below**: ใส่ **Name**/**Value** ของ **Header Parameters** ถ้าจะเพิ่มคู่ name/value ให้เลือก **Add Parameter** ชื่อคือ header ที่ต้องการ set และ value คือค่าที่จะส่ง
* **Using JSON**: ใส่ **JSON** เพื่อกำหนด header parameter

ดูรายละเอียดในเอกสาร API ของบริการที่คุณใช้

### Send Body

ถ้าต้องการส่ง body ไปกับ API request ให้เปิด option นี้

จากนั้นเลือก **Body Content Type** ที่ตรงกับรูปแบบข้อมูลที่ต้องการส่ง

<!-- vale Vale.Spelling = NO -->
#### Form URLencoded
<!-- vale Vale.Spelling = YES -->

ใช้ option นี้ถ้าต้องการส่ง body แบบ `application/x-www-form-urlencoded`

**ระบุ Body** ได้ 2 แบบ:

* **Using Fields Below**: ใส่ **Name**/**Value** ของ **Body Parameters** ถ้าจะเพิ่มคู่ name/value ให้เลือก **Add Parameter** ชื่อคือชื่อ field ใน form และ value คือค่าที่จะ set
* **Using Single Field**: ใส่ name/value ทั้งหมดใน **Body** เดียวกัน เช่น `fieldname1=value1&fieldname2=value2`

ดูรายละเอียดในเอกสาร API ของบริการที่คุณใช้

#### Form-Data

ใช้ option นี้ถ้าต้องการส่ง body แบบ `multipart/form-data`

ตั้งค่า **Body Parameters** โดยเลือก **Parameter Type**:

* เลือก **Form Data** เพื่อใส่ **Name**/**Value** คู่
* เลือก **n8n Binary File** เพื่อดึง body จากไฟล์ที่ node เข้าถึงได้
    * **Name**: ใส่ ID ของ field ที่จะ set
    * **Input Data Field Name**: ใส่ชื่อ field ที่มี binary file data ที่ต้องการใช้

เลือก **Add Parameter** เพื่อเพิ่ม parameter ได้

ดูรายละเอียดในเอกสาร API ของบริการที่คุณใช้

#### JSON

ใช้ option นี้ถ้าต้องการส่ง body เป็น JSON

**ระบุ Body** ได้ 2 แบบ:

* **Using Fields Below**: ใส่ **Name**/**Value** ของ **Body Parameters** ถ้าจะเพิ่มคู่ name/value ให้เลือก **Add Parameter**
* **Using JSON**: ใส่ **JSON** เพื่อกำหนด body

ดูรายละเอียดในเอกสาร API ของบริการที่คุณใช้

#### n8n Binary File

ใช้ option นี้ถ้าต้องการส่งไฟล์ที่เก็บใน n8n เป็น body

ใส่ชื่อ field ที่มีไฟล์ใน **Input Data Field Name**

ดูรายละเอียดในเอกสาร API ของบริการที่คุณใช้ว่าต้อง format ไฟล์ยังไง

#### Raw

ใช้ option นี้ถ้าต้องการส่ง raw data ใน body

* **Content Type**: ใส่ header `Content-Type` ที่จะใช้กับ raw body ดู MIME content type ได้ที่ IANA [Media types](https://www.iana.org/assignments/media-types/media-types.xhtml){:target=_blank .external-link}
* **Body**: ใส่ raw body ที่จะส่ง

ดูรายละเอียดในเอกสาร API ของบริการที่คุณใช้

## Node options

เลือก **Add Option** เพื่อดูและเลือก option เหล่านี้ Option เหล่านี้ใช้ได้กับทุก parameter เว้นแต่จะระบุไว้

### Array Format in Query Parameters

/// note | Option availability
Option นี้จะมีให้เลือกเมื่อเปิด **Send Query Parameters**
///

ใช้ option นี้เพื่อกำหนดรูปแบบ array ใน query parameter เลือกได้ดังนี้:

* **No Brackets**: array จะถูก format เป็น name=value สำหรับแต่ละ item เช่น `foo=bar&foo=qux`
* **Brackets Only**: node จะเติม [] หลังชื่อ array เช่น `foo[]=bar&foo[]=qux`
* **Brackets with Indices**: node จะเติม [index] หลังชื่อ array เช่น `foo[0]=bar&foo[1]=qux`

ดูเอกสาร API ของบริการที่คุณใช้ว่าควรใช้แบบไหน

### Batching

ควบคุมการ batch input จำนวนมาก:

* **Items per Batch**: ใส่จำนวน input ที่จะรวมในแต่ละ batch
* **Batch Interval**: ใส่เวลาที่จะรอระหว่างแต่ละ batch ของ request (ms) ใส่ 0 ถ้าไม่ต้องการ delay

### Ignore SSL Issues

โดยปกติ n8n จะดาวน์โหลด response เฉพาะเมื่อ SSL certificate validation ผ่าน ถ้าอยากดาวน์โหลด response แม้ validation จะ fail ให้เปิด option นี้

### Lowercase Headers

เลือกว่าจะให้ชื่อ header เป็นตัวพิมพ์เล็ก (เปิดไว้เป็นค่า default) หรือไม่

### Redirects

เลือกว่าจะให้ตาม redirect (เปิดไว้เป็น default) หรือไม่ ถ้าเปิด ให้ใส่จำนวน redirect สูงสุดใน **Max Redirects**

### Response

ตั้งค่ารายละเอียดเกี่ยวกับ API response ที่คาดว่าจะได้รับ เช่น:

* **Include Response Headers and Status**: ปกติ node จะคืนแค่ body ถ้าเปิด option นี้จะได้ response เต็ม (header และ status code) ด้วย
* **Never Error**: ปกติ node จะคืน success เฉพาะเมื่อ response เป็น 2xx ถ้าเปิด option นี้จะคืน success ไม่ว่า code อะไร
* **Response Format**: เลือกรูปแบบข้อมูลที่ต้องการให้ node คืน เลือกได้:
    * **Autodetect** (default): node จะตรวจสอบและ format response ตามข้อมูลที่ได้
    * **File**: เลือก option นี้เพื่อให้ response เป็นไฟล์ ใส่ชื่อ field ที่ต้องการใน **Put Output in Field**
    * **JSON**: เลือก option นี้เพื่อให้ response เป็น JSON
    * **Text**: เลือก option นี้เพื่อให้ response เป็น plain text ใส่ชื่อ field ที่ต้องการใน **Put Output in Field**

### Pagination

ใช้ option นี้เพื่อ paginate ผลลัพธ์ เหมาะกับกรณีที่ API คืนข้อมูลเยอะเกินจะส่งใน call เดียว

/// note | Inspect the API data first
บาง option ของ pagination ต้องรู้โครงสร้างข้อมูลที่ API คืนมา ก่อนตั้งค่า pagination ควรเช็คเอกสาร API หรือทดลอง call API โดยไม่เปิด pagination ก่อน
///
??? Details "Understand pagination"
    Pagination คือการแบ่งข้อมูลชุดใหญ่เป็นหลายหน้า ข้อมูลแต่ละหน้าจะขึ้นกับ limit ที่ตั้งไว้

    เช่น คุณ call API `/users` แล้ว API มีข้อมูล user 300 คน ซึ่งเยอะเกินจะส่งใน response เดียว

    ถ้า API รองรับ pagination คุณสามารถดึงข้อมูลทีละน้อยได้ โดย call `/users` พร้อม limit และ page number หรือ URL เพื่อบอก API ว่าจะเอาหน้าไหน เช่น limit 10, page 0 API จะส่ง user 10 คนแรกมา จากนั้น call ใหม่โดยเพิ่ม page number อีก 1 เพื่อเอา 10 คนถัดไป

ตั้งค่า pagination ได้ดังนี้:

* **Pagination Mode**:
    * **Off**: ปิด pagination
    * **Update a Parameter in Each Request**: ใช้เมื่อคุณต้อง set parameter ใหม่ทุก request
    * **Response Contains Next URL**: ใช้เมื่อ API response มี URL ของหน้าถัดไป ใช้ expression ตั้งค่า **Next URL**

ดูตัวอย่างได้ที่ [HTTP Request node cookbook | Pagination](/code/cookbook/http-node/pagination.md)

n8n มี built-in variable สำหรับใช้กับ HTTP node request/response ตอนใช้ pagination:

--8<-- "_snippets/integrations/builtin/core-nodes/http/pagination-variables.md"

--8<-- "_snippets/integrations/builtin/core-nodes/http/pagination-api-differences.md"

### Proxy

ใช้ option นี้ถ้าต้องการระบุ HTTP proxy

ใส่ **Proxy** ที่ request จะใช้

### Timeout

ใช้ option นี้เพื่อตั้งเวลารอ server ส่ง response header (และเริ่ม response body) node จะยกเลิก request ที่เกินเวลานี้

ใส่ **Timeout** ที่ต้องการ (ms)

## Tool-only options

option เหล่านี้จะมีให้เลือกเฉพาะตอนต่อกับ [AI agent](/integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.agent/tools-agent.md) เป็น [tool](/advanced-ai/examples/understand-tools.md){ data-preview }

### Optimize Response

เลือกว่าจะ optimize response ที่ส่งไป LLM เพื่อลดข้อมูลและช่วยให้ LLM โฟกัสเฉพาะจุดสำคัญ (ช่วยลด cost และได้ผลลัพธ์ดีขึ้น)

เวลาทำ optimize response คุณจะเลือก expected response type ซึ่งจะมี option ให้ตั้งค่าเพิ่มดังนี้

#### JSON

ถ้าคาดว่าจะได้ **JSON** response คุณสามารถเลือกส่วนของ JSON ที่จะใช้กับ LLM ได้:

* **Field Containing Data**: ระบุ field ใน JSON ที่มีข้อมูลสำคัญ จะเว้นว่างไว้เพื่อใช้ทั้ง response ก็ได้
* **Include Fields**: เลือก field ที่จะเอาไปใน response มี 3 แบบ:
	* **All**: เอาทุก field ใน response object
	* **Selected**: เอาเฉพาะ field ที่ระบุ
		* **Fields**: ใส่ชื่อ field ที่ต้องการ (comma-separated) ใช้ dot notation ได้ เช่น a.b.c สามารถลาก field จาก Input panel มาใส่ได้
	* **Exclude**: เอาทุก field ยกเว้น field ที่ระบุ
		* **Fields**: ใส่ชื่อ field ที่ไม่ต้องการ (comma-separated) ใช้ dot notation ได้ เช่น a.b.c สามารถลาก field จาก Input panel มาใส่ได้

#### HTML

ถ้าคาดว่าจะได้ **HTML** response คุณสามารถเลือกส่วนของ HTML ที่เกี่ยวข้องกับ LLM และ optimize ได้ดังนี้:

* **Selector (CSS)**: ระบุ element หรือชนิด element ที่จะเอาไปใน response HTML (default คือ `body`)
* **Return Only Content**: เลือกว่าจะลบ tag/attribute HTML ออก เหลือแต่เนื้อหา (ช่วยลด token และ LLM เข้าใจง่ายขึ้น)
	* **Elements To Omit**: ใส่ selector ของ element ที่ไม่ต้องการใน content (comma-separated)
* **Truncate Response**: เลือกว่าจะจำกัดขนาด response เพื่อประหยัด token
	* **Max Response Characters**: จำนวน character สูงสุดใน HTML response (default 1000)

#### Text

ถ้าคาดว่าจะได้ **Text** response ทั่วไป สามารถ optimize ได้ดังนี้:

* **Truncate Response**: เลือกว่าจะจำกัดขนาด response เพื่อประหยัด token
	* **Max Response Characters**: จำนวน character สูงสุดใน response (default 1000)

## Import curl command

[curl](https://curl.se/){:target=_blank .external-link} คือ command line tool และ library สำหรับ transfer ข้อมูลผ่าน URL

คุณสามารถใช้ curl เพื่อ call REST API ได้ ถ้าเอกสาร API ของบริการที่คุณใช้มีตัวอย่าง curl ก็ copy มาใส่ใน n8n เพื่อ config HTTP Request node ได้เลย

วิธี import curl command:

1. ที่ HTTP Request node แท็บ **Parameters** เลือก **Import cURL** จะมี modal **Import cURL command** ขึ้นมา
2. วาง curl command ลงในช่องข้อความ
3. เลือก **Import** n8n จะโหลดค่าจาก curl เข้า node ให้เลย (จะทับ config เดิมทั้งหมด)

## Templates and examples

<!-- see https://www.notion.so/n8n/Pull-in-templates-for-the-integrations-pages-37c716837b804d30a33b47475f6e3780 -->
[[ templatesWidget(page.title, 'http-request') ]]

## Common issues

ถ้ามีคำถามหรือปัญหาที่พบบ่อย ดูวิธีแก้ได้ที่ [Common Issues](/integrations/builtin/core-nodes/n8n-nodes-base.httprequest/common-issues.md)
