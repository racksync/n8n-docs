---
#https://www.notion.so/n8n/Frontmatter-432c2b8dff1f43d4b1c8d20075510fe4
contentType: howto
title: ติดตั้ง community nodes ด้วยตัวเอง
description: วิธีติดตั้ง community nodes ด้วยตัวเองบน n8n ที่ self-hosted
---

# Manually install community nodes

คุณสามารถติดตั้ง community nodes ด้วยตัวเองบน n8n ที่ self-hosted ได้

กรณีที่ต้องติดตั้ง community nodes ด้วยตัวเอง เช่น:

* instance ของ n8n ของคุณรันใน queue mode
* คุณต้องการติดตั้ง [private packages](https://docs.npmjs.com/creating-and-publishing-private-packages){:target=_blank .external-link}

## Install a community node

เข้า shell ของ Docker:

```sh
docker exec -it n8n sh
```

สร้าง `~/.n8n/nodes` ถ้ายังไม่มี และเข้าไปในโฟลเดอร์นี้:

```sh
mkdir ~/.n8n/nodes
cd ~/.n8n/nodes
```

ติดตั้ง node:

```sh
npm i n8n-nodes-nodeName
```
จากนั้น restart n8n

## Uninstall a community node

เข้า shell ของ Docker:

```sh
docker exec -it n8n sh
```

รันคำสั่ง npm uninstall:

```sh
npm uninstall n8n-nodes-nodeName
```

## Upgrade a community node

/// warning | Breaking changes in versions
นักพัฒนา node อาจมี breaking changes ในเวอร์ชันใหม่ๆ ได้ (breaking change คือการอัปเดตที่ทำให้ฟังก์ชันเดิมใช้ไม่ได้) ขึ้นอยู่กับวิธีการจัดการเวอร์ชันของนักพัฒนา node ถ้าอัปเกรดไปเวอร์ชันที่มี breaking change อาจทำให้ workflow ที่ใช้ node นั้นเสียได้ ควรตรวจสอบก่อนอัปเกรด ถ้าอัปเกรดแล้วมีปัญหา สามารถ [downgrade](#upgrade-or-downgrade-to-a-specific-version) กลับได้
///
### Upgrade to the latest version

เข้า shell ของ Docker:

```sh
docker exec -it n8n sh
```

รันคำสั่ง npm update:

```sh
npm update n8n-nodes-nodeName
```

### Upgrade or downgrade to a specific version

เข้า shell ของ Docker:

```sh
docker exec -it n8n sh
```

รัน npm uninstall เพื่อลบเวอร์ชันปัจจุบัน:

```sh
npm uninstall n8n-nodes-nodeName
```

รัน npm install พร้อมระบุเวอร์ชันที่ต้องการ:

```sh
# เปลี่ยน 2.1.0 เป็นหมายเลขเวอร์ชันที่ต้องการ
npm install n8n-nodes-nodeName@2.1.0
```
