---
#https://www.notion.so/n8n/Frontmatter-432c2b8dff1f43d4b1c8d20075510fe4
title: SSH credentials
description: Documentation for SSH credentials. Use these credentials to authenticate SSH in n8n, a workflow automation platform.
contentType: [integration, reference]
priority: medium
---

# SSH credentials

คุณสามารถใช้ credentials นี้เพื่อยืนยันตัวตนกับ node ต่อไปนี้:

- [SSH](/integrations/builtin/core-nodes/n8n-nodes-base.ssh.md)

## Prerequisites

- สร้าง remote server ที่เปิดใช้งาน SSH
- สร้าง user account ที่สามารถ `ssh` เข้า server ได้ โดยใช้วิธีใดวิธีหนึ่งต่อไปนี้:
    - ใช้ [password](#using-password) ของตัวเอง
    - ใช้ SSH [private key](#using-private-key)

## Supported authentication methods

- [Password](#using-password): ใช้วิธีนี้ถ้าคุณมี user account ที่สามารถ `ssh` เข้า server ด้วย password ของตัวเอง
- [Private key](#using-private-key): ใช้วิธีนี้ถ้าคุณมี user account ที่ใช้ SSH key สำหรับ server หรือ service

## Related resources

Secure Shell (SSH) protocol คือวิธีส่งคำสั่งอย่างปลอดภัยผ่าน network ดูตัวอย่างการตั้งค่า SSH ได้ที่ [Connecting to GitHub with SSH](https://docs.github.com/en/github/authenticating-to-github/connecting-to-github-with-ssh)

## Using password

ใช้วิธีนี้ถ้าคุณมี user account ที่สามารถ `ssh` เข้า server ด้วย password ของตัวเอง

วิธีตั้งค่า credential นี้ ให้กรอกข้อมูลดังนี้:

1. กรอก IP address ของ server ที่ต้องการเชื่อมต่อในช่อง **Host**
2. กรอก **Port** ที่ใช้เชื่อมต่อ (ปกติ SSH ใช้ port `22`)
3. กรอก **Username** ของ user account ที่มีสิทธิ์ `ssh` เข้า server
4. กรอก **Password** ของ user account นั้น

## Using private key

ใช้วิธีนี้ถ้าคุณมี user account ที่ใช้ SSH key สำหรับ server หรือ service

วิธีตั้งค่า credential นี้ ให้กรอกข้อมูลดังนี้:

1. กรอก IP address ของ server ที่ต้องการเชื่อมต่อในช่อง **Host**
2. กรอก **Port** ที่ใช้เชื่อมต่อ (ปกติ SSH ใช้ port `22`)
3. กรอก **Username** ของ account ที่สร้าง private key นี้
4. กรอกเนื้อหา SSH **Private Key** ทั้งหมด
5. ถ้าคุณตั้ง **Passphrase** ให้กับ **Private Key** ให้กรอก passphrase ด้วย
    - ถ้าไม่ได้ตั้ง passphrase ให้เว้นว่างไว้
