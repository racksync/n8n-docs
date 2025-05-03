---
#https://www.notion.so/n8n/Frontmatter-432c2b8dff1f43d4b1c8d20075510fe4
title: ปัญหาที่พบบ่อยใน Execute Command node
description: รวมปัญหาและคำถามที่พบบ่อยเกี่ยวกับ Execute Command node ใน n8n พร้อมแนวทางแก้ไข
contentType: [integration, reference]
priority: high
---

# Execute Command node common issues

นี่คือปัญหาที่เจอบ่อยกับ [Execute Command node](/integrations/builtin/core-nodes/n8n-nodes-base.executecommand/index.md) พร้อมวิธีแก้ไขหรือแนวทางตรวจสอบ

<!-- vale off -->
## Command failed: &lt;command&gt; /bin/sh: &lt;command&gt;: not found
<!-- vale on -->

ข้อผิดพลาดนี้เกิดขึ้นเมื่อ shell หา command ที่ใส่ใน **Command** parameter ไม่เจอ

วิธีแก้ไข ลองตรวจสอบตามนี้:

* ตรวจสอบว่า command และ argument ที่ใส่ใน **Command** parameter ไม่มีพิมพ์ผิด
* ตรวจสอบว่า command นั้นอยู่ใน `PATH` ของ user ที่รัน n8n
* ถ้ารัน n8n ด้วย Docker ให้เช็คว่า command นั้นมีอยู่ใน container หรือเปล่า โดยลองรันเองใน container ถ้าไม่มี command ที่ต้องการใน container อาจต้องสร้าง [custom image](https://docs.docker.com/build/building/base-images/){:target=_blank .external-link} ที่มี command นั้นเพิ่มเข้าไป
	* ถ้า n8n กำลังรันอยู่:
		```sh
		# หา container ID ของ n8n จะอยู่คอลัมน์แรก
		docker ps | grep n8n
		# ลองรัน command ใน container ที่กำลังรันอยู่
		docker container exec <container_ID> <command_to_run>
		```
	* ถ้า n8n ยังไม่รัน:
		```sh
		# สตาร์ท container ใหม่ที่รัน command แทนที่จะรัน n8n
		# ใช้ image และ tag เดียวกับที่ใช้รัน n8n ปกติ
		docker run -it --rm --entrypoint /bin/sh docker.n8n.io/n8nio/n8n -c <command_to_run>
		```

<!-- vale off -->
## Error: stdout maxBuffer length exceeded
<!-- vale on -->

ข้อผิดพลาดนี้เกิดขึ้นเมื่อ command ของคุณส่ง output ออกมามากเกินกว่าที่ Execute Command node จะรับไหวในครั้งเดียว

วิธีแก้ไข ให้ลด output ที่ command ส่งออกมา ลองดู manual หรือ documentation ของ command ว่ามี flag สำหรับจำกัดหรือกรอง output หรือเปล่า ถ้าไม่มี อาจต้อง pipe output ไปยัง command อื่นเพื่อตัดข้อมูลที่ไม่จำเป็นออก
