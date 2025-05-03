---
#https://www.notion.so/n8n/Frontmatter-432c2b8dff1f43d4b1c8d20075510fe4
title: รูปแบบ Branch
description: ทำความเข้าใจความสัมพันธ์รูปแบบต่างๆ ระหว่าง n8n instance กับ Git branch ที่เป็นไปได้ด้วย source control
contentType: explanation
---

# Branch patterns

ความสัมพันธ์ระหว่าง n8n instance กับ Git branch สามารถปรับเปลี่ยนได้ตามที่ต้องการ คุณสามารถตั้งค่าหลายแบบได้ตามความเหมาะสมของงาน

--8<-- "_snippets/source-control-environments/one-direction.md"

## Multiple instances, multiple branches

รูปแบบนี้คือการมี n8n instance หลายอัน โดยแต่ละอันเชื่อมกับ branch ของตัวเอง

คุณสามารถใช้ pattern นี้กับ environments ได้ เช่น สร้าง n8n instance สองอัน คือ development กับ production แล้วเชื่อมแต่ละอันกับ branch ของตัวเอง จากนั้น push งานจาก development instance ไปที่ branch ของมัน แล้วสร้าง pull request เพื่อย้ายงานไป production branch แล้วค่อย pull เข้า production instance

--8<-- "_snippets/source-control-environments/multi-instance-multi-branch-pros-cons.md"

![Diagram](/_images/source-control-environments/vc-multi-multi.png)

## Multiple instances, one branch

ใช้ pattern นี้ถ้าคุณอยากให้ workflow, tag, variable เหมือนกันทุกที่ แต่ใช้งานใน n8n instance หลายอัน

เหมาะกับการทำ environments เช่น สร้าง n8n instance สองอัน development กับ production แล้วเชื่อมทั้งสองอันกับ branch เดียวกัน จากนั้น push งานจาก development แล้ว pull เข้า production

pattern นี้ยังเหมาะกับการทดสอบ n8n เวอร์ชันใหม่ เช่น สร้าง instance ใหม่ที่เป็นเวอร์ชันใหม่ เชื่อมกับ Git branch เดิม แล้วทดสอบได้เลย ในขณะที่ production instance ยังใช้เวอร์ชันเก่าอยู่จนกว่าจะมั่นใจ

--8<-- "_snippets/source-control-environments/multi-instance-one-branch-pros-cons.md"

![Diagram](/_images/source-control-environments/vc-multi-one.png)

## One instance, multiple branches

เจ้าของ instance สามารถเปลี่ยน branch ที่เชื่อมกับ instance ได้ setup แบบนี้มักจะเป็น [Multiple instances, multiple branches](#multiple-instances-multiple-branches) แต่ใช้ instance เดียวสลับ branch ไปมา

เหมาะกับการ review งาน เช่น แต่ละ user ทำงานบน instance ของตัวเองแล้ว push ไป branch ของตัวเอง reviewer ใช้ review instance แล้วสลับ branch เพื่อดูงานของแต่ละคน

/// note | No cleanup
n8n จะไม่ลบข้อมูลเดิมใน instance ตอนเปลี่ยน branch การสลับ branch แบบนี้จะทำให้ workflow จากแต่ละ branch ไปอยู่รวมกันใน instance ของคุณ
///
![Diagram](/_images/source-control-environments/vc-one-multi.png)

## One instance, one branch

นี่คือ pattern ที่ง่ายที่สุด

![Diagram](/_images/source-control-environments/vc-one-one.png)
