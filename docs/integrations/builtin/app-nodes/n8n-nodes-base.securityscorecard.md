---
#https://www.notion.so/n8n/Frontmatter-432c2b8dff1f43d4b1c8d20075510fe4
title: SecurityScorecard node documentation
description: Learn how to use the SecurityScorecard node in n8n. Follow technical documentation to integrate SecurityScorecard node into your workflows.
contentType: [integration, reference]
---

# SecurityScorecard node

ใช้ SecurityScorecard node เพื่อให้การทำงานใน SecurityScorecard เป็นไปโดยอัตโนมัติและเชื่อมต่อกับแอปพลิเคชันอื่น ๆ ได้อย่างมีประสิทธิภาพ. n8n รองรับฟีเจอร์ของ SecurityScorecard หลากหลาย เช่น การสร้าง, อัปเดต, ลบ, และดึงข้อมูล portfolio รวมถึงการดึงข้อมูลของบริษัท.

/// note | Credentials
ดู [SecurityScorecard credentials](/integrations/builtin/credentials/securityscorecard.md) สำหรับคำแนะนำในการตั้งค่า authentication. 
///

## Operations

* Company
    * Get company factor scores and issue counts
    * Get company's historical factor scores
    * Get company's historical scores
    * Get company information and summary of their scorecard
    * Get company's score improvement plan
* Industry
    * Get Factor Scores
    * Get Historical Factor Scores
    * Get Score
* Invite
    * Create an invite for a company/user
* Portfolio
    * Create a portfolio
    * Delete a portfolio
    * Get all portfolios
    * Update a portfolio
* Portfolio Company
    * Add a company to portfolio
    * Get all companies in a portfolio
    * Remove a company from portfolio
* Report
    * Download a generated report
    * Generate a report
    * Get list of recently generated report

## Templates and examples

<!-- see https://www.notion.so/n8n/Pull-in-templates-for-the-integrations-pages-37c716837b804d30a33b47475f6e3780 -->
[[ templatesWidget(page.title, 'securityscorecard') ]]
