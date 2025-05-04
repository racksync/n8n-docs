ข้อดีของรูปแบบนี้คือ งานจะพร้อมใช้งานสำหรับ environment อื่น ๆ ทันทีเมื่อคุณ push จาก instance หนึ่ง

ข้อเสียคือ:

* หากคุณ push โดยไม่ได้ตั้งใจ มีความเสี่ยงที่งานนั้นจะเข้าไปอยู่ใน production instance ของคุณ หากคุณ [ใช้ GitHub Action เพื่อทำให้การ pull เป็นอัตโนมัติ](/source-control-environments/create-environments.md#optional-use-a-github-action-to-automate-pulls) ไปยัง production คุณต้องใช้รูปแบบ multi-instance, multi-branch หรือระมัดระวังไม่ push งานที่คุณไม่ต้องการให้เข้าสู่ production
* การ push และ pull ไปยัง instance เดียวกันอาจทำให้ข้อมูลสูญหายได้ เนื่องจากการเปลี่ยนแปลงจะถูกเขียนทับเมื่อดำเนินการเหล่านี้ คุณควรตั้งค่ากระบวนการเพื่อให้แน่ใจว่าเนื้อหาไหลไปในทิศทางเดียว
