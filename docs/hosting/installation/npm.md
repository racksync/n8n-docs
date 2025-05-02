---
#https://www.notion.so/n8n/Frontmatter-432c2b8dff1f43d4b1c8d20075510fe4
contentType: tutorial
---

# npm

npm เป็นวิธีที่ง่ายและรวดเร็วในการเริ่มต้นใช้งาน n8n บนเครื่องของคุณเอง คุณต้องติดตั้ง [Node.js](https://nodejs.org/en/){:target=_blank .external-link} ก่อน โดย n8n ต้องการ Node.js เวอร์ชัน 18 ขึ้นไป

--8<-- "_snippets/self-hosting/installation/latest-next-version.md"

## Try n8n with npx

คุณสามารถลองใช้ n8n ได้โดยไม่ต้องติดตั้ง เพียงใช้ npx

เปิด terminal แล้วรันคำสั่งนี้:

```bash
npx n8n
```

คำสั่งนี้จะดาวน์โหลดทุกอย่างที่จำเป็นสำหรับการเริ่มต้นใช้งาน n8n จากนั้นคุณสามารถเข้าใช้งาน n8n และเริ่มสร้าง workflow ได้ที่ [http://localhost:5678](http://localhost:5678){:target=_blank .external-link}

## Install globally with npm

ถ้าต้องการติดตั้ง n8n แบบ global ให้ใช้ npm:

```bash
npm install n8n -g
```

ถ้าต้องการติดตั้งหรืออัปเดตเป็นเวอร์ชันที่ต้องการ ให้ใช้ `@` ตามด้วยเวอร์ชัน เช่น:

```bash
npm install -g n8n@0.126.1
```

ถ้าต้องการติดตั้ง `next`:

```bash
npm install -g n8n@next
```

หลังติดตั้งเสร็จ ให้เริ่มต้น n8n โดยรัน:

```bash
n8n
# หรือ
n8n start
```

### Next steps

ลองใช้งาน n8n ได้ที่ [Quickstarts](/try-it-out/index.md)

## Updating

ถ้าต้องการอัปเดต n8n เป็นเวอร์ชันล่าสุด ให้รัน:

```bash
npm update -g n8n
```

ถ้าต้องการติดตั้งเวอร์ชัน `next`:

```bash
npm install -g n8n@next
```

--8<-- "_snippets/self-hosting/installation/tunnel.md"

เริ่ม n8n ด้วย `--tunnel` โดยรัน:

```bash
n8n start --tunnel
```

## Reverting an upgrade

ถ้าต้องการย้อนกลับไปใช้เวอร์ชันเก่า ให้ติดตั้งเวอร์ชันที่ต้องการ

ถ้าการอัปเกรดมีการเปลี่ยนแปลง database migration:

1. ตรวจสอบเอกสารฟีเจอร์และ release notes ว่าต้องทำอะไรเพิ่มเติมหรือไม่
1. รัน `n8n db:revert` บนเวอร์ชันปัจจุบันเพื่อย้อน database กลับ ถ้าต้องการย้อน migration มากกว่าหนึ่งครั้ง ให้ทำซ้ำขั้นตอนนี้

## Windows troubleshooting

ถ้าคุณเจอปัญหาในการใช้งาน n8n บน Windows ให้ตรวจสอบว่า Node.js ถูกติดตั้งและตั้งค่าอย่างถูกต้อง ดูคู่มือของ Microsoft ได้ที่ [Install NodeJS on Windows](https://learn.microsoft.com/en-us/windows/dev-environment/javascript/nodejs-on-windows){:target=_blank .external-link}
