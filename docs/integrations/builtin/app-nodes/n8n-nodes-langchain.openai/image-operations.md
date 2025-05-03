---
#https://www.notion.so/n8n/Frontmatter-432c2b8dff1f43d4b1c8d20075510fe4
title: OpenAI Image operations
description: เอกสารสำหรับ Image operations ใน OpenAI node ของ n8n. รวมรายละเอียด operations, การตั้งค่า, และลิงก์.
contentType: [integration, reference]
priority: critical
---

# OpenAI Image operations

ใช้ operation นี้เพื่อวิเคราะห์หรือสร้างภาพใน OpenAI. ดูข้อมูลเพิ่มเติมได้ที่ [OpenAI](/integrations/builtin/app-nodes/n8n-nodes-langchain.openai/index.md).

## Analyze Image

ใช้ operation นี้เพื่อนำเข้าภาพและตอบคำถามเกี่ยวกับภาพ.

Enter these parameters:
- **Credential to connect with**: สร้างหรือเลือก [OpenAI credential](/integrations/builtin/credentials/openai.md) ที่มีอยู่แล้ว.
- **Resource**: เลือก **Image**.
- **Operation**: เลือก **Analayze Image**.
- **Model**: เลือก Model ที่จะใช้ในการวิเคราะห์ภาพ.
- **Text Input**: ถามคำถามเกี่ยวกับภาพ.
- **Input Type**: เลือกวิธีการนำเข้าภาพ. ตัวเลือกรวมถึง:
    - **Image URL(s)**: ระบุ URL ของภาพที่ต้องการวิเคราะห์ โดยสามารถคั่นด้วยเครื่องหมายจุลภาคสำหรับหลาย URL.
    - **Binary File(s)**: ระบุชื่อ property แบบ binary ที่มีภาพใน **Input Data Field Name**.

### Options

- **Detail**: ระบุสมดุลระหว่างเวลาในการตอบกลับกับการใช้ token.
- **Length of Description (Max Tokens)**: ค่าเริ่มต้นคือ 300. จำนวน token ที่น้อยลงจะให้คำอธิบายภาพสั้นกว่าและมีรายละเอียดน้อยลง.

ดูรายละเอียดเพิ่มเติมที่ [Images | OpenAI](https://platform.openai.com/docs/api-reference/images){:target=_blank .external-link}.

## Generate an Image

Use this operation to create an image from a text prompt.

Enter these parameters:

- **Credential to connect with**: Create or select an existing [OpenAI credential](/integrations/builtin/credentials/openai.md).
- **Resource**: Select **Image**.
- **Operation**: Select **Generate an Image**.
- **Model**: Select the model you want to use to generate an image. 
- **Prompt**: Enter the text description of the desired image(s). The maximum length is 1000 characters for `dall-e-2` and 4000 characters for `dall-e-3`.

### Options

- **Quality**: The quality of the image you generate. **HD** creates images with finer details and greater consistency across the image. This option is only supported for `dall-e-3`. Otherwise, choose **Standard**.
- **Resolution**: Select the resolution of the generated images. Select **1024x1024** for `dall-e-2`. Select one of **1024x1024**, **1792x1024**, or **1024x1792** for `dall-e-3` models.
- **Style**: Select the style of the generated images. This option is only supported for `dall-e-3`. 
    - **Natural**: Use this to produce more natural looking images.
    - **Vivid**: Use this to produce hyper-real and dramatic images.
- **Respond with image URL(s)**: Whether to return image URL(s) instead of binary file(s).
- **Put Output in Field**: Defaults to `data`. Enter the name of the output field to put the binary file data in. Only available if **Respond with image URL(s)** is turned off.

Refer to [Create image | OpenAI](https://platform.openai.com/docs/api-reference/images/create){:target=_blank .external-link} documentation for more information.

## Common issues

For common errors or issues and suggested resolution steps, refer to [Common Issues](/integrations/builtin/app-nodes/n8n-nodes-langchain.openai/common-issues.md).
