---
#https://www.notion.so/n8n/Frontmatter-432c2b8dff1f43d4b1c8d20075510fe4
title: External Secrets
description: ใช้ external secrets vault กับ n8n
contentType: howto
---

# External secrets

/// info | Feature availability
* External secrets มีให้ใช้งานในแผน Enterprise Self-hosted และ Enterprise Cloud
* n8n รองรับ AWS Secrets Manager, Azure Key Vault, GCP Secrets Manager, Infisical และ HashiCorp Vault
* n8n ไม่รองรับ [HashiCorp Vault Secrets](https://developer.hashicorp.com/hcp/docs/vault-secrets){:target=_blank .external-link}
///

คุณสามารถใช้ external secrets store เพื่อจัดการ [credentials](/glossary.md#credential-n8n) สำหรับ n8n ได้

n8n จัดเก็บ credentials ทั้งหมดที่เข้ารหัสไว้ใน database และจำกัดการเข้าถึงโดยค่าเริ่มต้น ด้วยฟีเจอร์ external secrets คุณสามารถจัดเก็บข้อมูล credential ที่ละเอียดอ่อนไว้ใน external vault และให้ n8n โหลดเข้ามาเมื่อจำเป็น สิ่งนี้ให้ชั้นความปลอดภัยเพิ่มเติมและช่วยให้คุณจัดการ credentials ที่ใช้ใน [n8n environments](/source-control-environments/index.md) หลายแห่งได้ในที่เดียว

## Connect n8n to your secrets store

/// note | Secret names
ชื่อ secret ของคุณต้องไม่มีช่องว่าง, ขีดกลาง หรืออักขระพิเศษอื่นๆ n8n รองรับชื่อ secret ที่ประกอบด้วยตัวอักษรและตัวเลข (`a-z`, `A-Z`, และ `0-9`) และขีดล่าง
///
1. ใน n8n ไปที่ **Settings** > **External Secrets**
1. เลือก **Set Up** สำหรับ store provider ของคุณ
1. ป้อน credentials สำหรับ provider ของคุณ:
	* Azure Key Vault: ระบุ **vault name**, **tenant ID**, **client ID** และ **client secret** ของคุณ โปรดดูเอกสาร Azure เพื่อ [register a Microsoft Entra ID app and create a service principal](https://learn.microsoft.com/en-us/entra/identity-platform/howto-create-service-principal-portal){:target=_blank .external-link} n8n รองรับเฉพาะค่า single-line สำหรับ secrets
	* AWS Secrets Manager: ระบุ **access key ID**, **secret access key** และ **region** ของคุณ IAM user ต้องมี permissions `secretsmanager:ListSecrets`, `secretsmanager:BatchGetSecretValue` และ `secretsmanager:GetSecretValue`

		เพื่อให้ n8n เข้าถึง secrets ทั้งหมดใน AWS Secrets Manager ของคุณ คุณสามารถแนบ policy ต่อไปนี้กับ IAM user:
		```json
		{
			"Version": "2012-10-17",
			"Statement": [
				{
					"Sid": "AccessAllSecrets",
					"Effect": "Allow",
					"Action": [
						"secretsmanager:ListSecrets",
						"secretsmanager:BatchGetSecretValue",
 						"secretsmanager:GetResourcePolicy",
						"secretsmanager:GetSecretValue",
						"secretsmanager:DescribeSecret",
						"secretsmanager:ListSecretVersionIds",
					],
					"Resource": "*"
				}
			]
		}
		```

		คุณยังสามารถจำกัดสิทธิ์ให้เข้มงวดมากขึ้นและให้ n8n เข้าถึงเฉพาะ AWS Secret Manager secrets ที่เลือกได้ คุณยังคงต้องอนุญาต permissions `secretsmanager:ListSecrets` และ `secretsmanager:BatchGetSecretValue` เพื่อเข้าถึง resources ทั้งหมด permissions เหล่านี้อนุญาตให้ n8n ดึงข้อมูล secrets ที่กำหนดขอบเขตด้วย ARN แต่ไม่ได้ให้สิทธิ์เข้าถึงค่า secret

		ถัดไป คุณต้องตั้งค่าขอบเขตสำหรับ permission `secretsmanager:GetSecretValue` ให้กับ Amazon Resource Names (ARNs) เฉพาะสำหรับ secrets ที่คุณต้องการแชร์กับ n8n ตรวจสอบให้แน่ใจว่าคุณใช้ region และ account ID ที่ถูกต้องในแต่ละ resource ARNs คุณสามารถค้นหารายละเอียด ARN ได้ใน AWS dashboard สำหรับ secrets ของคุณ

		ตัวอย่างเช่น IAM policy ต่อไปนี้อนุญาตให้เข้าถึงเฉพาะ secrets ที่มีชื่อขึ้นต้นด้วย `n8n` ใน AWS account และ region ที่ระบุของคุณเท่านั้น:

		```json
		{
			"Version": "2012-10-17",
			"Statement": [
				{
					"Sid": "ListingSecrets",
					"Effect": "Allow",
					"Action": [
						"secretsmanager:ListSecrets",
						"secretsmanager:BatchGetSecretValue"
					],
					"Resource": "*"
				},
				{
					"Sid": "RetrievingSecrets",
					"Effect": "Allow",
					"Action": [
						"secretsmanager:GetSecretValue",
						"secretsmanager:DescribeSecret"
					],
					"Resource": [
						"arn:aws:secretsmanager:us-west-2:123456789000:secret:n8n*"
					]
				}
			]
		}
		```

		สำหรับตัวอย่าง IAM permission policy เพิ่มเติม โปรดดู [เอกสาร AWS](https://docs.aws.amazon.com/secretsmanager/latest/userguide/auth-and-access_iam-policies.html#auth-and-access_examples_batch){:target=_blank .external-link}

	* HashiCorp Vault: ระบุ **Vault URL** สำหรับ vault instance ของคุณ และเลือก **Authentication Method** ของคุณ ป้อนรายละเอียด authentication ของคุณ สามารถระบุ namespace ได้ (optional)
		- โปรดดูเอกสาร HashiCorp สำหรับ authentication method ของคุณ:
				[Token auth method](https://developer.hashicorp.com/vault/docs/auth/token){:target=_blank .external-link}
				[AppRole auth method](https://developer.hashicorp.com/vault/docs/auth/approle){:target=_blank .external-link}
				[Userpass auth method](https://developer.hashicorp.com/vault/docs/auth/userpass){:target=_blank .external-link}
		- หากคุณใช้ vault namespaces คุณสามารถป้อน namespace ที่ n8n ควรเชื่อมต่อได้ โปรดดู [Vault Enterprise namespaces](https://developer.hashicorp.com/vault/docs/enterprise/namespaces){:target=_blank .external-link} สำหรับข้อมูลเพิ่มเติมเกี่ยวกับ HashiCorp Vault namespaces

	* Infisical: ระบุ **Service Token** โปรดดูเอกสาร [Service token](https://infisical.com/docs/documentation/platform/token){:target=_blank .external-link} ของ Infisical สำหรับข้อมูลเกี่ยวกับการรับ token ของคุณ หากคุณ self-host Infisical ให้ป้อน **Site URL**

	    /// note | Infisical environment
		ตรวจสอบให้แน่ใจว่าคุณเลือก Infisical environment ที่ถูกต้องเมื่อสร้าง token ของคุณ n8n จะโหลด secrets จาก environment นี้ และจะไม่สามารถเข้าถึง secrets ใน Infisical environments อื่นได้ n8n รองรับเฉพาะ service tokens ที่สามารถเข้าถึง environment เดียวเท่านั้น
		///

	    /// note | Infisical folders
	 	n8n ไม่รองรับ [Infisical folders](https://infisical.com/docs/documentation/platform/folder){:target=_blank .external-link}
		///

	* Google Cloud Platform: ระบุ **Service Account Key** (JSON) สำหรับ service account ที่มี roles อย่างน้อยเหล่านี้: `Secret Manager Secret Accessor` และ `Secret Manager Secret Viewer` โปรดดู [เอกสาร service account](https://cloud.google.com/iam/docs/service-account-overview){:target=_blank .external-link} ของ Google สำหรับข้อมูลเพิ่มเติม

1. **Save** การกำหนดค่าของคุณ
1. เปิดใช้งาน provider โดยใช้ toggle **Disabled / Enabled**


## Use secrets in n8n credentials

หากต้องการใช้ secret จาก store ของคุณใน n8n credential:

1. สร้าง credential ใหม่ หรือเปิด credential ที่มีอยู่
1. ใน field ที่คุณต้องการใช้ secret:
	1. วางเมาส์เหนือ field
	1. เลือก **Expression**
1. ใน field ที่คุณต้องการใช้ secret ให้ป้อน [expression](/glossary.md#expression-n8n) ที่อ้างอิงชื่อ secret:
	```js
	{{ $secrets.<vault-name>.<secret-name> }}
	```
	`<vault-name>` คือ `vault` (สำหรับ HashiCorp) หรือ `infisical` หรือ `awsSecretsManager` แทนที่ `<secret-name>` ด้วยชื่อตามที่ปรากฏใน vault ของคุณ

## Using external secrets with n8n environments

ฟีเจอร์ [Source control and environments](/source-control-environments/index.md) ของ n8n ช่วยให้คุณสร้าง n8n environments ที่แตกต่างกันได้ โดยใช้ Git เป็น backend ฟีเจอร์นี้ไม่รองรับการใช้ credentials ที่แตกต่างกันใน instances ที่แตกต่างกัน คุณสามารถใช้ external secrets vault เพื่อจัดหา credentials ที่แตกต่างกันสำหรับ environments ที่แตกต่างกันได้โดยการเชื่อมต่อแต่ละ n8n instance กับ vault หรือ project environment ที่แตกต่างกัน

ตัวอย่างเช่น คุณมี n8n instances สองตัว ตัวหนึ่งสำหรับ development และอีกตัวสำหรับ production คุณใช้ Infisical สำหรับ vault ของคุณ ใน Infisical สร้าง project ที่มีสอง environments คือ development และ production สร้าง token สำหรับแต่ละ Infisical environment ใช้ token สำหรับ development environment เพื่อเชื่อมต่อ n8n instance สำหรับ development ของคุณ และใช้ token สำหรับ production environment เพื่อเชื่อมต่อ n8n instance สำหรับ production ของคุณ

## Using external secrets in projects

หากต้องการใช้ external secrets ใน [RBAC project](/user-management/rbac/index.md) คุณต้องมี [instance owner หรือ instance admin](/user-management/account-types.md) เป็นสมาชิกของ project

## Troubleshooting

### Infisical version changes

การอัปเกรดเวอร์ชัน Infisical อาจทำให้เกิดปัญหาในการเชื่อมต่อกับ n8n หากการเชื่อมต่อ Infisical ของคุณหยุดทำงาน ให้ตรวจสอบว่ามีการเปลี่ยนแปลงเวอร์ชันล่าสุดหรือไม่ หากใช่ โปรดรายงานปัญหาไปที่ help@n8n.io

### Only set external secrets on credentials owned by an instance owner or admin

เนื่องจาก permissions ที่ instance owners และ admins มี ทำให้ owners และ admins สามารถอัปเดต credentials ที่ผู้ใช้อื่นเป็นเจ้าของด้วย secrets expression ได้ สิ่งนี้จะดูเหมือนทำงานได้ใน preview สำหรับ instance owner หรือ admin แต่ secret จะไม่ resolve เมื่อ workflow ทำงานใน production

ใช้ external secrets สำหรับ credentials ที่ instance admin หรือ owner เป็นเจ้าของเท่านั้น เพื่อให้แน่ใจว่า resolve ได้อย่างถูกต้องใน production
