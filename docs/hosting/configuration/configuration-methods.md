---
#https://www.notion.so/n8n/Frontmatter-432c2b8dff1f43d4b1c8d20075510fe4
title: วิธีการตั้งค่า Configuration
description: วิธีตั้งค่า Environment Variables สำหรับ n8n
contentType: howto
---

# Configuration

คุณสามารถเปลี่ยนค่าต่าง ๆ ของ n8n ได้ด้วย environment variables ดูรายการ config ทั้งหมดได้ที่ [Environment Variables](/hosting/configuration/environment-variables/index.md)

## Set environment variables by command line

### npm

ถ้าใช้ npm ให้ตั้ง environment variables ที่ต้องการใน terminal ด้วยคำสั่ง `export` แบบนี้

```bash
export <variable>=<value>
```

### Docker

ถ้าใช้ Docker ให้ใช้ flag `-e` ตอนสั่งรันจาก command line

```bash
docker run -it --rm \
 --name n8n \
 -p 5678:5678 \
 -e N8N_TEMPLATES_ENABLED="false" \
 docker.n8n.io/n8nio/n8n
```

## Set environment variables using a file

คุณสามารถตั้งค่า n8n ด้วยไฟล์ config ได้เหมือนกัน

ในไฟล์ config ให้ใส่เฉพาะค่าที่ต่างจาก default ก็พอ คุณสามารถใช้หลายไฟล์ได้ เช่น มีไฟล์ base สำหรับค่ากลาง และไฟล์แยกสำหรับ environment ต่าง ๆ

### npm

ตั้ง path ไปยังไฟล์ JSON config ด้วย environment variable `N8N_CONFIG_FILES`:

```shell
# Bash - ไฟล์เดียว
export N8N_CONFIG_FILES=/<path-to-config>/my-config.json
# Bash - หลายไฟล์คั่นด้วย comma
export N8N_CONFIG_FILES=/<path-to-config>/my-config.json,/<path-to-config>/production.json

# PowerShell - ไฟล์เดียว, ใช้กับ user ปัจจุบัน
# การตั้ง scope (Process, User, Machine) ไม่มีผลบน Unix
[Environment]::SetEnvironmentVariable('N8N_CONFIG_FILES', '<path-to-config>\config.json', 'User')
```

ตัวอย่างไฟล์:

```json
{
 "executions": {
  "saveDataOnSuccess": "none"
 },
 "generic": {
  "timezone": "Europe/Berlin"
 },
 "nodes": {
  "exclude": "[\"n8n-nodes-base.executeCommand\",\"n8n-nodes-base.writeBinaryFile\"]"
 }
}
```

/// note | Formatting as JSON
บางทีดูจาก [Environment variables reference](/hosting/configuration/environment-variables/index.md) แล้วอาจจะไม่รู้ว่าต้องเขียน JSON ยังไง เช่น ถ้าจะตั้ง `N8N_METRICS` ให้เป็น `true` ต้องเขียนแบบนี้

```json
{
	"endpoints": {
		"metrics": {
			"enable": true
		}
	}
}
```

ดูรายละเอียด schema เต็ม ๆ ได้ที่ [Schema file ใน source code](https://github.com/n8n-io/n8n/blob/master/packages/cli/src/config/schema.ts){:target=_blank .external-link}
///

### Docker

ถ้าใช้ Docker ให้ตั้ง environment variables ใน `n8n: environment:` ของไฟล์ `docker-compose.yaml`

ตัวอย่าง:

```yaml
n8n:
    environment:
      - N8N_TEMPLATES_ENABLED=false
```

### Keeping sensitive data in separate files

คุณสามารถเติม `_FILE` ต่อท้าย environment variable เพื่อให้ค่า config ถูกอ่านมาจากไฟล์แยก ช่วยให้ไม่ต้องส่งข้อมูลสำคัญผ่าน environment variable โดยตรง n8n จะโหลดค่าจากไฟล์ที่กำหนด ทำให้ใช้กับ [Docker-Secrets](https://docs.docker.com/engine/swarm/secrets/){:target=_blank .external-link} และ [Kubernetes-Secrets](https://kubernetes.io/docs/concepts/configuration/secret/){:target=_blank .external-link} ได้

ดูรายละเอียดแต่ละตัวแปรได้ที่ [Environment variables](/hosting/configuration/environment-variables/index.md)

ส่วนใหญ่ environment variable จะใช้ `_FILE` ได้ โดยเหมาะกับข้อมูลสำคัญ เช่น [credentials](/glossary.md#credential-n8n) หรือ config database ตัวอย่างเช่น

```yaml
CREDENTIALS_OVERWRITE_DATA_FILE=/path/to/credentials_data
DB_TYPE_FILE=/path/to/db_type
DB_POSTGRESDB_DATABASE_FILE=/path/to/database_name
DB_POSTGRESDB_HOST_FILE=/path/to/database_host
DB_POSTGRESDB_PORT_FILE=/path/to/database_port
DB_POSTGRESDB_USER_FILE=/path/to/database_user
DB_POSTGRESDB_PASSWORD_FILE=/path/to/database_password
DB_POSTGRESDB_SCHEMA_FILE=/path/to/database_schema
DB_POSTGRESDB_SSL_CA_FILE=/path/to/ssl_ca
DB_POSTGRESDB_SSL_CERT_FILE=/path/to/ssl_cert
DB_POSTGRESDB_SSL_KEY_FILE=/path/to/ssl_key
DB_POSTGRESDB_SSL_REJECT_UNAUTHORIZED_FILE=/path/to/ssl_reject_unauth
```
