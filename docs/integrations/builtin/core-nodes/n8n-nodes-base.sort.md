---
#https://www.notion.so/n8n/Frontmatter-432c2b8dff1f43d4b1c8d20075510fe4
title: Sort
description: Documentation for the Sort node in n8n, a workflow automation platform. Includes guidance on usage, and links to examples.
contentType: [integration, reference]
priority: medium
---

# Sort

ใช้ Sort node เพื่อจัดเรียง (sort) รายการ item ตามลำดับที่ต้องการ หรือสุ่มเลือกข้อมูล

/// note | Array sort behavior
Sort operation จะใช้การ sort แบบ JavaScript ปกติ โดย element ที่จะ sort จะถูกแปลงเป็น string แล้วเปรียบเทียบกัน ดูรายละเอียดเพิ่มเติมได้ที่ [Mozilla's guide to Array sort](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/sort){:target=_blank .external-link}
///

## Node parameters

ตั้งค่า node นี้ด้วย parameter **Type**

เลือกวิธีการ sort ได้จาก dropdown ดังนี้

### Simple

จะทำการ sort แบบ ascending หรือ descending ตาม field ที่เลือก

เมื่อเลือก **Type** นี้:

* ใช้ปุ่ม **Add Field To Sort By** เพื่อกรอก **Field Name**
* เลือกว่าจะใช้ลำดับ **Ascending** หรือ **Descending**

#### Simple options

เมื่อเลือก **Simple** เป็น **Type** จะมี option ให้ **Disable Dot Notation** โดยปกติ n8n จะเปิด dot notation เพื่ออ้างถึง child field ในรูปแบบ `parent.child` สามารถปิด option นี้ได้ (เปิด/ปิด)

### Random

สุ่มลำดับรายการใน list

### Code

ใส่ JavaScript code เองเพื่อ custom การ sort เหมาะสำหรับกรณีที่ sort แบบ simple ไม่เพียงพอ

กรอก JavaScript code ในช่อง **Code**

## Templates and examples

[[ templatesWidget(page.title, 'sort') ]]

## Related resources

--8<-- "_snippets/integrations/builtin/core-nodes/data-transformation-actions/data-section-link.md"
