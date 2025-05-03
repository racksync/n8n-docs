---
#https://www.notion.so/n8n/Frontmatter-432c2b8dff1f43d4b1c8d20075510fe4
title: มาตรฐานการเขียนโค้ด
description: แนวทางการเขียนโค้ดสำหรับสร้าง node
contentType: reference
---

# Code standards

การทำตามมาตรฐานการเขียนโค้ดที่กำหนดไว้ตอนสร้าง node จะช่วยให้โค้ดของคุณอ่านง่าย ดูแลรักษาง่าย และช่วยลดข้อผิดพลาดต่างๆ เอกสารนี้จะให้คำแนะนำเกี่ยวกับแนวปฏิบัติที่ดีในการเขียน node โดยจะเน้นไปที่รายละเอียดของโค้ด ถ้าต้องการดูมาตรฐานด้าน UI และ UX ให้ดูที่ [Node UI design](/integrations/creating-nodes/plan/node-ui-design.md)

## Use the linter

n8n node linter จะช่วยตรวจสอบโค้ดของคุณให้อัตโนมัติในหลายๆ มาตรฐานที่เกี่ยวกับการสร้าง node คุณควรแน่ใจว่า node ของคุณผ่านการตรวจสอบของ linter ก่อนจะ publish ดูรายละเอียดเพิ่มเติมได้ที่ [n8n node linter](/integrations/creating-nodes/test/node-linter.md)

## Use the starter

n8n node starter project มีการตั้งค่าที่แนะนำ, dependencies (รวมถึง linter) และตัวอย่างต่างๆ เพื่อช่วยให้คุณเริ่มต้นได้ง่ายขึ้น เวลาจะเริ่มโปรเจกต์ใหม่ให้ใช้ [starter](https://github.com/n8n-io/n8n-nodes-starter){:target=_blank .external-link} นี้

## Write in TypeScript

โค้ดของ n8n ทั้งหมดใช้ TypeScript การเขียน node ของคุณด้วย TypeScript จะช่วยให้พัฒนาได้เร็วขึ้นและลด bug ได้

## Detailed guidelines for writing a node

แนวทางเหล่านี้ใช้กับ node ทุกตัวที่คุณสร้าง

### Resources and operations

ถ้า node ของคุณสามารถทำงานได้หลายอย่าง ให้ตั้งชื่อ parameter ที่เลือก operation ว่า `Operation` ถ้า node ของคุณทำ operation เหล่านี้ได้กับ resource หลายตัว ให้สร้าง parameter ชื่อ `Resource` ตัวอย่างโค้ดด้านล่างนี้แสดงการตั้งค่า resource และ operation แบบพื้นฐาน:

```js
export const ExampleNode implements INodeType {
    description: {
        displayName: 'Example Node',
        ...
        properties: [
            {
                displayName: 'Resource',
                name: 'resource',
                type: 'options',
                options: [
                    {
                        name: 'Resource One',
                        value: 'resourceOne'
                    },
                    {
                        name: 'Resource Two',
                        value: 'resourceTwo'
                    }
                ],
                default: 'resourceOne'
            },
            {
                displayName: 'Operation',
                name: 'operation',
                type: 'options',
                // Only show these operations for Resource One
                displayOptions: {
                    show: {
                        resource: [
                            'resourceOne'
                        ]
                    }
                },
                options: [
                    {
                        name: 'Create',
                        value: 'create',
                        description: 'Create an instance of Resource One'
                    }
                ]
            }
        ]
    }
}
```

### Reuse internal parameter names

field resource และ operation ทุกตัวใน node ของ n8n จะมี 2 ค่า: display name (ตั้งด้วย `name`) และ internal name (ตั้งด้วย `value`) การใช้ internal name ซ้ำกันในแต่ละ field จะช่วยให้ n8n เก็บข้อมูลที่ user กรอกไว้ได้ ถ้า user เปลี่ยน operation

เช่น ถ้าคุณสร้าง node ที่มี resource ชื่อ 'Order' ซึ่งมี operation หลายอย่าง เช่น Get, Edit, Delete แต่ละ operation ต้องใช้ order ID คุณต้องแสดง field สำหรับกรอก ID ให้ user โดยใช้ internal name เดียวกัน (ตั้งใน `value`) ในแต่ละ operation แบบนี้ user จะกรอก ID ในตอนเลือก Get แล้วถ้าเปลี่ยนไป Edit ข้อมูลก็ยังอยู่

เวลาจะใช้ internal name ซ้ำกัน ต้องแน่ใจว่ามี field เดียวที่แสดงให้ user เห็นในแต่ละครั้ง ควบคุมได้ด้วย `displayOptions`

## Detailed guidelines for writing a programmatic-style node

แนวทางนี้ใช้กับ node ที่สร้างแบบ programmatic เท่านั้น ถ้าใช้ declarative style ไม่ต้องสนใจส่วนนี้ ดูข้อมูลเพิ่มเติมเกี่ยวกับ style ได้ที่ [Choose your node building approach](/integrations/creating-nodes/plan/choose-node-method.md)

### Don't change incoming data

ห้ามแก้ไขข้อมูลที่ node ได้รับเข้ามา (ใช้ `this.getInputData()`) เพราะ node อื่นๆ ก็ใช้ข้อมูลเดียวกัน ถ้าต้องการเพิ่ม/แก้ไข/ลบข้อมูล ให้ clone ข้อมูลเข้ามาก่อนแล้วค่อย return ข้อมูลใหม่ ถ้าไม่ทำแบบนี้ node อื่นที่รันทีหลังจะได้ข้อมูลผิด

ไม่จำเป็นต้อง clone ข้อมูลทุกอย่างเสมอไป เช่น ถ้า node เปลี่ยนแค่ binary data แต่ไม่แตะ JSON data ก็สร้าง item ใหม่ที่อ้างอิง JSON เดิมได้

### Use the built in request library

บางบริการ third-party มี library ของตัวเองใน npm ซึ่งอาจช่วยให้เขียน integration ง่ายขึ้น แต่การใช้ package เหล่านี้จะเพิ่ม dependency (รวมถึง dependency ซ้อนๆ) ทำให้โค้ดใหญ่ขึ้น โหลดช้าขึ้น เสี่ยงเรื่อง security และ bug มากขึ้น แนะนำให้ใช้ module ที่ built-in มาให้:

```typescript
// If no auth needed
const response = await this.helpers.httpRequest(options);

// If auth needed
const response = await this.helpers.httpRequestWithAuthentication.call(
	this, 
	'credentialTypeName', // For example: pipedriveApi
	options,
);
```

อันนี้ใช้ npm package [Axios](https://www.npmjs.com/package/axios){:target=_blank .external-link}

ดูรายละเอียดเพิ่มเติมและวิธี migrate จาก `this.helpers.request` ที่ถูกถอดออกแล้ว ได้ที่ [HTTP helpers](/integrations/creating-nodes/build/reference/http-helpers.md)
