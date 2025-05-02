---
#https://www.notion.so/n8n/Frontmatter-432c2b8dff1f43d4b1c8d20075510fe4
title: Remove Duplicates node templates and Examples
description: เอกสารสำหรับ template และตัวอย่างใน Remove Duplicates node ใน n8n แพลตฟอร์ม workflow automation รวมถึง template ที่ใช้ node และตัวอย่างการใช้งาน
contentType: [integration, reference]
priority: medium
---

# Templates and examples

นี่คือตัวอย่าง workflow และ template สำหรับ [Remove Duplicates node](/integrations/builtin/core-nodes/n8n-nodes-base.removeduplicates/index.md)

/// note | Continuous examples
ตัวอย่างในส่วนนี้จะเรียงลำดับต่อเนื่องกัน แนะนำให้ทำตามลำดับเพื่อป้องกันผลลัพธ์ที่ไม่คาดคิด
///

## Templates

<!-- see https://www.notion.so/n8n/Pull-in-templates-for-the-integrations-pages-37c716837b804d30a33b47475f6e3780 -->
[[ templatesWidget(page.title, 'remove-duplicates') ]]

## Set up sample data using the Code node

สร้าง workflow พร้อมข้อมูลตัวอย่างเพื่อทดลองใช้ Remove Duplicates node

1. เพิ่ม Code node ลงบน canvas แล้วเชื่อมต่อกับ Manual Trigger node
2. ใน Code node ให้ตั้งค่า **Mode** เป็น **Run Once for Each Item** และ **Language** เป็น **JavaScript**
3. วางโค้ด JavaScript ด้านล่างนี้ในช่อง **JavaScript**:
```js
let data =[];

return {
  data: [
    { id: 1, name: 'Taylor Swift', job: 'Pop star', last_updated: '2024-09-20T10:12:43.493Z' },
    { id: 2, name: 'Ed Sheeran', job: 'Singer-songwriter', last_updated: '2024-10-05T08:30:59.493Z' },
    { id: 3, name: 'Adele', job: 'Singer-songwriter', last_updated: '2024-10-07T14:15:59.493Z' },
    { id: 4, name: 'Bruno Mars', job: 'Singer-songwriter', last_updated: '2024-08-25T17:45:12.493Z' },
    { id: 1, name: 'Taylor Swift', job: 'Pop star', last_updated: '2024-09-20T10:12:43.493Z' },  // duplicate
    { id: 5, name: 'Billie Eilish', job: 'Singer-songwriter', last_updated: '2024-09-10T09:30:12.493Z' },
    { id: 6, name: 'Katy Perry', job: 'Pop star', last_updated: '2024-10-08T12:30:45.493Z' },
    { id: 2, name: 'Ed Sheeran', job: 'Singer-songwriter', last_updated: '2024-10-05T08:30:59.493Z' },  // duplicate
    { id: 7, name: 'Lady Gaga', job: 'Pop star', last_updated: '2024-09-15T14:45:30.493Z' },
    { id: 8, name: 'Rihanna', job: 'Pop star', last_updated: '2024-10-01T11:50:22.493Z' },
    { id: 3, name: 'Adele', job: 'Singer-songwriter', last_updated: '2024-10-07T14:15:59.493Z' },  // duplicate
    //{ id: 9, name: 'Tom Hanks', job: 'Actor', last_updated: '2024-10-17T13:58:31.493Z' },
    //{ id: 0, name: 'Madonna', job: 'Pop star', last_updated: '2024-10-17T17:11:38.493Z' },
    //{ id: 15, name: 'Bob Dylan', job: 'Folk singer', last_updated: '2024-09-24T08:03:16.493Z'},
    //{ id: 10, name: 'Harry Nilsson', job: 'Singer-songwriter', last_updated: '2020-10-17T17:11:38.493Z' },
    //{ id: 11, name: 'Kylie Minogue', job: 'Pop star', last_updated: '2024-10-24T08:03:16.493Z'},
  ]
}
```
4. เพิ่ม Split Out node ลงบน canvas แล้วเชื่อมต่อกับ Code node
5. ใน Split Out node ให้กรอก `data` ในช่อง **Fields To Split Out**

## Removing duplicates from the current input

1. เพิ่ม Remove Duplicates node ลงบน canvas แล้วเชื่อมต่อกับ Split Out node เลือก **Remove items repeated within current input** ใน **Action** เพื่อเริ่มต้น
2. เปิด Remove Duplicates node แล้วตรวจสอบว่า **Operation** ตั้งเป็น **Remove Items Repeated Within Current Input**
3. เลือก **All fields** ในช่อง **Compare**
4. กด **Test step** เพื่อรัน Remove Duplicates node ข้อมูลที่ซ้ำกันใน input จะถูกลบออก

n8n จะลบรายการที่มีข้อมูลเหมือนกันทุก field ผลลัพธ์ใน table view จะเป็นแบบนี้:

<!-- vale off -->
| **id** | **name**      | **job**           | **last_updated**         |
|--------|---------------|-------------------|--------------------------|
| 1      | Taylor Swift  | Pop star          | 2024-09-20T10:12:43.493Z |
| 2      | Ed Sheeran    | Singer-songwriter | 2024-10-05T08:30:59.493Z |
| 3      | Adele         | Singer-songwriter | 2024-10-07T14:15:59.493Z |
| 4      | Bruno Mars    | Singer-songwriter | 2024-08-25T17:45:12.493Z |
| 5      | Billie Eilish | Singer-songwriter | 2024-09-10T09:30:12.493Z |
| 6      | Katy Perry    | Pop star          | 2024-10-08T12:30:45.493Z |
| 7      | Lady Gaga     | Pop star          | 2024-09-15T14:45:30.493Z |
| 8      | Rihanna       | Pop star          | 2024-10-01T11:50:22.493Z |
<!-- vale on -->

5. เปิด Remove Duplicates node อีกครั้งแล้วเปลี่ยน **Compare** เป็น **Selected Fields**
6. ในช่อง **Fields To Compare** ให้กรอก `job`
7. กด **Test step** เพื่อรัน Remove Duplicates node ข้อมูลที่ซ้ำกันใน field `job` จะถูกลบออก

n8n จะลบรายการที่มีค่า `job` ซ้ำกันใน input ผลลัพธ์ใน table view จะเป็นแบบนี้:

<!-- vale off -->
| **id** | **name**      | **job**           | **last_updated**         |
|--------|---------------|-------------------|--------------------------|
| 1      | Taylor Swift  | Pop star          | 2024-09-20T10:12:43.493Z |
| 2      | Ed Sheeran    | Singer-songwriter | 2024-10-05T08:30:59.493Z |
<!-- vale on -->

## Keep items where the value is new

1. เปิด Remove Duplicates node แล้วตั้งค่า **Operation** เป็น **Remove Items Processed in Previous Executions**
2. ตั้งค่า **Keep Items Where** เป็น **Value Is New**
3. ตั้งค่า **Value to Dedupe On** เป็น `{{ $json.name }}`
4. บน canvas ให้เลือก **Test workflow** เพื่อรัน workflow แล้วเปิด Remove Duplicates node เพื่อดูผลลัพธ์

n8n จะเปรียบเทียบข้อมูล input กับข้อมูลที่เก็บไว้จากการรันก่อนหน้า เนื่องจากนี่เป็นการรันครั้งแรก n8n จะ process ข้อมูลทั้งหมดและแสดงในแท็บ **Kept** ลำดับอาจไม่ตรงกับ input:

<!-- vale off -->
| **id** | **name**      | **job**           | **last_updated**         |
|--------|---------------|-------------------|--------------------------|
| 1      | Taylor Swift  | Pop star          | 2024-09-20T10:12:43.493Z |
| 1      | Taylor Swift  | Pop star          | 2024-09-20T10:12:43.493Z |
| 2      | Ed Sheeran    | Singer-songwriter | 2024-10-05T08:30:59.493Z |
| 2      | Ed Sheeran    | Singer-songwriter | 2024-10-05T08:30:59.493Z |
| 3      | Adele         | Singer-songwriter | 2024-10-07T14:15:59.493Z |
| 3      | Adele         | Singer-songwriter | 2024-10-07T14:15:59.493Z |
| 4      | Bruno Mars    | Singer-songwriter | 2024-08-25T17:45:12.493Z |
| 5      | Billie Eilish | Singer-songwriter | 2024-09-10T09:30:12.493Z |
| 6      | Katy Perry    | Pop star          | 2024-10-08T12:30:45.493Z |
| 7      | Lady Gaga     | Pop star          | 2024-09-15T14:45:30.493Z |
| 8      | Rihanna       | Pop star          | 2024-10-01T11:50:22.493Z |
<!-- vale on -->

/// note | Items are only compared against previous executions
ข้อมูล input จะถูกเปรียบเทียบกับข้อมูลที่เก็บไว้จากการรันก่อนหน้าเท่านั้น หมายความว่าข้อมูลที่ซ้ำกันใน input เดียวกันจะไม่ถูกลบในโหมดนี้ ถ้าต้องการลบทั้งข้อมูลซ้ำใน input และข้าม execution ให้เชื่อมต่อ Remove Duplicate node สองตัวต่อกัน โดยตัวแรกใช้ **Remove Items Repated Within Current Input** และตัวที่สองใช้ **Remove Items Processed in Previous Executions**
///

5. เปิด Code node แล้ว uncomment (ลบ `//`) บรรทัด "Tom Hanks"
6. บน canvas เลือก **Test workflow** อีกครั้ง แล้วเปิด Remove Duplicates node เพื่อดูผลลัพธ์

n8n จะเปรียบเทียบข้อมูล input กับข้อมูลที่เก็บไว้จากการรันก่อนหน้า คราวนี้แท็บ **Kept** จะมีแค่ record ใหม่จาก Code node:

<!-- vale off -->
| **id** | **name**  | **job** | **last_updated**         |
|--------|-----------|---------|--------------------------|
| 9      | Tom Hanks | Actor   | 2024-10-17T13:58:31.493Z |
<!-- vale on -->

แท็บ **Discarded** จะมีข้อมูลที่ process ไปแล้วจากการรันก่อนหน้า:

<!-- vale off -->
| **id** | **name**      | **job**           | **last_updated**         |
|--------|---------------|-------------------|--------------------------|
| 1      | Taylor Swift  | Pop star          | 2024-09-20T10:12:43.493Z |
| 1      | Taylor Swift  | Pop star          | 2024-09-20T10:12:43.493Z |
| 2      | Ed Sheeran    | Singer-songwriter | 2024-10-05T08:30:59.493Z |
| 2      | Ed Sheeran    | Singer-songwriter | 2024-10-05T08:30:59.493Z |
| 3      | Adele         | Singer-songwriter | 2024-10-07T14:15:59.493Z |
| 3      | Adele         | Singer-songwriter | 2024-10-07T14:15:59.493Z |
| 4      | Bruno Mars    | Singer-songwriter | 2024-08-25T17:45:12.493Z |
| 5      | Billie Eilish | Singer-songwriter | 2024-09-10T09:30:12.493Z |
| 6      | Katy Perry    | Pop star          | 2024-10-08T12:30:45.493Z |
| 7      | Lady Gaga     | Pop star          | 2024-09-15T14:45:30.493Z |
| 8      | Rihanna       | Pop star          | 2024-10-01T11:50:22.493Z |
<!-- vale on -->

ก่อนจะไปตัวอย่างถัดไป ให้เคลียร์ประวัติการ dedupe:

7. เปิด Remove Duplicates node แล้วตั้งค่า **Operation** เป็น **Clear Deduplication History**
8. กด **Test step** เพื่อเคลียร์ประวัติ dedupe

## Keep items where the value is higher than any previous value

1. เปิด Remove Duplicates node แล้วตั้งค่า **Operation** เป็น **Remove Items Processed in Previous Executions**
2. ตั้งค่า **Keep Items Where** เป็น **Value Is Higher than Any Previous Value**
3. ตั้งค่า **Value to Dedupe On** เป็น `{{ $json.id }}`
4. บน canvas เลือก **Test workflow** เพื่อรัน workflow แล้วเปิด Remove Duplicates node เพื่อดูผลลัพธ์

n8n จะเปรียบเทียบข้อมูล input กับข้อมูลที่เก็บไว้จากการรันก่อนหน้า เนื่องจากเพิ่งเคลียร์ประวัติ n8n จะ process ข้อมูลทั้งหมดและแสดงในแท็บ **Kept** ลำดับอาจไม่ตรงกับ input:

<!-- vale off -->
| **id** | **name**      | **job**           | **last_updated**         |
|--------|---------------|-------------------|--------------------------|
| 1      | Taylor Swift  | Pop star          | 2024-09-20T10:12:43.493Z |
| 1      | Taylor Swift  | Pop star          | 2024-09-20T10:12:43.493Z |
| 2      | Ed Sheeran    | Singer-songwriter | 2024-10-05T08:30:59.493Z |
| 2      | Ed Sheeran    | Singer-songwriter | 2024-10-05T08:30:59.493Z |
| 3      | Adele         | Singer-songwriter | 2024-10-07T14:15:59.493Z |
| 3      | Adele         | Singer-songwriter | 2024-10-07T14:15:59.493Z |
| 4      | Bruno Mars    | Singer-songwriter | 2024-08-25T17:45:12.493Z |
| 5      | Billie Eilish | Singer-songwriter | 2024-09-10T09:30:12.493Z |
| 6      | Katy Perry    | Pop star          | 2024-10-08T12:30:45.493Z |
| 7      | Lady Gaga     | Pop star          | 2024-09-15T14:45:30.493Z |
| 8      | Rihanna       | Pop star          | 2024-10-01T11:50:22.493Z |
| 9      | Tom Hanks     | Actor             | 2024-10-17T13:58:31.493Z |
<!-- vale on -->

5. เปิด Code node แล้ว uncomment (ลบ `//`) บรรทัด "Madonna" และ "Bob Dylan"
6. บน canvas เลือก **Test workflow** อีกครั้ง แล้วเปิด Remove Duplicates node เพื่อดูผลลัพธ์

n8n จะเปรียบเทียบข้อมูล input กับข้อมูลที่เก็บไว้จากการรันก่อนหน้า คราวนี้แท็บ **Kept** จะมีแค่ "Bob Dylan" เพราะค่า `id` (15) สูงกว่าค่าสูงสุดก่อนหน้า (9):

<!-- vale off -->
| **id** | **name**  | **job**     | **last_updated**         |
|--------|-----------|-------------|--------------------------|
| 15     | Bob Dylan | Folk singer | 2024-09-24T08:03:16.493Z |
<!-- vale on -->

แท็บ **Discarded** จะมีข้อมูล 13 รายการที่ค่า `id` เท่ากับหรือน้อยกว่าค่าสูงสุดก่อนหน้า (9) แม้ "Madonna" จะเป็นข้อมูลใหม่แต่ `id` ไม่สูงกว่าเดิม:

<!-- vale off -->
| **id** | **name**      | **job**           | **last_updated**         |
|--------|---------------|-------------------|--------------------------|
| 0      | Madonna       | Pop star          | 2024-10-17T17:11:38.493Z |
| 1      | Taylor Swift  | Pop star          | 2024-09-20T10:12:43.493Z |
| 1      | Taylor Swift  | Pop star          | 2024-09-20T10:12:43.493Z |
| 2      | Ed Sheeran    | Singer-songwriter | 2024-10-05T08:30:59.493Z |
| 2      | Ed Sheeran    | Singer-songwriter | 2024-10-05T08:30:59.493Z |
| 3      | Adele         | Singer-songwriter | 2024-10-07T14:15:59.493Z |
| 3      | Adele         | Singer-songwriter | 2024-10-07T14:15:59.493Z |
| 4      | Bruno Mars    | Singer-songwriter | 2024-08-25T17:45:12.493Z |
| 5      | Billie Eilish | Singer-songwriter | 2024-09-10T09:30:12.493Z |
| 6      | Katy Perry    | Pop star          | 2024-10-08T12:30:45.493Z |
| 7      | Lady Gaga     | Pop star          | 2024-09-15T14:45:30.493Z |
| 8      | Rihanna       | Pop star          | 2024-10-01T11:50:22.493Z |
| 9      | Tom Hanks     | Actor             | 2024-10-17T13:58:31.493Z |
<!-- vale on -->

ก่อนจะไปตัวอย่างถัดไป ให้เคลียร์ประวัติการ dedupe:

7. เปิด Remove Duplicates node แล้วตั้งค่า **Operation** เป็น **Clear Deduplication History**
8. กด **Test step** เพื่อเคลียร์ประวัติ dedupe

## Keep items where the value is a date later than any previous date

1. เปิด Remove Duplicates node แล้วตั้งค่า **Operation** เป็น **Remove Items Processed in Previous Executions**
2. ตั้งค่า **Keep Items Where** เป็น **Value Is a Date Later than Any Previous Date**
3. ตั้งค่า **Value to Dedupe On** เป็น `{{ $json.last_updated }}`
4. บน canvas เลือก **Test workflow** เพื่อรัน workflow แล้วเปิด Remove Duplicates node เพื่อดูผลลัพธ์

n8n จะเปรียบเทียบข้อมูล input กับข้อมูลที่เก็บไว้จากการรันก่อนหน้า เนื่องจากเพิ่งเคลียร์ประวัติ n8n จะ process ข้อมูลทั้งหมดและแสดงในแท็บ **Kept** ลำดับอาจไม่ตรงกับ input:

<!-- vale off -->
| **id** | **name**      | **job**           | **last_updated**         |
|--------|---------------|-------------------|--------------------------|
| 0      | Madonna       | Pop star          | 2024-10-17T17:11:38.493Z |
| 1      | Taylor Swift  | Pop star          | 2024-09-20T10:12:43.493Z |
| 1      | Taylor Swift  | Pop star          | 2024-09-20T10:12:43.493Z |
| 2      | Ed Sheeran    | Singer-songwriter | 2024-10-05T08:30:59.493Z |
| 2      | Ed Sheeran    | Singer-songwriter | 2024-10-05T08:30:59.493Z |
| 3      | Adele         | Singer-songwriter | 2024-10-07T14:15:59.493Z |
| 3      | Adele         | Singer-songwriter | 2024-10-07T14:15:59.493Z |
| 4      | Bruno Mars    | Singer-songwriter | 2024-08-25T17:45:12.493Z |
| 5      | Billie Eilish | Singer-songwriter | 2024-09-10T09:30:12.493Z |
| 6      | Katy Perry    | Pop star          | 2024-10-08T12:30:45.493Z |
| 7      | Lady Gaga     | Pop star          | 2024-09-15T14:45:30.493Z |
| 8      | Rihanna       | Pop star          | 2024-10-01T11:50:22.493Z |
| 9      | Tom Hanks     | Actor             | 2024-10-17T13:58:31.493Z |
| 15     | Bob Dylan     | Folk singer       | 2024-09-24T08:03:16.493Z |
<!-- vale on -->

<!-- vale off -->
5. เปิด Code node แล้ว uncomment (ลบ `//`) บรรทัด "Harry Nilsson" และ "Kylie Minogue"
<!-- vale on -->
6. บน canvas เลือก **Test workflow** อีกครั้ง แล้วเปิด Remove Duplicates node เพื่อดูผลลัพธ์

<!-- vale off -->
n8n จะเปรียบเทียบข้อมูล input กับข้อมูลที่เก็บไว้จากการรันก่อนหน้า คราวนี้แท็บ **Kept** จะมีแค่ "Kylie Minogue" เพราะค่า `last_updated` (`2024-10-24T08:03:16.493Z`) ใหม่กว่าค่าสูงสุดก่อนหน้า (`2024-10-17T17:11:38.493Z`):
<!-- vale on -->

<!-- vale off -->
| **id** | **name**      | **job**           | **last_updated**         |
|--------|---------------|-------------------|--------------------------|
| 11     | Kylie Minogue | Pop star          | 2024-10-24T08:03:16.493Z |
<!-- vale on -->

แท็บ **Discarded** จะมีข้อมูล 15 รายการที่ค่า `last_updated` เท่ากับหรือน้อยกว่าค่าสูงสุดก่อนหน้า (`2024-10-17T17:11:38.493Z`) แม้ "Harry Nilsson" จะเป็นข้อมูลใหม่แต่ `last_updated` ไม่ใหม่กว่าเดิม:

<!-- vale off -->
| **id** | **name**      | **job**           | **last_updated**         |
|--------|---------------|-------------------|--------------------------|
| 10     | Harry Nilsson | Singer-songwriter | 2020-10-17T17:11:38.493Z |
| 0      | Madonna       | Pop star          | 2024-10-17T17:11:38.493Z |
| 1      | Taylor Swift  | Pop star          | 2024-09-20T10:12:43.493Z |
| 1      | Taylor Swift  | Pop star          | 2024-09-20T10:12:43.493Z |
| 2      | Ed Sheeran    | Singer-songwriter | 2024-10-05T08:30:59.493Z |
| 2      | Ed Sheeran    | Singer-songwriter | 2024-10-05T08:30:59.493Z |
| 3      | Adele         | Singer-songwriter | 2024-10-07T14:15:59.493Z |
| 3      | Adele         | Singer-songwriter | 2024-10-07T14:15:59.493Z |
| 4      | Bruno Mars    | Singer-songwriter | 2024-08-25T17:45:12.493Z |
| 5      | Billie Eilish | Singer-songwriter | 2024-09-10T09:30:12.493Z |
| 6      | Katy Perry    | Pop star          | 2024-10-08T12:30:45.493Z |
| 7      | Lady Gaga     | Pop star          | 2024-09-15T14:45:30.493Z |
| 8      | Rihanna       | Pop star          | 2024-10-01T11:50:22.493Z |
| 9      | Tom Hanks     | Actor             | 2024-10-17T13:58:31.493Z |
| 15     | Bob Dylan     | Folk singer       | 2024-09-24T08:03:16.493Z |
<!-- vale on -->
