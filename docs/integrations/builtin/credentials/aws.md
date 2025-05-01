---
#https://www.notion.so/n8n/Frontmatter-432c2b8dff1f43d4b1c8d20075510fe4
title: AWS credentials
description: Documentation for AWS credentials. Use these credentials to authenticate AWS in n8n, a workflow automation platform.
contentType: [integration, reference]
priority: medium
---

# AWS credentials

คุณสามารถใช้ credentials นี้เพื่อเชื่อมต่อกับ node เหล่านี้:

- [AWS Bedrock Chat Model](/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.lmchatawsbedrock.md)
- [AWS Certificate Manager](/integrations/builtin/app-nodes/n8n-nodes-base.awscertificatemanager.md)
- [AWS DynamoDB](/integrations/builtin/app-nodes/n8n-nodes-base.awsdynamodb.md)
- [AWS Elastic Load Balancing](/integrations/builtin/app-nodes/n8n-nodes-base.awselb.md)
- [AWS Lambda](/integrations/builtin/app-nodes/n8n-nodes-base.awslambda.md)
- [AWS Rekognition](/integrations/builtin/app-nodes/n8n-nodes-base.awsrekognition.md)
- [AWS S3](/integrations/builtin/app-nodes/n8n-nodes-base.awss3.md)
- [AWS SES](/integrations/builtin/app-nodes/n8n-nodes-base.awsses.md)
- [AWS SNS](/integrations/builtin/app-nodes/n8n-nodes-base.awssns.md)
- [AWS SNS Trigger](/integrations/builtin/trigger-nodes/n8n-nodes-base.awssnstrigger.md)
- [AWS SQS](/integrations/builtin/app-nodes/n8n-nodes-base.awssqs.md)
- [AWS Textract](/integrations/builtin/app-nodes/n8n-nodes-base.awstextract.md)
- [AWS Transcribe](/integrations/builtin/app-nodes/n8n-nodes-base.awstranscribe.md)
- [Embeddings AWS Bedrock](/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.embeddingsawsbedrock.md)

## Supported authentication methods

- API access key

## Related resources

ดูข้อมูลเพิ่มเติมเกี่ยวกับบริการได้ที่ [AWS's Identity and Access Management documentation](https://docs.aws.amazon.com/IAM/latest/UserGuide/getting-started.html){:target=_blank .external-link}

## Using API access key

ถ้าจะตั้งค่า credentials นี้ คุณต้องมีบัญชี [AWS](https://aws.amazon.com/){:target=_blank .external-link} และ:

- AWS **Region** ของคุณ
- **Access Key ID**: สร้างขึ้นเมื่อคุณสร้าง access key
- **Secret Access Key**: สร้างขึ้นเมื่อคุณสร้าง access key

วิธีสร้าง access key และตั้งค่า credential:

1. ใน n8n credential ของคุณ เลือก AWS **Region** ของคุณ
1. ล็อกอินเข้าสู่ [IAM console](https://console.aws.amazon.com/iam){:target=_blank .external-link}
2. ในแถบนำทางด้านบนขวา เลือกชื่อผู้ใช้ของคุณแล้วเลือก **Security credentials**
3. ในส่วน **Access keys** เลือก **Create access key**
4. ในหน้า **Access key best practices & alternatives** เลือก use case ของคุณ หากไม่แจ้งให้คุณสร้าง access key ให้เลือก **Other**
5. เลือก **Next**
6. ตั้งค่า **description** tag value สำหรับ access key เพื่อให้ระบุได้ง่ายขึ้น เช่น `n8n integration`
7. เลือก **Create access key**
8. เปิดเผย **Access Key ID** และ **Secret Access Key** แล้วป้อนลงใน n8n
10. หากต้องการใช้ **Temporary security credential** ให้เปิดตัวเลือกนั้นแล้วเพิ่ม **Session token** ดูข้อมูลเพิ่มเติมเกี่ยวกับการทำงานกับ temporary security credentials ได้ที่ [AWS Temporary security credential documentation](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_temp.html){:target=_blank .external-link}
11. หากคุณใช้ [Amazon Virtual Private Cloud (VPC)](https://aws.amazon.com/vpc/){:target=_blank .external-link} เพื่อ host n8n คุณสามารถสร้างการเชื่อมต่อระหว่าง VPC ของคุณกับบาง apps ได้ ใช้ **Custom Endpoints** เพื่อป้อน custom endpoint ที่เกี่ยวข้องสำหรับการเชื่อมต่อนี้ การตั้งค่านี้ทำงานร่วมกับ apps เหล่านี้:
    - Rekognition
    - Lambda
    - SNS
    - SES
    - SQS
    - S3

คุณยังสามารถสร้าง access keys ผ่าน AWS CLI และ AWS API ได้ ดูคำแนะนำในการสร้าง access keys โดยใช้วิธีเหล่านี้ได้ที่ [AWS Managing Access Keys documentation](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_access-keys.html){:target=_blank .external-link}

