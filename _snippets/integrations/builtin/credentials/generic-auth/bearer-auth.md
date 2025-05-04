## การใช้ Bearer Auth

ใช้การยืนยันตัวตนทั่วไปนี้หากแอปหรือบริการของคุณรองรับ bearer authentication ประเภทการยืนยันตัวตนนี้เป็นเพียง header authentication โดยตั้งค่า `Name` เป็น `Authorization` และ `Value` เป็น `Bearer <token>`

ในการกำหนดค่า credential นี้ ให้ป้อน:

- **Bearer Token** ที่คุณต้องส่งไปยังแอปหรือบริการที่ HTTP request ของคุณกำหนดเป้าหมาย

อ่านเพิ่มเติมเกี่ยวกับ [bearer authentication](https://swagger.io/docs/specification/v3_0/authentication/bearer-authentication/)
