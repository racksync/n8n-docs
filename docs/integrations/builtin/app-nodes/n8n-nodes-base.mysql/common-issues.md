---
#https://www.notion.so/n8n/Frontmatter-432c2b8dff1f43d4b1c8d20075510fe4
title: MySQL node common issues
description: Documentation for common issues and questions in the MySQL node in n8n, a workflow automation platform. Includes details of the issue and suggested solutions.
contentType: [integration, reference]
priority: high
---

# MySQL node common issues

นี่คือข้อผิดพลาดและปัญหาทั่วไปที่พบในโหนด [MySQL](/integrations/builtin/app-nodes/n8n-nodes-base.mysql/index.md) และขั้นตอนในการแก้ไขหรือตรวจสอบปัญหา

## Update rows by composite key

การดำเนินการ **Update** ของโหนด MySQL ช่วยให้คุณอัปเดตแถวในตารางโดยระบุ **Column to Match On** และค่า การทำงานแบบนี้เหมาะกับตารางที่สามารถระบุแถวได้อย่างเฉพาะเจาะจงด้วยค่าคอลัมน์เดียว

คุณไม่สามารถใช้รูปแบบนี้กับตารางที่ใช้ [composite keys](https://en.wikipedia.org/wiki/Composite_key) ซึ่งคุณจำเป็นต้องใช้หลายคอลัมน์เพื่อระบุแถวอย่างเฉพาะเจาะจง ตัวอย่างเช่น [ตาราง `user`](https://mariadb.com/kb/en/mysql-user-table/) ใน MySQL ในฐานข้อมูล `mysql` ซึ่งคุณต้องใช้ทั้งคอลัมน์ `user` และ `host` เพื่อระบุแถวอย่างเฉพาะเจาะจง

ในการอัปเดตตารางที่มี composite keys ให้เขียนคำสั่ง query ด้วยตนเองโดยใช้การดำเนินการ **Execute SQL** แทน คุณสามารถจับคู่กับค่าหลายค่า เช่น ในตัวอย่างนี้ที่ทำการจับคู่ทั้ง `customer_id` และ `product_id`:

```sql
UPDATE orders SET quantity = 3 WHERE customer_id = 538 AND product_id = 800;
```

## Can't connect to a local MySQL server when using Docker

เมื่อคุณรัน n8n หรือ MySQL ใน Docker คุณจำเป็นต้องกำหนดค่าเครือข่ายเพื่อให้ n8n สามารถเชื่อมต่อกับ MySQL ได้

วิธีแก้ไขขึ้นอยู่กับวิธีการโฮสต์คอมโพเนนต์ทั้งสอง

### If only MySQL is in Docker

หากมีเพียง MySQL ที่รันใน Docker ให้กำหนดค่า MySQL ให้รับฟังทุก interface โดยการ binding กับ `0.0.0.0` ภายในคอนเทนเนอร์ (อิมเมจทางการได้รับการกำหนดค่าในลักษณะนี้แล้ว)

เมื่อรันคอนเทนเนอร์ ให้ [เผยแพร่พอร์ต](https://docs.docker.com/get-started/docker-concepts/running-containers/publishing-ports/) ด้วยแฟล็ก `-p` โดยค่าเริ่มต้น MySQL รันบนพอร์ต 3306 ดังนั้นคำสั่ง Docker ของคุณควรมีลักษณะดังนี้:

```shell
docker run -p 3306:3306 --name my-mysql -d mysql:latest
```

เมื่อกำหนดค่า [MySQL credentials](/integrations/builtin/credentials/mysql.md) แอดเดรส `localhost` ควรทำงานได้โดยไม่มีปัญหา (ตั้งค่า **Host** เป็น `localhost`)

### If only n8n is in Docker

หากมีเพียง n8n ที่รันใน Docker ให้กำหนดค่า MySQL ให้รับฟังทุก interface โดยการ binding กับ `0.0.0.0` บนโฮสต์

ถ้าคุณกำลังรัน n8n ใน Docker บน **Linux** ให้ใช้แฟล็ก `--add-host` เพื่อ map `host.docker.internal` ไปยัง `host-gateway` เมื่อคุณเริ่มต้นคอนเทนเนอร์ ตัวอย่างเช่น:

```shell
docker run -it --rm --add-host host.docker.internal:host-gateway --name n8n -p 5678:5678 -v n8n_data:/home/node/.n8n docker.n8n.io/n8nio/n8n
```

ถ้าคุณใช้ Docker Desktop การตั้งค่านี้จะถูกกำหนดค่าโดยอัตโนมัติ

เมื่อกำหนดค่า [MySQL credentials](/integrations/builtin/credentials/mysql.md) ให้ใช้ `host.docker.internal` เป็นแอดเดรส **Host** แทน `localhost`

### If MySQL and n8n are running in separate Docker containers

หากทั้ง n8n และ MySQL รันใน Docker ในคอนเทนเนอร์แยกกัน คุณสามารถใช้เครือข่าย Docker เพื่อเชื่อมต่อพวกมัน

กำหนดค่า MySQL ให้รับฟังทุก interface โดยการ binding กับ `0.0.0.0` ภายในคอนเทนเนอร์ (อิมเมจทางการได้รับการกำหนดค่าในลักษณะนี้แล้ว) เพิ่มทั้งคอนเทนเนอร์ MySQL และ n8n ใน [เครือข่าย bridge ที่ผู้ใช้กำหนดเอง](https://docs.docker.com/engine/network/drivers/bridge/)

เมื่อกำหนดค่า [MySQL credentials](/integrations/builtin/credentials/mysql.md) ให้ใช้ชื่อคอนเทนเนอร์ MySQL เป็นแอดเดรส host แทน `localhost` ตัวอย่างเช่น ถ้าคุณเรียกคอนเทนเนอร์ MySQL ว่า `my-mysql` คุณจะตั้งค่า **Host** เป็น `my-mysql`

### If MySQL and n8n are running in the same Docker container

หาก MySQL และ n8n รันในคอนเทนเนอร์ Docker เดียวกัน แอดเดรส `localhost` ไม่จำเป็นต้องมีการกำหนดค่าพิเศษ คุณสามารถกำหนดค่า MySQL ให้รับฟังที่ `localhost` และกำหนดค่า **Host** ใน [MySQL credentials ใน n8n](/integrations/builtin/credentials/ollama.md) ให้ใช้ `localhost`

## Decimal numbers returned as strings

โดยค่าเริ่มต้น โหนด MySQL จะส่งคืนค่า [`DECIMAL`](https://dev.mysql.com/doc/refman/8.4/en/fixed-point-types.html) เป็นสตริง นี่เป็นการทำโดยเจตนาเพื่อหลีกเลี่ยงการสูญเสียความแม่นยำที่อาจเกิดขึ้นเนื่องจากข้อจำกัดของวิธีที่ JavaScript แสดงตัวเลข คุณสามารถเรียนรู้เพิ่มเติมเกี่ยวกับการตัดสินใจนี้ในเอกสารสำหรับ [ไลบรารี MySQL](https://sidorares.github.io/node-mysql2/docs/api-and-configurations) ที่ n8n ใช้

เพื่อแสดงค่าทศนิยมเป็นตัวเลขแทนสตริงและเพิกเฉยต่อความเสี่ยงในการสูญเสียความแม่นยำ ให้เปิดใช้งานตัวเลือก **Output Decimals as Numbers** ซึ่งจะแสดงค่าเป็นตัวเลขแทนสตริง

อีกทางเลือกหนึ่ง คุณสามารถแปลงค่าจากสตริงเป็นทศนิยมด้วยตนเองโดยใช้ [ฟังก์ชั่น `toFloat()`](/code/builtin/data-transformation-functions/strings.md#string-toFloat) กับ [`toFixed()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Number/toFixed) หรือด้วย [โหนด Edit Fields (Set)](/integrations/builtin/core-nodes/n8n-nodes-base.set.md) หลังจากโหนด MySQL โปรดทราบว่าคุณอาจยังคงต้องระวังเรื่องการสูญเสียความแม่นยำที่อาจเกิดขึ้น
