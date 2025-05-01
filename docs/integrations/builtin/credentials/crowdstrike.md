---
#https://www.notion.so/n8n/Frontmatter-432c2b8dff1f43d4b1c8d20075510fe4
title: CrowdStrike credentials
description: Documentation for the CrowdStrike credentials. Use these credentials to authenticate CrowdStrike in n8n, a workflow automation platform.
contentType: [integration, reference]
priority: medium
---

# CrowdStrike credentials

--8<-- "_snippets/integrations/builtin/credentials/cred-only-statement.md"

## Prerequisites

สมัคร [CrowdStrike](https://www.crowdstrike.com/en-us/){:target=_blank .external-link} ให้เรียบร้อยก่อน

## Authentication methods

- OAuth2

## Related resources

ดูข้อมูลเพิ่มเติมเกี่ยวกับบริการได้ที่เอกสารของ CrowdStrike เอกสารของพวกเขาอยู่หลังการล็อกอิน ดังนั้นคุณต้องล็อกอินเข้าบัญชีของคุณบนเว็บไซต์ของพวกเขาเพื่อเข้าถึงเอกสาร API

นี่คือ credential-only node ดูรายละเอียดเพิ่มเติมได้ที่ [Custom API operations](/integrations/custom-operations.md) ดู [example workflows and related content](https://n8n.io/integrations/crowdstrike/){:target=_blank .external-link} บนเว็บไซต์ n8n

## Using OAuth2

ถ้าจะตั้งค่า credentials นี้ คุณต้องมี:

- **URL** ของ CrowdStrike instance ของคุณ
- **Client ID**: สร้างโดยการสร้าง API Client ใหม่ใน Crowdstrike ใน **Support > API Clients and Keys**
- **Client Secret**: สร้างโดยการสร้าง API Client ใหม่ใน Crowdstrike ใน **Support > API Clients and Keys**

โครงร่างกว้างๆ ของขั้นตอนที่เหมาะสมมีให้ดูแบบสาธารณะที่บล็อก CrowdStrike: [Getting Access to the CrowdStrike API](https://www.crowdstrike.com/blog/tech-center/get-access-falcon-apis/){:target=_blank .external-link} เอกสารฉบับเต็มของ CrowdStrike อยู่หลังการล็อกอิน ดังนั้นคุณต้องล็อกอินเข้าบัญชีของคุณเพื่อเข้าถึงเอกสาร API ฉบับเต็ม

