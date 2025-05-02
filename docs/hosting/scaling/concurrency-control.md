---
#https://www.notion.so/n8n/Frontmatter-432c2b8dff1f43d4b1c8d20075510fe4
contentType: explanation
---

# Self-hosted concurrency control

/// info | Only for self-hosted n8n
เอกสารนี้สำหรับ self-hosted concurrency control ถ้าใช้ n8n Cloud ดู [Cloud concurrency](/manage-cloud/concurrency.md) สำหรับการจัดการ concurrency ของ n8n Cloud
///

ใน regular mode, n8n จะไม่จำกัดจำนวน production execution ที่รันพร้อมกัน อาจทำให้มี execution เยอะเกินจน event loop ช้า ระบบช้า หรือไม่ตอบสนอง

เพื่อป้องกันปัญหานี้ คุณสามารถตั้ง limit สำหรับ production execution ใน regular mode ได้ ใช้ควบคุมจำนวน execution ที่รันพร้อมกัน ส่วนที่เกินจะถูก queue ไว้จนกว่าจะมี execution ว่าง แล้วจะเอาออกจาก queue แบบ FIFO

Concurrency control ถูกปิดไว้เป็นค่าเริ่มต้น ถ้าจะเปิดให้ใช้แบบนี้:

```sh
export N8N_CONCURRENCY_PRODUCTION_LIMIT=20
```

ข้อควรจำ:

- Concurrency control ใช้กับ production execution เท่านั้น: execution ที่เริ่มจาก webhook หรือ [trigger](/glossary.md#trigger-node-n8n) node ไม่รวม execution แบบ manual, sub-workflow, error, หรือที่เริ่มจาก CLI
- คุณไม่สามารถ retry execution ที่อยู่ใน queue ได้ ถ้ายกเลิกหรือ delete execution ที่ queue อยู่ execution นั้นจะถูกลบออกจาก queue ด้วย
- ตอน instance startup, n8n จะ resume execution ที่ queue ไว้ตาม limit ที่ตั้งไว้ ส่วนที่เหลือจะ re-enqueue
<!-- vale off -->
- ถ้าจะ monitor concurrency control ให้ดู log ว่ามี execution ถูก queue หรือถูกปล่อยออกจาก queue ในอนาคต n8n จะมี UI สำหรับ concurrency control
<!-- vale on -->

เมื่อเปิด concurrency control แล้ว คุณจะเห็นจำนวน execution ที่ active และ limit ที่ตั้งไว้ที่ด้านบนของแท็บ executions ของ project หรือ workflow

## Comparison to queue mode

ใน queue mode, คุณสามารถควบคุมจำนวน job ที่ worker ทำพร้อมกันได้ด้วย [`--concurrency` flag](/hosting/scaling/queue-mode.md#configure-worker-concurrency)

Concurrency control ใน queue mode เป็นคนละกลไกกับ regular mode แต่ environment variable `N8N_CONCURRENCY_PRODUCTION_LIMIT` จะควบคุมทั้งสองแบบ ถ้าตั้งค่านี้ (ไม่ใช่ `-1`) n8n จะใช้ค่านี้ใน queue mode แทนค่า default หรือ flag

