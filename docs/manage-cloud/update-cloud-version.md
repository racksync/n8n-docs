---
#https://www.notion.so/n8n/Frontmatter-432c2b8dff1f43d4b1c8d20075510fe4
description: How to update your n8n version on Cloud.
contentType: howto
---

# Update your Cloud version

n8n แนะนำให้อัปเดต Cloud version ของคุณเป็นประจำ ดู [Release notes](/release-notes.md) เพื่อดูรายละเอียดการเปลี่ยนแปลง

/// info
เฉพาะเจ้าของ instance เท่านั้นที่สามารถอัปเกรด n8n Cloud version ได้ ถ้าคุณไม่มีสิทธิ์อัปเดต ให้ติดต่อเจ้าของ instance
///

1. [Log in to the n8n Cloud dashboard](https://app.n8n.cloud/manage){:target=_blank .external-link}
1. ที่ dashboard ของคุณ เลือก **Manage**
1. ใช้ **n8n version** dropdown เพื่อเลือก release version ที่ต้องการ:
	* Latest Stable: แนะนำสำหรับผู้ใช้ทั่วไป
	* Latest Beta: ได้ n8n เวอร์ชันใหม่สุด อาจไม่เสถียร
1. กด **Save Changes** เพื่อ restart n8n instance และอัปเดต
1. ใน modal ยืนยัน ให้เลือก **Confirm**

## Best practices for updating

--8<-- "_snippets/manage-cloud/updating-best-practices.md"

## Automatic update

n8n จะอัปเดต Cloud instance ที่ล้าสมัยให้อัตโนมัติ

ถ้าคุณไม่อัปเดต instance เกิน 120 วัน n8n จะส่งอีเมลเตือนให้คุณอัปเดต หลังจากนั้นอีก 30 วัน n8n จะอัปเดต instance ของคุณให้อัตโนมัติ
