---
#https://www.notion.so/n8n/Frontmatter-432c2b8dff1f43d4b1c8d20075510fe4
title: Edit Fields (Set)
description: Documentation for the Edit Fields node in n8n, a workflow automation platform. Includes guidance on usage, and links to examples.
contentType: [integration, reference]
priority: critical
---

# Edit Fields (Set)

ใช้ Edit Fields node เพื่อเซ็ตข้อมูลใน workflow ของคุณ สามารถใช้ node นี้เพื่อเพิ่มข้อมูลใหม่หรือเขียนทับข้อมูลที่มีอยู่แล้วก็ได้ Node นี้สำคัญมากใน workflow ที่ต้องรับข้อมูลจาก node ก่อนหน้า เช่นเวลาจะ insert ข้อมูลไปยัง Google Sheets หรือ database

## Node parameters

นี่คือการตั้งค่าและ options ที่มีใน Edit Fields node

### Mode

คุณสามารถเลือกใช้ **Manual Mapping** เพื่อแก้ไข fields ผ่าน GUI หรือ **JSON Output** เพื่อเขียน JSON ที่ n8n จะเพิ่มเข้าไปใน input data

### Fields to Set

ถ้าเลือก **Mode** > **Manual Mapping** คุณสามารถตั้งค่า fields ได้โดยลากและวางค่าจาก **INPUT**

พฤติกรรมปกติเมื่อคุณลากค่า:

* n8n จะตั้งชื่อ field ตามชื่อของ value ที่ลากมา
* ค่า field จะเป็น expression ที่เข้าถึง value นั้น

ถ้าไม่อยากใช้ expressions:

1. เอา mouse ไปวางเหนือ field ที่ต้องการ n8n จะแสดง toggle **Fixed | Expressions**
1. เลือก **Fixed**

คุณสามารถทำแบบนี้ได้ทั้งกับชื่อ field และค่าของ field

![A gif showing the drag and drop action, as well as changing a field to fixed](/_images/integrations/builtin/core-nodes/set/drag-drop-fixed-toggle.gif)

### Keep Only Set Fields

เปิด option นี้ถ้าอยากให้ node ตัดข้อมูล input อื่น ๆ ที่ไม่ได้ใช้ใน **Fields to Set** ออก

### Include in Output

เลือกข้อมูล input ที่จะรวมไว้ใน output ของ node นี้

## Node options

ใช้ options เหล่านี้เพื่อปรับแต่งพฤติกรรมของ node

### Include Binary Data

ถ้า input data มี binary data อยู่ สามารถเลือกได้ว่าจะรวม binary data นี้ไว้ใน output ของ Edit Fields node หรือไม่

### Ignore Type Conversion Errors

ใช้ได้เฉพาะ Manual Mapping

ถ้าเปิด option นี้ n8n จะข้าม error บางอย่างที่เกี่ยวกับการแปลงชนิดข้อมูลเวลาทำ mapping fields

### Support Dot Notation

โดยปกติ n8n จะรองรับ dot notation

เช่น ถ้าใช้ manual mapping แล้วตั้งชื่อ field ใน **Name** ว่า `number.one` และค่าใน **Value** เป็น `20` JSON ที่ได้จะเป็นแบบนี้:

```json
{ "number": { "one": 20} }
```

ถ้าไม่อยากให้เป็นแบบนี้ ให้เลือก **Add Option** > **Support Dot Notation** แล้วปิด **Dot Notion** ผลลัพธ์จะเป็น:

```json
{ "number.one": 20 }
```
## Templates and examples

<!-- see https://www.notion.so/n8n/Pull-in-templates-for-the-integrations-pages-37c716837b804d30a33b47475f6e3780 -->
[[ templatesWidget(page.title, 'set') ]]

## Arrays and expressions in JSON Output mode

คุณสามารถใช้ array และ expression ตอนสร้าง JSON Output ได้

ตัวอย่างเช่น ถ้ามี input data จาก Customer Datastore node แบบนี้:

```json
[
  {
    "id": "23423532",
    "name": "Jay Gatsby",
    "email": "gatsby@west-egg.com",
    "notes": "Keeps asking about a green light??",
    "country": "US",
    "created": "1925-04-10"
  },
  {
    "id": "23423533",
    "name": "José Arcadio Buendía",
    "email": "jab@macondo.co",
    "notes": "Lots of people named after him. Very confusing",
    "country": "CO",
    "created": "1967-05-05"
  },
  {
    "id": "23423534",
    "name": "Max Sendak",
    "email": "info@in-and-out-of-weeks.org",
    "notes": "Keeps rolling his terrible eyes",
    "country": "US",
    "created": "1963-04-09"
  },
  {
    "id": "23423535",
    "name": "Zaphod Beeblebrox",
    "email": "captain@heartofgold.com",
    "notes": "Felt like I was talking to more than one person",
    "country": null,
    "created": "1979-10-12"
  },
  {
    "id": "23423536",
    "name": "Edmund Pevensie",
    "email": "edmund@narnia.gov",
    "notes": "Passionate sailor",
    "country": "UK",
    "created": "1950-10-16"
  }
]
```

เพิ่ม JSON นี้ใน **JSON Output** field พร้อมตั้ง **Include in Output** เป็น **All Input Fields**:

```json
{
  "newKey": "new value",
  "array": [{{ $json.id }},"{{ $json.name }}"],
  "object": {
    "innerKey1": "new value",
    "innerKey2": "{{ $json.id }}",
    "innerKey3": "{{ $json.name }}",
 }
}
```

คุณจะได้ output แบบนี้:

```json
[
  {
    "id": "23423532",
    "name": "Jay Gatsby",
    "email": "gatsby@west-egg.com",
    "notes": "Keeps asking about a green light??",
    "country": "US",
    "created": "1925-04-10",
    "newKey": "new value",
    "array": [
      23423532,
      "Jay Gatsby"
    ],
    "object": {
      "innerKey1": "new value",
      "innerKey2": "23423532",
      "innerKey3": "Jay Gatsby"
    }
  },
  {
    "id": "23423533",
    "name": "José Arcadio Buendía",
    "email": "jab@macondo.co",
    "notes": "Lots of people named after him. Very confusing",
    "country": "CO",
    "created": "1967-05-05",
    "newKey": "new value",
    "array": [
      23423533,
      "José Arcadio Buendía"
    ],
    "object": {
      "innerKey1": "new value",
      "innerKey2": "23423533",
      "innerKey3": "José Arcadio Buendía"
    }
  },
  {
    "id": "23423534",
    "name": "Max Sendak",
    "email": "info@in-and-out-of-weeks.org",
    "notes": "Keeps rolling his terrible eyes",
    "country": "US",
    "created": "1963-04-09",
    "newKey": "new value",
    "array": [
      23423534,
      "Max Sendak"
    ],
    "object": {
      "innerKey1": "new value",
      "innerKey2": "23423534",
      "innerKey3": "Max Sendak"
    }
  },
  {
    "id": "23423535",
    "name": "Zaphod Beeblebrox",
    "email": "captain@heartofgold.com",
    "notes": "Felt like I was talking to more than one person",
    "country": null,
    "created": "1979-10-12",
    "newKey": "new value",
    "array": [
      23423535,
      "Zaphod Beeblebrox"
    ],
    "object": {
      "innerKey1": "new value",
      "innerKey2": "23423535",
      "innerKey3": "Zaphod Beeblebrox"
    }
  },
  {
    "id": "23423536",
    "name": "Edmund Pevensie",
    "email": "edmund@narnia.gov",
    "notes": "Passionate sailor",
    "country": "UK",
    "created": "1950-10-16",
    "newKey": "new value",
    "array": [
      23423536,
      "Edmund Pevensie"
    ],
    "object": {
      "innerKey1": "new value",
      "innerKey2": "23423536",
      "innerKey3": "Edmund Pevensie"
    }
  }
]
```




