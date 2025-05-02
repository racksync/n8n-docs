---
#https://www.notion.so/n8n/Frontmatter-432c2b8dff1f43d4b1c8d20075510fe4
contentType: tutorial
---

# Hosting n8n on Heroku

คู่มือนี้จะสอนวิธีติดตั้ง n8n แบบ self-host บน Heroku โดยใช้:

- [Docker Compose](https://docs.docker.com/compose/){:target="_blank" .external-link} สำหรับจัดการ container ของแต่ละ service
- [Heroku's PostgreSQL service](https://devcenter.heroku.com/categories/heroku-postgres){:target="_blank" .external-link} สำหรับเก็บข้อมูลของ n8n
- ปุ่ม **Deploy to Heroku** ที่ช่วยให้ deploy ได้ง่าย ๆ แค่คลิกเดียว (แต่ต้องตั้งค่าบางอย่าง)

--8<-- "_snippets/self-hosting/warning.md"

--8<-- "_snippets/self-hosting/installation/latest-next-version.md"

## Use the deployment template to create a Heroku project

วิธีที่เร็วที่สุดในการ deploy n8n ขึ้น Heroku คือกดปุ่ม **Deploy to Heroku** ด้านล่างนี้

[![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://dashboard.heroku.com/new?template=https://github.com/n8n-io/n8n-heroku/tree/main)

จะเปิดหน้า **Create New App** บน Heroku ให้ตั้งชื่อ project และเลือก region ที่จะ deploy

### Configure environment variables

Heroku จะเติมค่าต่าง ๆ ที่ต้องใช้ใน `env` section ของไฟล์ `app.json` ให้อัตโนมัติ (รวมถึงค่า default ของ environment variable ที่ n8n ใช้)

คุณสามารถเปลี่ยนค่าเหล่านี้ได้ตามต้องการ แต่ **ต้องเปลี่ยน** ค่าต่อไปนี้:

- **N8N_ENCRYPTION_KEY**: ใช้สำหรับ [encrypt ข้อมูลบัญชีผู้ใช้](/hosting/configuration/environment-variables/deployment.md) ก่อนบันทึกลง database
- **WEBHOOK_URL**: ต้องตรงกับชื่อ app ที่สร้างไว้ เพื่อให้ webhook ใช้งานได้ถูกต้อง

### Deploy n8n

กด **Deploy app**

หลังจาก Heroku build และ deploy เสร็จ จะมีลิงก์ให้ **Manage App** หรือ **View** แอปที่สร้างไว้

/// note | Heroku and DNS
ดูวิธีเชื่อม domain ของคุณกับ Heroku app ได้ที่ [Heroku documentation](https://devcenter.heroku.com/categories/networking-dns){:target="_blank" .external-link}
///
## Changing the deployment template

ถ้าอยากแก้ไข template ที่ใช้ deploy สามารถ fork [repository](https://github.com/n8n-io/n8n-heroku){:target=_blank .external-link} แล้ว deploy จาก fork ของคุณเองได้

### The Dockerfile

โดยปกติ Dockerfile จะดึง n8n image ล่าสุด ถ้าอยากใช้ version อื่นหรือ fix version ให้แก้ tag ที่บรรทัดแรกของ `Dockerfile`

### Heroku and exposing ports

Heroku ไม่อนุญาตให้ Docker-based app ใช้คำสั่ง `EXPOSE` เพื่อกำหนด port เอง Heroku จะส่งค่า `PORT` มาเป็น environment variable ตอนรันแอปจริง ๆ ไฟล์ `entrypoint.sh` จะ override คำสั่งเริ่มต้นของ Docker image เพื่อใช้ port ที่ Heroku กำหนด คุณจะเข้าใช้งาน n8n ได้ที่ port 80 ผ่าน browser

/// note | Docker limitations with Heroku
อ่านรายละเอียดข้อจำกัดของ Docker บน Heroku ได้ที่ [ที่นี่](https://devcenter.heroku.com/articles/container-registry-and-runtime#unsupported-dockerfile-commands){:target="_blank" .external-link}
///
### Configuring Heroku

ไฟล์ `heroku.yml` จะกำหนดรายละเอียดของแอปบน Heroku มี 2 ส่วนหลัก:

* `setup` > `addons`: กำหนด Heroku addon ที่จะใช้ (เช่น PostgreSQL)
* `build`: กำหนดวิธี build แอป (ในที่นี้ใช้ Docker buildpack สร้าง service `web` จาก `Dockerfile` ที่ให้มา)

## Next steps

--8<-- "_snippets/self-hosting/installation/server-setups-next-steps.md"
