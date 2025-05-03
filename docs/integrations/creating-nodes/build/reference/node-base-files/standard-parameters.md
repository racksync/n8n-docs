---
#https://www.notion.so/n8n/Frontmatter-432c2b8dff1f43d4b1c8d20075510fe4
title: พารามิเตอร์มาตรฐาน
description: เอกสารอ้างอิงรายการพารามิเตอร์มาตรฐานของ node base file
contentType: reference
---

# Standard parameters

นี่คือ parameters มาตรฐานสำหรับ [node base file](/integrations/creating-nodes/build/reference/node-base-files/index.md) ซึ่งใช้เหมือนกันกับ node ทุกประเภท

## `displayName`

_String_ | _Required_

ชื่อนี้จะแสดงให้ผู้ใช้เห็นใน GUI ของ n8n

## `name`

_String_ | _Required_

ชื่อภายในของ object ใช้สำหรับอ้างอิงจากที่อื่นใน node

## `icon`

_String_ หรือ _Object_ | _Required_

กำหนด icon สำหรับ node นั้น ๆ แนะนำให้อัปโหลดไฟล์ภาพของตัวเอง

สามารถใส่ชื่อไฟล์ icon เป็น string หรือเป็น object เพื่อรองรับทั้ง light และ dark mode
ถ้า icon ใช้ได้ทั้งสองโหมด ให้ใช้ string ที่ขึ้นต้นด้วย `file:` เพื่อบอก path ของไฟล์ icon เช่น

```
icon: 'file:exampleNodeIcon.svg'
```
ถ้าต้องการแยก icon สำหรับ light/dark mode ให้ใช้ object แบบนี้:
```
icon: { 
  light: 'file:exampleNodeIcon.svg', 
  dark: 'file:exampleNodeIcon.dark.svg' 
}
```

--8<-- "_snippets/integrations/creating-nodes/node-icons.md"

## `group`

_Array of strings_ | _Required_

บอก n8n ว่า node นี้ทำงานแบบไหนตอน workflow รัน ตัวเลือกมีดังนี้:

* `trigger`: node จะรอ event trigger
* `schedule`: node จะรอ timer หมดเวลา
* `input`, `output`, `transform`: ตอนนี้ยังไม่มีผล
* ถ้าไม่ต้องการ trigger หรือ schedule ให้ใช้ array ว่าง `[]` เป็นค่า default

## `description`

_String_ | _Required_

คำอธิบายสั้น ๆ ของ node ซึ่งจะแสดงใน GUI ของ n8n

## `defaults`

_Object_ | _Required_

เก็บค่าต่าง ๆ ที่จำเป็นเกี่ยวกับ brand และชื่อ

object นี้จะมี:

* `name`: String. ใช้เป็นชื่อ node บน canvas ถ้า `displayName` ยาวเกินไป
* `color`: String. รหัสสี Hex ใส่สีประจำแบรนด์ของ integration เพื่อใช้ใน n8n

## `forceInputNodeExecution`

_Boolean_ | _Optional_

ถ้าสร้าง node ที่มีหลาย input สามารถเลือกได้ว่าจะให้ node ก่อนหน้าทุก branch ต้อง execute ก่อน node นี้จะรันหรือไม่ ค่า default คือ `false` (แค่ branch เดียวรันก็พอ)

## `inputs`

_Array of strings_ | _Required_

ตั้งชื่อ input connectors ควบคุมจำนวน connectors ที่ node มีฝั่ง input ถ้ามีแค่ 1 connector ให้ใช้ `input: ['main']`

## `outputs`

_Array of strings_ | _Required_  

ตั้งชื่อ output connectors ควบคุมจำนวน connectors ที่ node มีฝั่ง output ถ้ามีแค่ 1 connector ให้ใช้ `output: ['main']`

## `requiredInputs`

_Integer_ หรือ _Array_ | _Optional_

ใช้กับ node ที่มีหลาย input ระบุหมายเลข input ที่ต้องมีข้อมูล (branch นั้นต้องรัน) ก่อน node จะ execute

## `credentials`

_Array of objects_ | _Required_  

parameter นี้บอก n8n ว่ามี credential อะไรบ้าง แต่ละ object จะกำหนดประเภท authentication

object ต้องมี:

* `name`: ชื่อ credential ต้องตรงกับ property `name` ใน credential file เช่น `name: 'asanaApi'` ใน [`Asana.node.ts`](https://github.com/n8n-io/n8n/blob/master/packages/nodes-base/nodes/Asana/Asana.node.ts){:target=_blank .external-class} จะลิงก์กับ `name = 'asanaApi'` ใน [`AsanaApi.credential.ts`](https://github.com/n8n-io/n8n/blob/master/packages/nodes-base/credentials/AsanaApi.credentials.ts){:target=_blank .external-class}
* `required`: Boolean. ระบุว่า authentication จำเป็นต้องใช้กับ node นี้หรือไม่

## `requestDefaults`

_Object_ | _Required_  

ตั้งค่าข้อมูลพื้นฐานสำหรับ API call ที่ node จะใช้

object นี้ต้องมี:

* `baseURL`: URL หลักของ API

นอกจากนี้ยังเพิ่มได้:

* `headers`: object สำหรับ headers ของ API call เช่น content type
* `url`: string. ต่อท้าย `baseURL` ปกติจะไม่ต้องใส่ ตรงนี้มักจะกำหนดใน `operations` มากกว่า

## `properties`

_Array of objects_ | _Required_  

เก็บ resource และ operations objects ที่กำหนดพฤติกรรมของ node รวมถึง object สำหรับตั้งค่าฟิลด์บังคับและฟิลด์เสริมที่รับ input จากผู้ใช้

### Resource objects

object resource จะมี parameter ดังนี้:

* `displayName`: String. ควรเป็น `Resource` เสมอ
* `name`: String. ควรเป็น `resource` เสมอ
* `type`: String. บอก n8n ว่าใช้ UI element อะไร และรับ input แบบไหน เช่น `options` จะทำให้ n8n สร้าง dropdown ให้เลือก option ดูรายละเอียดที่ [Node UI elements](/integrations/creating-nodes/build/reference/ui-elements.md)
* `noDataExpression`: Boolean. ป้องกันการใช้ expression กับ parameter นี้ ต้องเป็น `true` เสมอสำหรับ `resource`

### Operations objects

object operations จะกำหนด operation ที่ใช้ได้กับ resource

* `displayName`: String. ควรเป็น `Options` เสมอ
* `name`: String. ควรเป็น `operation` เสมอ
* `type`: String. บอก n8n ว่าใช้ UI element อะไร เช่น `dateTime` จะทำให้มี date picker ดูรายละเอียดที่ [Node UI elements](/integrations/creating-nodes/build/reference/ui-elements.md)
* `noDataExpression`: Boolean. ป้องกันการใช้ expression กับ parameter นี้ ต้องเป็น `true` เสมอสำหรับ `operation`
* `options`: Array of objects. แต่ละ object จะอธิบายพฤติกรรมของ operation เช่น routing, REST verb ที่ใช้ ฯลฯ โดยใน `options` object จะมี:
	* `name`. String.
	* `value`. String.
	* `action`: String. parameter นี้จะรวม resource กับ operation ควรใส่ไว้เสมอ เพราะ n8n จะใช้ในอนาคต เช่น resource ชื่อ `"Card"` กับ operation `"Get all"` action จะเป็น `"Get all cards"`
	* `description`: String.
	* `routing`: Object ที่มีรายละเอียดของ request

### Additional fields objects

object เหล่านี้จะกำหนด parameter เสริม n8n จะแสดงใน GUI ใต้หัวข้อ **Additional Fields** ผู้ใช้เลือกได้ว่าจะตั้งค่าหรือไม่

object ต้องมี:

```js
displayName: 'Additional Fields',
name: 'additionalFields',
// The UI element type
type: ''
placeholder: 'Add Field',
default: {},
displayOptions: {
  // Set which resources and operations this field is available for
  show: {
    resource: [
      // Resource names
    ],
    operation: [
      // Operation names
    ]
  },
}
```

ดูรายละเอียด UI element types เพิ่มเติมได้ที่ [UI elements](/integrations/creating-nodes/build/reference/ui-elements.md)
