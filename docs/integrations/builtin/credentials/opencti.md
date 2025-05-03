---
#https://www.notion.so/n8n/Frontmatter-432c2b8dff1f43d4b1c8d20075510fe4
title: ข้อมูลยืนยันตัวตน OpenCTI
description: เอกสารสำหรับข้อมูลยืนยันตัวตน OpenCTI ใช้ข้อมูลนี้เพื่อยืนยันตัวตน OpenCTI ใน n8n แพลตฟอร์ม workflow automation
contentType: [integration, reference]
---

# OpenCTI credentials

--8<-- "_snippets/integrations/builtin/credentials/cred-only-statement.md"

## Prerequisites

สร้างบัญชีนักพัฒนา [OpenCTI](https://filigran.io/solutions/open-cti/){:target=_blank .external-link}

## Authentication methods

- API key

## Related resources

อ้างอิง [OpenCTI's documentation](https://docs.opencti.io/latest/){:target=_blank .external-link} สำหรับข้อมูลเพิ่มเติมเกี่ยวกับบริการนี้

นี่คือ node สำหรับ credential เท่านั้น อ้างอิง [Custom API operations](/integrations/custom-operations.md) เพื่อเรียนรู้เพิ่มเติม ดู [example workflows and related content](https://n8n.io/integrations/opencti/){:target=_blank .external-link} บนเว็บไซต์ของ n8n

## Using API key

ในการกำหนดค่า credential นี้ คุณจะต้องมี:

- **API Key**: หากต้องการรับ API key ของคุณ ให้ไปที่ **Profile > API access** อ้างอิงเอกสาร OpenCTI [Integrations Authentication documentation](https://docs.opencti.io/latest/deployment/integrations/#authentication){:target=_blank .external-link} สำหรับข้อมูลเพิ่มเติม