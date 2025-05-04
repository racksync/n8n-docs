ใช้ Code node เพื่อเขียน JavaScript หรือ Python แบบกำหนดเอง และรันเป็นขั้นตอนใน workflow ของคุณ

/// note | การเขียนโค้ดใน n8n
หน้านี้ให้ข้อมูลการใช้งานเกี่ยวกับ Code node สำหรับคำแนะนำเพิ่มเติมเกี่ยวกับการเขียนโค้ดใน n8n โปรดดูที่ส่วน [Code](/code/index.md) ซึ่งรวมถึง:

* เอกสารอ้างอิงเกี่ยวกับ [Built-in methods and variables](/code/builtin/overview.md)
* คำแนะนำเกี่ยวกับ [Handling dates](/code/cookbook/luxon.md) และ [Querying JSON](/code/cookbook/jmespath.md)
* ชุดตัวอย่างที่เพิ่มขึ้นเรื่อยๆ ใน [Cookbook](/code/cookbook/code-node/index.md)
///

/// note | ตัวอย่างและ Templates
สำหรับตัวอย่างการใช้งานและ templates เพื่อช่วยให้คุณเริ่มต้น โปรดดูที่หน้า [Code integrations](https://n8n.io/integrations/code/){:target=_blank .external-link} ของ n8n
///

/// note | Function และ Function Item nodes
Code node มาแทนที่ Function และ Function Item nodes ตั้งแต่เวอร์ชัน 0.198.0 หากคุณใช้ n8n เวอร์ชันเก่า คุณยังสามารถดู [เอกสาร Function node](https://github.com/n8n-io/n8n-docs/blob/67935ad2528e2e30d7984ea917e4af2910a096ec/docs/integrations/builtin/core-nodes/n8n-nodes-base.function.md){:target=_blank .external-link} และ [เอกสาร Function Item node](https://github.com/n8n-io/n8n-docs/blob/67935ad2528e2e30d7984ea917e4af2910a096ec/docs/integrations/builtin/core-nodes/n8n-nodes-base.functionItem.md){:target=_blank .external-link} ได้
///
## การใช้งาน

วิธีใช้ Code node

### เลือกโหมด

มีสองโหมด:

* **Run Once for All Items**: นี่คือค่าเริ่มต้น เมื่อ workflow ของคุณทำงาน โค้ดใน code node จะทำงานเพียงครั้งเดียว ไม่ว่าจะมี input items กี่รายการก็ตาม
* **Run Once for Each Item**: เลือกตัวเลือกนี้หากคุณต้องการให้โค้ดของคุณทำงานสำหรับทุก input item

## JavaScript

Code node รองรับ Node.js

### ฟีเจอร์ JavaScript ที่รองรับ

Code node รองรับ:

* Promises แทนที่จะ return items โดยตรง คุณสามารถ return promise ที่จะ resolve ตามนั้นได้
* การเขียนไปยัง console ของเบราว์เซอร์โดยใช้ `console.log` ซึ่งมีประโยชน์สำหรับการดีบักและแก้ไขปัญหา workflows ของคุณ

### External libraries

หากคุณ self-host n8n คุณสามารถ import และใช้ built-in และ external npm modules ใน Code node ได้ หากต้องการเรียนรู้วิธีเปิดใช้งาน external modules โปรดดูคู่มือ [Enable modules in Code node](/hosting/configuration/configuration-examples/modules-in-code-node.md)

หากคุณใช้ n8n Cloud คุณจะไม่สามารถ import external npm modules ได้ n8n มี modules สองตัวให้คุณใช้งาน:

* [crypto Node.js module](https://nodejs.org/docs/latest-v18.x/api/crypto.html){:target=_blank .external-link}
* [moment npm package](https://www.npmjs.com/package/moment){:target=_blank .external-link}

### Built-in methods and variables

n8n มี built-in methods และ variables สำหรับการทำงานกับข้อมูลและการเข้าถึงข้อมูล n8n โปรดดู [Built-in methods and variables](/code/builtin/overview.md) สำหรับข้อมูลเพิ่มเติม

Syntax ในการใช้ built-in methods และ variables คือ `$variableName` หรือ `$methodName()` พิมพ์ `$` ใน Code node หรือ expressions editor เพื่อดูรายการ methods และ variables ที่แนะนำ

### Keyboard shortcuts

สภาพแวดล้อมการแก้ไข Code node รองรับ keyboard shortcuts ที่ช่วยประหยัดเวลาและมีประโยชน์สำหรับการทำงานต่างๆ ตั้งแต่ autocompletion ไปจนถึง code-folding และการใช้ multiple-cursors สามารถดูรายการทั้งหมดได้ใน [list of keyboard shortcuts](/integrations/builtin/core-nodes/n8n-nodes-base.code/keyboard-shortcuts.md)

## Python

n8n เพิ่มการรองรับ Python ในเวอร์ชัน 1.0 โดยไม่ได้รวม Python executable มาด้วย แต่ n8n ให้การรองรับ Python โดยใช้ [Pyodide](https://pyodide.org/en/stable/){:target=_blank .external-link} ซึ่งเป็นการ port CPython ไปยัง WebAssembly สิ่งนี้จำกัด Python packages ที่มีให้เฉพาะ [Packages included with Pyodide](https://pyodide.org/en/stable/usage/packages-in-pyodide.html#packages-in-pyodide){:target=_blank .external-link} n8n จะดาวน์โหลด package โดยอัตโนมัติในครั้งแรกที่คุณใช้งาน

/// note | ช้ากว่า JavaScript
Code node ใช้เวลาประมวลผล Python นานกว่า JavaScript เนื่องจากมีขั้นตอนการคอมไพล์เพิ่มเติม
///
### Built-in methods and variables

n8n มี built-in methods และ variables สำหรับการทำงานกับข้อมูลและการเข้าถึงข้อมูล n8n โปรดดู [Built-in methods and variables](/code/builtin/overview.md) สำหรับข้อมูลเพิ่มเติม

Syntax ในการใช้ built-in methods และ variables คือ `_variableName` หรือ `_methodName()` พิมพ์ `_` ใน Code node เพื่อดูรายการ methods และ variables ที่แนะนำ

### Keyboard shortcuts

สภาพแวดล้อมการแก้ไข Code node รองรับ keyboard shortcuts ที่ช่วยประหยัดเวลาและมีประโยชน์สำหรับการทำงานต่างๆ ตั้งแต่ autocompletion ไปจนถึง code-folding และการใช้ multiple-cursors สามารถดูรายการทั้งหมดได้ใน [list of keyboard shortcuts](/integrations/builtin/core-nodes/n8n-nodes-base.code/keyboard-shortcuts.md)

## File system และ HTTP requests

คุณไม่สามารถเข้าถึง file system หรือทำการ HTTP requests ได้ ให้ใช้ nodes ต่อไปนี้แทน:

* [Read/Write File From Disk](/integrations/builtin/core-nodes/n8n-nodes-base.readwritefile.md)
* [HTTP Request](/integrations/builtin/core-nodes/n8n-nodes-base.httprequest/index.md)

## การเขียนโค้ดใน n8n

มีสองที่ที่คุณสามารถใช้โค้ดใน n8n ได้: Code node และ expressions editor เมื่อใช้พื้นที่ใดพื้นที่หนึ่ง มีแนวคิดหลักบางอย่างที่คุณต้องรู้ รวมถึง built-in methods และ variables บางอย่างเพื่อช่วยในงานทั่วไป

### แนวคิดหลัก

เมื่อทำงานกับ Code node คุณต้องเข้าใจแนวคิดต่อไปนี้:

* [Data structure](/data/data-structure.md): ทำความเข้าใจข้อมูลที่คุณได้รับใน Code node และข้อกำหนดสำหรับการส่งออกข้อมูลจาก node
* [Item linking](/data/data-mapping/data-item-linking/index.md): เรียนรู้วิธีการทำงานของ data items และวิธีเชื่อมโยงไปยัง items จาก nodes ก่อนหน้า คุณต้องจัดการ item linking ในโค้ดของคุณเมื่อจำนวน input และ output items ไม่ตรงกัน

### Built-in methods and variables

n8n มี built-in methods และ variables ซึ่งให้การสนับสนุนสำหรับ:

* การเข้าถึงข้อมูล item เฉพาะ
* การเข้าถึงข้อมูลเกี่ยวกับ workflows, executions และสภาพแวดล้อม n8n ของคุณ
* ตัวแปรอำนวยความสะดวกเพื่อช่วยเกี่ยวกับข้อมูลและเวลา

โปรดดู [Built-in methods and variables](/code/builtin/overview.md) สำหรับข้อมูลเพิ่มเติม

## ใช้ AI ใน Code node

--8<-- "_snippets/code/ai-how-to.md"
