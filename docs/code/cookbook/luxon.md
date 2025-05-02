---
#https://www.notion.so/n8n/Frontmatter-432c2b8dff1f43d4b1c8d20075510fe4
title: Date and time with Luxon
description: Use Luxon to work with date and time in n8n.
contentType: howto
---

# Date and time with Luxon

[Luxon](https://github.com/moment/luxon/){:target=_blank .external-link} เป็นไลบรารี JavaScript ที่ช่วยให้ทำงานกับวันที่และเวลาได้ง่ายขึ้น สำหรับรายละเอียดทั้งหมดเกี่ยวกับวิธีใช้ Luxon โปรดดู [เอกสารของ Luxon](https://moment.github.io/luxon/#/?id=luxon){:target=_blank .external-link}

n8n ส่งผ่านวันที่ระหว่าง nodes เป็นสตริง (strings) ดังนั้นคุณต้องทำการ parse มัน Luxon ทำให้สิ่งนี้ง่ายขึ้น

/// note | Python support
Luxon เป็นไลบรารี JavaScript ตัวแปรอำนวยความสะดวกสองตัว ([variables](#variables)) ที่สร้างโดย n8n มีให้ใช้งานเมื่อใช้ Python ใน Code node แต่ฟังก์ชันการทำงานมีจำกัด:

* คุณไม่สามารถดำเนินการ Luxon กับตัวแปรเหล่านี้ได้ ตัวอย่างเช่น ไม่มี Python ที่เทียบเท่ากับ `$today.minus(...)`
* ฟังก์ชัน Luxon ทั่วไป เช่น [Convert date string to Luxon](#convert-date-string-to-luxon) ไม่สามารถใช้ได้สำหรับผู้ใช้ Python
///	


## Variables

n8n ใช้ Luxon เพื่อให้ตัวแปรที่กำหนดเองสองตัว:

- `now`: ออบเจกต์ Luxon ที่มี timestamp ปัจจุบัน เทียบเท่ากับ `DateTime.now()`
- `today`: ออบเจกต์ Luxon ที่มี timestamp ปัจจุบัน ปัดเศษลงเป็นวัน เทียบเท่ากับ `DateTime.now().set({ hour: 0, minute: 0, second: 0, millisecond: 0 })`

โปรดทราบว่าตัวแปรเหล่านี้สามารถคืนค่ารูปแบบเวลาที่แตกต่างกันเมื่อแปลงเป็นสตริง นี่เป็นพฤติกรรมเดียวกับ `DateTime.now()` ของ Luxon

=== "Expressions (JavaScript)"

	``` js
	{{$now}}
	// n8n แสดง timestamp รูปแบบ ISO
	// ตัวอย่างเช่น 2022-03-09T14:02:37.065+00:00
	{{"Today's date is " + $now}}
	// n8n แสดง "Today's date is <unix timestamp>"
	// ตัวอย่างเช่น "Today's date is 1646834498755"
	```

=== "Code node (JavaScript)"

	``` js
	$now
	// n8n แสดง <ISO formatted timestamp>
	// ตัวอย่างเช่น 2022-03-09T14:00:25.058+00:00
	let rightNow = "Today's date is " + $now
	// n8n แสดง "Today's date is <unix timestamp>"
	// ตัวอย่างเช่น "Today's date is 1646834498755"
	```
=== "Code node (Python)"
	``` python
	_now
	# n8n แสดง <ISO formatted timestamp>
	# ตัวอย่างเช่น 2022-03-09T14:00:25.058+00:00
	rightNow = "Today's date is " + str(_now)
	# n8n แสดง "Today's date is <unix timestamp>"
	# ตัวอย่างเช่น "Today's date is 1646834498755"
	```

n8n มีฟังก์ชันอำนวยความสะดวกในตัวเพื่อรองรับการแปลงข้อมูลใน expressions สำหรับวันที่ โปรดดู [Data transformation functions | Dates](/code/builtin/data-transformation-functions/dates.md) สำหรับข้อมูลเพิ่มเติม

## Date and time behavior in n8n

โปรดระวังสิ่งต่อไปนี้:

* ใน workflow, n8n แปลงวันที่และเวลาเป็นสตริงระหว่าง nodes โปรดจำสิ่งนี้ไว้เมื่อทำการคำนวณทางคณิตศาสตร์กับวันที่และเวลาจาก nodes อื่นๆ
* ด้วย JavaScript ปกติ คุณสามารถแปลงสตริงเป็นวันที่ด้วย `new Date('2019-06-23')` ใน Luxon คุณต้องใช้ฟังก์ชันที่ระบุรูปแบบอย่างชัดเจน เช่น `DateTime.fromISO('2019-06-23')` หรือ `DateTime.fromFormat("23-06-2019", "dd-MM-yyyy")`

## Setting the timezone in n8n

Luxon ใช้ timezone ของ n8n ค่านี้คือ:

* ค่าเริ่มต้น: `America/New York`
* timezone ที่กำหนดเองสำหรับ n8n instance ของคุณ ตั้งค่าโดยใช้ตัวแปรสภาพแวดล้อม `GENERIC_TIMEZONE`
* timezone ที่กำหนดเองสำหรับ workflow แต่ละรายการ กำหนดค่าในการตั้งค่า workflow

## Common tasks

ส่วนนี้ให้ตัวอย่างสำหรับการดำเนินการทั่วไปบางอย่าง ตัวอย่างเพิ่มเติมและคำแนะนำโดยละเอียดมีอยู่ใน [เอกสารของ Luxon เอง](https://moment.github.io/luxon/#/?id=luxon){:target="_blank" .external-link}


### Convert date string to Luxon

คุณสามารถแปลงสตริงวันที่และรูปแบบวันที่อื่นๆ เป็นออบเจกต์ Luxon DateTime ได้ คุณสามารถแปลงจากรูปแบบมาตรฐานและจากสตริงตามอำเภอใจ

/// note | A difference between Luxon DateTime and JavaScript Date
ด้วย JavaScript ปกติ คุณสามารถแปลงสตริงเป็นวันที่ด้วย `new Date('2019-06-23')` ใน Luxon คุณต้องใช้ฟังก์ชันที่ระบุรูปแบบอย่างชัดเจน เช่น `DateTime.fromISO('2019-06-23')` หรือ `DateTime.fromFormat("23-06-2019", "dd-MM-yyyy")`
///
#### If you have a date in a supported standard technical format:

วันที่ส่วนใหญ่ใช้ `fromISO()` สิ่งนี้สร้าง Luxon DateTime จากสตริง ISO 8601 ตัวอย่างเช่น:

=== "Expressions (JavaScript)"

	```js
	{{DateTime.fromISO('2019-06-23T00:00:00.00')}}
	```

=== "Code node (JavaScript)"

	```js
	let luxonDateTime = DateTime.fromISO('2019-06-23T00:00:00.00')
	```


เอกสาร API ของ Luxon มีข้อมูลเพิ่มเติมเกี่ยวกับ [fromISO](https://moment.github.io/luxon/api-docs/index.html#datetimefromiso){:target="_blank" .external-link}

Luxon มีฟังก์ชันเพื่อจัดการการแปลงสำหรับรูปแบบต่างๆ โปรดดูคู่มือของ Luxon เกี่ยวกับ [Parsing technical formats](https://moment.github.io/luxon/#/parsing?id=parsing-technical-formats) สำหรับรายละเอียด

#### If you have a date as a string that doesn't use a standard format:

ใช้ [Ad-hoc parsing](https://moment.github.io/luxon/#/parsing?id=ad-hoc-parsing){:target="_blank" .external-link} ของ Luxon ในการทำเช่นนี้ ให้ใช้ฟังก์ชัน `fromFormat()` โดยระบุสตริงและชุดของ [tokens](https://moment.github.io/luxon/#/parsing?id=table-of-tokens){:target="_blank" .external-link} ที่อธิบายรูปแบบ

ตัวอย่างเช่น คุณมีวันก่อตั้ง n8n คือ 23 มิถุนายน 2019 จัดรูปแบบเป็น `23-06-2019` คุณต้องการเปลี่ยนสิ่งนี้เป็นออบเจกต์ Luxon:

=== "Expressions (JavaScript)"

	```js
	{{DateTime.fromFormat("23-06-2019", "dd-MM-yyyy")}}
	```

=== "Code node (JavaScript)"

	```js
	let newFormat = DateTime.fromFormat("23-06-2019", "dd-MM-yyyy")
	```

เมื่อใช้ ad-hoc parsing โปรดทราบคำเตือนของ Luxon เกี่ยวกับ [Limitations](https://moment.github.io/luxon/#/parsing?id=limitations){:target="_blank" .external-link} หากคุณเห็นผลลัพธ์ที่ไม่คาดคิด ลองดูคู่มือ [Debugging](https://moment.github.io/luxon/#/parsing?id=debugging){:target="_blank" .external-link} ของพวกเขา

### Get n days from today

รับจำนวนวันก่อนหรือหลังวันนี้

=== "Expressions (JavaScript)"

	ตัวอย่างเช่น คุณต้องการตั้งค่าฟิลด์ให้แสดงวันที่เจ็ดวันก่อนวันที่ปัจจุบันเสมอ

	ใน expression editor ป้อน:


	``` js
	{{$today.minus({days: 7})}}
	```

	ในวันที่ 23 มิถุนายน 2019 สิ่งนี้จะคืนค่า `[Object: "2019-06-16T00:00:00.000+00:00"]`

	ตัวอย่างนี้ใช้ตัวแปร `$today` ที่กำหนดเองของ n8n เพื่อความสะดวก เทียบเท่ากับ `DateTime.now().set({ hour: 0, minute: 0, second: 0, millisecond: 0 }).minus({days: 7})`

=== "Code node (JavaScript)"

	ตัวอย่างเช่น คุณต้องการตัวแปรที่มีวันที่เจ็ดวันก่อนวันที่ปัจจุบัน

	ใน code editor ป้อน:

	``` js
	let sevenDaysAgo = $today.minus({days: 7})
	```

	ในวันที่ 23 มิถุนายน 2019 สิ่งนี้จะคืนค่า `[Object: "2019-06-16T00:00:00.000+00:00"]`

	ตัวอย่างนี้ใช้ตัวแปร `$today` ที่กำหนดเองของ n8n เพื่อความสะดวก เทียบเท่ากับ `DateTime.now().set({ hour: 0, minute: 0, second: 0, millisecond: 0 }).minus({days: 7})`

สำหรับข้อมูลและตัวอย่างโดยละเอียดเพิ่มเติม โปรดดู:

* คู่มือของ Luxon เกี่ยวกับ [math](https://moment.github.io/luxon/#/math)
* เอกสาร API ของพวกเขาเกี่ยวกับ [DateTime plus](https://moment.github.io/luxon/api-docs/index.html#datetimeplus) และ [DateTime minus](https://moment.github.io/luxon/api-docs/index.html#datetimeminus)

### Create human-readable dates

ใน [Get n days from today](#get-n-days-from-today) ตัวอย่างจะรับวันที่เจ็ดวันก่อนวันที่ปัจจุบัน และคืนค่าเป็น `[Object: "yyyy-mm-dd-T00:00:00.000+00:00"]` (สำหรับ expressions) หรือ `yyyy-mm-dd-T00:00:00.000+00:00` (ใน Code node) เพื่อทำให้อ่านง่ายขึ้น คุณสามารถใช้ฟังก์ชันการจัดรูปแบบของ Luxon ได้

ตัวอย่างเช่น คุณต้องการให้ฟิลด์ที่มีวันที่ถูกจัดรูปแบบเป็น DD/MM/YYYY เพื่อที่ในวันที่ 23 มิถุนายน 2019 จะคืนค่า `23/06/2019`

expression นี้จะรับวันที่เจ็ดวันก่อนวันนี้ และแปลงเป็นรูปแบบ DD/MM/YYYY

=== "Expressions (JavaScript)"

	```js
	{{$today.minus({days: 7}).toLocaleString()}}
	```

=== "Code node (JavaScript)"

	```js
	let readableSevenDaysAgo = $today.minus({days: 7}).toLocaleString()
	```

คุณสามารถเปลี่ยนรูปแบบได้ ตัวอย่างเช่น:

=== "Expressions (JavaScript)"

	```js
	{{$today.minus({days: 7}).toLocaleString({month: 'long', day: 'numeric', year: 'numeric'})}}
	```

	ในวันที่ 23 มิถุนายน 2019 สิ่งนี้จะคืนค่า "16 June 2019"

=== "Code node (JavaScript)"

	```js
	let readableSevenDaysAgo = $today.minus({days: 7}).toLocaleString({month: 'long', day: 'numeric', year: 'numeric'})
	```

	ในวันที่ 23 มิถุนายน 2019 สิ่งนี้จะคืนค่า "16 June 2019"

โปรดดูคู่มือของ Luxon เกี่ยวกับ [toLocaleString (strings for humans)](https://moment.github.io/luxon/#/formatting?id=tolocalestring-strings-for-humans){:target="_blank" .external-link} สำหรับข้อมูลเพิ่มเติม


### Get the time between two dates

หากต้องการรับเวลาระหว่างวันที่สองวัน ให้ใช้ฟีเจอร์ diffs ของ Luxon สิ่งนี้จะลบวันที่หนึ่งออกจากอีกวันหนึ่งและคืนค่า duration

ตัวอย่างเช่น รับจำนวนเดือนระหว่างวันที่สองวัน:

=== "Expressions (JavaScript)"

	```js
	{{DateTime.fromISO('2019-06-23').diff(DateTime.fromISO('2019-05-23'), 'months').toObject()}}
	```

	สิ่งนี้จะคืนค่า `[Object: {"months":1}]`

=== "Code node (JavaScript)"

	```js
	let monthsBetweenDates = DateTime.fromISO('2019-06-23').diff(DateTime.fromISO('2019-05-23'), 'months').toObject()
	```

	สิ่งนี้จะคืนค่า `{"months":1}`

โปรดดู [Diffs](https://moment.github.io/luxon/#/math?id=diffs){:target=_blank .external-link} ของ Luxon สำหรับข้อมูลเพิ่มเติม

### A longer example: How many days to Christmas?

ตัวอย่างนี้นำฟีเจอร์ Luxon หลายอย่างมารวมกัน ใช้ JMESPath และทำการจัดการสตริงพื้นฐานบางอย่าง

สถานการณ์: คุณต้องการนับถอยหลังสู่วันที่ 25 ธันวาคม ทุกวัน มันควรจะบอกคุณถึงจำนวนวันที่เหลือถึงวันคริสต์มาส คุณไม่ต้องการอัปเดตสำหรับปีหน้า - มันต้องทำงานได้อย่างราบรื่นสำหรับทุกปี

=== "Expressions (JavaScript)"

	```js
	{{"There are " + $today.diff(DateTime.fromISO($today.year + '-12-25'), 'days').toObject().days.toString().substring(1) + " days to Christmas!"}}
	```

	สิ่งนี้จะแสดงผล `"There are <number of days> days to Christmas!"` ตัวอย่างเช่น ในวันที่ 9 มีนาคม จะแสดงผล "There are 291 days to Christmas!"

	คำอธิบายโดยละเอียดว่า expression ทำอะไร:

	* `{{`: บ่งชี้จุดเริ่มต้นของ expression
	* `"There are "`: สตริง
	* `+`: ใช้เพื่อเชื่อมสองสตริง
	* `$today.diff()`: คล้ายกับตัวอย่างใน [Get the time between two dates](#get-the-time-between-two-dates) แต่ใช้ตัวแปร `$today` ที่กำหนดเองของ n8n
	* `DateTime.fromISO($today.year + '-12-25'), 'days'`: ส่วนนี้รับปีปัจจุบันโดยใช้ `$today.year` เปลี่ยนเป็นสตริง ISO พร้อมกับเดือนและวันที่ จากนั้นนำสตริง ISO ทั้งหมดมาแปลงเป็นโครงสร้างข้อมูล Luxon DateTime นอกจากนี้ยังบอก Luxon ว่าคุณต้องการ duration เป็นวัน
	* `toObject()` เปลี่ยนผลลัพธ์ของ diff() เป็นออบเจกต์ที่ใช้งานได้ง่ายขึ้น ณ จุดนี้ expression จะคืนค่า `[Object: {"days":-<number-of-days>}]` ตัวอย่างเช่น ในวันที่ 9 มีนาคม `[Object: {"days":-291}]`
	* `.days` ใช้ синтаксис JMESPath เพื่อดึงเฉพาะจำนวนวันจากออบเจกต์ สำหรับข้อมูลเพิ่มเติมเกี่ยวกับการใช้ JMESPath กับ n8n โปรดดูเอกสาร [JMESpath](/code/cookbook/jmespath.md) ของเรา สิ่งนี้ให้จำนวนวันถึงคริสต์มาส เป็นจำนวนลบ
	* `.toString().substring(1)` เปลี่ยนตัวเลขเป็นสตริงและลบเครื่องหมาย `-` ออก
	* `+ " days to Christmas!"`: สตริงอีกอัน พร้อมเครื่องหมาย `+` เพื่อเชื่อมกับสตริงก่อนหน้า
	* `}}`: บ่งชี้จุดสิ้นสุดของ expression

=== "Code node (JavaScript)"

	```js
	let daysToChristmas = "There are " + $today.diff(DateTime.fromISO($today.year + '-12-25'), 'days').toObject().days.toString().substring(1) + " days to Christmas!";
	```

	สิ่งนี้จะแสดงผล `"There are <number of days> days to Christmas!"` ตัวอย่างเช่น ในวันที่ 9 มีนาคม จะแสดงผล "There are 291 days to Christmas!"

	คำอธิบายโดยละเอียดว่าโค้ดทำอะไร:

	* `"There are "`: สตริง
	* `+`: ใช้เพื่อเชื่อมสองสตริง
	* `$today.diff()`: คล้ายกับตัวอย่างใน [Get the time between two dates](#get-the-time-between-two-dates) แต่ใช้ตัวแปร `$today` ที่กำหนดเองของ n8n
	* `DateTime.fromISO($today.year + '-12-25'), 'days'`: ส่วนนี้รับปีปัจจุบันโดยใช้ `$today.year` เปลี่ยนเป็นสตริง ISO พร้อมกับเดือนและวันที่ จากนั้นนำสตริง ISO ทั้งหมดมาแปลงเป็นโครงสร้างข้อมูล Luxon DateTime นอกจากนี้ยังบอก Luxon ว่าคุณต้องการ duration เป็นวัน
	* `toObject()` เปลี่ยนผลลัพธ์ของ diff() เป็นออบเจกต์ที่ใช้งานได้ง่ายขึ้น ณ จุดนี้ expression จะคืนค่า `[Object: {"days":-<number-of-days>}]` ตัวอย่างเช่น ในวันที่ 9 มีนาคม `[Object: {"days":-291}]`
	* `.days` ใช้ синтаксис JMESPath เพื่อดึงเฉพาะจำนวนวันจากออบเจกต์ สำหรับข้อมูลเพิ่มเติมเกี่ยวกับการใช้ JMESPath กับ n8n โปรดดูเอกสาร [JMESpath](/code/cookbook/jmespath.md) ของเรา สิ่งนี้ให้จำนวนวันถึงคริสต์มาส เป็นจำนวนลบ
	* `.toString().substring(1)` เปลี่ยนตัวเลขเป็นสตริงและลบเครื่องหมาย `-` ออก
	* `+ " days to Christmas!"`: สตริงอีกอัน พร้อมเครื่องหมาย `+` เพื่อเชื่อมกับสตริงก่อนหน้า
