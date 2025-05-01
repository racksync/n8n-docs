---
#https://www.notion.so/n8n/Frontmatter-432c2b8dff1f43d4b1c8d20075510fe4
title: FTP credentials
description: Documentation for FTP credentials. Use these credentials to authenticate FTP in n8n, a workflow automation platform.
contentType: [integration, reference]
priority: medium
---

# FTP credentials

คุณสามารถใช้ credentials เหล่านี้เพื่อยืนยันตัวตนกับ node ต่อไปนี้:

- [FTP](/integrations/builtin/core-nodes/n8n-nodes-base.ftp.md)

## Prerequisites

สร้างบัญชีบนเซิร์ฟเวอร์ File Transfer Protocol (FTP) เช่น [JSCAPE](https://mft.jscape.com/lp/ftp-server){:target=_blank .external-link}, [OpenSSH](https://www.openssh.com/){:target=_blank .external-link}, หรือ [FileZilla Server](https://filezilla-project.org/){:target=_blank .external-link}

## Supported authentication methods

- **FTP account**: ใช้วิธีนี้หากเซิร์ฟเวอร์ FTP ของคุณไม่รองรับ SSH tunneling หรือการเชื่อมต่อที่เข้ารหัส
- **SFTP account**: ใช้วิธีนี้หากเซิร์ฟเวอร์ FTP ของคุณรองรับ SSH tunneling และการเชื่อมต่อที่เข้ารหัส

## Related resources

File Transfer Protocol (FTP) และ Secure Shell File Transfer Protocol (SFTP) เป็นโปรโตคอลสำหรับการถ่ายโอนไฟล์โดยตรงระหว่าง FTP/SFTP client และ server

## Using FTP account

ใช้วิธีนี้หากเซิร์ฟเวอร์ FTP ของคุณไม่รองรับ SSH tunneling หรือการเชื่อมต่อที่เข้ารหัส

ในการกำหนดค่า credential นี้ คุณจะต้อง:

1. ป้อนชื่อหรือ IP address ของ **Host** ของเซิร์ฟเวอร์ FTP ของคุณ
2. ป้อนหมายเลข **Port** ที่การเชื่อมต่อควรใช้
3. ป้อน **Username** ที่ credential ควรเชื่อมต่อเป็น
4. ป้อน **Password** ของผู้ใช้

ตรวจสอบเอกสารของผู้ให้บริการเซิร์ฟเวอร์ FTP ของคุณสำหรับคำแนะนำในการรับข้อมูลที่คุณต้องการ

## Using SFTP account

ใช้วิธีนี้หากเซิร์ฟเวอร์ FTP ของคุณรองรับ SSH tunneling และการเชื่อมต่อที่เข้ารหัส

ในการกำหนดค่า credential นี้ คุณจะต้อง:

1. ป้อนชื่อหรือ IP address ของ **Host** ของเซิร์ฟเวอร์ FTP ของคุณ
2. ป้อนหมายเลข **Port** ที่การเชื่อมต่อควรใช้
3. ป้อน **Username** ที่ credential ควรเชื่อมต่อเป็น
4. ป้อน **Password** ของผู้ใช้
5. สำหรับ **Private Key** ให้ป้อนสตริงสำหรับการยืนยันตัวตนผู้ใช้แบบ key-based หรือ host-based
    - ป้อน Private Key ของคุณในรูปแบบ OpenSSH ซึ่งส่วนใหญ่มักสร้างขึ้นโดยใช้พารามิเตอร์ `ssh-keygen -o` ตัวอย่างเช่น: `ssh-keygen -o -a 100 -t ed25519`
6. หาก **Private Key** ถูกเข้ารหัส ให้ป้อน **Passphrase** ที่ใช้ในการถอดรหัส
    - หาก **Private Key** ไม่ได้ใช้ passphrase ให้เว้นฟิลด์นี้ว่างไว้

ตรวจสอบเอกสารของผู้ให้บริการเซิร์ฟเวอร์ FTP ของคุณสำหรับคำแนะนำในการรับข้อมูลที่คุณต้องการ
