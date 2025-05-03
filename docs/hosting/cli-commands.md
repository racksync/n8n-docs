---
#https://www.notion.so/n8n/Frontmatter-432c2b8dff1f43d4b1c8d20075510fe4
title: คำสั่ง CLI สำหรับ n8n
description: คำสั่ง CLI ที่มีให้ใช้ใน n8n
contentType: reference
---

# CLI commands for n8n

n8n มี CLI (command line interface) ให้ใช้งาน สามารถสั่งงานต่างๆ ผ่าน CLI แทนการใช้ n8n editor ได้ เช่น สั่งรัน workflow, export/import workflows และ credentials

## Running CLI commands

คุณสามารถใช้ CLI commands กับ n8n แบบ self-hosted ได้ วิธีรันคำสั่งจะแตกต่างกันตามวิธีติดตั้ง:

* npm: ใช้คำสั่ง `n8n` ได้เลย ตัวอย่างในเอกสารนี้จะใช้แบบนี้
* Docker: ใช้คำสั่ง `n8n` ใน container ของคุณ:

    ```sh
    docker exec -u node -it <n8n-container-name> <n8n-cli-command>
    ```

## Start a workflow

คุณสามารถสั่งรัน workflow ได้โดยตรงผ่าน CLI

รัน workflow ที่บันทึกไว้ด้วย ID:

```bash
n8n execute --id <ID>
```

## Change the active status of a workflow

คุณสามารถเปลี่ยนสถานะ active ของ workflow ผ่าน CLI ได้

/// note | Restart required
คำสั่งนี้จะเปลี่ยนแปลงข้อมูลใน database ของ n8n ถ้าใช้ตอนที่ n8n กำลังรันอยู่ การเปลี่ยนแปลงจะยังไม่เกิดขึ้นจนกว่าจะ restart n8n
///

ตั้ง active status ของ workflow ตาม ID ให้เป็น false:

```bash
n8n update:workflow --id=<ID> --active=false
```

ตั้ง active status ของ workflow ตาม ID ให้เป็น true:

```bash
n8n update:workflow --id=<ID> --active=true
```

ตั้ง active status เป็น false สำหรับ workflow ทั้งหมด:

```bash
n8n update:workflow --all --active=false
```

ตั้ง active status เป็น true สำหรับ workflow ทั้งหมด:

```bash
n8n update:workflow --all --active=true
```

## Export workflows and credentials

คุณสามารถ export workflows และ credentials จาก n8n ผ่าน CLI ได้

Flag ที่ใช้กับคำสั่ง:

| Flag | Description |
|-------------|-------|
| --help | แสดง help |
| --all | export workflows/credentials ทั้งหมด |
| --backup | ตั้งค่า --all --pretty --separate สำหรับ backup สามารถกำหนด --output เพิ่มได้ |
| --id | export workflow ตาม ID |
| --output | กำหนดชื่อไฟล์หรือโฟลเดอร์ (ถ้าใช้ --separate) |
| --pretty | จัดรูปแบบ output ให้อ่านง่ายขึ้น |
| --separate | export เป็นไฟล์แยกแต่ละ workflow (เหมาะกับการทำ versioning) ต้องกำหนด directory ด้วย --output |
| --decrypted | export credentials แบบ plain text |

### Workflows

export workflows ทั้งหมดไปที่ terminal:

```bash
n8n export:workflow --all
```

export workflow ตาม ID และกำหนดชื่อไฟล์ output:

```bash
n8n export:workflow --id=<ID> --output=file.json
```

export workflows ทั้งหมดไปยังโฟลเดอร์ที่กำหนดในไฟล์เดียว:

```bash
n8n export:workflow --all --output=backups/latest/file.json
```

export workflows ทั้งหมดไปยังโฟลเดอร์ที่กำหนดโดยใช้ flag `--backup` (ดูรายละเอียดด้านบน):

```bash
n8n export:workflow --backup --output=backups/latest/
```

### Credentials

export credentials ทั้งหมดไปที่ terminal:

```bash
n8n export:credentials --all
```

export credentials ตาม ID และกำหนดชื่อไฟล์ output:

```bash
n8n export:credentials --id=<ID> --output=file.json
```

export credentials ทั้งหมดไปยังโฟลเดอร์ที่กำหนดในไฟล์เดียว:

```bash
n8n export:credentials --all --output=backups/latest/file.json
```

export credentials ทั้งหมดไปยังโฟลเดอร์ที่กำหนดโดยใช้ flag `--backup` (ดูรายละเอียดด้านบน):

```bash
n8n export:credentials --backup --output=backups/latest/
```

export credentials ทั้งหมดแบบ plain text (ใช้สำหรับย้ายข้อมูลไป instance อื่นที่มี secret key ต่างกัน):

/// warning | Sensitive information
ข้อมูลสำคัญทั้งหมดจะเห็นได้ในไฟล์นี้
///

```bash
n8n export:credentials --all --decrypted --output=backups/decrypted.json
```

## Import workflows and credentials

คุณสามารถ import workflows และ credentials เข้า n8n ผ่าน CLI ได้

/// warning | Update the IDs
ตอน export workflows และ credentials จะ export ID มาด้วย ถ้าใน database เดิมมี ID ซ้ำกัน ข้อมูลจะถูกเขียนทับ เพื่อป้องกันให้ลบหรือเปลี่ยน ID ก่อน import
///

Flag ที่ใช้ได้:

| Flag | Description |
|------|-------------|
| --help | แสดง help |
| --input | ชื่อไฟล์ input หรือโฟลเดอร์ (ถ้าใช้ --separate) |
| --projectId | import workflow หรือ credential ไปยัง project ที่กำหนด (ใช้กับ `--userId` ไม่ได้) |
| --separate | import ไฟล์ `*.json` ทั้งหมดจากโฟลเดอร์ที่กำหนดใน --input |
| --userId | import workflow หรือ credential ไปยัง user ที่กำหนด (ใช้กับ `--projectId` ไม่ได้) |

/// note | Migrating to SQLite
n8n จำกัดชื่อ workflow และ credential ไว้ที่ 128 ตัวอักษร แต่ SQLite ไม่ได้บังคับขนาดนี้

อาจเกิด error เช่น **Data too long for column name** ตอน import

ในกรณีนี้ให้แก้ชื่อจาก n8n interface แล้ว export ใหม่ หรือแก้ไขไฟล์ JSON ก่อน import
///

### Workflows

import workflows จากไฟล์ที่กำหนด:

```bash
n8n import:workflow --input=file.json
```

import workflow ไฟล์ทั้งหมดจากโฟลเดอร์ที่กำหนด:

```bash
n8n import:workflow --separate --input=backups/latest/
```

### Credentials

import credentials จากไฟล์ที่กำหนด:

```bash
n8n import:credentials --input=file.json
```

import credentials ไฟล์ทั้งหมดจากโฟลเดอร์ที่กำหนด:

```bash
n8n import:credentials --separate --input=backups/latest/
```

## License

### Clear

ลบ license ที่มีอยู่ใน database ของ n8n และรีเซ็ต n8n ให้กลับไปใช้ฟีเจอร์เริ่มต้น:

```sh
n8n license:clear
```

ถ้า license ของคุณมี [floating entitlements](/glossary.md#entitlement-n8n) การรันคำสั่งนี้จะพยายามคืน entitlement กลับ pool เพื่อให้ instance อื่นใช้ได้

### Info

แสดงข้อมูล license ที่มีอยู่:

```sh
n8n license:info
```

## User management

คุณสามารถรีเซ็ต user management ผ่าน n8n CLI ได้ จะทำให้ระบบกลับไปเหมือนก่อนตั้งค่า user management และลบ user ทั้งหมด

ใช้กรณีลืมรหัสผ่านและไม่มี SMTP สำหรับ reset รหัสผ่านทางอีเมล

```sh
n8n user-management:reset
```

### Disable MFA for a user

ถ้าผู้ใช้ทำ recovery code หาย สามารถปิด MFA ให้ user ด้วยคำสั่งนี้ จากนั้น user จะล็อกอินและตั้งค่า MFA ใหม่ได้

```sh
n8n mfa:disable --email=johndoe@example.com
```

### Disable LDAP

รีเซ็ต LDAP settings ด้วยคำสั่งนี้

```sh
n8n ldap:reset
```

## Security audit

คุณสามารถรัน [security audit](/hosting/securing/security-audit.md) บน n8n instance ของคุณ เพื่อตรวจสอบปัญหาความปลอดภัยทั่วไป

```sh
n8n audit
```
