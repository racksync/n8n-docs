---
#https://www.notion.so/n8n/Frontmatter-432c2b8dff1f43d4b1c8d20075510fe4
title: Ollama Chat Model node common issues
description: Documentation for common issues and questions in the Ollama Chat Model node in n8n, a workflow automation platform. Includes details of the issue and suggested solutions.
contentType: [integration, reference]
priority: high
---

# Ollama Chat Model node common issues

นี่คือข้อผิดพลาดและปัญหาทั่วไปที่พบบ่อยกับ [Ollama Chat Model node](/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.lmchatollama/index.md) พร้อมขั้นตอนในการแก้ไขหรือแก้ไขปัญหา

## Processing parameters

Ollama Chat Model node เป็น [sub-node](/glossary.md#sub-node-n8n) Sub-nodes มีพฤติกรรมแตกต่างจากโหนดอื่น ๆ เมื่อประมวลผลหลายรายการโดยใช้ expressions

โหนดส่วนใหญ่ รวมถึง [root nodes](/glossary.md#root-node-n8n) รับรายการจำนวนเท่าใดก็ได้เป็น input ประมวลผลรายการเหล่านี้ และ output ผลลัพธ์ คุณสามารถใช้ expressions เพื่ออ้างถึงรายการ input และโหนดจะประมวลผล expression สำหรับแต่ละรายการตามลำดับ ตัวอย่างเช่น หากมี input เป็นค่าชื่อห้าค่า expression `{{ $json.name }}` จะประมวลผลเป็นแต่ละชื่อตามลำดับ

ใน sub-nodes, expression จะประมวลผลเป็นรายการแรกเสมอ ตัวอย่างเช่น หากมี input เป็นค่าชื่อห้าค่า expression `{{ $json.name }}` จะประมวลผลเป็นชื่อแรกเสมอ

## Can't connect to a remote Ollama instance

Ollama Chat Model node ถูกออกแบบมาเพื่อเชื่อมต่อกับ Ollama instance ที่โฮสต์บนเครื่อง local เท่านั้น ไม่ได้รวมคุณสมบัติการ authentication ที่คุณต้องการเพื่อเชื่อมต่อกับ Ollama instance ที่โฮสต์จากระยะไกล

หากต้องการใช้ Ollama Chat Model ให้ทำตาม [Ollama credentials instructions](/integrations/builtin/credentials/ollama.md) เพื่อตั้งค่า Ollama บนเครื่อง local และกำหนดค่า instance URL ใน n8n

## Can't connect to a local Ollama instance when using Docker

Ollama Chat Model node เชื่อมต่อกับ Ollama instance ที่โฮสต์บนเครื่อง local โดยใช้ base URL ที่กำหนดโดย [Ollama credentials](/integrations/builtin/credentials/ollama.md) เมื่อคุณรัน n8n หรือ Ollama ใน Docker คุณต้องกำหนดค่า network เพื่อให้ n8n สามารถเชื่อมต่อกับ Ollama ได้

โดยปกติ Ollama จะรอการเชื่อมต่อบน `localhost` ซึ่งเป็น network address ของเครื่อง local ใน Docker โดยค่าเริ่มต้น แต่ละ container จะมี `localhost` ของตัวเองซึ่งสามารถเข้าถึงได้จากภายใน container เท่านั้น หาก n8n หรือ Ollama กำลังทำงานใน containers พวกมันจะไม่สามารถเชื่อมต่อผ่าน `localhost` ได้

วิธีแก้ปัญหาขึ้นอยู่กับว่าคุณโฮสต์ส่วนประกอบทั้งสองอย่างไร

### If only Ollama is in Docker

หากมีเพียง Ollama ที่ทำงานใน Docker ให้กำหนดค่า Ollama ให้รอรับการเชื่อมต่อบน interfaces ทั้งหมดโดย bind กับ `0.0.0.0` ภายใน container (official images ได้รับการกำหนดค่าด้วยวิธีนี้อยู่แล้ว)

เมื่อรัน container ให้ [publish the ports](https://docs.docker.com/get-started/docker-concepts/running-containers/publishing-ports/) ด้วย flag `-p` โดยค่าเริ่มต้น Ollama ทำงานบน port 11434 ดังนั้นคำสั่ง Docker ของคุณควรมีลักษณะดังนี้:

```shell
docker run -d -v ollama:/root/.ollama -p 11434:11434 --name ollama ollama/ollama
```

เมื่อกำหนดค่า [Ollama credentials](/integrations/builtin/credentials/ollama.md) ที่อยู่ `localhost` ควรทำงานได้โดยไม่มีปัญหา (ตั้งค่า **base URL** เป็น `http://localhost:11434`)

### If only n8n is in Docker

หากมีเพียง n8n ที่ทำงานใน Docker ให้กำหนดค่า Ollama ให้รอรับการเชื่อมต่อบน interfaces ทั้งหมดโดย bind กับ `0.0.0.0` บน host

หากคุณกำลังรัน n8n ใน Docker บน **Linux** ให้ใช้ flag `--add-host` เพื่อ map `host.docker.internal` ไปยัง `host-gateway` เมื่อคุณเริ่ม container ตัวอย่างเช่น:

```shell
docker run -it --rm --add-host host.docker.internal:host-gateway --name n8n -p 5678:5678 -v n8n_data:/home/node/.n8n docker.n8n.io/n8nio/n8n
```

หากคุณใช้ Docker Desktop สิ่งนี้จะถูกกำหนดค่าให้คุณโดยอัตโนมัติ

เมื่อกำหนดค่า [Ollama credentials](/integrations/builtin/credentials/ollama.md) ให้ใช้ `host.docker.internal` เป็น host address แทน `localhost` ตัวอย่างเช่น หากต้องการ bind กับ port 11434 ตามค่าเริ่มต้น คุณสามารถตั้งค่า base URL เป็น `http://host.docker.internal:11434`

### If Ollama and n8n are running in separate Docker containers

หากทั้ง n8n และ Ollama ทำงานใน Docker ใน containers แยกกัน คุณสามารถใช้ Docker networking เพื่อเชื่อมต่อพวกมันได้

กำหนดค่า Ollama ให้รอรับการเชื่อมต่อบน interfaces ทั้งหมดโดย bind กับ `0.0.0.0` ภายใน container (official images ได้รับการกำหนดค่าด้วยวิธีนี้อยู่แล้ว)

เมื่อกำหนดค่า [Ollama credentials](/integrations/builtin/credentials/ollama.md) ให้ใช้ชื่อของ Ollama container เป็น host address แทน `localhost` ตัวอย่างเช่น หากคุณเรียก Ollama container ว่า `my-ollama` และมันรอรับการเชื่อมต่อบน port 11434 ตามค่าเริ่มต้น คุณจะต้องตั้งค่า base URL เป็น `http://my-ollama:11434`

### If Ollama and n8n are running in the same Docker container

หาก Ollama และ n8n ทำงานใน Docker container เดียวกัน ที่อยู่ `localhost` ไม่จำเป็นต้องมีการกำหนดค่าพิเศษใดๆ คุณสามารถกำหนดค่า Ollama ให้รอรับการเชื่อมต่อบน localhost และกำหนดค่า base URL ใน [Ollama credentials in n8n](/integrations/builtin/credentials/ollama.md) ให้ใช้ localhost: `http://localhost:11434`

<!-- vale from-microsoft.HeadingColons = NO -->
## Error: connect ECONNREFUSED ::1:11434
<!-- vale from-microsoft.HeadingColons = YES -->

ข้อผิดพลาดนี้เกิดขึ้นเมื่อคอมพิวเตอร์ของคุณเปิดใช้งาน IPv6 แต่ Ollama กำลังรอรับการเชื่อมต่อที่ IPv4 address

ในการแก้ไขปัญหานี้ ให้เปลี่ยน base URL ใน [Ollama credentials](/integrations/builtin/credentials/ollama.md) ของคุณเพื่อเชื่อมต่อกับ `127.0.0.1` ซึ่งเป็น local address เฉพาะสำหรับ IPv4 แทนที่จะใช้ alias `localhost` ที่สามารถ resolve เป็น IPv4 หรือ IPv6 ได้: `http://127.0.0.1:11434`
