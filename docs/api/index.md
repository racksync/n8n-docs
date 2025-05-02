---
#https://www.notion.so/n8n/Frontmatter-432c2b8dff1f43d4b1c8d20075510fe4
title: n8n public REST API Documentation and Guides
description: Access n8n public REST API documentation and guides. Find comprehensive resources to programmatically perform tasks with the public API instead of the GUI.
contentType: overview
search:
    boost: 5
---

# n8n public REST API

/// info | Feature availability
n8n API ไม่มีให้บริการในช่วงทดลองใช้ฟรี โปรด upgrade เพื่อเข้าถึงฟีเจอร์นี้
///

การใช้ [API](/glossary.md#api) สาธารณะของ n8n คุณสามารถทำงานต่างๆ ได้เหมือนใน GUI แต่ใช้โปรแกรมแทน ส่วนนี้จะอธิบาย REST API ของ n8n รวมถึง:

* วิธี [authenticate](/api/authentication.md)
* [Paginating](/api/pagination.md) ผลลัพธ์
* การใช้ [built-in API playground](/api/using-api-playground.md) (เฉพาะ n8n แบบ self-hosted)
* [Endpoint reference](/api/api-reference.md)

n8n มี [n8n API node](/integrations/builtin/core-nodes/n8n-nodes-base.n8n.md) สำหรับเข้าถึง API ใน workflows ของคุณ

## Learn about REST APIs

เอกสาร API นี้สมมติว่าคุณคุ้นเคยกับ REST APIs ถ้ายังไม่คุ้นเคย ลองดูแหล่งข้อมูลเหล่านี้:

* [KnowledgeOwl's guide to working with APIs](https://support.knowledgeowl.com/help/working-with-apis){:target=_blank .external-link}: แนะนำเบื้องต้น พร้อมตัวอย่างการเรียก REST APIs
* [IBM Cloud Learn Hub - What is an Application Programming Interface (API)](https://www.ibm.com/cloud/learn/api){:target=_blank .external-link}: ข้อมูลเบื้องต้นเชิงเทคนิคเกี่ยวกับ APIs
* [IBM Cloud Learn Hub - What is a REST API?](https://www.ibm.com/cloud/learn/rest-apis){:target=_blank .external-link}: ข้อมูลเชิงลึกเกี่ยวกับ REST APIs
* [MDN web docs - An overview of HTTP](https://developer.mozilla.org/en-US/docs/Web/HTTP/Overview){:target=_blank .external-link}: REST APIs ทำงานผ่าน HTTP และใช้ HTTP verbs หรือ methods เพื่อระบุการกระทำ

/// tip | Use the API playground (self-hosted n8n only)
การลองใช้ API ใน [playground](/api/using-api-playground.md) จะช่วยให้เข้าใจการทำงานของ APIs ได้ดีขึ้น ถ้ากังวลเรื่องข้อมูลจริง ลองตั้งค่า workflow หรือ n8n instance สำหรับทดสอบก่อน
///
