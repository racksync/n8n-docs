---
#https://www.notion.so/n8n/Frontmatter-432c2b8dff1f43d4b1c8d20075510fe4
contentType: tutorial
---

<!-- vale from-microsoft.We = NO -->
<!-- vale from-microsoft.FirstPerson = NO -->
# Designing the Workflow

ตอนนี้เรารู้แล้วว่า Nathan ต้องการ automate อะไรบ้าง ลองพิจารณาขั้นตอนที่เขาต้องทำเพื่อให้บรรลุเป้าหมาย:

1. Get the relevant data (order id, order status, order value, employee name) from the data warehouse
2. Filter the orders by their status (Processing or Booked)
3. Calculate the total value of all the Booked orders
4. Notify the team members about the Booked orders in the company's Discord channel
5. Insert the details about the Processing orders in Airtable for follow-up
6. Schedule this workflow to run every Monday morning

Workflow ของ Nathan เกี่ยวข้องกับการส่งข้อมูลจาก data warehouse ของบริษัทไปยังบริการภายนอกสองแห่ง:

- Discord
- Airtable

ก่อนหน้านั้น ข้อมูลจะต้องถูกจัดการด้วยฟังก์ชันทั่วไป (การกรองตามเงื่อนไข การคำนวณ การตั้งเวลา)

n8n มี integrations สำหรับขั้นตอนเหล่านี้ทั้งหมด ดังนั้น workflow ของ Nathan ใน n8n จะมีลักษณะดังนี้:

[[ workflowDemo("file:////courses/level-one/finished.json") ]]

คุณจะสร้าง workflow นี้ในแปดขั้นตอน:

1. [Getting data from the data warehouse](/courses/level-one/chapter-5/chapter-5.1.md)
2. [Inserting data into Airtable](/courses/level-one/chapter-5/chapter-5.2.md)
3. [Filtering orders](/courses/level-one/chapter-5/chapter-5.3.md)
4. [Setting values for processing orders](/courses/level-one/chapter-5/chapter-5.4.md)
5. [Calculating booked orders](/courses/level-one/chapter-5/chapter-5.5.md)
6. [Notifying the team](/courses/level-one/chapter-5/chapter-5.6.md)
7. [Scheduling the workflow](/courses/level-one/chapter-5/chapter-5.7.md)
8. [Activating and examining the workflow](/courses/level-one/chapter-5/chapter-5.8.md)

ในการสร้าง workflow นี้ คุณจะต้องใช้ credentials ที่อยู่ในอีเมลที่คุณได้รับจาก n8n เมื่อคุณสมัครเข้าร่วมคอร์สนี้ หากคุณยังไม่ได้สมัคร คุณสามารถทำได้ [ที่นี่](https://n8n-community.typeform.com/to/PDEMrevI?typeform-source=127.0.0.1){:target="_blank" .external-link} หากคุณไม่ได้รับอีเมลยืนยันหลังจากสมัคร โปรด [ติดต่อเรา](mailto:help@n8n.io)

[Start building!](/courses/level-one/chapter-5/chapter-5.1.md){ .md-button }
