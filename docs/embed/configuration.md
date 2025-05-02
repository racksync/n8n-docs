---
#https://www.notion.so/n8n/Frontmatter-432c2b8dff1f43d4b1c8d20075510fe4
title: n8n Embed Configuration
description: Learn how to configure your n8n Embed.
contentType: howto
---

# Configuration

--8<-- "_snippets/embed-license.md"

## Authentication

คุณสามารถตั้งค่าความปลอดภัยให้ n8n ได้ด้วยการเปิดใช้ [User management](/user-management/index.md) ซึ่งเป็นฟีเจอร์ authentication ที่มีมาให้ในตัว

n8n รองรับ [LDAP](/user-management/ldap.md) และ [SAML](/user-management/saml/index.md)

### Credential overwrites

ถ้าคุณอยากให้ผู้ใช้ login ด้วย OAuth ได้ สามารถ overwrite [credentials](/glossary.md#credential-n8n) แบบ global ได้เลย Credential ที่ถูก overwrite นี้ผู้ใช้จะไม่เห็นข้อมูล แต่ backend จะนำไปใช้ให้อัตโนมัติ

ใน Editor UI, n8n จะซ่อน field ที่ถูก overwrite ไว้เสมอ หมายความว่าผู้ใช้จะสามารถ authenticate ด้วย OAuth แค่กดปุ่ม "connect" บน credentials ได้เลย

n8n มี 2 วิธีในการ apply credential overwrites: ใช้ Environment Variable หรือใช้ REST API

#### Using environment variables

คุณสามารถตั้งค่า credential overwrites ด้วย environment variable โดยตั้ง `CREDENTIALS_OVERWRITE_DATA` เป็น `{ CREDENTIAL_NAME: { PARAMETER: VALUE }}`

/// warning
ถึงจะทำได้ แต่ไม่แนะนำให้ใช้วิธีนี้ เพราะ environment variables ใน n8n ไม่ได้ถูกป้องกัน ข้อมูลอาจรั่วถึงผู้ใช้ได้
///

#### Using REST APIs

วิธีที่แนะนำคือโหลดข้อมูลผ่าน custom REST endpoint โดยตั้ง `CREDENTIALS_OVERWRITE_ENDPOINT` เป็น path ที่ endpoint นี้จะถูกเปิดใช้งาน

/// note
endpoint นี้จะถูกเรียกได้ทีละอันเท่านั้นเพื่อความปลอดภัย
///

ตัวอย่างเช่น:

1. เปิดใช้งาน endpoint โดยตั้ง environment variable ใน environment ที่ n8n รันอยู่:

    ```sh
    export CREDENTIALS_OVERWRITE_ENDPOINT=send-credentials
    ```

2. เตรียมไฟล์ JSON ที่มี credentials ที่จะ overwrite เช่น `oauth-credentials.json` สำหรับ overwrite credentials ของ Asana และ GitHub อาจหน้าตาแบบนี้:

    ```json
    {
        "asanaOAuth2Api": {
            "clientId": "<id>",
            "clientSecret": "<secret>"
        },
        "githubOAuth2Api": {
            "clientId": "<id>",
            "clientSecret": "<secret>"
        }
    }
    ```

3. ส่งไฟล์นี้เข้า instance ด้วย curl:

    ```sh
    curl -H "Content-Type: application/json" --data @oauth-credentials.json http://localhost:5678/send-credentials
    ```

/// note
บางกรณี credentials อาจ extend กัน เช่น `googleSheetsOAuth2Api` สืบทอดจาก `googleOAuth2Api`
ถ้าเป็นแบบนี้ สามารถตั้งค่าที่ parent credentials (`googleOAuth2Api`) แล้ว child credentials (`googleSheetsOAuth2Api`) จะใช้ค่าตามนั้น
///

## Environment variables

n8n มี [environment variables](/hosting/configuration/environment-variables/index.md) ให้ตั้งค่าหลายตัว ด้านล่างนี้คือ environment variables ที่สำคัญสำหรับการ host แบบนี้:

| Variable | Type | Default | Description |
| :------- | :--- | :------ | :---------- |
| `EXECUTIONS_TIMEOUT` | Number | `-1` | ตั้ง timeout (วินาที) ให้ workflow ทุกตัว ถ้าเกินนี้ n8n จะหยุด execution ผู้ใช้สามารถ override ได้ในแต่ละ workflow แต่ต้องไม่เกินค่าที่ตั้งใน `EXECUTIONS_TIMEOUT_MAX` ถ้าตั้ง `-1` คือปิดการใช้งาน |
| `EXECUTIONS_DATA_PRUNE` | Boolean | `true` | ลบข้อมูล execution เก่าๆ อัตโนมัติแบบ rolling |
| `EXECUTIONS_DATA_MAX_AGE` | Number | `336` | อายุ execution (ชั่วโมง) ก่อนจะถูกลบ |
| `EXECUTIONS_DATA_PRUNE_MAX_COUNT` | Number | `10000` | จำนวน execution สูงสุดที่จะเก็บใน database 0 = ไม่จำกัด |
| `NODES_EXCLUDE` | Array of strings | - | ระบุ node ที่ไม่ต้องการโหลด เช่น node ที่เสี่ยงด้าน security: `NODES_EXCLUDE: "[\"n8n-nodes-base.executeCommand\", \"n8n-nodes-base.readWriteFile\"]"` |
| `NODES_INCLUDE` | Array of strings | - | ระบุ node ที่ต้องการโหลดเท่านั้น |
| `N8N_TEMPLATES_ENABLED` | Boolean | `true` | เปิด/ปิด [workflow templates](/glossary.md#template-n8n) (true = เปิด, false = ปิด) |
| `N8N_TEMPLATES_HOST` | String | `https://api.n8n.io` | เปลี่ยน endpoint ถ้าจะใช้ workflow template library ของตัวเอง API ที่ใช้ต้องมี endpoint และ response structure แบบเดียวกับของ n8n ดูรายละเอียดที่ [Workflow templates](/workflows/templates.md) |

## Backend hooks

คุณสามารถกำหนด external hooks ที่ n8n จะ execute ทุกครั้งที่มี operation เฉพาะเกิดขึ้น ใช้สำหรับ log, เปลี่ยนแปลงข้อมูล หรือป้องกัน action โดย throw error ก็ได้

### Available hooks

| Hook     | Arguments | Description |
| :------- | :---------| :---------- |
| `credentials.create` | `[credentialData: ICredentialsDb]` | เรียกก่อนสร้าง credentials ใหม่ ใช้จำกัดจำนวน credentials ได้ |
| `credentials.delete` | `[id: credentialId]` | เรียกก่อนลบ credentials |
| `credentials.update` | `[credentialData: ICredentialsDb]` | เรียกก่อนบันทึก credentials ที่มีอยู่ |
| `frontend.settings` | `[frontendSettings: IN8nUISettings]` | เรียกตอน n8n startup ใช้ overwrite frontend data เช่น OAuth URL |
| `n8n.ready` | `[app: App]` | เรียกเมื่อ n8n พร้อมใช้งานแล้ว ใช้สำหรับ register custom API endpoint |
| `n8n.stop` |  | เรียกเมื่อ process n8n หยุด ใช้สำหรับบันทึก process data |
| `oauth1.authenticate` | `[oAuthOptions: clientOAuth1.Options, oauthRequestData: {oauth_callback: string}]` | เรียกก่อน OAuth1 authentication ใช้ overwrite OAuth callback URL |
| `oauth2.callback` | `[oAuth2Parameters: {clientId: string, clientSecret: string \| undefined, accessTokenUri: string, authorizationUri: string, redirectUri: string, scopes: string[]}]` | เรียกใน OAuth2 callback ใช้ overwrite OAuth callback URL |
| `workflow.activate` | `[workflowData: IWorkflowDb]` | เรียกก่อน activate workflow ใช้จำกัดจำนวน workflow ที่ active ได้ |
| `workflow.afterDelete` | `[workflowId: string]` | เรียกหลัง workflow ถูกลบ |
| `workflow.afterUpdate` | `[workflowData: IWorkflowBase]` | เรียกหลัง workflow ถูกบันทึก |
| `workflow.create` | `[workflowData: IWorkflowBase]` | เรียกก่อนสร้าง workflow ใช้จำกัดจำนวน workflow ที่บันทึกได้ |
| `workflow.delete` | `[workflowId: string]` | เรียกก่อนลบ workflow |
| `workflow.postExecute` | `[run: IRun, workflowData: IWorkflowBase]` | เรียกหลัง workflow execute เสร็จ |
| `workflow.preExecute` | `[workflow: Workflow: mode: WorkflowExecuteMode]` | เรียกก่อน workflow execute ใช้นับหรือจำกัดจำนวน execution ได้ |
| `workflow.update` | `[workflowData: IWorkflowBase]` | เรียกก่อนบันทึก workflow ที่มีอยู่ |

### Registering hooks

ตั้งค่า hook โดย register hook file ที่มีฟังก์ชัน hook ที่ต้องการ
register hook โดยตั้ง environment variable `EXTERNAL_HOOK_FILES`

ตั้งเป็นไฟล์เดียว:

`EXTERNAL_HOOK_FILES=/data/hook.js`

หรือหลายไฟล์คั่นด้วย semicolon:

`EXTERNAL_HOOK_FILES=/data/hook1.js;/data/hook2.js`

### Backend hook files

hook file เป็นไฟล์ JavaScript ปกติ รูปแบบประมาณนี้:

```js
module.exports = {
    "frontend": {
        "settings": [
            async function (settings) {
                settings.oauthCallbackUrls.oauth1 = 'https://n8n.example.com/oauth1/callback';
                settings.oauthCallbackUrls.oauth2 = 'https://n8n.example.com/oauth2/callback';
            }
        ]
    },
    "workflow": {
        "activate": [
            async function (workflowData) {
                const activeWorkflows = await this.dbCollections.Workflow.count({ active: true });

                if (activeWorkflows > 1) {
                    throw new Error(
                        'Active workflow limit reached.'
                    );
                }
            }
        ]
    }
}
```

### Backend hook functions

hook หรือ hook file สามารถมีฟังก์ชัน hook หลายตัวได้ ทุกตัวจะถูก execute ต่อกัน

ถ้าพารามิเตอร์ของ hook function เป็น object สามารถเปลี่ยนค่าพารามิเตอร์นั้นเพื่อเปลี่ยนพฤติกรรมของ n8n ได้

ในฟังก์ชัน hook สามารถเข้าถึง database ได้ด้วย `this.dbCollections` (ดูตัวอย่างใน [Backend hook files](#backend-hook-files))

## Frontend external hooks

เหมือน backend external hooks, คุณสามารถกำหนด external hooks ใน frontend code ได้ n8n จะ execute ทุกครั้งที่ผู้ใช้ทำ operation เฉพาะ ใช้ log หรือเปลี่ยนแปลงข้อมูลได้

### Available hooks

| Hook     | Description |
| :------- | :---------- |
| `credentialsEdit.credentialTypeChanged` | เรียกเมื่อ credential type เปลี่ยน |
| `credentials.create` | เรียกเมื่อมีการสร้าง credential ใหม่ |
| `credentialsList.dialogVisibleChanged` |  |
| `dataDisplay.nodeTypeChanged` |  |
| `dataDisplay.onDocumentationUrlClick` | เรียกเมื่อคลิก help documentation link |
| `execution.open` | เรียกเมื่อเปิด execution ที่มีอยู่ |
| `executionsList.openDialog` | เรียกเมื่อเลือก execution จาก Workflow Executions |
| `expressionEdit.itemSelected` |  |
| `expressionEdit.dialogVisibleChanged` |  |
| `nodeCreateList.filteredNodeTypesComputed` |  |
| `nodeCreateList.nodeFilterChanged` | เรียกเมื่อเปลี่ยน filter ใน node panel |
| `nodeCreateList.selectedTypeChanged` |  |
| `nodeCreateList.mounted` |  |
| `nodeCreateList.destroyed` |  |
| `nodeSettings.credentialSelected` |  |
| `nodeSettings.valueChanged` |  |
| `nodeView.createNodeActiveChanged` |  |
| `nodeView.addNodeButton` |  |
| `nodeView.createNodeActiveChanged` |  |
| `nodeView.mount` |  |
| `pushConnection.executionFinished` |  |
| `showMessage.showError` |  |
| `runData.displayModeChanged` |  |
| `workflow.activeChange` |  |
| `workflow.activeChangeCurrent` |  |
| `workflow.afterUpdate` | เรียกเมื่อ workflow ถูก update |
| `workflow.open` |  |
| `workflowRun.runError` |  |
| `workflowRun.runWorkflow` | เรียกเมื่อ workflow execute |
| `workflowSettings.dialogVisibleChanged` |  |
| `workflowSettings.saveSettings` | เรียกเมื่อ save workflow settings |

### Registering hooks

ตั้ง hook โดยโหลด hooks script ในหน้าเว็บ วิธีหนึ่งคือสร้าง hooks file ในโปรเจกต์ แล้วเพิ่ม script tag ใน `editor-ui/public/index.html`:

```html
<script src="frontend-hooks.js"></script>
```

### Frontend hook files

frontend external hook file เป็นไฟล์ JavaScript ปกติ รูปแบบประมาณนี้:

```js
window.n8nExternalHooks = {
  nodeView: {
    mount: [
      function (store, meta) {
        // ทำอะไรบางอย่าง
      },
    ],
    createNodeActiveChanged: [
      function (store, meta) {
        // ทำอะไรบางอย่าง
      },
      function (store, meta) {
        // ทำอย่างอื่น
      },
    ],
    addNodeButton: [
      function (store, meta) {
        // ทำอะไรบางอย่าง
      },
    ],
  },
};
```

### Frontend hook functions

สามารถกำหนด hook function หลายตัวต่อ hook ได้ แต่ละตัวจะถูกเรียกพร้อม argument ดังนี้:

* `store`: คือ Vuex store object ใช้เปลี่ยนหรืออ่านข้อมูลจาก store ได้
* `metadata`: object ที่มีข้อมูลจาก hook ดูว่ามีอะไรส่งมาบ้างให้ค้นหา hook นั้นใน package `editor-ui`
