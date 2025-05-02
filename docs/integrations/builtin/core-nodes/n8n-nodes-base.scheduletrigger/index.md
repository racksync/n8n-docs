---
#https://www.notion.so/n8n/Frontmatter-432c2b8dff1f43d4b1c8d20075510fe4
title: Schedule Trigger node documentation
description: เรียนรู้วิธีการใช้ Schedule Trigger node ใน n8n อ่านเอกสารทางเทคนิคเพื่อรวม Schedule Trigger node เข้ากับ workflow ของคุณ
contentType: [integration, reference]
priority: critical
---

# Schedule Trigger node

ใช้ Schedule Trigger node เพื่อให้ workflow ของคุณทำงานตามเวลาที่กำหนดไว้ล่วงหน้า เหมือนกับการใช้ Cron utility ในระบบ Unix

/// note | You must activate the workflow
ถ้า workflow ของคุณใช้ Schedule node เป็น trigger อย่าลืมกด Save และ Activate workflow ด้วยนะ
///

--8<-- "_snippets/integrations/builtin/core-nodes/schedule/timezone-settings.md"

## Node parameters

เพิ่ม **Trigger Rules** เพื่อกำหนดว่า trigger จะทำงานเมื่อไหร่

ใช้ **Trigger Interval** เพื่อเลือกหน่วยเวลาที่จะใช้ตั้งเวลาให้ trigger ทำงาน พารามิเตอร์อื่นๆ จะขึ้นอยู่กับ interval ที่เลือก สามารถเลือกได้จาก:

- [Schedule Trigger node](#schedule-trigger-node)
  - [Node parameters](#node-parameters)
    - [Seconds trigger interval](#seconds-trigger-interval)
    - [Minutes trigger interval](#minutes-trigger-interval)
    - [Hours trigger interval](#hours-trigger-interval)
    - [Days trigger interval](#days-trigger-interval)
    - [Weeks trigger interval](#weeks-trigger-interval)
    - [Months trigger interval](#months-trigger-interval)
    - [Custom (Cron) interval](#custom-cron-interval)
      - [Examples](#examples)
      - [Why there are six asterisks in the Cron expression](#why-there-are-six-asterisks-in-the-cron-expression)
  - [Templates and examples](#templates-and-examples)
  - [Common issues](#common-issues)

คุณสามารถเพิ่ม **Trigger Rules** ได้หลายอัน เพื่อให้ node ทำงานตามเวลาต่างๆ กัน

ดูรายละเอียดการตั้งค่าแต่ละ **Trigger Interval** ได้ในหัวข้อด้านล่าง และดูตัวอย่างเพิ่มเติมได้ที่ [Templates and examples](#templates-and-examples)

### Seconds trigger interval

* **Seconds Between Triggers**: ใส่จำนวนวินาทีที่ต้องการให้ workflow ทำงานแต่ละครั้ง เช่น ถ้าใส่ `30` trigger จะทำงานทุก 30 วินาที

### Minutes trigger interval

* **Minutes Between Triggers**: ใส่จำนวนนาทีที่ต้องการให้ workflow ทำงานแต่ละครั้ง เช่น ถ้าใส่ `5` trigger จะทำงานทุก 5 นาที

### Hours trigger interval

* **Hours Between Triggers**: ใส่จำนวนชั่วโมงที่ต้องการให้ workflow ทำงานแต่ละครั้ง
* **Trigger at Minute**: ใส่นาทีที่ต้องการให้ trigger ทำงานในแต่ละชั่วโมง (0 ถึง 59)

ตัวอย่างเช่น ถ้าใส่ `6` ใน **Hours Between Triggers** และ `30` ใน **Trigger at Minute** node จะทำงานทุก 6 ชั่วโมงที่นาทีที่ 30 ของชั่วโมงนั้น

### Days trigger interval

* **Days Between Triggers**: ใส่จำนวนวันที่ต้องการให้ workflow ทำงานแต่ละครั้ง
* **Trigger at Hour**: เลือกชั่วโมงที่ต้องการให้ trigger ทำงาน
* **Trigger at Minute**: ใส่นาทีที่ต้องการให้ trigger ทำงานในแต่ละชั่วโมง (0 ถึง 59)

<!-- vale from-microsoft.AMPM = NO -->
ตัวอย่างเช่น ถ้าใส่ `2` ใน **Days Between Triggers**, เลือก **9am** ใน **Trigger at Hour** และใส่ `15` ใน **Trigger at Minute** node จะทำงานทุก 2 วัน เวลา 9:15am
<!-- vale from-microsoft.AMPM = YES -->

### Weeks trigger interval

* **Weeks Between Triggers**: ใส่จำนวนสัปดาห์ที่ต้องการให้ workflow ทำงานแต่ละครั้ง
* **Trigger on Weekdays**: เลือกวันในสัปดาห์ที่ต้องการให้ trigger ทำงาน
* **Trigger at Hour**: เลือกชั่วโมงที่ต้องการให้ trigger ทำงาน
* **Trigger at Minute**: ใส่นาทีที่ต้องการให้ trigger ทำงานในแต่ละชั่วโมง (0 ถึง 59)

ตัวอย่างเช่น ถ้าใส่ `2` ใน **Weeks Between Triggers**, เลือก **Monday** ใน **Trigger on Weekdays**, เลือก **3pm** ใน **Trigger at Hour** และใส่ `30` ใน **Trigger at Minute** node จะทำงานทุก 2 สัปดาห์ในวันจันทร์ เวลา 3:30 PM

### Months trigger interval

* **Months Between Triggers**: ใส่จำนวนเดือนที่ต้องการให้ workflow ทำงานแต่ละครั้ง
* **Trigger at Day of Month**: ใส่วันที่ของเดือนที่ต้องการให้ trigger ทำงาน (1 ถึง 31) ถ้าเดือนนั้นไม่มีวันดังกล่าว node จะไม่ทำงาน เช่น ถ้าใส่ `30` node จะไม่ทำงานในเดือนกุมภาพันธ์
* **Trigger at Hour**: เลือกชั่วโมงที่ต้องการให้ trigger ทำงาน
* **Trigger at Minute**: ใส่นาทีที่ต้องการให้ trigger ทำงานในแต่ละชั่วโมง (0 ถึง 59)

ตัวอย่างเช่น ถ้าใส่ `3` ใน **Months Between Triggers**, ใส่ `28` ใน **Trigger at Day of Month**, เลือก **9am** ใน **Trigger at Hour** และใส่ `0` ใน **Trigger at Minute** node จะทำงานทุกไตรมาสในวันที่ 28 ของเดือน เวลา 9:00 AM

### Custom (Cron) interval

ใส่ custom cron **Expression** เพื่อกำหนดเวลาที่ต้องการให้ trigger ทำงาน

ถ้าต้องการสร้าง Cron expression สามารถใช้ [crontab guru](https://crontab.guru){:target=_blank .external-link} ได้เลย แล้วนำ expression ที่ได้มาใส่ในช่อง **Expression** ใน n8n

#### Examples

<!-- vale from-write-good.Weasel = NO -->
|Type|Cron Expression|Description|
|---|---|---|
|Every X Seconds|`*/10 * * * * *`|ทุก 10 วินาที|
|Every X Minutes|`*/5 * * * *`|ทุก 5 นาที|
|Hourly|`0 * * * *`|ทุกชั่วโมงตรง|
|Daily|`0 6 * * *`|ทุกวันเวลา 6:00 AM|
|Weekly|`0 12 * * 1`|ทุกวันจันทร์เวลาเที่ยงตรง|
|Monthly|`0 0 1 * *`|เที่ยงคืนของวันที่ 1 ของทุกเดือน|
|Every X Days|`0 0 */3 * *`|เที่ยงคืนของทุก 3 วัน|
|Only Weekdays|`0 9 * * 1-5`|ทุกวันจันทร์ถึงศุกร์ เวลา 9:00 AM|
|Custom Hourly Range|`0 9-17 * * *`|ทุกชั่วโมงตั้งแต่ 9:00 AM ถึง 5:00 PM ทุกวัน|
|Quarterly|`0 0 1 1,4,7,10 *`|เที่ยงคืนของวันที่ 1 มกราคม, เมษายน, กรกฎาคม, และตุลาคม|
<!-- vale from-write-good.Weasel = YES -->

/// warning | Using variables in the Cron expression
ถึงจะใช้ตัวแปรใน scheduled trigger ได้ แต่ค่าของตัวแปรจะถูกประเมินแค่ตอนที่ workflow ถูก activate เท่านั้น ถ้าเปลี่ยนค่าตัวแปรใน settings หลังจาก activate แล้ว schedule จะไม่เปลี่ยนตาม ต้อง set workflow เป็น **Inactive** แล้ว activate ใหม่อีกรอบเพื่อให้ค่าตัวแปรถูกนำไปใช้
/// 

#### Why there are six asterisks in the Cron expression

เครื่องหมายดอกจันตัวที่หกใน Cron expression คือค่าของวินาที ซึ่งเป็น optional จะใส่หรือไม่ใส่ก็ได้ node ก็จะทำงานอยู่ดี

|  (*)  |  *  |  *  |  *  |  *  |  *  |
|:--:|:--:|:--:|:--:|:--:|:--:|
|(second)|minute|hour|day of month|month|day of week(Sun-Sat)|

## Templates and examples

<!-- see https://www.notion.so/n8n/Pull-in-templates-for-the-integrations-pages-37c716837b804d30a33b47475f6e3780 -->
[[ templatesWidget(page.title, 'schedule-trigger') ]]

## Common issues

สำหรับคำถามหรือปัญหาที่พบบ่อยและวิธีแก้ไข ดูได้ที่ [Common Issues](/integrations/builtin/core-nodes/n8n-nodes-base.scheduletrigger/common-issues.md)
