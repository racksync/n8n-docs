---
#https://www.notion.so/n8n/Frontmatter-432c2b8dff1f43d4b1c8d20075510fe4
title: Git and n8n
description: Git concepts and limitations in n8n.
contentType: explanation
---

# Git and n8n

n8n ใช้ Git เพื่อจัดการ source control ถ้าคุณจะใช้ฟีเจอร์นี้ แนะนำให้รู้จักพื้นฐานของ Git ไว้บ้าง n8n ไม่ได้รองรับฟีเจอร์ Git ทั้งหมด: อย่าคิดว่า source control ของ n8n จะเหมือน version control เต็มรูปแบบ

/// note | New to Git and source control?
ถ้าคุณเพิ่งเริ่มใช้ Git ไม่ต้องกังวล คุณไม่จำเป็นต้องรู้ Git ลึกๆ เพื่อใช้ n8n เอกสารนี้จะอธิบาย concept ที่จำเป็น คุณจะต้องรู้ Git บ้างตอน setup source control เพราะต้องไปตั้งค่าที่ Git provider ของคุณ
///
/// note | Familiar with Git and source control?
ถ้าคุณคุ้นเคยกับ Git อยู่แล้ว อย่าคาดหวังว่า behavior จะเหมือนกันเป๊ะ โดยเฉพาะ source control ใน n8n จะไม่รองรับ pull request-style review และ merge process เว้นแต่คุณจะทำเองนอก n8n ใน Git provider
///

หน้านี้จะแนะนำ concept และคำศัพท์ Git ที่ใช้ใน n8n ไม่ได้อธิบายทุกอย่างที่ต้องรู้สำหรับ setup และจัดการ repository คนที่ทำ [Setup](/source-control-environments/setup.md) ควรคุ้นเคยกับ Git และ Git hosting provider ของตัวเอง

/// note | This is a brief introduction
Git เป็นเรื่องที่ซับซ้อน ส่วนนี้จะอธิบายแค่คำสำคัญที่ต้องใช้กับ environments ใน n8n ถ้าอยากเรียนรู้ Git แบบละเอียด ดูที่ [GitHub | Git and GitHub learning resources](https://docs.github.com/en/get-started/quickstart/git-and-github-learning-resources){:target=_blank .external-link}
///
## Git overview

[Git](https://git-scm.com/){:target=_blank .external-link} คือเครื่องมือสำหรับจัดการ, ติดตาม, และทำงานร่วมกันบนไฟล์หลายเวอร์ชัน เป็นพื้นฐานของ platform ที่ใช้กันเยอะอย่าง [GitHub](https://github.com/){:target=_blank .external-link} และ [GitLab](https://about.gitlab.com/){:target=_blank .external-link}

## Branches: Multiple copies of a project

Git ใช้ branch เพื่อเก็บไฟล์หลายชุดไว้ขนานกัน แต่ละ branch จะมีเวอร์ชันของตัวเอง ปกติจะมี main branch แล้วใครที่อยาก contribute ก็จะทำงานบน branch ของตัวเอง (เหมือน copy) พอเสร็จแล้วก็ merge กลับเข้า main branch

![Diagram](/_images/source-control-environments/simple-git-branch.png)

## Local and remote: Moving work between your machine and a Git provider

ปกติการใช้ Git จะติดตั้ง Git บนเครื่องตัวเอง แล้วใช้ Git provider เช่น GitHub เพื่อเก็บไฟล์บน cloud สรุปคือคุณจะมี repository (project) บน GitHub แล้ว sync งานกับเครื่องตัวเอง

n8n ก็ใช้ pattern นี้กับ source control: คุณจะทำงานกับ workflow บน n8n instance แล้วส่งไปเก็บที่ Git provider

## Push, pull, and commit

n8n ใช้ process หลักของ Git 3 อย่าง:

* **Push**: ส่งงานจาก instance ของคุณไปที่ Git จะเป็นการบันทึก workflow, tag, credential stub, variable stub ไปที่ Git คุณเลือกได้ว่าจะ push workflow ไหน
* **Pull**: ดึง workflow, tag, variable จาก Git มาโหลดเข้า n8n คุณต้องเติมค่า credentials หรือ variable stub เองหลังจาก pull
    /// warning | Pulling overwrites your work
    ถ้าคุณแก้ workflow ใน n8n แล้ว ยังไม่ได้ push ไป Git ถ้า pull จะโดน overwrite ทันที ต้อง push ก่อนค่อย pull
    ///
* **Commit**: ใน n8n commit คือการ push งานไป Git หนึ่งครั้ง ใน n8n commit กับ push จะเกิดพร้อมกัน

ดูรายละเอียดการ push/pull เพิ่มเติมที่ [Push and pull](/source-control-environments/using/push-pull.md)
