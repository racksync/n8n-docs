---
#https://www.notion.so/n8n/Frontmatter-432c2b8dff1f43d4b1c8d20075510fe4
title: Environment Variables สำหรับ Database
description: ตั้งค่าและ Configure Databases ด้วย Environment Variables สำหรับ n8n Self-hosted
contentType: reference
tags:
  - environment variables
hide:
  - toc
  - tags
---

# Database environment variables

--8<-- "_snippets/self-hosting/file-based-configuration.md"

โดยปกติ n8n จะใช้ SQLite เป็น database หลัก แต่ก็รองรับ PostgreSQL ด้วย n8n [เลิก support MySQL และ MariaDB](/1-0-migration-checklist.md#mysql-and-mariadb) ตั้งแต่ v1.0

หน้านี้จะสรุป environment variables สำหรับตั้งค่า database ที่ต้องการใช้กับ n8n

| Variable | Type  | Default  | Description |
| :------- | :---- | :------- | :---------- |
| `DB_TYPE`<br>/`_FILE` | Enum string:<br> `sqlite`, `postgresdb` | `sqlite` | เลือก database ที่จะใช้ |
| `DB_TABLE_PREFIX` | * | - | prefix สำหรับชื่อ table |

## PostgreSQL

| Variable | Type  | Default  | Description |
| :------- | :---- | :------- | :---------- |
| `DB_POSTGRESDB_DATABASE`<br>/`_FILE` | String | `n8n` | ชื่อ database ของ PostgreSQL |
| `DB_POSTGRESDB_HOST`<br>/`_FILE` | String | `localhost` | host ของ PostgreSQL |
| `DB_POSTGRESDB_PORT`<br>/`_FILE` | Number | `5432` | port ของ PostgreSQL |
| `DB_POSTGRESDB_USER`<br>/`_FILE` | String | `postgres` | user ของ PostgreSQL |
| `DB_POSTGRESDB_PASSWORD`<br>/`_FILE` | String | - | password ของ PostgreSQL |
| `DB_POSTGRESDB_POOL_SIZE`<br>/`_FILE` | Number | `2` | จำนวน connection ที่ n8n จะเปิดกับ Postgres พร้อมกัน เพิ่มได้ถ้าอยากให้ใช้ resource เต็มที่ แต่ถ้าเยอะเกินอาจช้าลง |
| `DB_POSTGRESDB_CONNECTION_TIMEOUT`<br>/`_FILE` | Number | `20000` | timeout ของการเชื่อมต่อ Postgres (ms) |
| `DB_POSTGRESDB_SCHEMA`<br>/`_FILE` | String | `public` | schema ของ PostgreSQL |
| `DB_POSTGRESDB_SSL_ENABLED`<br>/`_FILE` | Boolean | `false` | เปิด SSL หรือไม่ จะเปิดอัตโนมัติถ้ากำหนด `DB_POSTGRESDB_SSL_CA`, `DB_POSTGRESDB_SSL_CERT` หรือ `DB_POSTGRESDB_SSL_KEY` |
| `DB_POSTGRESDB_SSL_CA`<br>/`_FILE` | String | - | CA certificate ของ PostgreSQL |
| `DB_POSTGRESDB_SSL_CERT`<br>/`_FILE` | String | - | SSL certificate ของ PostgreSQL |
| `DB_POSTGRESDB_SSL_KEY`<br>/`_FILE` | String | - | SSL key ของ PostgreSQL |
| `DB_POSTGRESDB_SSL_REJECT_UNAUTHORIZED`<br>/`_FILE` | Boolean | `true` | จะ reject SSL connection ที่ไม่ผ่าน validation หรือไม่ |

## SQLite

| Variable | Type  | Default  | Description |
| :------- | :---- | :------- | :---------- |
| `DB_SQLITE_POOL_SIZE` | Number | `0` | ถ้าเป็น 0 จะเปิด SQLite แบบ [rollback journal mode](https://www.sqlite.org/lockingv3.html#rollback) ถ้ามากกว่า 0 จะใช้ [WAL mode](https://www.sqlite.org/wal.html) และกำหนดจำนวน read connection ที่เปิดพร้อมกัน WAL mode จะเร็วและเสถียรกว่า rollback |
| `DB_SQLITE_VACUUM_ON_STARTUP` | Boolean | `false` | สั่ง [VACUUM](https://www.sqlite.org/lang_vacuum.html){:target="_blank" .external-link} ตอนเริ่มต้นเพื่อลดขนาดไฟล์และ optimize index (จะใช้เวลานานขึ้นตอน start) |
