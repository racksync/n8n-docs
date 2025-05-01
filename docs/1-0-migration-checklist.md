---
#https://www.notion.so/n8n/Frontmatter-432c2b8dff1f43d4b1c8d20075510fe4
title: n8n v1.0 migration guide
description: What's new in version 1
contentType: reference
---

# n8n v1.0 migration guide

เอกสารนี้ให้ข้อมูลสรุปเกี่ยวกับสิ่งที่คุณควรทราบก่อนอัปเดตเป็น n8n เวอร์ชัน 1.0

การเปิดตัว n8n 1.0 ถือเป็นก้าวสำคัญในการเดินทางของ n8n เพื่อทำให้ n8n พร้อมใช้งานสำหรับสภาพแวดล้อม production ที่มีความต้องการสูง เวอร์ชัน 1.0 แสดงถึงการทำงานหนักที่ลงทุนไปตลอดสี่ปีที่ผ่านมาเพื่อทำให้ n8n เป็นเครื่องมือ automation ที่เข้าถึงได้ง่าย ทรงพลัง และหลากหลายที่สุด n8n 1.0 พร้อมใช้งานใน production แล้ว

## New features

### Python support in the Code node

แม้ว่า JavaScript จะยังคงเป็นภาษาเริ่มต้น แต่ตอนนี้คุณสามารถเลือก Python เป็นตัวเลือกใน [Code node](/code/code-node.md) ได้แล้ว และยังสามารถใช้ [Python modules จำนวนมาก](https://pyodide.org/en/stable/usage/packages-in-pyodide.html#packages-in-pyodide){:target=_blank .external link} ได้อีกด้วย โปรดทราบว่า Python ไม่สามารถใช้งานได้ใน Code nodes ที่เพิ่มเข้ามาใน workflow ก่อน v1.0

[PR #4295](https://github.com/n8n-io/n8n/pull/4295){:target=_blank .external link}, [PR #6209](https://github.com/n8n-io/n8n/pull/6209){:target=_blank .external link}

### Execution order

n8n 1.0 แนะนำลำดับการ execution ใหม่สำหรับ multi-branch workflows:

ใน multi-branch workflows, n8n ต้องกำหนดลำดับในการ execute nodes บน branches ก่อนหน้านี้ n8n จะ execute node แรกของแต่ละ branch จากนั้นจึง execute node ที่สองของแต่ละ branch และต่อไปเรื่อยๆ (breadth-first) ลำดับการ execution ใหม่ช่วยให้มั่นใจได้ว่าแต่ละ branch จะ execute เสร็จสมบูรณ์ก่อนที่จะเริ่ม branch ถัดไป (depth-first) Branches จะ execute ตามตำแหน่งบน canvas จากบนลงล่าง หากสอง branches อยู่ที่ความสูงเท่ากัน branch ซ้ายสุดจะ execute ก่อน

n8n เคย execute multi-input nodes ตราบใดที่ได้รับข้อมูลบน input แรก Nodes ที่เชื่อมต่อกับ input ที่สองของ multi-input nodes จะ execute โดยอัตโนมัติโดยไม่คำนึงว่าได้รับข้อมูลหรือไม่ ลำดับการ execution ใหม่ที่แนะนำใน n8n 1.0 ทำให้พฤติกรรมนี้ง่ายขึ้น: Nodes ตอนนี้จะ execute เฉพาะเมื่อได้รับข้อมูลเท่านั้น และ multi-input nodes ต้องการข้อมูลบน input อย่างน้อยหนึ่งรายการเพื่อ execute

workflows ที่มีอยู่ของคุณจะใช้ลำดับแบบ legacy ในขณะที่ workflows ใหม่จะ execute โดยใช้ลำดับ v1 คุณสามารถกำหนดค่าลำดับการ execution สำหรับแต่ละ workflow ได้ใน [workflow settings](/workflows/settings.md)

[PR #4238](https://github.com/n8n-io/n8n/pull/4238){:target=_blank .external link}, [PR #6246](https://github.com/n8n-io/n8n/pull/6246){:target=_blank .external link}, [PR #6507](https://github.com/n8n-io/n8n/pull/6507){:target=_blank .external link}

## Deprecations

### MySQL and MariaDB

n8n ได้ลบการรองรับ MySQL และ MariaDB ในฐานะ storage backends สำหรับ n8n ระบบฐานข้อมูลเหล่านี้มีผู้ใช้เพียงไม่กี่ราย แต่ต้องการความพยายามในการพัฒนาและบำรุงรักษาอย่างต่อเนื่อง n8n แนะนำให้ย้ายไปยัง PostgreSQL เพื่อความเข้ากันได้ที่ดีขึ้นและการสนับสนุนในระยะยาว

[PR #6189](https://github.com/n8n-io/n8n/pull/6189){:target=_blank .external link}

### EXECUTIONS_PROCESS and "own" mode

ก่อนหน้านี้ คุณสามารถใช้ environment variable `EXECUTIONS_PROCESS` เพื่อระบุว่า executions ควรทำงานใน process `main` หรือใน process `own` ของตัวเอง ตัวเลือกนี้และโหมด `own` ตอนนี้ถูก deprecated และจะถูกลบออกใน n8n เวอร์ชันอนาคต เนื่องจากทำให้โค้ดมีความซับซ้อนเพิ่มขึ้นในขณะที่ให้ประโยชน์เพียงเล็กน้อย เริ่มต้นจาก n8n 1.0, `main` จะเป็นค่าเริ่มต้นใหม่

โปรดทราบว่า executions เริ่มทำงานเร็วกว่ามากในโหมด `main` มากกว่าในโหมด `own` อย่างไรก็ตาม หาก workflow ใช้หน่วยความจำมากกว่าที่มีอยู่ อาจทำให้แอปพลิเคชัน n8n ทั้งหมดล่มแทนที่จะเป็นเพียง worker thread เท่านั้น เพื่อลดปัญหานี้ ตรวจสอบให้แน่ใจว่าได้จัดสรรทรัพยากรระบบให้เพียงพอหรือกำหนดค่า [queue mode](/hosting/scaling/queue-mode.md) เพื่อกระจาย executions ไปยัง workers หลายตัว

[PR #6196](https://github.com/n8n-io/n8n/pull/6196){:target=_blank .external link}

## Breaking changes

### Docker

#### Permissions change

เมื่อใช้ deployments ที่ใช้ Docker, process n8n ตอนนี้จะทำงานโดย user `node` แทน `root` การเปลี่ยนแปลงนี้เพิ่มความปลอดภัย

หากข้อผิดพลาดเกี่ยวกับ permission ปรากฏใน logs ของ n8n container ของคุณเมื่อเริ่ม n8n คุณอาจต้องอัปเดต permissions โดยการ execute คำสั่งต่อไปนี้บน Docker host:

```bash
docker run --rm -it --user root -v ~/.n8n:/home/node/.n8n --entrypoint chown n8nio/base:16 -R node:node /home/node/.n8n
```

#### Image removal

เราได้ลบ Debian และ RHEL images ออกแล้ว หากคุณกำลังใช้สิ่งเหล่านี้ คุณต้องเปลี่ยน image ที่คุณใช้ สิ่งนี้ไม่ควรส่งผลให้เกิดข้อผิดพลาดใดๆ เว้นแต่คุณกำลังสร้าง custom image โดยอิงตาม image เหล่านั้น

#### Entrypoint change

entrypoint สำหรับ container ได้เปลี่ยนไป และคุณไม่จำเป็นต้องระบุคำสั่ง n8n อีกต่อไป หากก่อนหน้านี้คุณรัน `n8n worker --concurrency=5` ตอนนี้จะเป็น `worker --concurrency=5`

[PR #6365](https://github.com/n8n-io/n8n/pull/6365){:target=_blank .external link}

### Workflow failures due to expression errors

Workflow executions อาจล้มเหลวเนื่องจาก syntax หรือ runtime errors ใน expressions เช่น ที่อ้างอิงถึง nodes ที่ไม่มีอยู่จริง แม้ว่า expressions จะแสดงข้อผิดพลาดบน frontend อยู่แล้ว แต่การเปลี่ยนแปลงนี้ช่วยให้มั่นใจได้ว่า n8n จะแสดงข้อผิดพลาดบน backend ด้วย ซึ่งก่อนหน้านี้ถูกละเว้นไปอย่างเงียบๆ หากต้องการรับการแจ้งเตือนเกี่ยวกับ workflows ที่ล้มเหลว n8n แนะนำให้ตั้งค่า "error workflow" ภายใต้ workflow settings

[PR #6352](https://github.com/n8n-io/n8n/pull/6352){:target=_blank .external link}

### Mandatory owner account

การเปลี่ยนแปลงนี้ทำให้ [User Management](/user-management/index.md) เป็นข้อบังคับและลบการรองรับสำหรับ authentication methods อื่นๆ เช่น BasicAuth และ External JWT โปรดทราบว่าจำนวนผู้ใช้ที่อนุญาตบน [n8n.cloud](https://n8n.cloud/){:target=_blank .external link} หรือแผน custom ยังคงแตกต่างกันไปขึ้นอยู่กับการสมัครสมาชิกของคุณ

[PR #6362](https://github.com/n8n-io/n8n/pull/6362){:target=_blank .external link}

### Directory for installing custom nodes

n8n จะไม่โหลด custom nodes จาก global `node_modules` directory อีกต่อไป แต่คุณต้องติดตั้ง (หรือ link) ไปยัง `~/.n8n/custom` (หรือ directory ที่กำหนดโดย `N8N_CUSTOM_EXTENSIONS`) Custom nodes ที่เป็น npm packages จะอยู่ใน `~/.n8n/nodes`
หากคุณมี custom nodes ที่ถูก link โดยใช้ `npm link` เข้าไปใน global `node_modules` directory คุณต้อง link ใหม่อีกครั้ง เข้าไปใน `~/.n8n/nodes` แทน

[PR #6396](https://github.com/n8n-io/n8n/pull/6396){:target=_blank .external link}

### WebSockets

environment variable `N8N_PUSH_BACKEND` สามารถใช้เพื่อกำหนดค่าหนึ่งในสองวิธีที่มีอยู่สำหรับการ push updates ไปยัง user interface: `sse` และ `websocket` เริ่มต้นด้วย n8n 1.0, `websocket` เป็นวิธีเริ่มต้น

[PR #6196](https://github.com/n8n-io/n8n/pull/6196){:target=_blank .external link}

### Date transformation functions

n8n มี transformation functions ต่างๆ ที่ทำงานกับ dates ฟังก์ชันเหล่านี้อาจคืนค่าเป็น JavaScript `Date` หรือ Luxon `DateTime` object ด้วยพฤติกรรมใหม่ ประเภทการคืนค่าจะตรงกับ input เสมอ หากคุณเรียก date transformation function บน `Date` มันจะคืนค่าเป็น `Date` ในทำนองเดียวกัน หากคุณเรียกมันบน `DateTime` object มันจะคืนค่าเป็น `DateTime` object

เพื่อระบุ workflows และ nodes ใดๆ ที่อาจได้รับผลกระทบจากการเปลี่ยนแปลงนี้ คุณสามารถใช้ [utility workflow](https://n8n.io/workflows/1929-v1-helper-find-params-with-affected-expressions/){:target=_blank .external link} นี้ได้

สำหรับข้อมูลเพิ่มเติมเกี่ยวกับ date transformation functions โปรดดูที่ [official documentation](/code/builtin/data-transformation-functions/dates.md)

[PR #6435](https://github.com/n8n-io/n8n/pull/6435){:target=_blank .external link}

### Execution data retention

เริ่มต้นจาก n8n 1.0, workflow executions ที่สำเร็จ, ล้มเหลว และ manual ทั้งหมดจะถูกบันทึกโดยค่าเริ่มต้น การตั้งค่าเหล่านี้สามารถแก้ไขได้สำหรับแต่ละ workflow ภายใต้ "Workflow Settings" หรือทั่วโลกโดยใช้ environment variables ที่เกี่ยวข้อง นอกจากนี้ การตั้งค่า `EXECUTIONS_DATA_PRUNE` จะเปิดใช้งานโดยค่าเริ่มต้น โดย `EXECUTIONS_DATA_PRUNE_MAX_COUNT` ตั้งค่าเป็น 10,000 การตั้งค่าเริ่มต้นเหล่านี้ออกแบบมาเพื่อป้องกันประสิทธิภาพที่ลดลงเมื่อใช้ SQLite ตรวจสอบให้แน่ใจว่าได้กำหนดค่าตามความต้องการและขีดความสามารถของระบบของคุณ

[PR #6577](https://github.com/n8n-io/n8n/pull/6577){:target=_blank .external link}

### Removed N8N_USE_DEPRECATED_REQUEST_LIB

legacy `request` library ถูก deprecated มาระยะหนึ่งแล้ว ณ n8n 1.0 ความสามารถในการ fallback ไปใช้มันใน HTTP Request node โดยการตั้งค่า environment variable `N8N_USE_DEPRECATED_REQUEST_LIB` ได้ถูกลบออกไปอย่างสมบูรณ์ HTTP Request node ตอนนี้จะใช้ `HttpRequest` interface ใหม่เสมอ

หากคุณสร้าง custom nodes โปรดดูที่ [HTTP request helpers](/integrations/creating-nodes/build/reference/http-helpers.md) สำหรับข้อมูลเพิ่มเติมเกี่ยวกับการย้ายไปยัง interface ใหม่

[PR #6413](https://github.com/n8n-io/n8n/pull/6413){:target=_blank .external link}

### Removed WEBHOOK_TUNNEL_URL

ณ เวอร์ชัน 0.227.0, n8n ได้เปลี่ยนชื่อตัวเลือกการกำหนดค่า `WEBHOOK_TUNNEL_URL` เป็น `WEBHOOK_URL` ใน n8n 1.0, `WEBHOOK_TUNNEL_URL` ได้ถูกลบออกไปแล้ว อัปเดตการตั้งค่าของคุณเพื่อสะท้อนชื่อใหม่ สำหรับข้อมูลเพิ่มเติมเกี่ยวกับตัวเลือกการกำหนดค่านี้ โปรดดูที่ [the docs](/hosting/configuration/configuration-examples/webhook-url.md)

[PR #1408](https://github.com/n8n-io/n8n/pull/1408){:target=_blank .external link}

### Remove Node 16 support

n8n ตอนนี้ต้องการ Node 18.17.0 หรือสูงกว่า

## Updating to n8n 1.0

1. สร้าง backup เต็มรูปแบบของ n8n
2. n8n แนะนำให้อัปเดตเป็น n8n 0.x release ล่าสุดก่อนอัปเดตเป็น n8n 1.x สิ่งนี้จะช่วยให้คุณระบุปัญหาที่อาจเกิดขึ้นกับ release ที่ถูกต้องได้ เมื่อคุณตรวจสอบแล้วว่า n8n 0.x เริ่มทำงานโดยไม่มีปัญหาใดๆ ให้ดำเนินการขั้นตอนต่อไป
3. อ่านส่วน [Deprecations](#deprecations) และ [Breaking Changes](#breaking-changes) ด้านบนอย่างละเอียดเพื่อประเมินว่าอาจส่งผลกระทบต่อการตั้งค่าของคุณอย่างไร
4. อัปเดตเป็น n8n 1.0:
	* ระหว่าง beta (ก่อนวันที่ 24 กรกฎาคม 2023): หากใช้ Docker ให้ pull `next` Docker image
	* หลังวันที่ 24 กรกฎาคม 2023: หากใช้ Docker ให้ pull `latest` Docker image
5. หากคุณพบปัญหาใดๆ ให้ redeploy n8n เวอร์ชันก่อนหน้าและ restore backup

## Reporting issues

หากคุณพบปัญหาใดๆ ในระหว่างกระบวนการอัปเดตเป็น n8n 1.0 โปรดขอความช่วยเหลือใน community [forum](https://community.n8n.io/){:target=_blank .external link}

## Thank you

เราขอใช้โอกาสนี้แสดงความขอบคุณต่อผู้ใช้ทุกคนสำหรับการสนับสนุนและข้อเสนอแนะอย่างต่อเนื่อง การมีส่วนร่วมของคุณมีค่าอย่างยิ่งในการช่วยให้เราทำให้ n8n เป็นเครื่องมือ automation ที่ดีที่สุดเท่าที่จะเป็นไปได้ เรารู้สึกตื่นเต้นที่จะได้ทำงานร่วมกับคุณต่อไปในขณะที่เราก้าวไปข้างหน้าด้วยการเปิดตัวเวอร์ชัน 1.0 และต่อๆ ไป ขอบคุณที่เป็นส่วนหนึ่งของการเดินทางของเรา!
