คุณสามารถทดสอบ node ของคุณในขณะที่สร้างได้โดยการรันใน n8n instance บนเครื่องของคุณ

1. ติดตั้ง n8n โดยใช้ npm:
  ```shell
  npm install n8n -g
  ```
2. เมื่อคุณพร้อมที่จะทดสอบ node ของคุณ ให้ publish มันในเครื่อง:
  ```shell
  # ในไดเรกทอรี node ของคุณ
  npm run build
  npm link
  ```
3. ติดตั้ง node ลงใน n8n instance บนเครื่องของคุณ:
  ```shell
  # ในไดเรกทอรี nodes ภายในการติดตั้ง n8n ของคุณ
  # node-package-name คือชื่อจาก package.json
  npm link <node-package-name>
  ```

    /// note | ตรวจสอบไดเรกทอรีของคุณ
	ตรวจสอบให้แน่ใจว่าคุณรัน `npm link <node-name>` ในไดเรกทอรี nodes ภายในการติดตั้ง n8n ของคุณ ซึ่งอาจเป็น:

	* `~/.n8n/custom/`
	* `~/.n8n/<your-custom-name>`: หากการติดตั้ง n8n ของคุณตั้งชื่ออื่นโดยใช้ `N8N_CUSTOM_EXTENSIONS`
	///

4. เริ่ม n8n:
  ```
  n8n start
  ```
5. เปิด n8n ในเบราว์เซอร์ของคุณ คุณควรเห็น nodes ของคุณเมื่อคุณค้นหาในแผง nodes

    /// note | ชื่อ Node
    ตรวจสอบให้แน่ใจว่าคุณค้นหาโดยใช้ชื่อ node ไม่ใช่ชื่อ package ตัวอย่างเช่น หากชื่อ npm package ของคุณคือ `n8n-nodes-weather-nodes` และ package นั้นมี nodes ชื่อ `rain`, `sun`, `snow` คุณควรค้นหา `rain` ไม่ใช่ `weather-nodes`
    ///

### การแก้ไขปัญหา

- ไม่มีไดเรกทอรี `custom` ในการติดตั้ง `~/.n8n` บนเครื่อง

คุณต้องสร้างไดเรกทอรี `custom` ด้วยตนเองและรัน `npm init`
```shell
# ในไดเรกทอรี ~/.n8n รันคำสั่ง
mkdir custom
cd custom
npm init
```
