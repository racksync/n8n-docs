---
#https://www.notion.so/n8n/Frontmatter-432c2b8dff1f43d4b1c8d20075510fe4
description: วิธีใช้ API playground เพื่อทดลองใช้ n8n public REST API
contentType: howto
---

# Using the API playground

/// info | Feature availability
API playground ไม่มีให้บริการบน Cloud แต่มีให้ใช้งานสำหรับ self-hosted ทุก pricing tiers
///

n8n API มาพร้อมกับ Swagger UI playground ในตัวสำหรับเวอร์ชัน self-hosted ซึ่งเป็นเอกสารแบบโต้ตอบที่คุณสามารถลองส่ง request ได้ path สำหรับเข้าถึง playground จะขึ้นอยู่กับการ hosting ของคุณ

n8n สร้าง path จากค่าที่ตั้งไว้ใน environment variables ของคุณ:

```shell
N8N_HOST:N8N_PORT/N8N_PATH/api/v<api-version-number>/docs
```

หมายเลขเวอร์ชัน API คือ `1` อาจมีหลายเวอร์ชันในอนาคต

/// warning | Real data
หากคุณเลือก **Authorize** และป้อน API key ของคุณใน API playground คุณจะสามารถเข้าถึงข้อมูลจริงของคุณได้ สิ่งนี้มีประโยชน์สำหรับการลองส่ง request โปรดระวังว่าคุณสามารถเปลี่ยนแปลงหรือลบข้อมูลจริงได้
///
API มีเอกสารเกี่ยวกับรูปแบบ credential ในตัว สามารถเข้าถึงได้โดยใช้ `credentials` endpoint:

```shell
N8N_HOST:N8N_PORT/N8N_PATH/api/v<api-version-number>/credentials/schema/{credentialTypeName}
```

/// note | How to find `credentialTypeName`
หากต้องการค้นหา type ให้ดาวน์โหลด workflow ของคุณเป็น JSON แล้วตรวจสอบ ตัวอย่างเช่น สำหรับ Google Drive node `{credentialTypeName}` คือ `googleDriveOAuth2Api`:
```json
{
    ...,
    "credentials": {
        "googleDriveOAuth2Api": {
        "id": "9",
        "name": "Google Drive"
        }
    }
}
}
```
///
