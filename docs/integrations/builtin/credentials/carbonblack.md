---
#https://www.notion.so/n8n/Frontmatter-432c2b8dff1f43d4b1c8d20075510fe4
title: ข้อมูลรับรอง Carbon Black
description: เอกสารข้อมูลรับรอง Carbon Black ใช้ข้อมูลนี้เพื่อยืนยันตัวตน Carbon Black ใน n8n
contentType: [integration, reference]
priority: medium
---

# Carbon Black credentials

--8<-- "_snippets/integrations/builtin/credentials/cred-only-statement.md"

## Prerequisites

- สมัคร [Carbon Black subscription](https://www.vmware.com/products/carbon-black-cloud.html){:target=_blank .external-link} ให้เรียบร้อยก่อน
- สมัคร [Carbon Black developer account](https://developer.carbonblack.com/){:target=_blank .external-link} ให้เรียบร้อยก่อน

## Authentication methods

- API key

## Related resources

ดูข้อมูลเพิ่มเติมเกี่ยวกับบริการได้ที่ [Carbon Black's documentation](https://developer.carbonblack.com/reference/carbon-black-cloud/cb-defense/latest/rest-api/){:target=_blank .external-link}

นี่คือ credential-only node ดูรายละเอียดเพิ่มเติมได้ที่ [Custom API operations](/integrations/custom-operations.md) ดู [example workflows and related content](https://n8n.io/integrations/carbon-black/){:target=_blank .external-link} บนเว็บไซต์ n8n

## Using API key

ถ้าจะตั้งค่า credentials นี้ คุณต้องมี:

- **URL**: URL นี้กำหนดโดย environment/product URL ที่คุณใช้ คุณสามารถค้นหาได้โดยดูที่ web address ของ Carbon Black Cloud console ของคุณ ดูข้อมูลเพิ่มเติมได้ที่ [Carbon Black's URL Parts documentation](https://developer.carbonblack.com/reference/carbon-black-cloud/authentication#the-url-parts){:target=_blank .external-link}
- **Access Token**: ดู [Carbon Black Create an API key documentation](https://developer.carbonblack.com/reference/carbon-black-cloud/authentication#carbon-black-cloud-manages-identities-and-roles){:target=_blank .external-link} เพื่อสร้าง API key เพิ่ม **API Secret Key** เป็น **Access Token** ใน n8n
