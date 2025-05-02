---
#https://www.notion.so/n8n/Frontmatter-432c2b8dff1f43d4b1c8d20075510fe4
title: Logs environment variables
description: Environment variables to configure logging and diagnostic data. 
contentType: reference
tags:
  - environment variables
hide:
  - toc
  - tags
---

# Logs environment variables

--8<-- "_snippets/self-hosting/file-based-configuration.md"

หน้านี้จะสรุป environment variables สำหรับตั้งค่า logging เพื่อ debug ดูรายละเอียดที่ [Logging in n8n](/hosting/logging-monitoring/logging.md)

## n8n logs

<!-- vale off -->
| Variable | Type  | Default  | Description |
| :------- | :---- | :------- | :---------- |
| `N8N_LOG_LEVEL` | Enum string: `info`, `warn`, `error`, `debug` | `info` | ระดับ log output ดู [Log levels](/hosting/logging-monitoring/logging.md#log-levels) |
| `N8N_LOG_OUTPUT` | Enum string: `console`, `file` | `console` | จะ output log ไปที่ไหน (ใส่หลายค่าคั่น comma) |
| `N8N_LOG_FILE_COUNT_MAX` | Number | `100` | จำนวน log file สูงสุดที่เก็บไว้ |
| `N8N_LOG_FILE_SIZE_MAX` | Number | `16` | ขนาด log file สูงสุด (MB) |
| `N8N_LOG_FILE_LOCATION` | String | `<n8n-directory-path>/logs/n8n.log` | ที่เก็บ log file (ต้องตั้ง N8N_LOG_OUTPUT เป็น `file`) |
| `DB_LOGGING_ENABLED` | Boolean | `false` | เปิด database-specific logging หรือไม่ |
| `DB_LOGGING_OPTIONS` | Enum string: `query`, `error`, `schema`, `warn`, `info`, `log`  | `error` | ระดับ log ของ database ถ้าอยากเปิดทุกอย่างให้ใส่ `all` ดู [TypeORM logging options](https://orkhan.gitbook.io/typeorm/docs/logging#logging-options){:target=_blank .external-link} |
| `DB_LOGGING_MAX_EXECUTION_TIME` | Number | `1000` | เวลารัน query (ms) เกินนี้จะ log เป็น warning ถ้าตั้ง `0` จะปิด warning |
| `CODE_ENABLE_STDOUT` | Boolean | `false` | ตั้งเป็น `true` เพื่อให้ Code node log ไป stdout (debug/monitor/log) |
| `NO_COLOR` | any | `undefined` | ตั้งค่าอะไรก็ได้เพื่อปิด ANSI color ใน log ดู [no-color.org](https://no-color.org/){:target=_blank .external-link} |
<!-- vale on -->

## Log streaming

ดูรายละเอียดที่ [Log streaming](/log-streaming.md)

| Variable | Type  | Default  | Description |
| :------- | :---- | :------- | :---------- |
| `N8N_EVENTBUS_CHECKUNSENTINTERVAL` | Number | `0` | ความถี่ (ms) ที่จะเช็ค event message ที่ยังไม่ได้ส่ง (อาจส่งซ้ำได้ในบางกรณี) ถ้าตั้ง `0` จะปิด |
| `N8N_EVENTBUS_LOGWRITER_SYNCFILEACCESS` | Boolean | `false` | ให้ file access ทั้งหมดเป็น synchronous ใน thread เดียวหรือไม่ |
| `N8N_EVENTBUS_LOGWRITER_KEEPLOGCOUNT` | Number | `3` | จำนวน event log file ที่เก็บไว้ |
| `N8N_EVENTBUS_LOGWRITER_MAXFILESIZEINKB` | Number | `10240` | ขนาดสูงสุด (KB) ของ event log file ก่อนจะเริ่มไฟล์ใหม่ |
| `N8N_EVENTBUS_LOGWRITER_LOGBASENAME` | String | `n8nEventLog` | ชื่อไฟล์หลักของ event log |
