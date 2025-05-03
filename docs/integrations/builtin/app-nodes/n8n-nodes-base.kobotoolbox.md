---
#https://www.notion.so/n8n/Frontmatter-432c2b8dff1f43d4b1c8d20075510fe4
title: เอกสารคู่มือ KoboToolbox node
description: เรียนรู้วิธีใช้ KoboToolbox node ใน n8n และดูเอกสารทางเทคนิคเพื่อเชื่อมต่อ KoboToolbox node เข้ากับ workflows ของคุณ
contentType: [integration, reference]
---

# KoboToolbox node

ใช้ KoboToolbox node เพื่อทำงานอัตโนมัติใน KoboToolbox และเชื่อมต่อ KoboToolbox กับแอปอื่นๆ ได้เลย n8n รองรับฟีเจอร์ของ KoboToolbox หลายอย่าง เช่น การสร้าง อัปเดต ลบ และดึงข้อมูล files, forms, hooks, และ submissions

ในหน้านี้จะมีรายการ operations ที่ KoboToolbox node รองรับ พร้อมลิงก์ไปยังแหล่งข้อมูลอื่นๆ

/// note | Credentials
โปรดดู [KoboToolbox credentials](/integrations/builtin/credentials/kobotoolbox.md) สำหรับคำแนะนำการตั้งค่าการยืนยันตัวตน
///

## Operations

* File
	* Create
	* Delete
	* Get
	* Get Many
* Form
    * Get
    * Get Many
		* Redeploy
* Hook
    * Get
    * Get Many
    * Logs
    * Retry All
    * Retry One
* Submission
    * Delete
    * Get
    * Get Many
    * Get Validation Status
    * Update Validation Status

## Templates and examples

<!-- see https://www.notion.so/n8n/Pull-in-templates-for-the-integrations-pages-37c716837b804d30a33b47475f6e3780 -->
[[ templatesWidget(page.title, 'kobotoolbox') ]]

## Options

### Query Options

Operation Query Submission รองรับ query options ดังนี้:

* ในส่วนหลักของ **Parameters** panel:
    * **Start** ใช้ควบคุม index offset ที่จะเริ่ม query (ใช้กับ pagination ของ API)
    * **Limit** กำหนดจำนวน records สูงสุดที่จะคืนค่า (API จำกัดสูงสุด 30,000 records ไม่ว่าคุณจะใส่ค่าอะไร)
* ในส่วน **Query Options** คุณสามารถเปิดใช้งาน parameters ต่อไปนี้:
    * **Query** ให้คุณระบุ filter predicates ในรูปแบบ MongoDB JSON query เช่น `{"status": "success", "_submission_time": {"$lt": "2021-11-01T01:02:03"}}` เพื่อ query submissions ที่ status เป็น `success` และส่งก่อนวันที่ 1 พ.ย. 2021 เวลา 01:02:03
    * **Fields** ระบุรายชื่อ fields ที่ต้องการดึงข้อมูล เพื่อลดขนาด response
    * **Sort** ระบุลำดับการ sort ในรูปแบบ MongoDB JSON เช่น `{"status": 1, "_submission_time": -1}` จะ sort ตาม status จากน้อยไปมาก แล้วตาม submission time จากมากไปน้อย

ดูรายละเอียดเพิ่มเติมเกี่ยวกับ options เหล่านี้ได้ที่ [Formhub API docs](https://github.com/SEL-Columbia/formhub/wiki/Formhub-Access-Points-(API)#api-parameters)

### Submission options

ทุก operation ที่คืนข้อมูล form submission จะมี options ให้ปรับแต่ง response ได้ เช่น:

- Download options ให้ดาวน์โหลดไฟล์แนบที่เชื่อมกับแต่ละ submission เช่น รูปภาพ วิดีโอ และเลือก pattern การตั้งชื่อไฟล์ รวมถึงขนาดไฟล์ที่จะดาวน์โหลด (ถ้ามี - ส่วนใหญ่ใช้กับรูปภาพ)
- Formatting options จะช่วยจัดรูปแบบข้อมูลใหม่ ตามที่อธิบายไว้ใน [About reformatting](#about-reformatting)

#### About reformatting

JSON format ปกติของข้อมูล submission ใน KoboToolbox อาจใช้งานยาก เพราะไม่ schema-aware และทุก field จะถูกส่งกลับมาเป็น string

node นี้มี logic สำหรับ reformatting แบบเบาๆ เปิดใช้งานได้ด้วย parameter **Reformat?** ในทุก operation ที่คืนข้อมูล form submission: ทั้ง query, get, และ download attachment

เมื่อเปิดใช้งาน reformatting:

- จะจัดโครงสร้าง JSON ใหม่เป็น multi-level hierarchy ตามกลุ่มในฟอร์ม โดยปกติชื่อ field จะใช้ `/` เช่น `Group1/Question1` ถ้าเปิด reformatting n8n จะเปลี่ยนเป็น `Group1.Question1` แบบ nested JSON object
- เปลี่ยนชื่อ field เพื่อตัด `_` ออก (บางระบบ downstream ไม่รองรับ)
- แปลง field ที่เป็น geospatial (Point, Line, Area) เป็น GeoJSON มาตรฐาน
- แยก field ที่ตรงกับ **Multiselect Mask** ให้เป็น array (multi-select ปกติเป็น string คั่นด้วย space ต้องระบุ mask เอง เช่น `Crops_*`)
- แปลง field ที่ตรงกับ **Number Mask** ให้เป็น float

ตัวอย่าง JSON:

```json
{
  "_id": 471987,
  "formhub/uuid": "189436bb09a54957bfcc798e338b54d6",
  "start": "2021-12-05T16:13:38.527+02:00",
  "end": "2021-12-05T16:15:33.407+02:00",
  "Field_Details/Field_Name": "Test Fields",
  "Field_Details/Field_Location": "-1.932914 30.078211 1421 165",
  "Field_Details/Field_Shape": "-1.932914 30.078211 1421 165;-1.933011 30.078085 0 0;-1.933257 30.078004 0 0;-1.933338 30.078197 0 0;-1.933107 30.078299 0 0;-1.932914 30.078211 1421 165",
  "Field_Details/Crops_Grown": "maize beans avocado",
  "Field_Details/Field_Size_sqm": "2300",
  "__version__": "veGcULpqP6JNFKRJbbMvMs",
  "meta/instanceID": "uuid:2356cbbe-c1fd-414d-85c8-84f33e92618a",
  "_xform_id_string": "ajXVJpBkTD5tB4Nu9QXpgm",
  "_uuid": "2356cbbe-c1fd-414d-85c8-84f33e92618a",
  "_attachments": [],
  "_status": "submitted_via_web",
  "_geolocation": [
    -1.932914,
    30.078211
  ],
  "_submission_time": "2021-12-05T14:15:44",
  "_tags": [],
  "_notes": [],
  "_validation_status": {},
  "_submitted_by": null
}
```

ถ้าเปิด reformatting และตั้งค่า mask สำหรับ multi-select กับ number (เช่น `Crops_*` และ `*_sqm`) n8n จะ parse เป็นแบบนี้:

```json
{
  "id": 471987,
  "formhub": {
    "uuid": "189436bb09a54957bfcc798e338b54d6"
  },
  "start": "2021-12-05T16:13:38.527+02:00",
  "end": "2021-12-05T16:15:33.407+02:00",
  "Field_Details": {
    "Field_Name": "Test Fields",
    "Field_Location": {
      "lat": -1.932914,
      "lon": 30.078211
    },
    "Field_Shape": {
      "type": "polygon",
      "coordinates": [
        {
          "lat": -1.932914,
          "lon": 30.078211
        },
        {
          "lat": -1.933011,
          "lon": 30.078085
        },
        {
          "lat": -1.933257,
          "lon": 30.078004
        },
        {
          "lat": -1.933338,
          "lon": 30.078197
        },
        {
          "lat": -1.933107,
          "lon": 30.078299
        },
        {
          "lat": -1.932914,
          "lon": 30.078211
        }
      ]
    },
    "Crops_Grown": [
      "maize",
      "beans",
      "avocado"
    ],
    "Field_Size_sqm": 2300
  },
  "version": "veGcULpqP6JNFKRJbbMvMs",
  "meta": {
    "instanceID": "uuid:2356cbbe-c1fd-414d-85c8-84f33e92618a"
  },
  "xform_id_string": "ajXVJpBkTD5tB4Nu9QXpgm",
  "uuid": "2356cbbe-c1fd-414d-85c8-84f33e92618a",
  "attachments": [],
  "status": "submitted_via_web",
  "geolocation": {
    "lat": -1.932914,
    "lon": 30.078211
  },
  "submission_time": "2021-12-05T14:15:44",
  "tags": [],
  "notes": [],
  "validation_status": {},
  "submitted_by": null
}
```

--8<-- "_snippets/integrations/builtin/app-nodes/operation-not-supported.md"
