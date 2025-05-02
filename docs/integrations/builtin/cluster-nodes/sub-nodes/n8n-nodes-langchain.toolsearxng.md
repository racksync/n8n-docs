---
#https://www.notion.so/n8n/Frontmatter-432c2b8dff1f43d4b1c8d20075510fe4
title: SearXNG Tool node documentation
description: Learn how to use the SearXNG Tool node in n8n. Follow technical documentation to integrate SearXNG Tool node into your workflows.
contentType: [integration, reference]
---

# SearXNG Tool node

SearXNG Tool node ช่วยให้คุณเพิ่มความสามารถในการค้นหา (search) ใน workflow ของคุณโดยใช้ SearXNG ซึ่งจะรวมผลลัพธ์จาก search engine หลายตัวโดยไม่ track ข้อมูลของคุณ

ในหน้านี้จะมี option ของ node SearXNG Tool และลิงก์ไปยัง resource อื่นๆ

/// note | Credentials
ดูข้อมูลการตั้งค่า authentication สำหรับ node นี้ [ที่นี่](/integrations/builtin/credentials/searxng.md)
///

--8<-- "_snippets/integrations/builtin/cluster-nodes/sub-node-expression-resolution.md"

## Node Options

* **Number of Results**: จำนวนผลลัพธ์ที่ต้องการดึงมา ค่าเริ่มต้นคือ 10
* **Page Number**: เลขหน้าของผลลัพธ์ที่ต้องการดึง ค่าเริ่มต้นคือ 1
* **Language**: รหัสภาษา 2 ตัวอักษร ([language code](https://en.wikipedia.org/wiki/List_of_ISO_639_language_codes)) เพื่อกรองผลลัพธ์ ตัวอย่างเช่น `en` สำหรับภาษาอังกฤษ, `fr` สำหรับภาษาฝรั่งเศส ค่าเริ่มต้นคือ `en`
* **Safe Search**: เปิดหรือปิดการกรองเนื้อหาที่ไม่เหมาะสมในผลลัพธ์ เลือกได้เป็น None, Moderate, หรือ Strict ค่าเริ่มต้นคือ None

## Running a SearXNG instance

node นี้ต้องใช้ SearXNG service ที่รันอยู่ใน network เดียวกับ n8n instance ของคุณ ตรวจสอบให้แน่ใจว่า n8n instance ของคุณเข้าถึง SearXNG service ได้

node นี้ต้องการผลลัพธ์เป็น JSON ซึ่งค่า default ของ SearXNG จะยังไม่เปิด JSON output ต้องเพิ่ม `json` ใน section `search.formats` ของไฟล์ `settings.yml` ของ SearXNG instance:

```yaml
search:
  # options available for formats: [html, csv, json, rss]
  formats:
    - html
    - json
```

ถ้า section `formats` ยังไม่มี ให้เพิ่มเข้าไป ตำแหน่งของไฟล์ `settings.yml` ขึ้นอยู่กับวิธีที่คุณติดตั้ง SearXNG ดูรายละเอียดเพิ่มเติมได้ที่ [SearXNG configuration documentation](https://docs.searxng.org/admin/installation-searxng.html#configuration)

คุณภาพและความพร้อมของผลลัพธ์ขึ้นอยู่กับการตั้งค่าและสุขภาพของ SearXNG instance ที่คุณใช้

## Templates and examples

<!-- see https://www.notion.so/n8n/Pull-in-templates-for-the-integrations-pages-37c716837b804d30a33b47475f6e3780 -->
[[ templatesWidget(page.title, 'searxng') ]]

## Related resources

ดูข้อมูลเพิ่มเติมเกี่ยวกับบริการนี้ได้ที่ [SearXNG's documentation](https://docs.searxng.org/) หรือดู [LangChain's documentation on their SearXNG integration](https://python.langchain.com/docs/integrations/tools/searx_search/)

--8<-- "_snippets/integrations/builtin/cluster-nodes/langchain-overview-link.md"
--8<-- "_glossary/ai-glossary.md"
