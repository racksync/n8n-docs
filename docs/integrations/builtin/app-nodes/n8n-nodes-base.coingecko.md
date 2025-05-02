---
#https://www.notion.so/n8n/Frontmatter-432c2b8dff1f43d4b1c8d20075510fe4
title: CoinGecko node documentation
description: Learn how to use the CoinGecko node in n8n. Follow technical documentation to integrate CoinGecko node into your workflows.
contentType: [integration, reference]
---

# CoinGecko node

ใช้ CoinGecko node เพื่อทำงานอัตโนมัติใน CoinGecko และ integrate CoinGecko กับแอปพลิเคชันอื่นๆ n8n มีการรองรับในตัวสำหรับฟีเจอร์ต่างๆ ของ CoinGecko รวมถึงการดึง coins และ events

ในหน้านี้ คุณจะพบรายการ operations ที่ CoinGecko node รองรับ และลิงก์ไปยังแหล่งข้อมูลเพิ่มเติม

--8<-- "_snippets/integrations/builtin/app-nodes/ai-tools.md"

## Operations

* Coin
    * รับกราฟแท่งเทียน open-high-low-close สำหรับสกุลเงินที่เลือก
    * รับข้อมูลปัจจุบันสำหรับเหรียญ
    * รับเหรียญทั้งหมด
    * รับข้อมูลประวัติ (ชื่อ, ราคา, ตลาด, สถิติ) ในวันที่กำหนดสำหรับเหรียญ
    * รับราคาหรือข้อมูลตลาดที่เกี่ยวข้องสำหรับคู่การซื้อขายทั้งหมดที่ตรงกับสกุลเงินที่เลือก
    * รับข้อมูลตลาดประวัติรวมถึงราคา, มูลค่าตลาด, และปริมาณ 24 ชั่วโมง (ความละเอียดอัตโนมัติ)
    * รับราคาปัจจุบันของสกุลเงินดิจิทัลใดๆ ในสกุลเงินอื่นๆ ที่รองรับที่คุณต้องการ
    * รับ tickers ของเหรียญ
* Event
    * รับ events ทั้งหมด

## Templates and examples

<!-- see https://www.notion.so/n8n/Pull-in-templates-for-the-integrations-pages-37c716837b804d30a33b47475f6e3780 -->
[[ templatesWidget(page.title, 'coingecko') ]]
