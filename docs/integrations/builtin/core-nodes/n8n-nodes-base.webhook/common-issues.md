---
#https://www.notion.so/n8n/Frontmatter-432c2b8dff1f43d4b1c8d20075510fe4
title: ปัญหาที่พบบ่อยใน Webhook node
description: รวมปัญหาและคำถามที่พบบ่อยเกี่ยวกับ Webhook node ใน n8n พร้อมแนวทางแก้ไข
contentType: [integration, reference]
priority: critical
---

# Common issues and questions

รวมปัญหาและคำถามที่พบบ่อยสำหรับ [Webhook node](/integrations/builtin/core-nodes/n8n-nodes-base.webhook/index.md) พร้อมวิธีแก้ไข

## Listen for multiple HTTP methods

โดยปกติ Webhook node จะรับแค่ HTTP method เดียว เช่น รับ GET หรือ POST อย่างใดอย่างหนึ่ง ถ้าอยากให้รับได้หลาย method:

1. เปิด **Settings** ของ node
1. เปิด **Allow Multiple HTTP Methods**
1. กลับไปที่ **Parameters** ตอนนี้ node จะรับ GET และ POST ได้แล้วโดย default สามารถเพิ่ม method อื่นใน field **HTTP Methods** ได้

Webhook node จะมี output แยกตามแต่ละ method ทำให้กำหนด action ต่างกันได้ตาม method ที่รับ

## Use the HTTP Request node to trigger the Webhook node

[HTTP Request](/integrations/builtin/core-nodes/n8n-nodes-base.httprequest/index.md) node ใช้ส่ง HTTP request ไปยัง URL ที่กำหนด

1. สร้าง workflow ใหม่
2. เพิ่ม HTTP Request node ใน workflow
3. เลือก method ที่ต้องการใน **Request Method** เช่น ถ้า Webhook node ใช้ GET ให้ HTTP Request node ใช้ GET ด้วย
4. คัดลอก URL จาก Webhook node ไปวางใน **URL** ของ HTTP Request node
5. ถ้าใช้ test URL ของ webhook node: ให้ execute workflow ที่มี Webhook node ก่อน
6. Execute HTTP Request node

## Use curl to trigger the Webhook node

สามารถใช้ [curl](https://curl.se/){:target=_blank .external-link} เพื่อส่ง HTTP request ไป trigger Webhook node ได้

/// note
ในตัวอย่าง ให้แทนที่ `<https://your-n8n.url/webhook/path>` ด้วย webhook URL ของคุณ  
ตัวอย่างใช้ GET request แต่สามารถใช้ method อื่นที่ตั้งไว้ใน **HTTP Method** ได้
///

ส่ง HTTP request โดยไม่มี parameter:

```sh
curl --request GET <https://your-n8n.url/webhook/path>
```

ส่ง HTTP request พร้อม body parameter:

```sh
curl --request GET <https://your-n8n.url/webhook/path> --data 'key=value'
```

ส่ง HTTP request พร้อม header parameter:

```sh
curl --request GET <https://your-n8n.url/webhook/path> --header 'key=value'
```

ส่ง HTTP request เพื่ออัปโหลดไฟล์:

```sh
curl --request GET <https://your-n8n.url/webhook/path> --from 'key=@/path/to/file'
```
แทนที่ `/path/to/file` ด้วย path ของไฟล์ที่ต้องการส่ง

## Send a response of type string

โดยปกติ response format จะเป็น JSON หรือ array ถ้าอยากให้ส่ง response เป็น string:

1. เลือก **Response Mode** > **When Last Node Finishes**
2. เลือก **Response Data** > **First Entry JSON**
3. เลือก **Add Option** > **Property Name**
4. ใส่ชื่อ property ที่เก็บ response โดย default คือ `data`
5. เชื่อม [Edit Fields node](/integrations/builtin/core-nodes/n8n-nodes-base.set.md) กับ Webhook node
6. ใน Edit Fields node เลือก **Add Value** > **String**
7. ใส่ชื่อ property ใน **Name** ให้ตรงกับข้อ 4
8. ใส่ค่าที่ต้องการใน **Value**
9. เปิด **Keep Only Set** (ให้เป็นสีเขียว)

เมื่อเรียก Webhook จะได้ string response จาก Edit Fields node

## Test URL versus Production URL

n8n จะสร้าง **Webhook URLs** สองแบบให้แต่ละ Webhook node: **Test URL** และ **Production URL**

ตอนสร้างหรือทดสอบ workflow ให้ใช้ **Test URL** เมื่อพร้อมใช้งานจริงให้เปลี่ยนไปใช้ **Production URL**

| **URL type** | **How to trigger** | **Listening duration** | **Data shown in editor UI?** | 
| :--- | --- | --- | :---: |
| Test URL | เลือก **Listen for test event** แล้ว trigger event จากต้นทาง | 120 seconds | :white_check_mark: |
| Production URL | Activate workflow | จนกว่าจะ deactivate workflow | :x: |

ดูรายละเอียดเพิ่มเติมที่ [Workflow development](/integrations/builtin/core-nodes/n8n-nodes-base.webhook/workflow-development.md)

## IPs in Whitelist are failing to connect

ถ้าเชื่อมต่อจาก IP ที่อยู่ใน IP Whitelist ไม่ได้ ให้ตรวจสอบว่ารัน n8n อยู่หลัง reverse proxy หรือไม่

ถ้าใช่ ให้ตั้งค่า [environment variable](/hosting/configuration/environment-variables/index.md) `N8N_PROXY_HOPS` เป็นจำนวน reverse-proxy ที่ n8n อยู่ข้างหลัง
