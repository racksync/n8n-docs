---
#https://www.notion.so/n8n/Frontmatter-432c2b8dff1f43d4b1c8d20075510fe4
contentType: explanation
---

# Memory-related errors

n8n ไม่จำกัดปริมาณข้อมูลที่แต่ละ node จะดึงหรือประมวลผลได้ ซึ่งให้ความยืดหยุ่นแต่ก็อาจทำให้เกิด error ถ้า workflow ใช้ memory เกินที่มีอยู่ หน้านี้จะอธิบายวิธีสังเกตและหลีกเลี่ยง error แบบนี้

/// note | Only for self-hosted n8n
หน้านี้พูดถึง memory error สำหรับ [self-hosting n8n](/hosting/index.md) ถ้าใช้ n8n Cloud ดูที่ [Cloud data management](/manage-cloud/cloud-data-management.md) สำหรับ memory limit ของ [n8n Cloud](/manage-cloud/overview.md)
///

## Identifying out of memory situations

n8n จะมี error message แจ้งเตือนถ้าเกิด out of memory เช่น **Execution stopped at this node (n8n may have run out of memory while executing it)**

error ที่มีข้อความ **Problem running workflow**, **Connection Lost**, หรือ **503 Service Temporarily Unavailable** อาจแปลว่า n8n instance ใช้งานไม่ได้ชั่วคราว

ถ้า self-hosting n8n อาจเห็น error เช่น **Allocation failed - JavaScript heap out of memory** ใน server log

ถ้าใช้ n8n Cloud หรือ Docker image, n8n จะ restart อัตโนมัติเมื่อเจอปัญหานี้ แต่ถ้ารันด้วย npm อาจต้อง restart เอง

## Typical causes

ปัญหานี้เกิดเมื่อ workflow ใช้ memory เกินที่ instance มี ปัจจัยที่ทำให้ใช้ memory เยอะขึ้น เช่น:

- ปริมาณ [JSON data](/data/data-structure.md)
- ขนาด binary data
- จำนวน node ใน workflow
- node บางตัวใช้ memory เยอะ เช่น [Code](/integrations/builtin/core-nodes/n8n-nodes-base.code/index.md) node และ Function node เก่า
- การรัน workflow แบบ manual หรือ auto: manual จะใช้ memory เพิ่มเพราะต้อง copy ข้อมูลไป frontend
- มี workflow อื่นรันพร้อมกัน

## Avoiding out of memory situations

ถ้าเจอ out of memory มี 2 ทางเลือก: เพิ่ม memory ให้ n8n หรือ ลดการใช้ memory

### Increase available memory

ถ้า self-hosting n8n ให้เพิ่ม memory ที่ให้กับ instance (อาจมีค่าใช้จ่ายเพิ่มกับผู้ให้บริการ)

ถ้าใช้ n8n cloud ต้องอัปเกรด plan

### Reduce memory consumption

วิธีนี้ซับซ้อนกว่า ต้องปรับ workflow ที่ใช้ memory เยอะ ดู guideline ด้านล่าง (ไม่ใช่ทุกข้อจะเหมาะกับทุก workflow)

--8<-- "_snippets/self-hosting/scaling/reduce-memory-consumption.md"

### Increase old memory

สำหรับ self-hosting n8n ถ้าเจอ error **JavaScript heap out of memory** ให้เพิ่ม memory ส่วน old memory ของ V8 engine โดยตั้ง [V8 option](https://nodejs.org/api/cli.html#--max-old-space-sizesize-in-megabytes){:target=_blank .external-link} `--max-old-space-size=SIZE` ผ่าน CLI หรือ [environment variable](https://nodejs.org/api/cli.html#node_optionsoptions){:target=_blank .external-link} `NODE_OPTIONS`
