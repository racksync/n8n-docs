---
#https://www.notion.so/n8n/Frontmatter-432c2b8dff1f43d4b1c8d20075510fe4
title: ปัญหาที่พบบ่อยใน HTTP Request node
description: รวมปัญหาและคำถามที่พบบ่อยเกี่ยวกับ HTTP Request node ใน n8n พร้อมแนวทางแก้ไขและคำแนะนำ
contentType: [integration, reference]
priority: critical
---

# HTTP Request node common issues

รวม error และปัญหาที่เจอบ่อยกับ [HTTP Request node](/integrations/builtin/core-nodes/n8n-nodes-base.httprequest/index.md) พร้อมวิธีแก้หรือแนวทางตรวจสอบ

## Bad request - please check your parameters

error นี้จะขึ้นเมื่อ node ได้รับ 400 error (bad request) สาเหตุที่เจอบ่อยคือ:

* ใช้ชื่อหรือ value ของ **Query Parameter** ไม่ถูกต้อง
* ส่ง array ใน **Query Parameter** แต่ format ไม่ถูก ลองใช้ option [**Array Format in Query Parameters**](/integrations/builtin/core-nodes/n8n-nodes-base.httprequest/index.md#array-format-in-query-parameters) ดู

แนะนำให้เช็คเอกสาร API ของบริการที่ใช้ว่าควร format query parameter ยังไง

<!-- vale off -->
## The resource you are requesting could not be found
<!-- vale on -->

error นี้จะขึ้นเมื่อ endpoint **URL** ที่ใส่ไม่ถูกต้อง

อาจจะพิมพ์ URL ผิด หรือ API นั้นเลิกใช้แล้ว ให้เช็คเอกสาร API ของบริการนั้นๆ ว่า endpoint ถูกต้องไหม

## JSON parameter need to be an valid JSON

error นี้จะขึ้นเมื่อส่ง parameter เป็น JSON แต่ format ไม่ถูกต้อง

วิธีแก้:

* ลองเช็ค JSON ที่ใส่ใน JSON checker หรือ syntax parser เพื่อหาข้อผิดพลาด เช่น ลืมใส่เครื่องหมายคำพูด, มี comma เกิน/ขาด, array format ผิด, ลืมปิด [] หรือ {} ฯลฯ
* ถ้าใช้ **Expression** ใน node ต้องครอบ JSON ทั้งหมดด้วย double curly brackets เช่น:
    ```
    {{
        {
        "myjson":
        {
            "name1": "value1",
            "name2": "value2",
            "array1":
                ["value1","value2"]
        }
        }
    }}
    ```

## Forbidden - perhaps check your credentials

error นี้จะขึ้นเมื่อ node ได้รับ 403 error (authentication fail)

วิธีแก้:

* ตรวจสอบ credential ที่เลือกว่าถูกต้องไหม และสามารถ authenticate ได้จริงหรือเปล่า
* อาจจะต้องอัปเดต permission หรือ scope ของ API key/account ให้สามารถทำ operation ที่เลือกได้
* ลอง format generic credential ใหม่
* สร้าง API key หรือ token ใหม่ที่มี permission/scope ที่ต้องการ

## 429 - The service is receiving too many requests from you

error นี้จะขึ้นเมื่อ node ได้รับ [429 error](https://developer.mozilla.org/en-US/docs/Web/HTTP/Status/429){:target=_blank .external-link} จากบริการที่เรียก ซึ่งมักจะหมายถึงคุณส่ง request ไปเยอะเกิน limit ของบริการนั้น ดูรายละเอียดเพิ่มเติมที่ [Handling API rate limits](/integrations/builtin/rate-limits.md)

วิธีแก้ สามารถใช้ option ใน HTTP request node ได้ดังนี้:

### Batching

ใช้ option นี้เพื่อส่ง request ทีละ batch และหน่วงเวลาแต่ละ batch

1. ที่ HTTP Request node เลือก **Add Option > Batching**
1. ตั้งค่า **Items per Batch** เป็นจำนวน input ที่จะรวมในแต่ละ request
1. ตั้งค่า **Batch Interval (ms)** เพื่อหน่วงเวลาระหว่างแต่ละ request (ms) เช่น ถ้าจะส่ง 1 request ต่อวินาที ให้ตั้ง **Batch Interval (ms)** เป็น `1000`

### Retry on Fail

ใช้ option นี้เพื่อ retry node ถ้า request fail

1. ที่ HTTP Request node ไปที่ **Settings** แล้วเปิด **Retry on Fail**
1. ตั้งค่า **Max Tries** เป็นจำนวนครั้งสูงสุดที่ n8n จะ retry node
1. ตั้งค่า **Wait Between Tries (ms)** เป็นเวลาที่จะรอก่อน retry (ms) เช่น ถ้าจะรอ 1 วินาทีก่อน retry ให้ตั้ง **Wait Between Tries (ms)** เป็น `1000`

