### โหมด Every Hour (Every Hour mode)

ป้อน **Minute** ของชั่วโมงเพื่อเริ่มการ poll ตั้งแต่ `0` ถึง `59`

### โหมด Every Day (Every Day mode)

*   ป้อน **Hour** ของวันเพื่อเริ่มการ poll ในรูปแบบ 24 ชั่วโมง ตั้งแต่ `0` ถึง `23`
*   ป้อน **Minute** ของชั่วโมงเพื่อเริ่มการ poll ตั้งแต่ `0` ถึง `59`

### โหมด Every Week (Every Week mode)

*   ป้อน **Hour** ของวันเพื่อเริ่มการ poll ในรูปแบบ 24 ชั่วโมง ตั้งแต่ `0` ถึง `23`
*   ป้อน **Minute** ของชั่วโมงเพื่อเริ่มการ poll ตั้งแต่ `0` ถึง `59`
*   เลือก **Weekday** เพื่อเริ่มการ poll

### โหมด Every Month (Every Month mode)

*   ป้อน **Hour** ของวันเพื่อเริ่มการ poll ในรูปแบบ 24 ชั่วโมง ตั้งแต่ `0` ถึง `23`
*   ป้อน **Minute** ของชั่วโมงเพื่อเริ่มการ poll ตั้งแต่ `0` ถึง `59`
*   ป้อน **Day of the Month** เพื่อเริ่มการ poll ตั้งแต่ `0` ถึง `31`

### โหมด Every X (Every X mode)

*   ป้อน **Value** ของการวัดความถี่ในการเริ่มการ poll เป็นนาทีหรือชั่วโมง
*   เลือก **Unit** สำหรับค่า หน่วยที่รองรับคือ **Minutes** และ **Hours**

### โหมด Custom (Custom mode)

ป้อน **Cron Expression** ที่กำหนดเองเพื่อเริ่มการ poll ใช้ค่าและช่วงเหล่านี้:

*   Seconds: `0` - `59`
*   Minutes: `0` - `59`
*   Hours: `0` - `23`
*   Day of Month: `1` - `31`
*   Months: `0` - `11` (Jan - Dec)
*   Day of Week: `0` - `6` (Sun - Sat)

ในการสร้าง Cron expression คุณสามารถใช้ [crontab guru](https://crontab.guru){:target=_blank .external-link} คัดลอก Cron expression ที่คุณสร้างโดยใช้ crontab guru ไปวางในช่อง **Cron Expression** ใน n8n

#### ตัวอย่าง (Examples)

หากคุณต้องการเริ่ม workflow ทุกวันเวลา 04:08:30 ให้ป้อนข้อมูลต่อไปนี้ในช่อง **Cron Expression**
```
30 8 4 * * *
```

หากคุณต้องการเริ่ม workflow ทุกวันเวลา 04:08 ให้ป้อนข้อมูลต่อไปนี้ในช่อง **Cron Expression**
```
8 4 * * *
```

#### ทำไมถึงมีเครื่องหมายดอกจันหกตัวใน Cron expression (Why there are six asterisks in the Cron expression)

เครื่องหมายดอกจันตัวที่หกใน Cron expression แทนวินาที การตั้งค่านี้เป็นทางเลือก Node จะทำงานแม้ว่าคุณจะไม่ได้ตั้งค่าวินาทีก็ตาม

|  *  |  *  |  *  |  *  |  *  |  *  |
|:--:|:--:|:--:|:--:|:--:|:--:|
|second|minute|hour|day of month|month|day of week|