---
#https://www.notion.so/n8n/Frontmatter-432c2b8dff1f43d4b1c8d20075510fe4
contentType: howto
---

# Install community nodes in the n8n app

/// note | Limited to n8n instance owners
เฉพาะเจ้าของ instance ของ n8n เท่านั้นที่สามารถติดตั้งและจัดการ community nodes ได้ เจ้าของ instance คือคนที่ตั้งค่าและดูแล user management
///
## Install a community node

วิธีติดตั้ง community node:

1. ไปที่ **Settings** > **Community Nodes**
2. เลือก **Install**
3. หา node ที่ต้องการติดตั้ง:
    1. เลือก **Browse** แล้ว n8n จะพาไปที่หน้าค้นหา npm ซึ่งแสดง npm packages ทั้งหมดที่ติด tag คำว่า `n8n-community-node-package`
    2. เลื่อนดูรายการผลลัพธ์ สามารถกรองผลลัพธ์หรือเพิ่มคีย์เวิร์ดได้
    3. เมื่อเจอ package ที่ต้องการ ให้จดชื่อ package ไว้ ถ้าต้องการติดตั้งเวอร์ชันเฉพาะ ให้จดเวอร์ชันไว้ด้วย
    4. กลับมาที่ n8n
4. ใส่ชื่อ npm package และเวอร์ชันถ้าต้องการ เช่น ถ้ามี community node สำหรับดึงข้อมูล weather API ชื่อ "Storms" โดย package ชื่อ n8n-node-storms และมี 3 major versions
    * ถ้าต้องการติดตั้งเวอร์ชันล่าสุดของ package ชื่อ n8n-node-weather: ให้ใส่ `n8n-nodes-storms` ในช่อง **Enter npm package name**
    * ถ้าต้องการติดตั้งเวอร์ชัน 2.3: ให้ใส่ `n8n-node-storms@2.3` ในช่อง **Enter npm package name**
    <!-- vale off -->
5. ยอมรับ [risks](/integrations/community-nodes/risks.md) ของการใช้ community nodes: เลือก **I understand the risks of installing unverified code from a public source.**
    <!-- vale on -->
6. เลือก **Install** n8n จะติดตั้ง node แล้วกลับไปที่รายการ **Community Nodes** ใน **Settings**

/// note | Nodes on the blocklist
n8n มี blocklist สำหรับ community nodes ที่ไม่อนุญาตให้ติดตั้ง ดูรายละเอียดได้ที่ [n8n community node blocklist](/integrations/community-nodes/blocklist.md)
///
## Uninstall a community node

วิธีลบ community node:

1. ไปที่ **Settings** > **Community nodes**
2. ที่ node ที่ต้องการลบ ให้เลือก **Options** <span class="inline-image">![Three dots options menu](/_images/common-icons/three-dot-options-menu.png){.off-glb}</span>
3. เลือก **Uninstall package**
4. เลือก **Uninstall Package** ในหน้าต่างยืนยัน

## Upgrade a community node

/// warning | Breaking changes in versions
นักพัฒนา node อาจมี breaking changes ในเวอร์ชันใหม่ๆ ได้ (breaking change คือการอัปเดตที่ทำให้ฟังก์ชันเดิมใช้ไม่ได้) ขึ้นอยู่กับวิธีการจัดการเวอร์ชันของนักพัฒนา node ถ้าอัปเกรดไปเวอร์ชันที่มี breaking change อาจทำให้ workflow ที่ใช้ node นั้นเสียได้ ควรตรวจสอบก่อนอัปเกรด ถ้าอัปเกรดแล้วมีปัญหา สามารถ [downgrade](#downgrade-a-community-node) กลับได้
///
### Upgrade to the latest version

สามารถอัปเกรด community node เป็นเวอร์ชันล่าสุดได้จากรายการ node ใน **Settings** > **community nodes**

ถ้ามีเวอร์ชันใหม่ของ community node นั้น n8n จะแสดงปุ่ม **Update** ที่ node นั้น กดปุ่มเพื่ออัปเกรดเป็นเวอร์ชันล่าสุด

### Upgrade to a specific version

ถ้าต้องการอัปเกรดเป็นเวอร์ชันเฉพาะ (ไม่ใช่เวอร์ชันล่าสุด) ให้ลบ node เดิมออกก่อน แล้วติดตั้งใหม่โดยระบุเวอร์ชันที่ต้องการ ดูวิธีที่หัวข้อ [Installation](#install-a-community-node)

## Downgrade a community node

ถ้าเจอปัญหากับเวอร์ชันของ community node ที่ใช้อยู่ อาจต้อง rollback กลับไปใช้เวอร์ชันก่อนหน้า

ให้ลบ community node ออกก่อน แล้วติดตั้งใหม่โดยระบุเวอร์ชันที่ต้องการ ดูวิธีที่หัวข้อ [Installation](#install-a-community-node)

