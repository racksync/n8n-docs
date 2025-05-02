---
#https://www.notion.so/n8n/Frontmatter-432c2b8dff1f43d4b1c8d20075510fe4
title: Crypto
description: Documentation for the Crypto node in n8n, a workflow automation platform. Includes guidance on usage, and links to examples.
contentType: [integration, reference]
priority: medium
---

# Crypto

ใช้ Crypto node เพื่อเข้ารหัส (encrypt) ข้อมูลใน workflow

## Actions

* [**Generate** a random string](#generate-parameters)
* [**Hash** a text or file](#hash-parameters) ใน format ที่เลือก
* [**Hmac** a text or file](#hmac-parameters) ใน format ที่เลือก
* [**Sign** a string](#sign-parameters) ด้วย private key

## Node parameters

--8<-- "_snippets/integrations/builtin/app-nodes/ai-tools.md"

parameter ของ node จะขึ้นอยู่กับ action ที่เลือก

### Generate parameters

* **Property Name**: ใส่ชื่อ property ที่จะเขียน random string ลงไป
* **Type**: เลือก encoding type ที่จะใช้ generate string เลือกได้:
	* **ASCII**
	* **BASE64**
	* **HEX**
	* **UUID**

### Hash parameters

* **Type**: เลือก hash type ที่จะใช้ เลือกได้:
	* **MD5**
	* **SHA256**
	* **SHA3-256**
	* **SHA3-384**
	* **SHA3-512**
	* **SHA385**
	* **SHA512**
* **Binary File**: เปิดถ้าข้อมูลที่ต้องการ hash มาจาก binary file
	* **Value**: ถ้าปิด **Binary File** ให้ใส่ค่าที่ต้องการ hash
	* **Binary Property Name**: ถ้าเปิด **Binary File** ให้ใส่ชื่อ binary property ที่มีข้อมูลที่ต้องการ hash
* **Property Name**: ใส่ชื่อ property ที่จะเขียน hash ลงไป
* **Encoding**: เลือก encoding type ที่จะใช้ เลือกได้:
	* **BASE64**
	* **HEX**

### Hmac parameters

* **Binary File**: เปิดถ้าข้อมูลที่ต้องการ encrypt มาจาก binary file
	* **Value**: ถ้าปิด **Binary File** ให้ใส่ค่าที่ต้องการ encrypt
	* **Binary Property Name**: ถ้าเปิด **Binary File** ให้ใส่ชื่อ binary property ที่มีข้อมูลที่ต้องการ encrypt
* **Type**: เลือก encryption type ที่จะใช้ เลือกได้:
	* **MD5**
	* **SHA256**
	* **SHA3-256**
	* **SHA3-384**
	* **SHA3-512**
	* **SHA385**
	* **SHA512**
* **Property Name**: ใส่ชื่อ property ที่จะเขียน hash ลงไป
* **Secret**: ใส่ secret หรือ secret key ที่ใช้สำหรับ decode
* **Encoding**: เลือก encoding type ที่จะใช้ เลือกได้:
	* **BASE64**
	* **HEX**

### Sign parameters

* **Value**: ใส่ค่าที่ต้องการ sign
* **Property Name**: ใส่ชื่อ property ที่จะเขียน signed value ลงไป
* **Algorithm Name or ID**: เลือก algorithm name จาก list หรือใส่ ID ด้วย [expression](/code/expressions.md)
* **Encoding**: เลือก encoding type ที่จะใช้ เลือกได้:
	* **BASE64**
	* **HEX**
* **Private Key**: ใส่ private key ที่จะใช้ sign string

## Templates and examples

<!-- see https://www.notion.so/n8n/Pull-in-templates-for-the-integrations-pages-37c716837b804d30a33b47475f6e3780 -->
[[ templatesWidget(page.title, 'crypto') ]]
