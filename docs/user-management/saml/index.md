---
#https://www.notion.so/n8n/Frontmatter-432c2b8dff1f43d4b1c8d20075510fe4
contentType: overview
---

# Security Assertion Markup Language (SAML)

<!-- Assuming the snippet explains what SAML is and its benefits for n8n -->
SAML เป็นมาตรฐานแบบเปิดที่ช่วยให้ผู้ให้บริการข้อมูลประจำตัว (IdPs) สามารถส่งข้อมูลการยืนยันตัวตน (authentication) และการอนุญาต (authorization) ไปยังผู้ให้บริการ (SPs) ได้อย่างปลอดภัย ในบริบทของ n8n การใช้ SAML ช่วยให้ผู้ใช้สามารถ login เข้าสู่ n8n โดยใช้ข้อมูลประจำตัวที่มีอยู่แล้วจากองค์กรของคุณ (เช่น Okta, Azure AD) ผ่านกระบวนการ Single Sign-On (SSO) ซึ่งช่วยเพิ่มความปลอดภัยและปรับปรุงประสบการณ์ผู้ใช้โดยลดความจำเป็นในการจำรหัสผ่านหลายชุด ส่วนนี้จะแนะนำวิธีการตั้งค่า จัดการ และแก้ไขปัญหาการใช้งาน SAML กับ n8n ของคุณ
<!-- End of assumed snippet translation -->
--8<-- "_snippets/user-management/saml-overview.md"
