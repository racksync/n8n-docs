---
#https://www.notion.so/n8n/Frontmatter-432c2b8dff1f43d4b1c8d20075510fe4
title: เอกสารคู่มือ OpenWeatherMap node
description: เรียนรู้วิธีใช้ OpenWeatherMap node ใน n8n และดูเอกสารทางเทคนิคเพื่อเชื่อมต่อ OpenWeatherMap node เข้ากับ workflow ของคุณ
contentType: [integration, reference]
priority: medium
---

# OpenWeatherMap node

ใช้ OpenWeatherMap node เพื่อทำงานอัตโนมัติใน OpenWeatherMap และเชื่อมต่อกับแอปอื่น ๆ. n8n รองรับการดึงข้อมูลสภาพอากาศปัจจุบันและอนาคตจาก OpenWeatherMap

ในหน้านี้ คุณจะพบรายการ operations ที่ OpenWeatherMap node รองรับ พร้อมลิงก์สำหรับข้อมูลเพิ่มเติม

/// note | Credentials
ดู [OpenWeatherMap credentials](/integrations/builtin/credentials/openweathermap.md) เพื่อดูวิธีการตั้งค่า authentication
///

--8<-- "_snippets/integrations/builtin/app-nodes/ai-tools.md"

## Operations

* Returns the current weather data
* Returns the weather data for the next 5 days

## Templates and examples

<!-- see https://www.notion.so/n8n/Pull-in-templates-for-the-integrations-pages-37c716837b804d30a33b47475f6e3780 -->
[[ templatesWidget(page.title, 'openweathermap') ]]
