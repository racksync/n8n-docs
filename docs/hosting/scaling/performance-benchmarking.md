---
#https://www.notion.so/n8n/Frontmatter-432c2b8dff1f43d4b1c8d20075510fe4
description: n8n performance and resource consumption benchmarking.
contentType: explanation
---

# Performance and benchmarking

n8n สามารถรองรับ workflow execution ได้สูงสุด 220 ครั้งต่อวินาทีบน instance เดียว และสามารถขยายได้อีกโดยเพิ่ม instance

เอกสารนี้จะอธิบายการทดสอบประสิทธิภาพ (benchmarking) ของ n8n ปัจจัยที่มีผลต่อ performance และตัวอย่าง benchmark 2 แบบ

## Performance factors

ประสิทธิภาพของ n8n ขึ้นอยู่กับปัจจัยเหล่านี้:

* ประเภท workflow
* ทรัพยากรที่ให้กับ n8n
* การตั้งค่า scaling ของ n8n

## Run your own benchmarking

ถ้าอยากได้ตัวเลขที่ตรงกับ use case ของคุณ ให้รัน [benchmarking framework ของ n8n](https://github.com/n8n-io/n8n/tree/master/packages/%40n8n/benchmark){:target=_blank .external-link} ดูรายละเอียดใน repository

## Example: Single instance performance

การทดสอบนี้ดูว่า response time จะเพิ่มขึ้นยังไงเมื่อ request per second เพิ่มขึ้น โดยวัด response time ตอนเรียก Webhook Trigger node

Setup:

- Hardware: ECS c5a.large instance (RAM 4GB)
- n8n setup: n8n instance เดียว (main mode, ใช้ Postgres database)
- Workflow: Webhook Trigger node, Edit Fields node

<figure markdown>
  ![Graph showing n8n response times by requests per second](/_images/hosting/scaling/benchmarking-single-instance-100-250.png)
  <figcaption>กราฟนี้แสดงเปอร์เซ็นต์ของ request ที่ Webhook Trigger node ที่ได้ response ภายใน 100 วินาที และเปรียบเทียบกับปริมาณโหลด ถ้าโหลดสูง n8n ยัง process ข้อมูลได้แต่ใช้เวลาตอบเกิน 100 วินาที</figcaption>
</figure>

## Example: Multi-instance performance

การทดสอบนี้ดูว่า response time จะเพิ่มขึ้นยังไงเมื่อ request per second เพิ่มขึ้น โดยวัด response time ตอนเรียก Webhook Trigger node

Setup:

- Hardware: ECS c5a.4xlarge 7 เครื่อง (RAM 8GB ต่อเครื่อง)
- n8n setup: webhook instance 2 ตัว, worker 4 ตัว, database (MySQL) 1 ตัว, main instance 1 ตัว (รัน n8n และ Redis)
- Workflow: Webhook Trigger node, Edit Fields node
- Multi-instance setup ใช้ [Queue mode](/hosting/scaling/queue-mode.md)

<figure markdown>
  ![Graph showing n8n response times by requests per second](/_images/hosting/scaling/benchmarking-multi-instance-500-2500.png)
  <figcaption>กราฟนี้แสดงเปอร์เซ็นต์ของ request ที่ Webhook Trigger node ที่ได้ response ภายใน 100 วินาที และเปรียบเทียบกับปริมาณโหลด ถ้าโหลดสูง n8n ยัง process ข้อมูลได้แต่ใช้เวลาตอบเกิน 100 วินาที</figcaption>
</figure>

