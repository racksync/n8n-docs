---
#https://www.notion.so/n8n/Frontmatter-432c2b8dff1f43d4b1c8d20075510fe4
title: เลือกแนวทางการสร้าง Node
description: อธิบายความแตกต่างระหว่าง declarative และ programmatic style
contentType: explanation
---

# Choose your node building approach

n8n มีสไตล์การสร้าง node อยู่ 2 แบบ คือ declarative และ programmatic

โดยปกติแล้วควรเลือกใช้แบบ declarative สำหรับ node ส่วนใหญ่ เพราะแบบนี้:

* ใช้ syntax แบบ JSON-based ทำให้เขียนง่าย ลดโอกาสเกิด bug
* รองรับอนาคตได้ดีกว่า
* เหมาะกับการเชื่อมต่อ REST APIs

ส่วนแบบ programmatic จะเขียนเยอะกว่า และควรใช้ในกรณีต่อไปนี้:

* Trigger nodes
* Node ที่ไม่ได้เชื่อมต่อ REST API เช่น ต้องเรียก GraphQL API หรือใช้ dependency ภายนอก
* Node ที่ต้องแปลงข้อมูลขาเข้า
* ต้องการ versioning เต็มรูปแบบ ดูรายละเอียดที่ [Node versioning](/integrations/creating-nodes/build/reference/node-versioning.md)

## Data handling differences

ความแตกต่างหลักระหว่าง declarative กับ programmatic คือวิธีจัดการข้อมูลขาเข้าและการสร้าง API request แบบ programmatic ต้องมี `execute()` method เพื่ออ่านข้อมูลและ parameter แล้วสร้าง request เอง ส่วน declarative จะใช้ key `routing` ใน object `operations` จัดการให้ ดูรายละเอียดเพิ่มเติมที่ [Node base file](/integrations/creating-nodes/build/reference/node-base-files/index.md) สำหรับ parameter และ `execute()` method

## Syntax differences

เพื่อให้เห็นความต่างระหว่าง declarative กับ programmatic ดูตัวอย่างโค้ดด้านล่างนี้ ตัวอย่างนี้คือ node สำหรับ FriendGrid (คล้าย SendGrid แบบง่าย) โค้ดนี้ไม่สมบูรณ์ แค่เน้นให้เห็นความต่างของแต่ละสไตล์

แบบ programmatic:

```js
import {
	IExecuteFunctions,
	INodeExecutionData,
	INodeType,
	INodeTypeDescription,
	IRequestOptions,
} from 'n8n-workflow';

// Create the FriendGrid class
export class FriendGrid implements INodeType {
  description: INodeTypeDescription = {
    displayName: 'FriendGrid',
    name: 'friendGrid',
    . . .
    properties: [
      {
        displayName: 'Resource',
        . . .
      },
      {
        displayName: 'Operation',
        name: 'operation',
        type: 'options',
        displayOptions: {
          show: {
              resource: [
              'contact',
              ],
          },
        },
        options: [
          {
            name: 'Create',
            value: 'create',
            description: 'Create a contact',
          },
        ],
        default: 'create',
        description: 'The operation to perform.',
      },
      {
        displayName: 'Email',
        name: 'email',
        . . .
      },
      {
        displayName: 'Additional Fields',
        // Sets up optional fields
      },
    ],
};

  async execute(this: IExecuteFunctions): Promise<INodeExecutionData[][]> {
    let responseData;
    const resource = this.getNodeParameter('resource', 0) as string;
    const operation = this.getNodeParameter('operation', 0) as string;
    //Get credentials the user provided for this node
    const credentials = await this.getCredentials('friendGridApi') as IDataObject;

    if (resource === 'contact') {
      if (operation === 'create') {
      // Get email input
      const email = this.getNodeParameter('email', 0) as string;
      // Get additional fields input
      const additionalFields = this.getNodeParameter('additionalFields', 0) as IDataObject;
      const data: IDataObject = {
          email,
      };

      Object.assign(data, additionalFields);

      // Make HTTP request as defined in https://sendgrid.com/docs/api-reference/
      const options: IRequestOptions = {
        headers: {
            'Accept': 'application/json',
            'Authorization': `Bearer ${credentials.apiKey}`,
        },
        method: 'PUT',
        body: {
            contacts: [
            data,
            ],
        },
        url: `https://api.sendgrid.com/v3/marketing/contacts`,
        json: true,
      };
      responseData = await this.helpers.httpRequest(options);
      }
    }
    // Map data to n8n data
    return [this.helpers.returnJsonArray(responseData)];
  }
}
```

แบบ declarative:

```js
import { INodeType, INodeTypeDescription } from 'n8n-workflow';

// Create the FriendGrid class
export class FriendGrid implements INodeType {
  description: INodeTypeDescription = {
    displayName: 'FriendGrid',
    name: 'friendGrid',
    . . .
    // Set up the basic request configuration
    requestDefaults: {
      baseURL: 'https://api.sendgrid.com/v3/marketing'
    },
    properties: [
      {
        displayName: 'Resource',
        . . .
      },
      {
        displayName: 'Operation',
        name: 'operation',
        type: 'options',
        displayOptions: {
          show: {
            resource: [
              'contact',
            ],
          },
        },
        options: [
          {
            name: 'Create',
            value: 'create',
            description: 'Create a contact',
            // Add the routing object
            routing: {
              request: {
                method: 'POST',
                url: '=/contacts',
                send: {
                  type: 'body',
                  properties: {
                    email: {{$parameter["email"]}}
                  }
                }
              }
            },
            // Handle the response to contact creation
            output: {
              postReceive: [
                {
                  type: 'set',
                  properties: {
                    value: '={{ { "success": $response } }}'
                  }
                }
              ]
            }
          },
        ],
        default: 'create',
        description: 'The operation to perform.',
      },
      {
        displayName: 'Email',
        . . .
      },
      {
        displayName: 'Additional Fields',
        // Sets up optional fields
      },
    ],
  }
  // No execute method needed
}
```
