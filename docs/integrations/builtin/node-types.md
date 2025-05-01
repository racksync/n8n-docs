---
#https://www.notion.so/n8n/Frontmatter-432c2b8dff1f43d4b1c8d20075510fe4
contentType: overview
---

# Built-in integrations

ส่วนนี้คือ [node](/glossary.md#node-n8n) library: เป็นเอกสารอ้างอิงสำหรับ node ที่มีใน n8n และ credential ที่ใช้กับ node เหล่านั้น

--8<-- "_snippets/integrations/builtin/node-operations.md"

## Core nodes

Core node สามารถเป็น action หรือ [trigger](/glossary.md#trigger-node-n8n) ก็ได้ โดยส่วนใหญ่ node จะเชื่อมต่อกับ service ภายนอกแบบเฉพาะเจาะจง แต่ core node จะให้ฟีเจอร์ทั่วไป เช่น logic, scheduling หรือการเรียก API แบบ generic

## Cluster nodes

--8<-- "_snippets/integrations/builtin/cluster-nodes/cluster-nodes-summary.md"

## Credentials

service ภายนอกต้องการวิธีระบุตัวตนและยืนยันตัวผู้ใช้ ข้อมูล credential อาจเป็น API key, อีเมล/รหัสผ่าน หรือ private key แบบหลายบรรทัดก็ได้ คุณสามารถบันทึก credential เหล่านี้ใน n8n ได้ที่ [credentials](/glossary.md#credential-n8n)

node ใน n8n สามารถร้องขอข้อมูล credential ได้ และเพื่อความปลอดภัย node แต่ละประเภทจะเข้าถึง credential ได้เฉพาะที่มีสิทธิ์เท่านั้น

เพื่อความปลอดภัย ข้อมูล credential จะถูกบันทึกในฐานข้อมูลแบบเข้ารหัส n8n จะสร้าง personal encryption key แบบสุ่มให้อัตโนมัติเมื่อรัน n8n ครั้งแรก และบันทึกไว้ที่ `~/.n8n/config`

ถ้าอยากรู้วิธีสร้าง จัดการ และแชร์ credential ดูได้ที่ [Manage credentials](/credentials/index.md)

## Community nodes

n8n รองรับ custom node ที่สร้างโดย community ดูวิธีติดตั้งและใช้งานได้ที่ [Community nodes](/integrations/community-nodes/installation/index.md)

ถ้าอยากสร้าง custom node เองและ publish ไปที่ [npm](https://www.npmjs.com/){:target=_blank .external-link} ดูวิธีได้ที่ [Creating nodes](/integrations/creating-nodes/overview.md)
