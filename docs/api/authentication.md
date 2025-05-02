---
#https://www.notion.so/n8n/Frontmatter-432c2b8dff1f43d4b1c8d20075510fe4
description: Authentication for n8n's public REST API.
contentType: howto
---

# API authentication

n8n ใช้ API keys เพื่อ authenticate การเรียก API

/// info | Feature availability
n8n API ไม่มีให้บริการในช่วงทดลองใช้ฟรี โปรด upgrade เพื่อเข้าถึงฟีเจอร์นี้
///


## Create an API key

1.  Log in เข้าสู่ n8n
2.  ไปที่ **Settings** > **n8n API**
3.  เลือก **Create an API key**
4.  คัดลอก **My API Key** และใช้ key นี้เพื่อ authenticate การเรียกของคุณ


## Call the API using your key

ส่ง API key ในการเรียก API ของคุณเป็น header ชื่อ `X-N8N-API-KEY`

ตัวอย่างเช่น สมมติว่าคุณต้องการดึงข้อมูล workflows ที่ active ทั้งหมด request curl ของคุณจะมีลักษณะดังนี้:

```shell
# สำหรับ n8n instance แบบ self-hosted
curl -X 'GET' \
  '<N8N_HOST>:<N8N_PORT>/<N8N_PATH>/api/v<version-number>/workflows?active=true' \
  -H 'accept: application/json' \
  -H 'X-N8N-API-KEY: <your-api-key>'

# สำหรับ n8n Cloud
curl -X 'GET' \
  '<your-cloud-instance>/api/v<version-number>/workflows?active=true' \
  -H 'accept: application/json' \
  -H 'X-N8N-API-KEY: <your-api-key>'
```

## Delete an API key

1.  Log in เข้าสู่ n8n
2.  ไปที่ **Settings** > **n8n API**
3.  เลือก **Delete** ถัดจาก key ที่คุณต้องการลบ
4.  ยืนยันการลบโดยเลือก **Delete Forever**
