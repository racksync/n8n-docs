---
#https://www.notion.so/n8n/Frontmatter-432c2b8dff1f43d4b1c8d20075510fe4
description: การจัดเก็บ binary data ภายนอกสำหรับ n8n instance ของคุณ
contentType: howto
tags:
  - external storage
  - storage
hide:
  - tags
search:
  boost: 1.5
---

# External storage

/// info | Feature availability

* ใช้ได้เฉพาะ Self-hosted Enterprise plans
* ถ้าอยากใช้บน Cloud Enterprise [ติดต่อ n8n](https://n8n-community.typeform.com/to/y9X2YuGa){:target=_blank .external-link}
///

n8n สามารถเก็บ binary data ที่ workflow สร้างไว้ภายนอกได้ ฟีเจอร์นี้เหมาะกับคนที่ไม่อยากเก็บไฟล์ใหญ่ๆ ไว้ใน filesystem

ในอนาคต n8n จะรองรับ external storage สำหรับข้อมูลประเภทอื่นด้วย

## Storing n8n's binary data in S3

n8n รองรับ [AWS S3](https://docs.aws.amazon.com/AmazonS3/latest/userguide/Welcome.html){:target=_blank .external-link} เป็น external store สำหรับ binary data ที่ workflow สร้าง คุณสามารถใช้ S3-compatible อื่นๆ เช่น Cloudflare R2, Backblaze B2 ได้ แต่ n8n ยังไม่รองรับอย่างเป็นทางการ

/// info | Enterprise-tier feature
ต้องมี [Enterprise license key](/license-key.md) เพื่อใช้ external storage ถ้า license หมดอายุและยังใช้ S3 mode instance จะอ่านจาก S3 ได้แต่เขียนไม่ได้
///

### Setup

สร้างและตั้งค่า bucket ตาม [AWS documentation](https://docs.aws.amazon.com/AmazonS3/latest/userguide/creating-bucket.html){:target=_blank .external-link} ใช้ policy นี้ (เปลี่ยน `<bucket-name>` เป็นชื่อ bucket ของคุณ):

```json
{
 "Version": "2012-10-17",
 "Statement": [
  {
   "Sid": "VisualEditor0",
   "Effect": "Allow",
   "Action": ["s3:*"],
   "Resource": ["arn:aws:s3:::<bucket-name>", "arn:aws:s3:::<bucket-name>/*"]
  }
 ]
}
```

ตั้ง bucket-level lifecycle configuration ให้ S3 ลบ binary data เก่าอัตโนมัติ n8n จะไม่ลบ binary data เองถ้าใช้ S3 ต้องตั้ง lifecycle นี้เอง (ถ้าไม่อยากเก็บถาวร)

เมื่อสร้าง bucket เสร็จ คุณจะได้ host, bucket name, region, access key ID และ secret access key ตั้งค่าใน environment ของ n8n:

```sh
export N8N_EXTERNAL_STORAGE_S3_HOST=... # ตัวอย่าง: s3.us-east-1.amazonaws.com
export N8N_EXTERNAL_STORAGE_S3_BUCKET_NAME=...
export N8N_EXTERNAL_STORAGE_S3_BUCKET_REGION=...
export N8N_EXTERNAL_STORAGE_S3_ACCESS_KEY=...
export N8N_EXTERNAL_STORAGE_S3_ACCESS_SECRET=...
```

/// note | No region
ถ้า provider ไม่ต้องใช้ region ให้ตั้ง `N8N_EXTERNAL_STORAGE_S3_BUCKET_REGION` เป็น `'auto'`
///
บอก n8n ให้เก็บ binary data ใน S3:

```sh
export N8N_AVAILABLE_BINARY_DATA_MODES=filesystem,s3
export N8N_DEFAULT_BINARY_DATA_MODE=s3
```

/// note | Auth autodetection
ถ้าอยากให้ n8n ตรวจ credentials S3 อัตโนมัติ ให้ตั้ง `N8N_EXTERNAL_STORAGE_S3_AUTH_AUTO_DETECT` เป็น `true` จะใช้ [credential provider chain](https://docs.aws.amazon.com/sdk-for-javascript/v3/developer-guide/setting-credentials-node.html#credchain) ของ AWS
///

restart server เพื่อโหลด config ใหม่

### Usage

หลังเปิด S3 แล้ว n8n จะอ่าน/เขียน binary data ใหม่ไปที่ S3 bucket โดยใช้ format นี้:

```
workflows/{workflowId}/executions/{executionId}/binary_data/{binaryFileId}
```

n8n จะยังอ่าน binary data เก่าจาก filesystem ถ้า `filesystem` ยังอยู่ใน `N8N_AVAILABLE_BINARY_DATA_MODES`

ถ้าเปลี่ยนจาก S3 กลับไป filesystem instance จะยังอ่านข้อมูลใน S3 ได้ถ้า `s3` ยังอยู่ใน `N8N_AVAILABLE_BINARY_DATA_MODES` และ credential S3 ยังใช้ได้

--8<-- "_snippets/self-hosting/scaling/binary-data-pruning.md"
