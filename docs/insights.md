---
#https://www.notion.so/n8n/Frontmatter-432c2b8dff1f43d4b1c8d20075510fe4
description: Insights
contentType: explanation
---

# Insights

Insights ช่วยให้เจ้าของ instance และผู้ดูแลระบบมองเห็นภาพรวมว่า workflows ทำงานอย่างไรเมื่อเวลาผ่านไป ฟีเจอร์นี้ประกอบด้วยสามส่วน:

- [**Insights summary banner**](#insights-summary-banner): แสดงเมตริกสำคัญเกี่ยวกับ instance ของคุณจาก 7 วันที่ผ่านมาที่ด้านบนของพื้นที่ภาพรวม
- [**Insights dashboard**](#insights-dashboard): การแจกแจงภาพที่ละเอียดมากขึ้นพร้อมเมตริกต่อ workflow และการเปรียบเทียบย้อนหลัง
- **Time saved (Workflow ROI)**: สำหรับแต่ละ workflow คุณสามารถตั้งค่าจำนวนนาทีที่ประหยัดได้สำหรับการ execution ใน production แต่ละครั้ง

/// info | Feature availability
Insights summary banner แสดงกิจกรรมจาก 7 วันที่ผ่านมาสำหรับทุกแผน Insights dashboard มีให้ใช้งานเฉพาะในแผน Pro (พร้อมช่วงวันที่จำกัด) และ Enterprise เท่านั้น
///

## Insights summary banner

n8n รวบรวมเมตริกหลายรายการสำหรับทั้ง insights summary banner และ dashboard ซึ่งรวมถึง:

- Total production executions (ไม่รวม sub-workflow executions หรือ manual executions)
- Total failed production executions
- Production execution failure rate
- Time saved (เมื่อตั้งค่าไว้อย่างน้อยหนึ่ง workflow ที่ใช้งานอยู่)
- Run time average (รวม wait time จาก wait nodes ใดๆ)

## Insights dashboard

ผู้ที่อยู่ในแผน Pro และ Enterprise สามารถเข้าถึงส่วน **Insights** ได้จากแถบนำทางด้านข้าง เมตริกแต่ละรายการจาก summary banner ยังสามารถคลิกได้ ซึ่งจะนำคุณไปยังแผนภูมิที่เกี่ยวข้อง

Insights dashboard ยังมีตารางที่แสดง insights แต่ละรายการจากแต่ละ workflow รวมถึง total production executions, failed production executions, failure rate, time saved และ run time average

## Insights time periods

Insights summary banner และ dashboard จะแสดงหน้าต่าง 7 วันแบบ rolling เสมอ พร้อมการเปรียบเทียบกับช่วงเวลาก่อนหน้าเพื่อแสดงการเพิ่มขึ้นหรือลดลงสำหรับแต่ละเมตริก

## Disable or configure insights metrics collection

หากคุณ self-host n8n คุณสามารถปิดใช้งานหรือกำหนดค่าการรวบรวม insights และ metrics ได้โดยใช้ [environment variables](/hosting/configuration/environment-variables/insights.md)
