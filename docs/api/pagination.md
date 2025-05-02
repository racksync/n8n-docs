---
#https://www.notion.so/n8n/Frontmatter-432c2b8dff1f43d4b1c8d20075510fe4
description: Pagination in n8n's public REST API.
contentType: howto
---

# API pagination

ขนาดหน้าเริ่มต้นคือ 100 ผลลัพธ์ คุณสามารถเปลี่ยนขีดจำกัดขนาดหน้าได้ ขนาดสูงสุดที่อนุญาตคือ 250

เมื่อ response มีมากกว่าหนึ่งหน้า จะมี cursor ซึ่งคุณสามารถใช้เพื่อขอหน้าถัดไปได้

ตัวอย่างเช่น สมมติว่าคุณต้องการดึงข้อมูล workflows ที่ active ทั้งหมด ครั้งละ 150 รายการ

รับหน้าแรก:

```shell
# สำหรับ n8n instance แบบ self-hosted
curl -X 'GET' \
  '<N8N_HOST>:<N8N_PORT>/<N8N_PATH>/api/v<version-number>/workflows?active=true&limit=150' \
  -H 'accept: application/json' \
  -H 'X-N8N-API-KEY: <your-api-key>'

# สำหรับ n8n Cloud
curl -X 'GET' \
  '<your-cloud-instance>/api/v<version-number>/workflows?active=true&limit=150' \
  -H 'accept: application/json' \
  -H 'X-N8N-API-KEY: <your-api-key>'
```

response อยู่ในรูปแบบ JSON และมีค่า `nextCursor` นี่คือตัวอย่าง response

```js
{
  "data": [
    // The response contains an object for each workflow
    {
      // Workflow data
    }
  ],
  "nextCursor": "MTIzZTQ1NjctZTg5Yi0xMmQzLWE0NTYtNDI2NjE0MTc0MDA"
}
```

จากนั้น หากต้องการขอหน้าถัดไป:

```bash
# สำหรับ n8n instance แบบ self-hosted
curl -X 'GET' \
  '<N8N_HOST>:<N8N_PORT>/<N8N_PATH>/api/v<version-number>/workflows?active=true&limit=150&cursor=MTIzZTQ1NjctZTg5Yi0xMmQzLWE0NTYtNDI2NjE0MTc0MDA' \
  -H 'accept: application/json'

# สำหรับ n8n Cloud
curl -X 'GET' \
  '<your-cloud-instance>/api/v<version-number>/workflows?active=true&limit=150&cursor=MTIzZTQ1NjctZTg5Yi0xMmQzLWE0NTYtNDI2NjE0MTc0MDA' \
  -H 'accept: application/json'
```
