/// note | อาจมีการเปลี่ยนแปลง
มาตรฐานที่อธิบายในเอกสารนี้มีไว้สำหรับ community nodes repository รุ่นแรก ซึ่งอาจมีการเปลี่ยนแปลงในรุ่นต่อๆ ไป
///
Community nodes คือ npm packages ซึ่งโฮสต์อยู่ใน npm registry

เมื่อสร้าง node เพื่อส่งไปยัง community node repository ให้ใช้แหล่งข้อมูลต่อไปนี้เพื่อให้แน่ใจว่าการตั้งค่า node ของคุณถูกต้อง:

* ดู [starter node](https://github.com/n8n-io/n8n-nodes-starter){:target=_blank .external-link} และ [nodes ของ n8n เอง](https://github.com/n8n-io/n8n/tree/master/packages/nodes-base/nodes){:target=_blank .external-link} สำหรับตัวอย่างบางส่วน
* อ้างอิงเอกสารเกี่ยวกับ [การสร้าง nodes ของคุณเอง](/integrations/creating-nodes/overview.md)
* ตรวจสอบให้แน่ใจว่า node ของคุณเป็นไปตาม [มาตรฐาน](#standards) สำหรับ community nodes

## มาตรฐาน

เพื่อให้ node ของคุณพร้อมใช้งานใน n8n community node repository คุณต้อง:

* ตรวจสอบให้แน่ใจว่าชื่อ package เริ่มต้นด้วย `n8n-nodes-` หรือ `@<scope>/n8n-nodes-` ตัวอย่างเช่น `n8n-nodes-weather` หรือ `@weatherPlugins/n8n-nodes-weather`
* รวม `n8n-community-node-package` ไว้ใน keywords ของ package ของคุณ
* ตรวจสอบให้แน่ใจว่าคุณได้เพิ่ม nodes และ credentials ของคุณลงในไฟล์ `package.json` ภายใน attribute `n8n` อ้างอิง [package.json ใน starter node](https://github.com/n8n-io/n8n-nodes-starter/blob/master/package.json){:target=_blank .external-link} สำหรับตัวอย่าง
* ตรวจสอบ node ของคุณโดยใช้ [linter](/integrations/creating-nodes/test/node-linter.md) และทดสอบในเครื่องเพื่อให้แน่ใจว่าใช้งานได้
* ส่ง package ไปยัง npm registry อ้างอิงเอกสารของ npm เกี่ยวกับ [Contributing packages to the registry](https://docs.npmjs.com/packages-and-modules/contributing-packages-to-the-registry){:target=_blank .external-link} สำหรับข้อมูลเพิ่มเติม

