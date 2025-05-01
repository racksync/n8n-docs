---
#https://www.notion.so/n8n/Frontmatter-432c2b8dff1f43d4b1c8d20075510fe4
contentType: howto
---

# n8n node linter

n8n node linter หรือ [`eslint-plugin-n8n-nodes-base`](https://github.com/ivov/eslint-plugin-n8n-nodes-base) จะช่วยตรวจสอบ (lint) โค้ดของ n8n nodes และ credentials ทั้งใน repository หลักและ community packages โดยจะช่วยหาปัญหาและแก้ไขให้อัตโนมัติ เพื่อให้คุณทำตาม best practices ได้ง่ายขึ้น

`eslint-plugin-n8n-nodes-base` มี [กฎต่างๆ](https://github.com/ivov/eslint-plugin-n8n-nodes-base#ruleset) สำหรับไฟล์ node (`*.node.ts`), resource description (`*Description.ts`), credential (`*.credentials.ts`) และ `package.json` ของ community package

## Setup

ถ้าใช้ [n8n node starter](https://github.com/n8n-io/n8n-nodes-starter): ให้รัน `npm install` ในโปรเจกต์ starter เพื่อ install dependencies ทั้งหมด หลังจากติดตั้งเสร็จ linter ก็จะพร้อมใช้งานทันที

ถ้าใช้ VS Code ให้ติดตั้ง [ESLint VS Code extension](https://marketplace.visualstudio.com/items?itemName=dbaeumer.VS Code-eslint) สำหรับ IDE อื่นๆ ให้ดูวิธีการ integrate ESLint ของแต่ละตัว

/// note | Don't edit the configuration file
[`.eslintrc.js`](https://github.com/n8n-io/n8n-nodes-starter/blob/master/.eslintrc.js) คือไฟล์ config สำหรับ `eslint-plugin-n8n-nodes-base` ไม่ควรแก้ไขไฟล์นี้
///

## Usage

คุณสามารถใช้ linter ได้ทั้งใน community package หรือใน main n8n repository

### Linting

ใน community package, linter จะรันอัตโนมัติหลังจาก install dependencies และก่อน publish package ไปที่ npm ส่วนใน [main n8n repository](https://github.com/n8n-io/n8n){:target=_blank .external-link} linter จะรันอัตโนมัติผ่าน GitHub Actions ทุกครั้งที่คุณ push ไปที่ pull request

ทั้งสองกรณี ถ้าใช้ VS Code จะมีการ lint โค้ดให้ตลอดเวลาในขณะที่คุณทำงานกับโปรเจกต์ สามารถ hover ที่ปัญหาที่เจอเพื่อดูรายละเอียดและลิงก์ข้อมูลเพิ่มเติม

คุณยังสามารถรัน linter ด้วยตัวเองได้ด้วย:

* รัน `npm run lint` เพื่อ lint และดูปัญหาที่เจอใน console
* รัน `npm run lintfix` เพื่อ lint และแก้ไขปัญหาให้อัตโนมัติ โดยจะ fix เฉพาะกฎที่ [สามารถแก้ไขอัตโนมัติได้](https://github.com/ivov/eslint-plugin-n8n-nodes-base#ruleset)

ทั้งสองคำสั่งนี้สามารถรันได้ที่ root directory ของ community package หรือที่ `/packages/nodes-base/` ใน main repository

### Exceptions

ถ้าคุณไม่ต้องการแก้ไข rule ที่ linter แจ้งเตือน สามารถยกเว้น rule นั้นได้ เพื่อไม่ให้ linter แจ้งเตือนอีก

ถ้าต้องการยกเว้น lint จาก VS Code: hover ที่ปัญหาแล้วคลิก `Quick fix` (หรือ `cmd+.` บน macOS) แล้วเลือก **Disable {rule} for this line** ควรปิด rule เฉพาะกรณีที่มีเหตุผลเท่านั้น ถ้าคิดว่า linter แจ้งเตือนผิด สามารถ [แจ้งปัญหาใน linter repository](https://github.com/ivov/eslint-plugin-n8n-nodes-base/issues)

ถ้าต้องการยกเว้น lint ทั้งไฟล์ ให้เพิ่ม code comment โดยเฉพาะ TSLint rules อาจจะไม่แสดงใน VS Code และอาจต้องปิดด้วย code comment ดูรายละเอียดเพิ่มเติมได้ที่ [TSLint documentation](https://palantir.github.io/tslint/usage/rule-flags/)
