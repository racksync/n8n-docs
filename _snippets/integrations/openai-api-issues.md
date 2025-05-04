## บริการได้รับคำขอจากคุณมากเกินไป

ข้อผิดพลาดนี้จะแสดงขึ้นเมื่อคุณใช้งานเกิน [rate limits ของ OpenAI](https://platform.openai.com/docs/guides/rate-limits){:target=_blank .external-link}

มีสองวิธีในการแก้ไขปัญหานี้:

1. แบ่งข้อมูลของคุณออกเป็นส่วนเล็กๆ โดยใช้ [Loop Over Items](/integrations/builtin/core-nodes/n8n-nodes-base.splitinbatches.md) node และเพิ่ม [Wait](/integrations/builtin/core-nodes/n8n-nodes-base.wait.md) node ที่ส่วนท้ายเพื่อกำหนดระยะเวลาที่จะช่วยได้ คัดลอกโค้ดด้านล่างและวางลงใน workflow เพื่อใช้เป็น template
    ```
    {
        "nodes": [
        {
            "parameters": {},
            "id": "35d05920-ad75-402a-be3c-3277bff7cc67",
            "name": "When clicking ‘Test workflow’",
            "type": "n8n-nodes-base.manualTrigger",
            "typeVersion": 1,
            "position": [
            880,
            400
            ]
        },
        {
            "parameters": {
            "batchSize": 500,
            "options": {}
            },
            "id": "ae9baa80-4cf9-4848-8953-22e1b7187bf6",
            "name": "Loop Over Items",
            "type": "n8n-nodes-base.splitInBatches",
            "typeVersion": 3,
            "position": [
            1120,
            420
            ]
        },
        {
            "parameters": {
            "resource": "chat",
            "options": {},
            "requestOptions": {}
            },
            "id": "a519f271-82dc-4f60-8cfd-533dec580acc",
            "name": "OpenAI",
            "type": "n8n-nodes-base.openAi",
            "typeVersion": 1,
            "position": [
            1380,
            440
            ]
        },
        {
            "parameters": {
            "unit": "minutes"
            },
            "id": "562d9da3-2142-49bc-9b8f-71b0af42b449",
            "name": "Wait",
            "type": "n8n-nodes-base.wait",
            "typeVersion": 1,
            "position": [
            1620,
            440
            ],
            "webhookId": "714ab157-96d1-448f-b7f5-677882b92b13"
        }
        ],
        "connections": {
        "When clicking ‘Test workflow’": {
            "main": [
            [
                {
                "node": "Loop Over Items",
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
                "node": "OpenAI",
                "type": "main",
                "index": 0
                }
            ]
            ]
        },
        "OpenAI": {
            "main": [
            [
                {
                "node": "Wait",
                "type": "main",
                "index": 0
                }
            ]
            ]
        },
        "Wait": {
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
2. ใช้ [HTTP Request](/integrations/builtin/core-nodes/n8n-nodes-base.httprequest/index.md) node พร้อมกับตัวเลือก batch-limit ในตัวเพื่อเรียกใช้ [OpenAI API](https://platform.openai.com/docs/quickstart){:target=_blank .external-link} แทนการใช้ OpenAI node

## Quota ไม่เพียงพอ

/// note | ปัญหาเกี่ยวกับ Quota
มีปัญหาหลายอย่างเกี่ยวกับ quota ของ OpenAI รวมถึงความล้มเหลวเมื่อเพิ่งเติม quota ไป เพื่อหลีกเลี่ยงปัญหาเหล่านี้ ตรวจสอบให้แน่ใจว่ามีเครดิตในบัญชีและออก API key ใหม่จากหน้าจอ [API keys](https://platform.openai.com/settings/organization/api-keys)
///

ข้อผิดพลาดนี้จะแสดงขึ้นเมื่อบัญชี OpenAI ของคุณมีเครดิตหรือความจุไม่เพียงพอที่จะดำเนินการตามคำขอของคุณ ซึ่งอาจหมายความว่าช่วงทดลองใช้ OpenAI ของคุณสิ้นสุดลงแล้ว บัญชีของคุณต้องการเครดิตเพิ่ม หรือคุณใช้เกินขีดจำกัดการใช้งาน

ในการแก้ไขข้อผิดพลาดนี้ บนหน้า [OpenAI settings](https://platform.openai.com/settings/organization/billing/overview){:target=_blank .external-link} ของคุณ:

* เลือก organization ที่ถูกต้องสำหรับ API key ของคุณในตัวเลือกแรกที่มุมบนซ้าย
* เลือก project ที่ถูกต้องสำหรับ API key ของคุณในตัวเลือกที่สองที่มุมบนซ้าย
* ตรวจสอบหน้า [billing overview](https://platform.openai.com/settings/organization/billing/overview){:target=_blank .external-link} ระดับ organization เพื่อให้แน่ใจว่า organization มีเครดิตเพียงพอ ตรวจสอบอีกครั้งว่าคุณเลือก organization ที่ถูกต้องสำหรับหน้านี้
* ตรวจสอบหน้า [usage limits](https://platform.openai.com/settings/organization/limits){:target=_blank .external-link} ระดับ organization ตรวจสอบอีกครั้งว่าคุณเลือก organization ที่ถูกต้องสำหรับหน้านี้ และเลื่อนไปที่ส่วน **Usage limits** เพื่อตรวจสอบว่าคุณไม่ได้ใช้เกินขีดจำกัดการใช้งานของ organization ของคุณ
* ตรวจสอบ usage limits ของ OpenAI project ของคุณ ตรวจสอบอีกครั้งว่าคุณเลือก project ที่ถูกต้องในตัวเลือกที่สองที่มุมบนซ้าย เลือก **Project** > **Limits** เพื่อดูหรือเปลี่ยนแปลง project limits
* ตรวจสอบว่า [OpenAI API](https://status.openai.com/){:target=_blank .external-link} ทำงานตามที่คาดไว้

/// note | ระยะเวลารอ Balance
หลังจากเติม balance ของคุณ อาจมีความล่าช้าก่อนที่บัญชี OpenAI ของคุณจะแสดง balance ใหม่
///

ใน n8n:

* ตรวจสอบว่า [OpenAI credentials](/integrations/builtin/credentials/openai.md) ใช้ [OpenAI API key](https://platform.openai.com/api-keys){:target=_blank .external-link} ที่ถูกต้องสำหรับบัญชีที่คุณได้เติมเงินเข้าไป
* ตรวจสอบให้แน่ใจว่าคุณเชื่อมต่อ [OpenAI node](/integrations/builtin/app-nodes/n8n-nodes-langchain.openai/index.md) กับ [OpenAI credentials](/integrations/builtin/credentials/openai.md) ที่ถูกต้อง

หากคุณพบว่าเครดิตในบัญชีหมดบ่อยครั้ง ให้พิจารณาเปิดใช้งาน auto recharge ใน [OpenAI billing settings](https://platform.openai.com/settings/organization/billing/overview){:target=_blank .external-link} ของคุณ เพื่อเติมเครดิตเข้าบัญชีของคุณโดยอัตโนมัติเมื่อ balance ของคุณเหลือ $0

## Bad request - โปรดตรวจสอบ parameters ของคุณ

ข้อผิดพลาดนี้จะแสดงขึ้นเมื่อคำขอส่งผลให้เกิดข้อผิดพลาด แต่ n8n ไม่สามารถตีความข้อความแสดงข้อผิดพลาดจาก OpenAI ได้

ในการเริ่มต้นแก้ไขปัญหา ให้ลองดำเนินการแบบเดียวกันโดยใช้ [HTTP Request](/integrations/builtin/core-nodes/n8n-nodes-base.httprequest/index.md) node ซึ่งควรจะให้ข้อความแสดงข้อผิดพลาดที่ละเอียดมากขึ้น
