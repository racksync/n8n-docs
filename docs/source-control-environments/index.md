---
#https://www.notion.so/n8n/Frontmatter-432c2b8dff1f43d4b1c8d20075510fe4
title: Source control and environments
description: Overview of source control and environments in n8n
contentType: overview
hide:
  - toc
---

# Source control and environments

--8<-- "_snippets/source-control-environments/feature-availability.md"

n8n ใช้ Git-based source control เพื่อรองรับ environments การเชื่อม n8n instance ของคุณกับ Git repository จะช่วยให้คุณสร้าง n8n environments หลายอัน โดยแต่ละอันผูกกับ Git branch

ใน section นี้:

* [Understand](/source-control-environments/understand/index.md):
	* [Environments in n8n](/source-control-environments/understand/environments.md): จุดประสงค์ของ environments และวิธีการทำงานใน n8n
	* [Git and n8n](/source-control-environments/understand/git.md): วิธีที่ n8n ใช้ Git
	* [Branch patterns](/source-control-environments/understand/patterns.md): ความสัมพันธ์ที่เป็นไปได้ระหว่าง n8n instance กับ Git branch
* [Set up source control for environments](/source-control-environments/setup.md): วิธีเชื่อม n8n instance ของคุณกับ Git
* [Using](/source-control-environments/using/index.md):
	* [Push and pull](/source-control-environments/using/push-pull.md): ส่งงานไป Git และดึงงานจาก Git เข้า instance ของคุณ
	* [Copy work between environments](/source-control-environments/using/copy-work.md): วิธี copy งานระหว่าง n8n instance ต่างๆ
	* [Manage variables](/source-control-environments/using/manage-variables.md): จัดการค่า variable ด้วย n8n API และ source control
* [Tutorial: Create environments with source control](/source-control-environments/create-environments.md): ตัวอย่างตั้งค่า environments ด้วย config ที่ n8n แนะนำ

หัวข้อที่เกี่ยวข้อง:

* [Variables](/code/variables.md): ค่าที่นำกลับมาใช้ซ้ำได้
* [External secrets](/external-secrets.md): จัดการ [credentials](/glossary.md#credential-n8n) ด้วย external secrets vault
