หากหลาย items ที่ index เดียวกันมี field ที่มีชื่อเหมือนกัน นี่คือการ clash ตัวอย่างเช่น หาก items ทั้งหมดใน Input 1 และ Input 2 มี field ชื่อ `language` field เหล่านี้จะ clash โดยค่าเริ่มต้น n8n จะให้ความสำคัญกับ Input 2 หมายความว่าหาก `language` มีค่าใน Input 2 n8n จะใช้ค่านั้นเมื่อ merge items

คุณสามารถเปลี่ยนพฤติกรรมนี้ได้โดยเลือก **Options** > **Clash Handling**:

- **When Field Values Clash**: เลือก input ที่จะให้ความสำคัญ หรือเลือก **Always Add Input Number to Field Names** เพื่อเก็บ field และค่าทั้งหมด โดยมีหมายเลข input ต่อท้ายชื่อ field เพื่อแสดงว่ามาจาก input ใด
- **Merging Nested Fields**
    - **Deep Merge**: Merge properties ในทุกระดับของ items รวมถึง nested objects สิ่งนี้มีประโยชน์เมื่อต้องจัดการกับโครงสร้างข้อมูลที่ซับซ้อนและซ้อนกัน ซึ่งคุณต้องแน่ใจว่ามีการ merge properties ในทุกระดับ
    - **Shallow Merge**: Merge properties ที่ระดับบนสุดของ items เท่านั้น โดยไม่ merge nested objects สิ่งนี้มีประโยชน์เมื่อคุณมีโครงสร้างข้อมูลแบบ flat หรือเมื่อคุณต้องการ merge เฉพาะ top-level properties โดยไม่ต้องกังวลเกี่ยวกับ nested properties
