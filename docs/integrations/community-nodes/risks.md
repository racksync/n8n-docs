---
#https://www.notion.so/n8n/Frontmatter-432c2b8dff1f43d4b1c8d20075510fe4
contentType: explanation
---

# Risks when using community nodes

การใช้ community nodes หมายถึงคุณกำลังติดตั้งโค้ดที่ยังไม่ได้รับการตรวจสอบจากแหล่งสาธารณะลงใน instance ของ n8n ซึ่งมีความเสี่ยงบางอย่าง

ความเสี่ยงที่อาจเกิดขึ้น เช่น:

* System security: community nodes สามารถเข้าถึงเครื่องที่รัน n8n ได้เต็มที่ และอาจทำอะไรก็ได้ รวมถึงการกระทำที่เป็นอันตราย
* Data security: community node ที่คุณใช้สามารถเข้าถึงข้อมูลใน workflow ของคุณได้
* Breaking changes: นักพัฒนา node อาจมี breaking changes ในเวอร์ชันใหม่ๆ ได้ (breaking change คือการอัปเดตที่ทำให้ฟังก์ชันเดิมใช้ไม่ได้) ขึ้นอยู่กับวิธีการจัดการเวอร์ชันของนักพัฒนา node ถ้าอัปเกรดไปเวอร์ชันที่มี breaking change อาจทำให้ workflow ที่ใช้ node นั้นเสียได้ ควรตรวจสอบก่อนอัปเกรด

## Report bad community nodes

<!-- vale off -->

คุณสามารถแจ้ง community node ที่มีปัญหาได้ที่ [security@n8n.io](mailto: security@n8n.io)

<!-- vale on -->

## Disable community nodes

สามารถปิดการใช้งาน community nodes ได้โดยตั้งค่า `N8N_COMMUNITY_PACKAGES_ENABLED` เป็น `false`
