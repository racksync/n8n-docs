---
#https://www.notion.so/n8n/Frontmatter-432c2b8dff1f43d4b1c8d20075510fe4
title: Environments in n8n
description: Understand the concepts behind environments in n8n.
contentType: explanation
---

# Environments in n8n

n8n สร้างฟีเจอร์ environments ขึ้นมาบนพื้นฐานของ Git ซึ่งเป็นซอฟต์แวร์สำหรับ version control เอกสารนี้จะช่วยให้คุณเข้าใจว่า:

* จุดประสงค์ของ environments คืออะไร
* environments ใน n8n ทำงานยังไง

## Environments: What and why

ในสายงาน software development, environment คือทุกอย่างที่เป็น infrastructure และเครื่องมือรอบๆ ตัวโค้ด รวมถึงเครื่องมือที่ใช้รันซอฟต์แวร์ และการตั้งค่าต่างๆ ของเครื่องมือเหล่านั้น ถ้าอยากอ่านแนะนำเรื่อง environments ในสาย software development แบบละเอียดขึ้น ดูได้ที่ [Codecademy | Environments](https://www.codecademy.com/article/environments){:target=_blank .external-link}

การพัฒนาแบบ low-code ใน n8n ก็คล้ายๆ กัน n8n คือที่ที่คุณสร้างและรัน workflow ของคุณ แต่ละ instance ของคุณอาจจะมีการตั้งค่าที่ต่างกัน: ถ้าใช้บน Cloud, n8n จะเป็นคนกำหนด config ให้ แต่ถ้าเป็น self-hosted instance คุณสามารถตั้งค่าได้เยอะมากๆ ดูรายละเอียดที่ [configuration options](/hosting/configuration/configuration-methods.md) คุณอาจจะมีการเปลี่ยนแปลง settings ของ instance ด้วย ซึ่งทั้งหมดนี้ (n8n + config + settings) ก็คือ environment ที่ workflow ของคุณจะรันอยู่

การมี environment มากกว่าหนึ่งมีข้อดี เช่น pattern ที่เจอบ่อยคือแยก environment สำหรับ development กับ production:

* Development: เอาไว้ทำงานและแก้ไข
* Production: คือ environment ที่ใช้งานจริง

การแยกแบบนี้ช่วยให้คุณแก้ไข workflow ได้โดยไม่ไปกระทบ workflow ที่กำลังใช้งานจริง

## Environments in n8n

ใน n8n, environment จะประกอบด้วย 2 ส่วน คือ n8n instance กับ Git branch:

* n8n instance คือที่ที่คุณสร้างและรัน workflow
* Git branch จะเก็บสำเนา workflow, tags, และ variable/credential stubs

n8n จะไม่ sync credentials กับ variable values ไปที่ Git คุณต้องตั้งค่า credentials กับ variable values เองตอนตั้ง instance ใหม่ ดูรายละเอียดที่ [Push and pull | What gets committed](/source-control-environments/using/push-pull.md#what-gets-committed) และ [Manage variables](/source-control-environments/using/manage-variables.md)

วิธีการ copy งานระหว่าง environments จะขึ้นอยู่กับการตั้งค่า branch กับ instance ของคุณ:

* มีหลาย instance แต่ใช้ branch เดียว: คุณ push งานจาก instance หนึ่งไปที่ Git branch แล้วไป pull งานนั้นที่อีก instance ได้เลย
* มีหลาย instance หลาย branch: คุณต้องสร้าง pull request และ merge ใน Git provider เช่น ถ้ามี branch สำหรับ development, test, production แต่ละอันผูกกับ instance ของตัวเอง คุณต้อง merge branch development ไป test ก่อน งานจาก development instance ถึงจะไปโผล่ที่ test instance ได้ ดูรายละเอียดที่ [Copy work between environments](/source-control-environments/using/copy-work.md) มีขั้นตอนและวิธี automate บางส่วนด้วย

ถ้าอยากดูวิธี push/pull งานแบบละเอียด ดูที่ [Push and pull](/source-control-environments/using/push-pull.md)

ดูวิธีเชื่อม n8n instance กับ Git ได้ที่ [Set up source control](/source-control-environments/setup.md) หรือจะลองทำตาม [Tutorial: Create environments with source control](/source-control-environments/create-environments.md) ก็ได้
