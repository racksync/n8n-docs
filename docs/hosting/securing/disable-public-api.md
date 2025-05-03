---
#https://www.notion.so/n8n/Frontmatter-432c2b8dff1f43d4b1c8d20075510fe4
title: ปิด public REST API
description: "ปิด n8n public REST API เพื่อป้องกันการใช้งานจากภายนอก"
contentType: howto
---

# Disable the public REST API

[n8n public REST API](/api/index.md) ช่วยให้คุณสั่งงาน n8n ได้แบบเดียวกับใน GUI ผ่านโปรแกรม

ถ้าไม่ได้ใช้ API นี้ แนะนำให้ปิดเพื่อเพิ่มความปลอดภัยให้ n8n ของคุณ

ถ้าต้องการปิด [public REST API](/api/index.md) ให้ตั้งค่า environment variable `N8N_PUBLIC_API_DISABLED` เป็น `true` ตัวอย่างเช่น

```bash
export N8N_PUBLIC_API_DISABLED=true
```

## Disable the API playground

ถ้าอยากปิด [API playground](/api/using-api-playground.md) ให้ตั้งค่า environment variable `N8N_PUBLIC_API_SWAGGERUI_DISABLED` เป็น `true` ตัวอย่างเช่น

```bash
export N8N_PUBLIC_API_SWAGGERUI_DISABLED=true
```

## Related resources

ดูข้อมูลเพิ่มเติมเกี่ยวกับ environment variables เหล่านี้ได้ที่ [Deployment environment variables](/hosting/configuration/environment-variables/deployment.md)

ดูวิธีตั้งค่า environment variables ได้ที่ [Configuration](/hosting/configuration/configuration-methods.md)
