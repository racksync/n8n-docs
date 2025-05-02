---
#https://www.notion.so/n8n/Frontmatter-432c2b8dff1f43d4b1c8d20075510fe4
contentType: howto
---

# Mapping in the UI

Data mapping หมายถึงการอ้างอิงข้อมูลจาก node ก่อนหน้า ไม่รวมถึงการเปลี่ยนแปลง (transform) ข้อมูล เป็นเพียงการอ้างอิงเท่านั้น

คุณสามารถ map ข้อมูลได้ด้วยวิธีต่อไปนี้:

* การใช้ expressions editor
* โดยการลากและวางข้อมูลจาก **INPUT** ไปยัง parameters วิธีนี้จะสร้าง expression ให้คุณโดยอัตโนมัติ

สำหรับข้อมูลเกี่ยวกับข้อผิดพลาดในการ map และการ link item โปรดดูที่ [Item linking errors](/data/data-mapping/data-item-linking/item-linking-errors.md)

## How to drag and drop data

1.  Run workflow ของคุณเพื่อโหลดข้อมูล
2.  เปิด node ที่คุณต้องการ map ข้อมูล
3.  คุณสามารถ map ในมุมมอง table, JSON และ schema:
    *   ในมุมมอง table: คลิกค้างที่หัวตารางเพื่อ map ข้อมูลระดับบนสุด หรือคลิกค้างที่ field ในตารางเพื่อ map ข้อมูลที่ซ้อนกัน (nested data)
    *   ในมุมมอง JSON: คลิกค้างที่ key
    *   ในมุมมอง schema: คลิกค้างที่ key
4.  ลาก item ไปยัง field ที่คุณต้องการใช้ข้อมูล

### Understand what you're mapping with drag and drop

Data mapping จะ map เส้นทางของ key (key path) และโหลดค่าของ key นั้นไปยัง field ตัวอย่างเช่น หากมีข้อมูลดังต่อไปนี้:

```js
[
	{
		"fruit": "apples",
		"color": "green"
	}
]
```

คุณสามารถ map `fruit` โดยการลากและวาง **fruit** จาก **INPUT** ไปยัง field ที่คุณต้องการใช้ค่าของมัน การทำเช่นนี้จะสร้าง expression `{{ $json.fruit }}` ขึ้นมา เมื่อ node วนซ้ำ (iterate) ผ่าน input item ค่าของ field จะกลายเป็นค่าของ `fruit` สำหรับแต่ละ item

### Understand nested data

หากมีข้อมูลดังต่อไปนี้:

```js
[
  {
    "name": "First item",
    "nested": {
      "example-number-field": 1,
      "example-string-field": "apples"
    }
  },
  {
    "name": "Second item",
    "nested": {
      "example-number-field": 2,
      "example-string-field": "oranges"
    }
  }
]
```

n8n จะแสดงข้อมูลในรูปแบบตารางดังนี้:

!["Screenshot of a table in the INPUT panel. It includes a top level field named "nested." This field contains nested data, which is indicated in bold."](/_images/data/data-mapping/nested-data.png)

