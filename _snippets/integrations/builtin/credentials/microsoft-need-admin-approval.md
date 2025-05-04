### ต้องการการอนุมัติจาก Admin (Need admin approval)

เมื่อพยายามเพิ่ม credentials สำหรับบัญชี Microsoft360 หรือ Microsoft Entra ผู้ใช้อาจเห็นข้อความเมื่อทำตามขั้นตอนว่าการดำเนินการนี้ต้องการการอนุมัติจาก admin

ข้อความนี้จะปรากฏขึ้นเมื่อบัญชีที่พยายามให้สิทธิ์สำหรับ credential ถูกจัดการโดย Microsoft Entra เพื่อที่จะออก credential บัญชี administrator จำเป็นต้องให้สิทธิ์แก่ผู้ใช้ (หรือ "tenant") สำหรับแอปพลิเคชันนั้น

ขั้นตอนสำหรับเรื่องนี้มีอยู่ใน [Microsoft Entra documentation](https://learn.microsoft.com/en-us/entra/identity/enterprise-apps/grant-admin-consent)
