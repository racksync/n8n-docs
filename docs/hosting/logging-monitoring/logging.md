---
#https://www.notion.so/n8n/Frontmatter-432c2b8dff1f43d4b1c8d20075510fe4
contentType: howto
---

# Logging in n8n

Logging เป็นฟีเจอร์สำคัญสำหรับการ debug n8n ใช้ [winston](https://www.npmjs.com/package/winston){:target=_blank .external-link} เป็น logging library

/// note | Log streaming
n8n Self-hosted Enterprise tier มี [Log streaming](/log-streaming.md) ให้ใช้งานเพิ่มจาก logging ปกติที่อธิบายไว้ในเอกสารนี้
///
## Setup

ถ้าต้องการตั้งค่า logging ใน n8n ให้ตั้ง environment variable เหล่านี้ (หรือจะตั้งใน [configuration file](/hosting/configuration/environment-variables/index.md) ก็ได้)

| Setting in the configuration file | Using environment variables | Description |
|-----------------------------------|-----------------------------|-------------|
| n8n.log.level | N8N_LOG_LEVEL | ระดับ log output ที่ต้องการ เลือกได้จาก error, warn, info, debug (เรียงจากน้อยไปมาก) ค่าเริ่มต้นคือ `info` ดูรายละเอียดแต่ละระดับได้ที่ [ด้านล่าง](#log-levels) |
| n8n.log.output | N8N_LOG_OUTPUT | จะให้ log ไปที่ไหน เลือกได้ `console` หรือ `file` หรือทั้งสองอย่าง (คั่นด้วย comma) ค่าเริ่มต้นคือ `console` |
| n8n.log.file.location | N8N_LOG_FILE_LOCATION | ตำแหน่งไฟล์ log (ใช้เฉพาะถ้าเลือก output เป็น file) ค่าเริ่มต้นคือ `<n8nFolderPath>/logs/n8n.log` |
| n8n.log.file.maxsize | N8N_LOG_FILE_SIZE_MAX | ขนาดสูงสุด (MB) ต่อไฟล์ log แต่ละไฟล์ ค่าเริ่มต้นคือ 16 MB |
| n8n.log.file.maxcount | N8N_LOG_FILE_COUNT_MAX | จำนวนไฟล์ log สูงสุดที่จะเก็บไว้ ค่าเริ่มต้นคือ 100 (ควรตั้งค่านี้ถ้าใช้ worker) |


```bash
# ตั้งระดับ log เป็น 'debug'
export N8N_LOG_LEVEL=debug

# ให้ log ออกทั้ง console และไฟล์
export N8N_LOG_OUTPUT=console,file

# กำหนดที่เก็บไฟล์ log
export N8N_LOG_FILE_LOCATION=/home/jim/n8n/logs/n8n.log

# กำหนดขนาดไฟล์ log สูงสุด 50 MB
export N8N_LOG_FILE_MAXSIZE=50

# เก็บไฟล์ log สูงสุด 60 ไฟล์
export N8N_LOG_FILE_MAXCOUNT=60
```

### Log levels

n8n ใช้ระดับ log มาตรฐานดังนี้:

- `silent`: ไม่แสดงอะไรเลย
- `error`: แสดงเฉพาะ error
- `warn`: แสดง error และ warning
- `info`: แสดงข้อมูลที่มีประโยชน์เกี่ยวกับความคืบหน้า
- `debug`: แสดงข้อมูลละเอียดสุด เหมาะกับ debug ปัญหา

## Development

ระหว่างพัฒนา การเพิ่ม log message จะช่วยให้ debug ง่ายขึ้น ถ้าต้องการตั้งค่า logging สำหรับ development ดูตัวอย่างด้านล่าง

### Implementation details

n8n ใช้คลาส `LoggerProxy` ที่อยู่ใน package `workflow` โดยต้องเรียก `LoggerProxy.init()` พร้อม instance ของ `Logger` เพื่อ initialize class นี้ก่อนใช้งาน

การ initialize จะเกิดขึ้นแค่ครั้งเดียว [`start.ts`](https://github.com/n8n-io/n8n/blob/master/packages/cli/src/commands/start.ts) ได้ทำไว้ให้แล้ว ถ้าคุณสร้าง command ใหม่เอง ต้อง initialize `LoggerProxy` เอง

เมื่อสร้าง logger ใน package `cli` แล้ว สามารถเรียกใช้งานได้ด้วย method `getInstance` ที่ export ไว้

ดูตัวอย่างในไฟล์ [start.ts](https://github.com/n8n-io/n8n/blob/master/packages/cli/src/commands/start.ts) ได้เลย

### Adding logs

เมื่อ initialize `LoggerProxy` แล้ว สามารถ import ไปใช้ในไฟล์อื่นๆ เพื่อเพิ่ม log ได้

มี method สำหรับแต่ละระดับ log เช่น `Logger.<logLevel>('<message>', ...meta)` โดย `meta` คือ property เพิ่มเติมที่อยากแนบไปกับ message

ตัวอย่างนี้ใช้ log ระดับ info พร้อมแนบชื่อ workflow และ workflow ID เป็น metadata

```js
// ต้อง import LoggerProxy มาก่อน (เปลี่ยนชื่อเป็น Logger เพื่อให้ใช้ง่ายขึ้น)

import {
	LoggerProxy as Logger
} from 'n8n-workflow';

// log ข้อมูล trigger function ระดับ info พร้อมชื่อ workflow และ workflow ID

Logger.info(`Polling trigger initiated for workflow "${workflow.name}"`, {workflowName: workflow.name, workflowId: workflow.id});
```

เวลาสร้าง log ใหม่ๆ มีแนวทางที่ควรทำ เช่น:

- เขียนข้อความ log ให้อ่านง่าย เช่น ใส่ชื่อใน quote เสมอ
- ข้อมูลที่ซ้ำกันใน message กับ metadata (เช่นชื่อ workflow) จะช่วยให้ค้นหาและ filter log ได้ง่ายขึ้น
- ใส่ ID หลายตัว (เช่น executionId, workflowId, sessionId) ใน log ให้ครบ
- ใช้ node type แทน node name (หรือใส่ทั้งสองอย่าง) เพราะ node type ค้นหาง่ายกว่า

## Front-end logs

ตอนนี้ยังไม่มี log ฝั่ง front-end ถ้าใช้ `Logger` หรือ `LoggerProxy` ใน package `editor-ui` จะ error ฟีเจอร์นี้จะมีในเวอร์ชันถัดไป
