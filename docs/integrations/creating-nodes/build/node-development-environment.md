---
#https://www.notion.so/n8n/Frontmatter-432c2b8dff1f43d4b1c8d20075510fe4
contentType: howto
---

# Set up your development environment

หน้านี้จะบอก dependencies ที่จำเป็นสำหรับการพัฒนา node และแนะนำการตั้งค่า editor

## Requirements

ถ้าจะ build และ test node คุณต้องมี:

* Node.js และ npm (เวอร์ชันขั้นต่ำ Node 18.17.0) ดูวิธีติดตั้งผ่าน nvm (Node Version Manager) สำหรับ Linux, Mac, และ WSL (Windows Subsystem for Linux) ได้ที่ [ที่นี่](https://github.com/nvm-sh/nvm){:target=_blank class=.external-link} สำหรับ Windows ดูคู่มือ Microsoft [Install NodeJS on Windows](https://docs.microsoft.com/en-us/windows/dev-environment/javascript/nodejs-on-windows){:target=_blank class=.external-link}
* n8n ที่รัน local ในเครื่องคุณ ติดตั้ง n8n ได้ด้วย `npm install n8n -g` แล้วทำตามขั้นตอนใน [Run your node locally](/integrations/creating-nodes/test/run-node-locally.md) เพื่อทดสอบ node ของคุณ

ควรติดตั้ง [git](https://git-scm.com/){:target=_blank class=.external-link} ด้วย เพื่อ clone และใช้ [n8n-node-starter](https://github.com/n8n-io/n8n-nodes-starter){:target=_blank class=.external-link}

## Editor setup

n8n แนะนำให้ใช้ [VS Code](https://code.visualstudio.com/){:target=_blank class=.external-link} เป็น editor

ติดตั้ง extension เหล่านี้:

* [ESLint](https://marketplace.visualstudio.com/items?itemName=dbaeumer.vscode-eslint){:target=_blank class=.external-link}
* [EditorConfig](https://marketplace.visualstudio.com/items?itemName=EditorConfig.EditorConfig){:target=_blank class=.external-link}
* [Prettier](https://marketplace.visualstudio.com/items?itemName=esbenp.prettier-vscode){:target=_blank class=.external-link}

ถ้าใช้ VS Code และ extension เหล่านี้ คุณจะเห็น warning จาก n8n node linter ขณะเขียนโค้ดทันที
