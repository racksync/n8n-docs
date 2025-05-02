---
#https://www.notion.so/n8n/Frontmatter-432c2b8dff1f43d4b1c8d20075510fe4
contentType: howto
---

# Check incoming data

บางครั้ง คุณอาจต้องการตรวจสอบข้อมูลขาเข้า หากข้อมูลขาเข้าไม่ตรงกับเงื่อนไข คุณอาจต้องการคืนค่าที่แตกต่างออกไป ตัวอย่างเช่น คุณต้องการตรวจสอบว่าตัวแปรจาก node ก่อนหน้าว่างเปล่าหรือไม่ และคืนค่าเป็นสตริงหากว่างเปล่า ใช้โค้ด snippet ต่อไปนี้เพื่อคืนค่า `not found` หากตัวแปรว่างเปล่า

```javascript
{{$json["variable_name"]? $json["variable_name"] :"not found"}}
```

expression ข้างต้นใช้ ternary operator คุณสามารถเรียนรู้เพิ่มเติมเกี่ยวกับ ternary operator ได้ [here](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Conditional_Operator)

อีกทางเลือกหนึ่ง คุณสามารถใช้ [nullish coalescing operator (??)](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Nullish_coalescing) หรือ [logical or operator (||)](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Logical_OR):

```javascript
{{ $x ?? "default value" }}
{{ $x || "default value" }}
```

ในทั้งสองกรณีข้างต้น ค่าของ `$x` จะถูกใช้หากมีการตั้งค่าเป็นค่าที่ไม่ใช่ null และไม่ใช่ false สตริง `default value` คือค่าสำรอง (fallback value)
