---
#https://www.notion.so/n8n/Frontmatter-432c2b8dff1f43d4b1c8d20075510fe4
title: n8n Hosting Documentation and Guides
description: Access n8n hosting documentation and guides. Find comprehensive resources to help you set up and manage your self-hosted n8n instances.
contentType: overview
hide:
  - toc
---

# Self-hosting n8n

หน้านี้จะอธิบายวิธีการตั้งค่า n8n สำหรับทั้ง Enterprise และ Community edition ที่เป็น self-hosted โดย Community edition จะใช้ฟรี ส่วน Enterprise edition จะมีค่าใช้จ่าย

ดู [Community edition features](/hosting/community-edition-features.md) สำหรับรายการฟีเจอร์ที่มีให้ใช้งาน

<div class="grid-cards-vertical cards" markdown>

- __Installation and server setups__

	ติดตั้ง n8n ได้บนทุกแพลตฟอร์มผ่าน npm หรือ Docker หรือจะดูคู่มือสำหรับแพลตฟอร์มยอดนิยมก็ได้

	[:octicons-arrow-right-24: Docker installation guide](/hosting/installation/docker.md)

- __Configuration__

	เรียนรู้วิธีตั้งค่า n8n ด้วย environment variables

	[:octicons-arrow-right-24: Environment Variables](/hosting/configuration/environment-variables/index.md)

- __Users and authentication__

	เลือกและตั้งค่าการยืนยันตัวตน (authentication) สำหรับ n8n instance ของคุณ

	[:octicons-arrow-right-24: Authentication](/hosting/configuration/user-management-self-hosted.md)

- __Scaling__

	จัดการข้อมูล, โหมด, และ process ต่างๆ เพื่อให้ n8n ทำงานได้ดีแม้จะขยายระบบ

	[:octicons-arrow-right-24: Scaling](/hosting/scaling/queue-mode.md)

- __Securing n8n__

	ป้องกัน n8n instance ของคุณด้วยการตั้งค่า SSL, SSO, 2FA หรือบล็อก/ปิดการเก็บข้อมูลบางอย่าง

	[:octicons-arrow-right-24: Securing n8n guide](/hosting/securing/overview.md)

- __Starter kits__

	ถ้าเพิ่งเริ่มใช้ n8n หรือสนใจ AI ลอง Self-hosted AI Starter Kit ที่ n8n คัดสรรมาให้ รวมแพลตฟอร์ม n8n แบบ self-hosted กับ AI products และ components ที่เข้ากันได้ ให้คุณเริ่มสร้าง workflow AI ได้ทันที

	[:octicons-arrow-right-24: Starter kits](/hosting/starter-kits/ai-starter-kit.md)

</div>

--8<-- "_snippets/self-hosting/warning.md"
