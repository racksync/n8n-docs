---
#https://www.notion.so/n8n/Frontmatter-432c2b8dff1f43d4b1c8d20075510fe4
title: การแก้ไขปัญหา
description: วิธีแก้ปัญหาที่พบบ่อยในการพัฒนา node
contentType: howto
---

# Troubleshooting

## Credentials

<!-- vale off -->
### Error message: 'Credentials of type "*" aren't known'
<!-- vale on -->

ตรวจสอบว่า ชื่อใน credentials array ตรงกับชื่อที่ใช้ใน property name ของ credentials class หรือไม่

![Troubleshooting credentials](/_images/integrations/creating-nodes/troubleshooting-credentials-1.png)

<!-- vale off -->
## Editor UI
<!-- vale on -->

<!-- vale off -->
### Error message: 'There was a problem loading init data: API-Server can not be reached. It's probably down'
<!-- vale on -->

- ตรวจสอบว่าชื่อไฟล์ node, โฟลเดอร์ node และชื่อ class ตรงกับ path ที่เพิ่มใน `packages/nodes-base/package.json`
- ตรวจสอบว่าชื่อที่ใช้ใน property `displayOptions` ตรงกับชื่อที่ใช้ใน UI elements ของ node

<!-- vale off -->
### Node icon doesn't show up in the Add Node menu and the Editor UI
<!-- vale on -->

- ตรวจสอบว่า icon อยู่ในโฟลเดอร์เดียวกับ node
- ตรวจสอบว่าเป็นไฟล์ PNG หรือ SVG
- เวลาอ้างอิงไฟล์ icon ใน property `icon` ให้ใส่นามสกุลไฟล์ (`.png` หรือ `.svg`) และเติม `file:` ข้างหน้า เช่น `file:friendGrid.png` หรือ `file:friendGrid.svg`

### Node icon doesn't fit

- ถ้าใช้ไฟล์ SVG ให้แน่ใจว่า canvas เป็นสี่เหลี่ยมจัตุรัส ดูวิธีปรับขนาด canvas ของ SVG ด้วย GIMP [ที่นี่](https://docs.gimp.org/2.10/en/gimp-image-resize.html)
- ถ้าใช้ PNG ให้แน่ใจว่าขนาด 60x60 พิกเซล

### Node doesn't show up in the Add Node menu

ตรวจสอบว่าคุณได้ register node ในไฟล์ `package.json` ของโปรเจกต์แล้ว

<!-- vale off -->
### Changes to the description properties don't show in the UI on refreshing
<!-- vale on -->

ทุกครั้งที่เปลี่ยน description properties ต้องหยุด process n8n ที่รันอยู่ (`ctrl` + `c`) แล้วรันใหม่ อาจต้องรัน `npm link` ใหม่ด้วย

### Linter incorrectly warning about file name case

node linter มีกฎเกี่ยวกับชื่อไฟล์ รวมถึงรูปแบบตัวพิมพ์ (case) ผู้ใช้ Windows อาจเจอปัญหาเวลา rename ไฟล์แล้ว linter ยังแจ้งเตือนเหมือนเดิม ทั้งที่ rename แล้ว สาเหตุเพราะ [ปัญหาใน Windows](https://answers.microsoft.com/en-us/windows/forum/all/file-renaming-when-changing-case-doesnt-work/aa15ff7c-dd2d-4ed3-bcce-799ca90d4e58) เวลาตั้งชื่อไฟล์ใหม่แค่เปลี่ยน case
