---
#https://www.notion.so/n8n/Frontmatter-432c2b8dff1f43d4b1c8d20075510fe4
title: ข้อมูลยืนยันตัวตน Jenkins
description: เอกสารสำหรับ Jenkins credentials ใช้เพื่อเชื่อมต่อ Jenkins ใน n8n
contentType: [integration, reference]
---

# Jenkins credentials

คุณสามารถใช้ credentials เหล่านี้เพื่อยืนยันตัวตนกับ node ต่อไปนี้ได้:

- [Jenkins](/integrations/builtin/app-nodes/n8n-nodes-base.jenkins.md)


## Prerequisites

สร้างบัญชีบน instance ของ [Jenkins](https://www.jenkins.io/){:target=_blank .external-link}

## Supported authentication methods

- API token

## Related resources

Jenkins ไม่ได้ให้เอกสาร API สาธารณะ เอกสาร API สำหรับแต่ละหน้ามีอยู่ใน user interface ที่มุมล่างขวา โปรดดูรายละเอียดเพิ่มเติมในหน้าเหล่านั้น ดูข้อมูลเกี่ยวกับ API และ API wrappers ได้ที่ [Jenkins Remote Access API](https://www.jenkins.io/doc/book/using/remote-access-api/){:target=_blank .external-link}

## Using API token

ในการตั้งค่า credential นี้ คุณจะต้องมี:

- **Jenkins Username**: สำหรับผู้ใช้ที่เป็นเจ้าของ token
- **Personal API Token**: สร้างสิ่งนี้จาก **profile details > Configure > Add new token** ของผู้ใช้ ดูรายละเอียดเพิ่มเติมได้ที่ [these Stack Overflow instructions](https://stackoverflow.com/questions/45466090/how-to-get-the-api-token-for-jenkins){:target=_blank .external-link}
- **Jenkins Instance URL**

Jenkins ได้สร้างการตั้งค่า API token ใหม่ในปี 2018 หากคุณกำลังทำงานกับ Jenkins instance ที่เก่ากว่า ตรวจสอบให้แน่ใจว่าคุณกำลังใช้ API token ที่ไม่ใช่แบบ legacy ดูข้อมูลเพิ่มเติมได้ที่ [Security Hardening: New API token system in Jenkins 2.129+](https://www.jenkins.io/blog/2018/07/02/new-api-token-system/){:target=_blank .external-link}

