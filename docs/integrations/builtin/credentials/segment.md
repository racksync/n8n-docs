---
#https://www.notion.so/n8n/Frontmatter-432c2b8dff1f43d4b1c8d20075510fe4
title: Segment credentials
description: Documentation for Segment credentials. Use these credentials to authenticate Segment in n8n, a workflow automation platform.
contentType: [integration, reference]
---

# Segment credentials

คุณสามารถใช้ credentials เหล่านี้เพื่อยืนยันตัวตนกับ node ต่อไปนี้:

- [Segment](/integrations/builtin/app-nodes/n8n-nodes-base.segment.md)

## Prerequisites

สร้าง [Segment](https://segment.com/){:target=_blank .external-link} account

## Supported authentication methods

- API key

## Related resources

ดูรายละเอียดเพิ่มเติมเกี่ยวกับบริการนี้ได้ที่ [Segment's Sources documentation](https://segment.com/docs/connections/sources/){:target=_blank .external-link}

## Using API key

ในการตั้งค่า credentials นี้ คุณจะต้องมี:

- **Write Key**: ไปที่ **Sources > Add Source** แล้วเพิ่ม **Node.js** source จากนั้น copy write key มาใส่ใน n8n credential ของคุณ

ดูวิธีหา Write Key ได้ที่ [Locate your Write Key](https://segment.com/docs/connections/find-writekey/){:target=_blank .external-link}

