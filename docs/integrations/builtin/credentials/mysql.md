---
title: ข้อมูลยืนยันตัวตน MySQL
description: เอกสารสำหรับการยืนยันตัวตน MySQL. ใช้ข้อมูลเหล่านี้เพื่อยืนยันตัวตน MySQL ใน n8n.
contentType: [integration, reference]
priority: high
---

# MySQL credentials

คุณสามารถใช้ credentials เหล่านี้เพื่อยืนยันตัวตนใน nodes ต่อไปนี้:

- [MySQL](/integrations/builtin/app-nodes/n8n-nodes-base.mysql/index.md)
- [Agent](/integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.agent/index.md)

/// note | Agent node users
Agent node ไม่รองรับ SSH tunnels
///

## Prerequisites

สร้างบัญชีผู้ใช้บนฐานข้อมูลเซิร์ฟเวอร์ [MySQL](https://www.mysql.com/){:target=_blank .external-link}

## Supported authentication methods

- Database connection

## Related resources

อ้างอิง [MySQL's documentation](https://dev.mysql.com/doc/refman/8.3/en/){:target=_blank .external-link} สำหรับข้อมูลเพิ่มเติมเกี่ยวกับบริการนี้

## Using database connection

ในการกำหนดค่า credential นี้ คุณจะต้องมี:

- **Host** ของเซิร์ฟเวอร์: ชื่อ host หรือ IP address ของฐานข้อมูล
- ชื่อ **Database**
- ชื่อ **User**
- **Password** สำหรับผู้ใช้นั้น
- หมายเลข **Port** ที่เซิร์ฟเวอร์ MySQL ใช้
- **Connect Timeout**: จำนวนมิลลิวินาทีระหว่างการเชื่อมต่อฐานข้อมูลเริ่มต้นก่อนที่จะเกิด timeout
- **SSL**: หากฐานข้อมูลของคุณใช้ SSL ให้เปิดใช้งานและเพิ่มรายละเอียดสำหรับใบรับรอง SSL
- **SSH Tunnel**: เลือกว่าจะเชื่อมต่อผ่าน SSH tunnel หรือไม่ SSH tunnel ช่วยให้ traffic ที่ไม่ได้เข้ารหัสผ่านการเชื่อมต่อที่เข้ารหัส และเปิดใช้งานการเข้าถึงระยะไกลที่ได้รับอนุญาตไปยังเซิร์ฟเวอร์ที่ได้รับการป้องกันจากการเชื่อมต่อภายนอกโดย firewall

วิธีตั้งค่า credential การเชื่อมต่อฐานข้อมูลของคุณ:

1. ป้อน hostname ของฐานข้อมูลของคุณเป็น **Host** ใน credential ของ n8n รัน query นี้เพื่อยืนยัน hostname:

    ```
    SHOW VARIABLES WHERE Variable_name = 'hostname';
    ```

2. ป้อนชื่อฐานข้อมูลของคุณเป็น **Database** ใน credential ของ n8n รัน query นี้เพื่อยืนยันชื่อฐานข้อมูล:

    ```
    SHOW DATABASES;
    ```

3. ป้อนชื่อผู้ใช้ของ **User** ในฐานข้อมูล ผู้ใช้นี้ควรมี permissions ที่เหมาะสมสำหรับการดำเนินการใดๆ ที่คุณต้องการให้ n8n ทำ
4. ป้อน **Password** สำหรับผู้ใช้นั้น
5. ป้อนหมายเลข **Port** ที่เซิร์ฟเวอร์ MySQL ใช้ (ค่าเริ่มต้นคือ `3306`) รัน query นี้เพื่อยืนยันหมายเลข port:

    ```
    SHOW VARIABLES WHERE Variable_name = 'port';
    ```

6. ป้อน **Connect Timeout** ที่คุณต้องการให้ node ใช้ Connect Timeout คือจำนวนมิลลิวินาทีระหว่างการเชื่อมต่อฐานข้อมูลเริ่มต้นที่ node ควรรอก่อนที่จะหมดเวลา n8n ตั้งค่าเริ่มต้นเป็น `1000` ซึ่งเป็นค่าเริ่มต้นที่ MySQL ใช้คือ 10 วินาที หากคุณต้องการให้ตรงกับ `connect_timeout` ของฐานข้อมูลของคุณ ให้รัน query นี้เพื่อรับค่า จากนั้นคูณด้วย 100 ก่อนป้อนลงใน n8n:

    ```
    SHOW VARIABLES WHERE Variable_name = 'connect_timeout';
    ```

7. หากฐานข้อมูลของคุณใช้ SSL และคุณต้องการใช้ **SSL** สำหรับการเชื่อมต่อ ให้เปิดใช้งานตัวเลือกนี้ใน credential หากคุณเปิดใช้งาน ให้ป้อนข้อมูลจากใบรับรอง MySQL SSL ของคุณในฟิลด์เหล่านี้:
    1. ป้อนเนื้อหาไฟล์ `ca.pem` ในฟิลด์ **CA Certificate**
    2. ป้อนเนื้อหาไฟล์ `client-key.pem` ในฟิลด์ **Client Private Key**
    3. ป้อนเนื้อหาไฟล์ `client-cert.pem` ในฟิลด์ **Client Certificate**
8. หากคุณต้องการใช้ **SSH Tunnel** สำหรับการเชื่อมต่อ ให้เปิดใช้งานตัวเลือกนี้ใน credential มิฉะนั้น ให้ข้ามไป หากคุณเปิดใช้งาน:
    1. เลือก **SSH Authenticate with** เพื่อตั้งค่าประเภท SSH Tunnel ที่จะสร้าง:
        - เลือก **Password** หากคุณต้องการเชื่อมต่อกับ SSH โดยใช้รหัสผ่าน
        - เลือก **Private Key** หากคุณต้องการเชื่อมต่อกับ SSH โดยใช้ identity file (private key) และ passphrase
    2. ป้อน **SSH Host** n8n ใช้ host นี้เพื่อสร้าง SSH URI ที่จัดรูปแบบเป็น: `[user@]host:port`
    3. ป้อน **SSH Port** n8n ใช้ port นี้เพื่อสร้าง SSH URI ที่จัดรูปแบบเป็น: `[user@]host:port`
    4. ป้อน **SSH User** ที่จะเชื่อมต่อด้วย n8n ใช้ user นี้เพื่อสร้าง SSH URI ที่จัดรูปแบบเป็น: `[user@]host:port`
    5. หากคุณเลือก **Password** สำหรับ **SSH Authenticate with** ให้เพิ่ม **SSH Password**
    6. หากคุณเลือก **Private Key** สำหรับ **SSH Authenticate with**:
        1. เพิ่มเนื้อหาของ **Private Key** หรือ identity file ที่ใช้สำหรับ SSH ซึ่งเหมือนกับการใช้ตัวเลือก `ssh-identity-file` กับคำสั่ง `shell-connect()` ใน MySQL
        2. หาก **Private Key** ถูกสร้างขึ้นด้วย passphrase ให้ป้อน **Passphrase** นั้น ซึ่งเหมือนกับการใช้ตัวเลือก `ssh-identity-pass` กับคำสั่ง `shell-connect()` ใน MySQL หาก **Private Key** ไม่มี passphrase ให้เว้นฟิลด์นี้ว่างไว้

อ้างอิง [MySQL | Creating SSL and RSA Certificates and Keys](https://dev.mysql.com/doc/refman/8.0/en/creating-ssl-rsa-files.html){:target=_blank .external-link} สำหรับข้อมูลเพิ่มเติมเกี่ยวกับการทำงานกับใบรับรอง SSL ใน MySQL อ้างอิง [MySQL | Using an SSH Tunnel](https://dev.mysql.com/doc/mysql-shell/8.0/en/mysql-shell-connection-ssh.html){:target=_blank .external-link} สำหรับข้อมูลเพิ่มเติมเกี่ยวกับการทำงานกับ SSH tunnels ใน MySQL
