---
#https://www.notion.so/n8n/Frontmatter-432c2b8dff1f43d4b1c8d20075510fe4
title: อภิธานศัพท์ n8n
description: อภิธานศัพท์ที่ใช้บ่อยเมื่อทำงานกับ n8n และซอฟต์แวร์ที่เกี่ยวข้อง
contentType: reference
---

#### AI agent

AI agents คือระบบปัญญาประดิษฐ์ที่สามารถตอบสนองต่อคำขอ ตัดสินใจ และทำงานในโลกแห่งความเป็นจริงให้กับผู้ใช้ได้ พวกเขาใช้ large language models (LLMs) เพื่อตีความข้อมูลที่ผู้ใช้ป้อนเข้ามาและตัดสินใจว่าจะประมวลผลคำขออย่างไรให้ดีที่สุดโดยใช้ข้อมูลและทรัพยากรที่มีอยู่

#### AI chain

AI chains ช่วยให้คุณโต้ตอบกับ large language models (LLMs) และทรัพยากรอื่นๆ ในลำดับการเรียก components ได้ AI chains ใน n8n ไม่ใช้ persistent memory ดังนั้นคุณจึงไม่สามารถใช้อ้างอิง context ก่อนหน้าได้ (ใช้ AI agents สำหรับสิ่งนี้)

#### AI embedding

Embeddings คือการแสดงข้อมูลเชิงตัวเลขโดยใช้ vectors ใช้โดย AI เพื่อตีความข้อมูลและความสัมพันธ์ที่ซับซ้อนโดยการจับคู่ค่าต่างๆ ในหลายมิติ Vector databases หรือ vector stores คือฐานข้อมูลที่ออกแบบมาเพื่อจัดเก็บและเข้าถึง embeddings

#### AI memory

ในบริบทของ AI, memory ช่วยให้เครื่องมือ AI สามารถคง context ของข้อความไว้ได้ตลอดการโต้ตอบ สิ่งนี้ช่วยให้คุณสามารถสนทนาต่อเนื่องกับ AI agents ได้ ตัวอย่างเช่น โดยไม่ต้องส่ง context ต่อเนื่องไปกับทุกข้อความ ใน n8n, AI agent nodes สามารถใช้ memory ได้ แต่ AI chains ไม่สามารถใช้ได้

#### AI tool

ในบริบทของ AI, tool คือทรัพยากรเสริมที่ AI สามารถอ้างอิงถึงสำหรับข้อมูลหรือฟังก์ชันเฉพาะเมื่อตอบสนองต่อคำขอ AI model สามารถใช้ tool เพื่อโต้ตอบกับระบบภายนอกหรือทำงานเฉพาะที่เน้นได้

#### AI vector store

Vector stores หรือ vector databases คือฐานข้อมูลที่ออกแบบมาเพื่อจัดเก็บการแสดงข้อมูลเชิงตัวเลขที่เรียกว่า embeddings

#### API

APIs หรือ application programming interfaces ช่วยให้สามารถเข้าถึงข้อมูลและฟังก์ชันของบริการผ่านโปรแกรมได้ APIs ทำให้ซอฟต์แวร์โต้ตอบกับระบบภายนอกได้ง่ายขึ้น มักจะถูกนำเสนอเป็นทางเลือกแทนอินเทอร์เฟซแบบดั้งเดิมที่เน้นผู้ใช้ซึ่งเข้าถึงผ่านเว็บเบราว์เซอร์หรือ UI

#### canvas (n8n)

Canvas คืออินเทอร์เฟซหลักสำหรับการสร้าง workflows ใน editor UI ของ n8n คุณใช้ canvas เพื่อเพิ่มและเชื่อมต่อ nodes เพื่อประกอบ workflows

#### cluster node (n8n)

ใน n8n, cluster nodes คือกลุ่มของ nodes ที่ทำงานร่วมกันเพื่อมอบฟังก์ชันการทำงานใน workflow ประกอบด้วย root node และ sub nodes หนึ่งรายการขึ้นไปที่ขยายฟังก์ชันการทำงานของ node

#### credential (n8n)

ใน n8n, credentials จัดเก็บข้อมูล authentication เพื่อเชื่อมต่อกับแอปและบริการเฉพาะ หลังจากสร้าง credentials ด้วยข้อมูล authentication ของคุณ (username และ password, API key, OAuth secrets ฯลฯ) คุณสามารถใช้ app node ที่เกี่ยวข้องเพื่อโต้ตอบกับบริการได้

#### data pinning (n8n)

Data pinning ช่วยให้คุณสามารถหยุดข้อมูล output ของ node ชั่วคราวระหว่างการพัฒนา workflow ได้ สิ่งนี้ช่วยให้คุณพัฒนา workflows ด้วยข้อมูลที่คาดการณ์ได้โดยไม่ต้องส่งคำขอซ้ำๆ ไปยังบริการภายนอก Production workflows จะละเว้นข้อมูลที่ pin ไว้และขอข้อมูลใหม่ทุกครั้งที่ execution

#### editor (n8n)

n8n editor UI ช่วยให้คุณสร้างและจัดการ workflows ได้ พื้นที่หลักคือ canvas ซึ่งคุณสามารถประกอบ workflows โดยการเพิ่ม กำหนดค่า และเชื่อมต่อ nodes ได้ แผงด้านข้างและด้านบนช่วยให้คุณเข้าถึงส่วนอื่นๆ ของ UI เช่น credentials, templates, variables, executions และอื่นๆ

#### entitlement (n8n)

ใน n8n, entitlements ให้สิทธิ์ n8n instances ในการเข้าถึงฟีเจอร์ที่จำกัดตามแผนสำหรับช่วงเวลาที่กำหนด

Floating entitlements คือกลุ่มของ entitlements ที่คุณสามารถแจกจ่ายให้กับ n8n instances ต่างๆ ได้ คุณสามารถกำหนด floating entitlement ใหม่เพื่อโอนสิทธิ์การเข้าถึงไปยัง n8n instance อื่นได้

#### evaluation (n8n)

ใน n8n, evaluation ช่วยให้คุณสามารถแท็กและจัดระเบียบประวัติ execution และเปรียบเทียบกับ executions ใหม่ได้ คุณสามารถใช้สิ่งนี้เพื่อทำความเข้าใจว่า workflow ของคุณทำงานอย่างไรเมื่อเวลาผ่านไปในขณะที่คุณทำการเปลี่ยนแปลง โดยเฉพาะอย่างยิ่ง สิ่งนี้มีประโยชน์ในขณะที่พัฒนา workflows ที่เน้น AI

#### expression (n8n)

ใน n8n, expressions ช่วยให้คุณสามารถเติมค่า parameters ของ node แบบไดนามิกได้โดยการ execute โค้ด JavaScript แทนที่จะให้ค่าคงที่ คุณสามารถใช้ syntax ของ n8n expression เพื่อกำหนดค่าโดยใช้ข้อมูลจาก nodes ก่อนหน้า, workflows อื่นๆ หรือ n8n environment ของคุณ

#### LangChain

LangChain คือ AI-development framework ที่ใช้ในการทำงานกับ large language models (LLMs) LangChain จัดเตรียมระบบที่เป็นมาตรฐานสำหรับการทำงานกับ models และทรัพยากรอื่นๆ ที่หลากหลาย และเชื่อมโยง components ต่างๆ เข้าด้วยกันเพื่อสร้างแอปพลิเคชันที่ซับซ้อน

#### Large language model (LLM)

Large language models หรือ LLMs คือ AI machine learning models ที่ออกแบบมาเพื่อให้เก่งในงาน natural language processing (NLP) สร้างขึ้นโดยการฝึกฝนกับข้อมูลจำนวนมากเพื่อพัฒนารูปแบบความน่าจะเป็นของภาษาและข้อมูลอื่นๆ

#### node (n8n)

ใน n8n, nodes คือ components แต่ละส่วนที่คุณประกอบขึ้นเพื่อสร้าง workflows Nodes กำหนดว่า workflow ควรทำงานเมื่อใด, ช่วยให้คุณดึง, ส่ง และประมวลผลข้อมูล, สามารถกำหนด logic การควบคุม flow และเชื่อมต่อกับบริการภายนอกได้

#### project (n8n)

n8n projects ช่วยให้คุณสามารถแยก workflows, variables และ credentials ออกเป็นกลุ่มๆ เพื่อการจัดการที่ง่ายขึ้น Projects ทำให้ทีมทำงานร่วมกันได้ง่ายขึ้นโดยการแชร์และแบ่งส่วนทรัพยากรที่เกี่ยวข้อง

#### root node (n8n)

แต่ละ n8n cluster node ประกอบด้วย root nodes เดียวที่กำหนดฟังก์ชันการทำงานหลักของ cluster sub nodes หนึ่งรายการขึ้นไปจะแนบกับ root node เพื่อขยายฟังก์ชันการทำงาน

#### sub node (n8n)

n8n cluster nodes ประกอบด้วย sub nodes หนึ่งรายการขึ้นไปที่เชื่อมต่อกับ root node Sub nodes ขยายฟังก์ชันการทำงานของ root node โดยให้การเข้าถึงบริการหรือทรัพยากรเฉพาะ หรือนำเสนอการประมวลผลเฉพาะประเภท เช่น ฟังก์ชันเครื่องคิดเลข เป็นต้น

#### template (n8n)

n8n templates คือ workflows ที่สร้างไว้ล่วงหน้าซึ่งออกแบบโดย n8n และสมาชิก community ที่คุณสามารถ import เข้าสู่ n8n instance ของคุณได้ เมื่อใช้ templates คุณอาจต้องกรอก credentials และปรับการกำหนดค่าให้เหมาะกับความต้องการของคุณ

#### trigger node (n8n)

Trigger node คือ node พิเศษที่รับผิดชอบในการ execute workflow เพื่อตอบสนองต่อเงื่อนไขบางอย่าง Production workflows ทั้งหมดต้องการ trigger อย่างน้อยหนึ่งรายการเพื่อกำหนดว่า workflow ควรทำงานเมื่อใด

#### workflow (n8n)

n8n workflow คือชุดของ nodes ที่ทำงานอัตโนมัติในกระบวนการ Workflows เริ่ม execution เมื่อเงื่อนไข trigger เกิดขึ้นและ execute ตามลำดับเพื่อให้บรรลุภารกิจที่ซับซ้อน

<!-- To do
#### OAuth
#### pagination
#### Role-based access control (RBAC)
#### SAML/SSO
#### two-factor authentication (2FA)
#### webhook
-->
