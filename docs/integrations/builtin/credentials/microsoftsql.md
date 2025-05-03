---
#https://www.notion.so/n8n/Frontmatter-432c2b8dff1f43d4b1c8d20075510fe4
title: ข้อมูลยืนยันตัวตน Microsoft SQL
description: เอกสารสำหรับ Microsoft SQL credentials ใช้เพื่อเชื่อมต่อ Microsoft SQL ใน n8n
contentType: [integration, reference]
priority: medium
---

# Microsoft SQL credentials

คุณสามารถใช้ credentials เหล่านี้เพื่อยืนยันตัวตนใน nodes ต่อไปนี้:

- [Microsoft SQL](/integrations/builtin/app-nodes/n8n-nodes-base.microsoftsql.md)

## Prerequisites

สร้างบัญชีผู้ใช้บนฐานข้อมูล [Microsoft SQL server](https://learn.microsoft.com/en-us/sql/sql-server/what-is-sql-server){:target=_blank .external-link}

## Supported authentication methods

- SQL database connection

## Related resources

อ้างอิง [Microsoft's Connect to SQL Server documentation](https://learn.microsoft.com/en-us/sql/sql-server/connect-to-database-engine?view=sql-server-ver16&tabs=sqldb#connect-to-sql-server){:target=_blank .external-link} สำหรับข้อมูลเพิ่มเติมเกี่ยวกับการเชื่อมต่อกับบริการ

## Using SQL database connection

ในการกำหนดค่า credential นี้ คุณจะต้องมี:

- ชื่อ **Server**
- ชื่อ **Database**
- บัญชี/ID **User** ของคุณ
- **Password** ของคุณ
- **Port** ที่จะใช้สำหรับการเชื่อมต่อ
- ชื่อ **Domain**
- ว่าจะใช้ **TLS** หรือไม่
- ว่าจะ **Ignore SSL Issues** หรือไม่
- **Connect Timeout**
- **Request Timeout**
- **TDS Version** ที่การเชื่อมต่อควรใช้

วิธีตั้งค่าการเชื่อมต่อฐานข้อมูล:

1. ป้อน SQL Server Host Name เป็น **Server** ในการเชื่อมต่อ SQL Server ที่มีอยู่ host name จะอยู่ก่อน instance name ในรูปแบบ `HOSTNAME\INSTANCENAME` ค้นหา host name:
    - ในบานหน้าต่าง **Object Explorer** เป็น object ระดับบนสุดสำหรับฐานข้อมูลของคุณ
    - ในส่วนท้ายของหน้าต่าง query
    - ดู **Properties** ของการเชื่อมต่อปัจจุบันและมองหา **Name** หรือ **Display Name**
    - อ้างอิง [Find SQL Server Instance Name | When you're connected to SQL Server](https://learn.microsoft.com/en-us/sql/ssms/tutorials/ssms-tricks?view=sql-server-ver16#when-youre-connected-to-sql-server){:target=_blank .external-link} สำหรับข้อมูลเพิ่มเติม คุณยังสามารถค้นหาข้อมูลใน [Error logs](https://learn.microsoft.com/en-us/sql/ssms/tutorials/ssms-tricks?view=sql-server-ver16#before-you-connect-to-sql-server){:target=_blank .external-link}
2. ป้อน SQL Server Instance Name เป็นชื่อ **Database** ค้นหาชื่อนี้โดยใช้ขั้นตอนเดียวกับที่ระบุไว้ข้างต้นสำหรับการค้นหา host name
    - หากคุณไม่เห็น instance name ในที่ใดๆ เหล่านี้ แสดงว่าฐานข้อมูลของคุณใช้ instance name เริ่มต้น `MSSQLSERVER`
3. ป้อนชื่อบัญชีหรือ ID **User** ของคุณ
4. ป้อน **Password** ของคุณ
5. สำหรับ **Port**:
    - SQL Server ใช้ค่าเริ่มต้น `1433`
    - หากคุณไม่สามารถเชื่อมต่อผ่าน port 1433 ได้ ให้ตรวจสอบ [Error logs](https://learn.microsoft.com/en-us/sql/ssms/tutorials/ssms-tricks?view=sql-server-ver16#before-you-connect-to-sql-server){:target=_blank .external-link} สำหรับวลี `Server is listening on` เพื่อระบุหมายเลข port ที่คุณควรป้อน
6. คุณต้องป้อนชื่อ **Domain** เฉพาะเมื่อผู้ใช้ในหลาย domains เข้าถึงฐานข้อมูลของคุณ รัน SQL query นี้เพื่อรับชื่อ domain:

    ```sql
    SELECT DEFAULT_DOMAIN()[DomainName];
    ```

7. เลือกว่าจะใช้ **TLS** หรือไม่
8. เลือกว่าจะ **Ignore SSL Issues**: หากเปิดใช้งาน credential จะเชื่อมต่อแม้ว่าการตรวจสอบใบรับรอง SSL จะล้มเหลว
9. ป้อนจำนวนมิลลิวินาทีที่ n8n ควรพยายามให้การเชื่อมต่อเริ่มต้นเสร็จสมบูรณ์ก่อนที่จะตัดการเชื่อมต่อเป็น **Connect Timeout** อ้างอิงเอกสาร [SqlConnection.ConnectionTimeout property documentation](https://learn.microsoft.com/en-us/dotnet/api/system.data.sqlclient.sqlconnection.connectiontimeout){:target=_blank .external-link} สำหรับข้อมูลเพิ่มเติม
    - SQL Server จัดเก็บ timeout นี้เป็นวินาที ในขณะที่ n8n จัดเก็บเป็นมิลลิวินาที หากคุณกำลังคัดลอกค่าเริ่มต้นของ SQL Server ของคุณ ให้คูณด้วย 100 ก่อนป้อนตัวเลขที่นี่
10. ป้อนจำนวนมิลลิวินาทีที่ n8n ควรรอสำหรับคำขอที่กำหนดก่อนที่จะหมดเวลาเป็น **Request Timeout** โดยพื้นฐานแล้วนี่คือพารามิเตอร์ query timeout อ้างอิง [Troubleshoot query time-out errors](https://learn.microsoft.com/en-us/troubleshoot/sql/database-engine/performance/troubleshoot-query-timeouts#explanation){:target=_blank .external-link} สำหรับข้อมูลเพิ่มเติม
11. เลือกโปรโตคอล Tabular Data Stream (TDS) ที่จะใช้จากรายการดรอปดาวน์ **TDS Version** หากเซิร์ฟเวอร์ไม่รองรับเวอร์ชันที่คุณเลือกที่นี่ การเชื่อมต่อจะใช้เวอร์ชันทางเลือกที่เจรจาต่อรอง อ้างอิง [Appendix A: Product Behavior](https://learn.microsoft.com/en-us/openspecs/windows_protocols/ms-tds/135d0ebe-5c4c-4a94-99bf-1811eccb9f4a){:target=_blank .external-link} สำหรับรายละเอียดเพิ่มเติมเกี่ยวกับความเข้ากันได้ของเวอร์ชัน TDS กับเวอร์ชัน SQL Server และ .NET frameworks ต่างๆ ตัวเลือกได้แก่:
    - **7_4 (SQL Server 2012 ~ 2019)**: TDS เวอร์ชัน 7.4
    - **7_3_B (SQL Server 2008R2)**: TDS เวอร์ชัน 7.3.B
    - **7_3_A (SQL Server 2008)**: TDS เวอร์ชัน 7.3.A
    - **7_2 (SQL Server 2005)**: TDS เวอร์ชัน 7.2
    - **7_1 (SQL Server 2000)**: TDS เวอร์ชัน 7.1
