---
#https://www.notion.so/n8n/Frontmatter-432c2b8dff1f43d4b1c8d20075510fe4
title: Expressions
contentType: howto
---

# Expressions

Expressions เป็น feature ที่ทรงพลังซึ่งถูกนำไปใช้ใน n8n nodes ทั้งหมด ช่วยให้สามารถตั้งค่าพารามิเตอร์ของ node แบบไดนามิกตามข้อมูลจาก:

- การทำงานของ node ก่อนหน้า
- Workflow
- สภาพแวดล้อม n8n ของคุณ

คุณยังสามารถรัน JavaScript ภายใน expression ได้ ทำให้เป็นวิธีที่สะดวกและง่ายในการจัดการข้อมูลให้เป็นค่าพารามิเตอร์ที่มีประโยชน์โดยไม่ต้องเขียน code เพิ่มเติมมากมาย

n8n สร้างและใช้ภาษา templating ที่เรียกว่า [Tournament](https://github.com/n8n-io/tournament){:target=_blank .external-link} และขยายความสามารถด้วย [custom methods and variables](/code/builtin/overview.md) และ [data transformation functions](/code/builtin/data-transformation-functions/index.md) ฟีเจอร์เหล่านี้ช่วยให้การทำงานทั่วไปง่ายขึ้น เช่น การดึงข้อมูลจาก nodes อื่นๆ หรือการเข้าถึง metadata ของ workflow

นอกจากนี้ n8n ยังรองรับไลบรารีสองตัว:

- [Luxon](https://github.com/moment/luxon/){:target=_blank .external-link}, สำหรับทำงานกับวันที่และเวลา
- [JMESPath](https://jmespath.org/){:target=_blank .external-link}, สำหรับการ query ข้อมูล JSON

/// note | Data in n8n
เมื่อเขียน expressions การทำความเข้าใจโครงสร้างข้อมูลและพฤติกรรมใน n8n จะเป็นประโยชน์ โปรดดู [Data](/data/index.md) สำหรับข้อมูลเพิ่มเติมเกี่ยวกับการทำงานกับข้อมูลใน workflows ของคุณ
///

## Writing expressions

วิธีใช้ expression เพื่อตั้งค่าพารามิเตอร์:

1.  เลื่อนเมาส์ไปเหนือพารามิเตอร์ที่คุณต้องการใช้ expression
2.  เลือก **Expressions** ในตัวสลับ **Fixed/Expression**
3.  เขียน expression ของคุณในพารามิเตอร์ หรือเลือก **Open expression editor** <span class="inline-image">![Open expressions editor icon](/_images/common-icons/open-expression-editor.png){.off-glb}</span> เพื่อเปิด expression editor หากคุณใช้ expression editor คุณสามารถเรียกดูข้อมูลที่มีอยู่ใน **Variable selector** ได้ Expressions ทั้งหมดมีรูปแบบ `{{ your expression here }}`


### Example: Get data from webhook body

พิจารณาสถานการณ์ต่อไปนี้: คุณมี webhook trigger ที่รับข้อมูลผ่าน webhook body คุณต้องการดึงข้อมูลบางส่วนนั้นมาใช้ใน workflow

ข้อมูล webhook ของคุณมีลักษณะคล้ายกับนี้:


```json
[
  {
    "headers": {
      "host": "n8n.instance.address",
      ...
    },
    "params": {},
    "query": {},
    "body": {
      "name": "Jim",
      "age": 30,
      "city": "New York"
    }
  }
]
```


ใน node ถัดไปใน workflow คุณต้องการรับเฉพาะค่าของ `city` คุณสามารถใช้ expression ต่อไปนี้:


```js
{{$json.body.city}}
```

Expression นี้:

1.  เข้าถึงข้อมูลรูปแบบ JSON ที่เข้ามาโดยใช้ตัวแปร `$json` ที่กำหนดเองของ n8n
2.  ค้นหาค่าของ `city` (ในตัวอย่างนี้คือ "New York") โปรดทราบว่าตัวอย่างนี้ใช้ синтаксис JMESPath เพื่อ query ข้อมูล JSON คุณยังสามารถเขียน expression นี้เป็น `{{$json['body']['city']}}` ได้


### Example: Writing longer JavaScript

Expression ประกอบด้วย JavaScript หนึ่งบรรทัด ซึ่งหมายความว่าคุณไม่สามารถทำสิ่งต่างๆ เช่น การกำหนดค่าตัวแปร หรือการดำเนินการแบบสแตนด์อโลนหลายรายการได้

เพื่อให้เข้าใจข้อจำกัดของ JavaScript ใน expressions และเริ่มคิดเกี่ยวกับวิธีแก้ปัญหา ลองดูโค้ดสองตัวอย่างต่อไปนี้ ทั้งสองตัวอย่างใช้ไลบรารีวันที่และเวลา Luxon เพื่อหาเวลาระหว่างวันที่สองวันในหน่วยเดือน และครอบโค้ดด้วยวงเล็บปีกกา เหมือนกับ expression

อย่างไรก็ตาม ตัวอย่างแรกไม่ใช่ expression ที่ถูกต้องของ n8n:

```js
// This example is split over multiple lines for readability
// It's still invalid when formatted as a single line
{{
  function example() {
    let end = DateTime.fromISO('2017-03-13');
    let start = DateTime.fromISO('2017-02-13');
    let diffInMonths = end.diff(start, 'months');
    return diffInMonths.toObject();
  }
  example();
}}
```

ในขณะที่ตัวอย่างที่สองถูกต้อง:

```js
{{DateTime.fromISO('2017-03-13').diff(DateTime.fromISO('2017-02-13'), 'months').toObject()}}
```

## Common issues

สำหรับข้อผิดพลาดหรือปัญหาทั่วไปเกี่ยวกับ expressions และขั้นตอนการแก้ไขที่แนะนำ โปรดดูที่ [Common Issues](/code/cookbook/expressions/common-issues.md)
