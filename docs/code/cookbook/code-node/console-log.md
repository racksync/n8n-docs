---
#https://www.notion.so/n8n/Frontmatter-432c2b8dff1f43d4b1c8d20075510fe4
description: วิธีใช้ console.log() หรือ print()
contentType: howto
---

# Output to the browser console with `console.log()` or `print()` in the Code node

คุณสามารถใช้ `console.log()` หรือ `print()` ใน Code node เพื่อช่วยในการเขียนและดีบักโค้ดของคุณ

สำหรับความช่วยเหลือในการเปิด browser console ของคุณ โปรดอ้างอิง [this guide by Balsamiq](https://balsamiq.com/support/faqs/browserconsole/){:target=_blank .external-link}

## console.log (JavaScript)

สำหรับข้อมูลทางเทคนิคเกี่ยวกับ `console.log()` โปรดอ้างอิง [MDN developer docs](https://developer.mozilla.org/en-US/docs/Web/API/Console/log){:target=_blank .external-link}

ตัวอย่างเช่น คัดลอกโค้ดต่อไปนี้ลงใน Code node จากนั้นเปิด console ของคุณและรัน node:

```js
let a = "apple";
console.log(a);
```

## print (Python)

สำหรับข้อมูลทางเทคนิคเกี่ยวกับ `print()` โปรดอ้างอิง [Real Python's guide](https://realpython.com/python-print/){:target=_blank .external-link}

ตัวอย่างเช่น ตั้งค่า **Language** ของ Code node เป็น **Python**, คัดลอกโค้ดต่อไปนี้ลงใน node จากนั้นเปิด console ของคุณและรัน node:

```python
a = "apple"
print(a)
```

### Handling an output of `[object Object]`

หาก console แสดง `[object Object]` เมื่อคุณ print ให้ตรวจสอบชนิดข้อมูล (data type) จากนั้นแปลงตามความจำเป็น

ในการตรวจสอบชนิดข้อมูล:

```python
print(type(myData))
```

#### JsProxy

หาก `type()` แสดงผลลัพธ์เป็น `<class 'pyodide.ffi.JsProxy'>` คุณต้องแปลง JsProxy เป็น object ของ Python โดยใช้ `to_py()` สิ่งนี้เกิดขึ้นเมื่อทำงานกับข้อมูลในโครงสร้างข้อมูลของ node n8n เช่น input และ output ของ node ตัวอย่างเช่น หากคุณต้องการ print ข้อมูลจาก node ก่อนหน้าใน workflow:

```python
previousNodeData = _("<node-name>").all();
for item in previousNodeData:
	# item is of type <class 'pyodide.ffi.JsProxy'>
	# You need to convert it to a Dict
	itemDict = item.json.to_py()
	print(itemDict)
```

อ้างอิงเอกสาร Pyodide เกี่ยวกับ [JsProxy](https://pyodide.org/en/stable/usage/api/python-api/ffi.html#pyodide.ffi.JsProxy){:target=_blank .external-link} สำหรับข้อมูลเพิ่มเติมเกี่ยวกับ class นี้








