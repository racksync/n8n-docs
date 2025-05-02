---
#https://www.notion.so/n8n/Frontmatter-432c2b8dff1f43d4b1c8d20075510fe4
contentType: tutorial
---

# Workflow 2: Generating reports

ใน workflow นี้ คุณจะรวมข้อมูลจากแหล่งต่างๆ, แปลง binary data, สร้างไฟล์, และส่งการแจ้งเตือนเกี่ยวกับไฟล์เหล่านั้น workflow สุดท้ายควรมีลักษณะดังนี้:

<figure><img src="/_images/courses/level-two/chapter-five/workflow2.png" alt="Workflow 2 for aggregating data and generating files" style="width:100%"><figcaption align = "center"><i>Workflow 2 for aggregating data and generating files</i></figcaption></figure>

เพื่อให้ง่ายขึ้น มาแบ่ง workflow ออกเป็นสามส่วนกัน

## Part 1: Getting data from different sources

ส่วนแรกของ workflow ประกอบด้วยห้า nodes:

<figure><img src="/_images/courses/level-two/chapter-five/workflow2_1.png" alt="Workflow 1: Getting data from different sources" style="width:100%"><figcaption align = "center"><i>Workflow 1: Getting data from different sources</i></figcaption></figure>

1. ใช้ [**HTTP Request node**](/integrations/builtin/core-nodes/n8n-nodes-base.httprequest/index.md) เพื่อรับข้อมูลจาก API endpoint ที่เก็บข้อมูลบริษัท กำหนดค่า node parameters ต่อไปนี้:

    - **Method**: Get
    - **URL**: **Dataset URL** ที่คุณได้รับในอีเมลเมื่อคุณลงทะเบียนสำหรับคอร์สนี้
    - **Authentication**: Generic Credential Type
        - **Generic Auth Type**: Header Auth
        - **Credentials for Header Auth**: Header Auth name และ Header Auth value ที่คุณได้รับในอีเมลเมื่อคุณลงทะเบียนสำหรับคอร์สนี้
    - **Send Headers**: สลับเป็น true
        - **Specify Headers**: เลือก `Using Fields Below`
        - **Name**: `unique_id`
        - **Value**: unique ID ที่คุณได้รับในอีเมลเมื่อคุณลงทะเบียนสำหรับคอร์สนี้

2. ใช้ [**Airtable node**](/integrations/builtin/app-nodes/n8n-nodes-base.airtable/index.md) เพื่อ list ข้อมูลจากตาราง `customers` (ที่คุณอัปเดต fields `region` และ `subregion`)
3. ใช้ [**Merge node**](/integrations/builtin/core-nodes/n8n-nodes-base.merge.md) เพื่อรวมข้อมูลจาก Airtable และ HTTP Request node โดยอิงจากการจับคู่ input fields สำหรับ `customerID`
4. ใช้ [**Sort node**](/integrations/builtin/core-nodes/n8n-nodes-base.sort.md) เพื่อเรียงลำดับข้อมูลตาม `orderPrice` จากมากไปน้อย

/// question | Quiz questions
* ชื่อของพนักงานที่ได้รับมอบหมายให้ดูแล customer 1 คืออะไร?
* สถานะ order ของ customer 2 คืออะไร?
* ราคา order สูงสุดคือเท่าไหร่?
///

## Part 2: Generating file for regional sales

ส่วนที่สองของ workflow ประกอบด้วยสี่ nodes:

<figure><img src="/_images/courses/level-two/chapter-five/workflow2_2.png" alt="Workflow 2: Generating file for regional sales" style="width:100%"><figcaption align = "center"><i>Workflow 2: Generating file for regional sales</i></figcaption></figure>

1. ใช้ [**If node**](/integrations/builtin/core-nodes/n8n-nodes-base.if.md) เพื่อกรองให้แสดงเฉพาะ orders จาก region `Americas`
2. ใช้ [**Convert to File**](/integrations/builtin/core-nodes/n8n-nodes-base.converttofile.md) เพื่อแปลงข้อมูลขาเข้าจากรูปแบบ JSON เป็น binary แปลงแต่ละ item เป็นไฟล์แยกกัน (คะแนนโบนัสถ้าคุณสามารถหาวิธีตั้งชื่อแต่ละ report ตาม orderID ได้!)
3. ใช้ [**Gmail node**](/integrations/builtin/app-nodes/n8n-nodes-base.gmail/index.md) (หรือ email node อื่น) เพื่อส่งไฟล์ทางอีเมลไปยังที่อยู่ที่คุณเข้าถึงได้ โปรดทราบว่าคุณต้องเพิ่ม attachment ด้วย data property
4. ใช้ [**Discord node**](/integrations/builtin/app-nodes/n8n-nodes-base.discord/index.md) เพื่อส่งข้อความในช่อง Discord ของ n8n `#course-level-two` ใน node ให้กำหนดค่า parameters ต่อไปนี้:
    * **Webhook URL**: Discord URL ที่คุณได้รับในอีเมลเมื่อคุณลงทะเบียนสำหรับคอร์สนี้
    * **Text**: "I sent the file using email with the label ID `{label ID}`. My ID: " ตามด้วย unique ID ที่ส่งให้คุณทางอีเมลเมื่อคุณลงทะเบียนสำหรับคอร์สนี้ <br/> โปรดทราบว่าคุณต้องแทนที่ข้อความในวงเล็บปีกกา `{}` ด้วย [expressions](/glossary.md#expression-n8n) ที่อ้างอิงข้อมูลจาก nodes

/// question | Quiz questions
* มี orders กี่รายการที่ถูกกำหนดให้กับ region `Americas`?
* ราคารวมของ orders ใน region `Americas` คือเท่าไหร่?
* **Write Binary File node** คืนค่ากี่ items?
///

## Part 3: Generating files for total sales

ส่วนที่สามของ workflow ประกอบด้วยห้า nodes:

<figure><img src="/_images/courses/level-two/chapter-five/workflow2_3.png" alt="Workflow 3: Generating files for total sales" style="width:100%"><figcaption align = "center"><i>Workflow 3: Generating files for total sales</i></figcaption></figure>

1. ใช้ [**Loop Over Items node**](/integrations/builtin/core-nodes/n8n-nodes-base.splitinbatches.md) เพื่อแบ่งข้อมูลจาก Item Lists node ออกเป็น batches ละ 5 รายการ
2. ใช้ [**Set node**](/integrations/builtin/core-nodes/n8n-nodes-base.set.md) เพื่อตั้งค่าสี่ values โดยอ้างอิงด้วย expressions จาก node ก่อนหน้า: `customerEmail`, `customerRegion`, `customerSince`, และ `orderPrice`
3. ใช้ [**Date & Time node**](/integrations/builtin/core-nodes/n8n-nodes-base.datetime.md) เพื่อเปลี่ยนรูปแบบวันที่ของ field `customerSince` เป็นรูปแบบ MM/DD/YYYY
    - ตั้งค่า option **Include Input Fields** เพื่อเก็บข้อมูลทั้งหมดไว้ด้วยกัน
4. ใช้ [**Convert to File node**](/integrations/builtin/core-nodes/n8n-nodes-base.converttofile.md) เพื่อสร้าง spreadsheet CSV โดยตั้งชื่อไฟล์เป็น expression: `{{$runIndex > 0 ? 'file_low_orders':'file_high_orders'}}`
5. ใช้ [**Discord node**](/integrations/builtin/app-nodes/n8n-nodes-base.discord/index.md) เพื่อส่งข้อความในช่อง Discord ของ n8n `#course-level-two` ใน node ให้กำหนดค่า parameters ต่อไปนี้:
    * **Webhook URL**: Discord URL ที่คุณได้รับในอีเมลเมื่อคุณลงทะเบียนสำหรับคอร์สนี้
    * **Text**: "I created the spreadsheet `{file name}`. My ID:" ตามด้วย unique ID ที่ส่งให้คุณทางอีเมลเมื่อคุณลงทะเบียนสำหรับคอร์สนี้ <br/> โปรดทราบว่าคุณต้องแทนที่ `{file name}` ด้วย expression ที่อ้างอิงข้อมูลจาก **Convert to File node** ก่อนหน้า<br/>

/// question | Quiz questions
* ราคา order ต่ำสุดใน batch แรกของ items คือเท่าไหร่?
* วันที่ที่จัดรูปแบบแล้วของ customer 7 คืออะไร?
* **Convert to File node** คืนค่ากี่ items?
///

??? note "Show me the solution"

	หากต้องการตรวจสอบการกำหนดค่าของ nodes คุณสามารถคัดลอกโค้ด JSON workflow ด้านล่างและวางลงใน Editor UI ของคุณ:

	```json
    {
    "meta": {
        "templateCredsSetupCompleted": true,
        "instanceId": "cb484ba7b742928a2048bf8829668bed5b5ad9787579adea888f05980292a4a7"
    },
    "nodes": [
        {
        "parameters": {
            "sendTo": "bart@n8n.io",
            "subject": "Your TPS Reports",
            "emailType": "text",
            "message": "Please find your TPS report attached.",
            "options": {
            "attachmentsUi": {
                "attachmentsBinary": [
                {}
                ]
            }
            }
        },
        "id": "d889eb42-8b34-4718-b961-38c8e7839ea6",
        "name": "Gmail",
        "type": "n8n-nodes-base.gmail",
        "typeVersion": 2.1,
        "position": [
            2100,
            500
        ],
        "credentials": {
            "gmailOAuth2": {
            "id": "HFesCcFcn1NW81yu",
            "name": "Gmail account 7"
            }
        }
        },
        {
        "parameters": {},
        "id": "c0236456-40be-4f8f-a730-e56cb62b7b5c",
        "name": "When clicking \"Test workflow\"",
        "type": "n8n-nodes-base.manualTrigger",
        "typeVersion": 1,
        "position": [
            780,
            600
        ]
        },
        {
        "parameters": {
            "url": "https://internal.users.n8n.cloud/webhook/level2-erp",
            "authentication": "genericCredentialType",
            "genericAuthType": "httpHeaderAuth",
            "sendHeaders": true,
            "headerParameters": {
            "parameters": [
                {
                "name": "unique_id",
                "value": "recFIcD6UlSyxaVMQ"
                }
            ]
            },
            "options": {}
        },
        "id": "cc106fa0-6630-4c84-aea4-a4c7a3c149e9",
        "name": "HTTP Request",
        "type": "n8n-nodes-base.httpRequest",
        "typeVersion": 4.1,
        "position": [
            1000,
            500
        ],
        "credentials": {
            "httpHeaderAuth": {
            "id": "qeHdJdqqqaTC69cm",
            "name": "Course L2 Credentials"
            }
        }
        },
        {
        "parameters": {
            "operation": "search",
            "base": {
            "__rl": true,
            "value": "apprtKkVasbQDbFa1",
            "mode": "list",
            "cachedResultName": "All your base",
            "cachedResultUrl": "https://airtable.com/apprtKkVasbQDbFa1"
            },
            "table": {
            "__rl": true,
            "value": "tblInZ7jeNdlUOvxZ",
            "mode": "list",
            "cachedResultName": "Course L2, Workflow 1",
            "cachedResultUrl": "https://airtable.com/apprtKkVasbQDbFa1/tblInZ7jeNdlUOvxZ"
            },
            "options": {}
        },
        "id": "e5ae1927-b531-401c-9cb2-ecf1f2836ba6",
        "name": "Airtable",
        "type": "n8n-nodes-base.airtable",
        "typeVersion": 2,
        "position": [
            1000,
            700
        ],
        "credentials": {
            "airtableTokenApi": {
            "id": "MIplo6lY3AEsdf7L",
            "name": "Airtable Personal Access Token account 4"
            }
        }
        },
        {
        "parameters": {
            "mode": "combine",
            "mergeByFields": {
            "values": [
                {
                "field1": "customerID",
                "field2": "customerID"
                }
            ]
            },
            "options": {}
        },
        "id": "1cddc984-7fca-45e0-83b8-0c502cb4c78c",
        "name": "Merge",
        "type": "n8n-nodes-base.merge",
        "typeVersion": 2.1,
        "position": [
            1220,
            600
        ]
        },
        {
        "parameters": {
            "sortFieldsUi": {
            "sortField": [
                {
                "fieldName": "orderPrice",
                "order": "descending"
                }
            ]
            },
            "options": {}
        },
        "id": "2f55af2e-f69b-4f61-a9e5-c7eefaad93ba",
        "name": "Sort",
        "type": "n8n-nodes-base.sort",
        "typeVersion": 1,
        "position": [
            1440,
            600
        ]
        },
        {
        "parameters": {
            "conditions": {
            "options": {
                "caseSensitive": true,
                "leftValue": "",
                "typeValidation": "strict"
            },
            "conditions": [
                {
                "id": "d3afe65c-7c80-4caa-9d1c-33c62fbc2197",
                "leftValue": "={{ $json.region }}",
                "rightValue": "Americas",
                "operator": {
                    "type": "string",
                    "operation": "equals",
                    "name": "filter.operator.equals"
                }
                }
            ],
            "combinator": "and"
            },
            "options": {}
        },
        "id": "2ed874a9-5bcf-4cc9-9b52-ea503a562892",
        "name": "If",
        "type": "n8n-nodes-base.if",
        "typeVersion": 2,
        "position": [
            1660,
            500
        ]
        },
        {
        "parameters": {
            "operation": "toJson",
            "mode": "each",
            "options": {
            "fileName": "=report_orderID_{{ $('If').item.json.orderID }}.json"
            }
        },
        "id": "d93b4429-2200-4a84-8505-16266fedfccd",
        "name": "Convert to File",
        "type": "n8n-nodes-base.convertToFile",
        "typeVersion": 1.1,
        "position": [
            1880,
            500
        ]
        },
        {
        "parameters": {
            "authentication": "webhook",
            "content": "I sent the file using email with the label ID  and wrote the binary file {file name}. My ID: 123",
            "options": {}
        },
        "id": "26f43f2c-1422-40de-9f40-dd2d80926b1c",
        "name": "Discord",
        "type": "n8n-nodes-base.discord",
        "typeVersion": 2,
        "position": [
            2320,
            500
        ],
        "credentials": {
            "discordWebhookApi": {
            "id": "WEBrtPdoLrhlDYKr",
            "name": "L2 Course Discord Webhook account"
            }
        }
        },
        {
        "parameters": {
            "batchSize": 5,
            "options": {}
        },
        "id": "0fa1fbf6-fe77-4044-a445-c49a1db37dec",
        "name": "Loop Over Items",
        "type": "n8n-nodes-base.splitInBatches",
        "typeVersion": 3,
        "position": [
            1660,
            700
        ]
        },
        {
        "parameters": {
            "assignments": {
            "assignments": [
                {
                "id": "ce839b80-c50d-48f5-9a24-bb2df6fdd2ff",
                "name": "customerEmail",
                "value": "={{ $json.customerEmail }}",
                "type": "string"
                },
                {
                "id": "0c613366-3808-45a2-89cc-b34c7b9f3fb7",
                "name": "region",
                "value": "={{ $json.region }}",
                "type": "string"
                },
                {
                "id": "0f19a88c-deb0-4119-8965-06ed62a840b2",
                "name": "customerSince",
                "value": "={{ $json.customerSince }}",
                "type": "string"
                },
                {
                "id": "a7e890d6-86af-4839-b5df-d2a4efe923f7",
                "name": "orderPrice",
                "value": "={{ $json.orderPrice }}",
                "type": "number"
                }
            ]
            },
            "options": {}
        },
        "id": "09b8584c-4ead-4007-a6cd-edaa4669a757",
        "name": "Edit Fields",
        "type": "n8n-nodes-base.set",
        "typeVersion": 3.3,
        "position": [
            1880,
            700
        ]
        },
        {
        "parameters": {
            "operation": "formatDate",
            "date": "={{ $json.customerSince }}",
            "options": {
            "includeInputFields": true
            }
        },
        "id": "c96fae90-e080-48dd-9bff-3e4506aafb86",
        "name": "Date & Time",
        "type": "n8n-nodes-base.dateTime",
        "typeVersion": 2,
        "position": [
            2100,
            700
        ]
        },
        {
        "parameters": {
            "options": {
            "fileName": "={{$runIndex > 0 ? 'file_low_orders':'file_high_orders'}}"
            }
        },
        "id": "43dc8634-2f16-442b-a754-89f47c51c591",
        "name": "Convert to File1",
        "type": "n8n-nodes-base.convertToFile",
        "typeVersion": 1.1,
        "position": [
            2320,
            700
        ]
        },
        {
        "parameters": {
            "authentication": "webhook",
            "content": "I created the spreadsheet {file name}. My ID: 123",
            "options": {}
        },
        "id": "05da1c22-d1f6-4ea6-9102-f74f9ae2e9d3",
        "name": "Discord1",
        "type": "n8n-nodes-base.discord",
        "typeVersion": 2,
        "position": [
            2540,
            700
        ],
        "credentials": {
            "discordWebhookApi": {
            "id": "WEBrtPdoLrhlDYKr",
            "name": "L2 Course Discord Webhook account"
            }
        }
        }
    ],
    "connections": {
        "Gmail": {
        "main": [
            [
            {
                "node": "Discord",
                "type": "main",
                "index": 0
            }
            ]
        ]
        },
        "When clicking \"Test workflow\"": {
        "main": [
            [
            {
                "node": "HTTP Request",
                "type": "main",
                "index": 0
            },
            {
                "node": "Airtable",
                "type": "main",
                "index": 0
            }
            ]
        ]
        },
        "HTTP Request": {
        "main": [
            [
            {
                "node": "Merge",
                "type": "main",
                "index": 0
            }
            ]
        ]
        },
        "Airtable": {
        "main": [
            [
            {
                "node": "Merge",
                "type": "main",
                "index": 1
            }
            ]
        ]
        },
        "Merge": {
        "main": [
            [
            {
                "node": "Sort",
                "type": "main",
                "index": 0
            }
            ]
        ]
        },
        "Sort": {
        "main": [
            [
            {
                "node": "Loop Over Items",
                "type": "main",
                "index": 0
            },
            {
                "node": "If",
                "type": "main",
                "index": 0
            }
            ]
        ]
        },
        "If": {
        "main": [
            [
            {
                "node": "Convert to File",
                "type": "main",
                "index": 0
            }
            ]
        ]
        },
        "Convert to File": {
        "main": [
            [
            {
                "node": "Gmail",
                "type": "main",
                "index": 0
            }
            ]
        ]
        },
        "Loop Over Items": {
        "main": [
            null,
            [
            {
                "node": "Edit Fields",
                "type": "main",
                "index": 0
            }
            ]
        ]
        },
        "Edit Fields": {
        "main": [
            [
            {
                "node": "Date & Time",
                "type": "main",
                "index": 0
            }
            ]
        ]
        },
        "Date & Time": {
        "main": [
            [
            {
                "node": "Convert to File1",
                "type": "main",
                "index": 0
            }
            ]
        ]
        },
        "Convert to File1": {
        "main": [
            [
            {
                "node": "Discord1",
                "type": "main",
                "index": 0
            }
            ]
        ]
        },
        "Discord1": {
        "main": [
            [
            {
                "node": "Loop Over Items",
                "type": "main",
                "index": 0
            }
            ]
        ]
        }
    },
    "pinData": {}
    }
    ```
