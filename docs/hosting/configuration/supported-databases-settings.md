---
#https://www.notion.so/n8n/Frontmatter-432c2b8dff1f43d4b1c8d20075510fe4
title: Database ที่รองรับ
description: Database ที่ n8n รองรับและการตั้งค่า
contentType: reference
---

# Supported databases

โดยปกติ n8n จะใช้ SQLite สำหรับเก็บ credentials, execution ที่ผ่านมา และ workflows ต่าง ๆ แต่ก็รองรับ PostgresDB ด้วย

## Shared settings

environment variables เหล่านี้ใช้ได้กับทุก database:

 - `DB_TABLE_PREFIX` (default: -) - prefix สำหรับชื่อ table

## PostgresDB

ถ้าต้องการใช้ PostgresDB เป็น database ให้ตั้ง environment variables เหล่านี้

 - `DB_TYPE=postgresdb`
 - `DB_POSTGRESDB_DATABASE` (default: 'n8n')
 - `DB_POSTGRESDB_HOST` (default: 'localhost')
 - `DB_POSTGRESDB_PORT` (default: 5432)
 - `DB_POSTGRESDB_USER` (default: 'postgres')
 - `DB_POSTGRESDB_PASSWORD` (default: empty)
 - `DB_POSTGRESDB_SCHEMA` (default: 'public')
 - `DB_POSTGRESDB_SSL_CA` (default: undefined): path ไปยัง CA certificate ของ server สำหรับ validate connection (ไม่รองรับ opportunistic encryption)
 - `DB_POSTGRESDB_SSL_CERT` (default: undefined): path ไปยัง TLS certificate ของ client
 - `DB_POSTGRESDB_SSL_KEY` (default: undefined): path ไปยัง private key ของ client ที่ตรงกับ certificate
 - `DB_POSTGRESDB_SSL_REJECT_UNAUTHORIZED` (default: true): จะ reject TLS connection ที่ validate ไม่ผ่านหรือไม่

```bash
export DB_TYPE=postgresdb
export DB_POSTGRESDB_DATABASE=n8n
export DB_POSTGRESDB_HOST=postgresdb
export DB_POSTGRESDB_PORT=5432
export DB_POSTGRESDB_USER=n8n
export DB_POSTGRESDB_PASSWORD=n8n
export DB_POSTGRESDB_SCHEMA=n8n

# optional:
export DB_POSTGRESDB_SSL_CA=$(pwd)/ca.crt
export DB_POSTGRESDB_SSL_REJECT_UNAUTHORIZED=false

n8n start
```

### Required permissions

n8n ต้องสร้างและแก้ไข schema ของ table ที่ใช้งาน

สิทธิที่แนะนำ:

```sql
CREATE DATABASE n8n-db;
CREATE USER n8n-user WITH PASSWORD 'random-password';
GRANT ALL PRIVILEGES ON DATABASE n8n-db TO n8n-user;
```

### TLS

เลือก config ได้ตามนี้:

- ไม่กำหนดอะไร (default): เชื่อมต่อแบบ `SSL=off`
- กำหนดแค่ CA กับ unauthorized flag: เชื่อมต่อแบบ `SSL=on` และตรวจสอบลายเซ็น server
- กำหนด `_{CERT,KEY}` ด้วย: ใช้ certificate กับ key สำหรับ client TLS authentication

## SQLite

นี่คือ database ที่ถูกใช้เป็น default ถ้าไม่ได้กำหนดอะไร

ไฟล์ database จะอยู่ที่:
`~/.n8n/database.sqlite`
