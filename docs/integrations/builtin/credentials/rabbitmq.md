---
#https://www.notion.so/n8n/Frontmatter-432c2b8dff1f43d4b1c8d20075510fe4
title: ข้อมูลยืนยันตัวตน RabbitMQ
description: เอกสารสำหรับข้อมูลยืนยันตัวตน RabbitMQ ใช้ข้อมูลนี้เพื่อยืนยันตัวตน RabbitMQ ใน n8n แพลตฟอร์ม workflow automation
contentType: [integration, reference]
priority: medium
---

# RabbitMQ credentials

คุณสามารถใช้ credentials นี้เพื่อยืนยันตัวตนกับ node ต่อไปนี้ได้:

- [RabbitMQ](/integrations/builtin/app-nodes/n8n-nodes-base.rabbitmq.md)
- [RabbitMQ Trigger](/integrations/builtin/trigger-nodes/n8n-nodes-base.rabbitmqtrigger.md)

## Supported authentication methods

- User connection

## Related resources

ดูข้อมูลเพิ่มเติมเกี่ยวกับบริการนี้ได้ที่ [RabbitMQ's Connections documentation](https://www.rabbitmq.com/docs/connections){:target=_blank .external-link}

## Using user connection

สำหรับการตั้งค่า credentials นี้ คุณจะต้องติดตั้ง [RabbitMQ broker](https://www.rabbitmq.com/){:target=_blank .external-link} และ:

1. กรอก **Hostname** สำหรับ RabbitMQ broker
2. กรอก **Port** ที่การเชื่อมต่อควรใช้
3. กรอก **User** ที่การเชื่อมต่อควรใช้เพื่อล็อกอิน
    - ค่า default คือ `guest` RabbitMQ แนะนำให้ใช้ user อื่นใน production environments ดูข้อมูลเพิ่มเติมที่ [Access Control | The Basics](https://www.rabbitmq.com/docs/access-control#basics){:target=_blank .external-link} หากคุณใช้ `guest` account กับการเชื่อมต่อที่ไม่ใช่ localhost โปรดดูเคล็ดลับการแก้ไขปัญหาที่ [`guest` user issues](#guest-user-issues) ด้านล่าง
4. กรอก **Password** ของ user
    - password default สำหรับ `guest` user คือ `guest`
5. กรอก [virtual host](https://www.rabbitmq.com/docs/vhosts){:target=_blank .external-link} ที่การเชื่อมต่อควรใช้เป็น **Vhost** virtual host default คือ `/`
6. เลือกว่าการเชื่อมต่อควรใช้ **SSL** หรือไม่ หากเปิดใช้งาน ให้ตั้งค่าเพิ่มเติมดังนี้:
    - **Passwordless**: เลือกว่าการเชื่อมต่อ SSL certificate จะใช้ SASL mechanism EXTERNAL (ปิด) หรือไม่ใช้ password (เปิด) หากเปิดใช้งาน คุณจะต้องกรอก:
        - **Client Certificate**: วางข้อความของ SSL client certificate ที่จะใช้
        - **Client Key**: วาง SSL client key ที่จะใช้
        - **Passphrase**: วาง SSL passphrase ที่จะใช้
    - **CA Certificates**: วางข้อความของ SSL CA certificates ที่จะใช้

## guest user issues

หากคุณใช้ `guest` user สำหรับ credential และพยายามเข้าถึง remote host คุณอาจเห็นข้อผิดพลาดในการเชื่อมต่อ log ของ RabbitMQ จะแสดงข้อผิดพลาดดังนี้:

    [error] <0.918.0> PLAIN login refused: user 'guest' can only connect via localhost

สิ่งนี้เกิดขึ้นเนื่องจาก RabbitMQ ห้าม `guest` user default เชื่อมต่อจาก remote hosts สามารถเชื่อมต่อผ่าน `localhost` เท่านั้น

ในการแก้ไขข้อผิดพลาดนี้ คุณสามารถ:

- อัปเดต `guest` user เพื่ออนุญาตให้เข้าถึง remote host ได้
- สร้างหรือใช้ user อื่นเพื่อเชื่อมต่อกับ remote host `guest` user เป็น user เดียวที่ถูกจำกัดโดย default

ดูข้อมูลเพิ่มเติมที่ ["guest" user can only connect from localhost](https://www.rabbitmq.com/docs/access-control#loopback-users){:target=_blank .external-link}

