---
#https://www.notion.so/n8n/Frontmatter-432c2b8dff1f43d4b1c8d20075510fe4
title: SerpApi (Google Search) node documentation
description: เรียนรู้วิธีการใช้ SerpApi (Google Search) node ใน n8n พร้อมคำแนะนำทางเทคนิคในการรวม SerpApi (Google Search) node เข้ากับ workflow ของคุณ
contentType: [integration, reference]
priority: high
---

# SerpApi (Google Search) node

SerpAPI node ช่วยให้ [agent](/glossary.md#ai-agent) ใน workflow ของคุณสามารถเรียกใช้ Google Search API ได้

ในหน้านี้จะมี parameter ของ node SerpAPI และลิงก์ไปยัง resource อื่นๆ

/// note | Credentials
ดูข้อมูลการตั้งค่า authentication สำหรับ node นี้ [ที่นี่](/integrations/builtin/credentials/serp.md)
///

--8<-- "_snippets/integrations/builtin/cluster-nodes/sub-node-expression-resolution.md"

## Node options

* **Country**: กรอกรหัสประเทศที่ต้องการใช้งาน ดูรหัสประเทศที่รองรับได้ที่ [Google GL Parameter: Supported Google Countries](https://serpapi.com/google-countries){:target=_blank .external-link}
* **Device**: เลือกอุปกรณ์ที่ต้องการใช้สำหรับค้นหา
* **Explicit Array**: เลือกว่าจะบังคับให้ SerpApi ดึงผลลัพธ์ Google ใหม่ทุกครั้ง (เปิด) หรือใช้ cache (ปิด)
* **Google Domain**: กรอก Google Domain ที่ต้องการใช้งาน ดู domain ที่รองรับได้ที่ [Supported Google Domains](https://serpapi.com/google-domains)
* **Language**: กรอกรหัสภาษาที่ต้องการใช้งาน ดูรหัสภาษาที่รองรับได้ที่ [Google HL Parameter: Supported Google Languages](https://serpapi.com/google-languages){:target=_blank .external-link}

## Templates and examples

<!-- see https://www.notion.so/n8n/Pull-in-templates-for-the-integrations-pages-37c716837b804d30a33b47475f6e3780 -->
[[ templatesWidget(page.title, 'serpapi') ]]

## Related resources

ดูข้อมูลเพิ่มเติมเกี่ยวกับบริการนี้ได้ที่ [Serp's documentation](https://serpapi.com/search-api){:target=_blank .external-link} หรือดู [LangChain's documentation on their Serp integration](https://js.langchain.com/docs/integrations/tools/serpapi/){:target=_blank .external-link}

--8<-- "_snippets/integrations/builtin/cluster-nodes/langchain-overview-link.md"
--8<-- "_glossary/ai-glossary.md"
