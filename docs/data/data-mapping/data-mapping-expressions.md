---
#https://www.notion.so/n8n/Frontmatter-432c2b8dff1f43d4b1c8d20075510fe4
contentType: howto
---

# Mapping in the expressions editor

ตัวอย่างเหล่านี้แสดงวิธีการเข้าถึง linked item ใน expressions editor โปรดดู [expressions](/code/expressions.md) สำหรับข้อมูลเพิ่มเติมเกี่ยวกับ expressions รวมถึงตัวแปรและ method ที่มีอยู่แล้ว (built-in)

สำหรับข้อมูลเกี่ยวกับข้อผิดพลาดในการ map และการ link item โปรดดูที่ [Item linking errors](/data/data-mapping/data-item-linking/item-linking-errors.md)

## Access the linked item in a previous node's output

เมื่อคุณใช้สิ่งนี้ n8n จะทำงานย้อนกลับไปตามสายโซ่ของ item linking เพื่อค้นหา parent item ใน node ที่ระบุ

```js
// Returns the linked item
{{$("<node-name>").item}}
```

ตัวอย่างที่ยาวขึ้น ลองพิจารณาสถานการณ์ที่ node ก่อนหน้าใน workflow มีข้อมูล output ดังนี้:

```json
[
  {
    "id": "23423532",
    "name": "Jay Gatsby",
  },
  {
    "id": "23423533",
    "name": "José Arcadio Buendía",
  },
  {
    "id": "23423534",
    "name": "Max Sendak",
  },
  {
    "id": "23423535",
    "name": "Zaphod Beeblebrox",
  },
  {
    "id": "23423536",
    "name": "Edmund Pevensie",
  }
]
```

ในการดึงชื่อออกมา ให้ใช้ expression ต่อไปนี้:

```js
{{$("<node-name>").item.json.name}}
```

### Access the linked item in the current node's input

ในกรณีนี้ item linking จะอยู่ภายใน node: ค้นหา input item ที่ node link ไปยัง output item

```js
// Returns the linked item
{{$input.item}}
```

ตัวอย่างที่ยาวขึ้น ลองพิจารณาสถานการณ์ที่ node ปัจจุบันมีข้อมูล input ดังนี้:

```json
[
  {
    "id": "23423532",
    "name": "Jay Gatsby",
  },
  {
    "id": "23423533",
    "name": "José Arcadio Buendía",
  },
  {
    "id": "23423534",
    "name": "Max Sendak",
  },
  {
    "id": "23423535",
    "name": "Zaphod Beeblebrox",
  },
  {
    "id": "23423536",
    "name": "Edmund Pevensie",
  }
]
```

ในการดึงชื่อออกมา ปกติคุณจะใช้การลากและวาง [Data mapping](/data/data-mapping/index.md) แต่คุณก็สามารถเขียน expression ต่อไปนี้ได้เช่นกัน:

```js
{{$input.item.json.name}}
```
