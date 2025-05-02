---
#https://www.notion.so/n8n/Frontmatter-432c2b8dff1f43d4b1c8d20075510fe4
contentType: tutorial
---

# Hosting n8n on Azure

คู่มือนี้จะสอนวิธีติดตั้ง n8n แบบ self-host บน Azure โดยใช้ n8n กับ Postgres เป็น database backend และใช้ Kubernetes จัดการ resource ต่าง ๆ และ reverse proxy

## Prerequisites

ต้องมี [Azure command line tool](https://learn.microsoft.com/en-us/cli/azure/install-azure-cli){:target="_blank" .external-link}

--8<-- "_snippets/self-hosting/warning.md"

--8<-- "_snippets/self-hosting/installation/latest-next-version.md"

## Hosting options

Azure มีหลายวิธีให้ deploy n8n เช่น Azure Container Instances, Linux VM, หรือ Azure Kubernetes Service (AKS)

คู่มือนี้จะใช้ AKS ซึ่งเหมาะกับการ scale ตามความต้องการ

ขั้นตอนในคู่มือนี้จะใช้ทั้ง Azure UI และ command line tool สามารถเลือกใช้วิธีไหนก็ได้

## Open the Azure Kubernetes Service

เข้า [Azure portal](https://portal.azure.com/){:target="_blank" .external-link} แล้วเลือก **Kubernetes services**

## Create a cluster

ในหน้า Kubernetes services กด **Create** > **Create a Kubernetes cluster**

ตั้งค่าตามต้องการ แล้วกด **Create**

## Set Kubectl context

ขั้นตอนต่อไปต้องตั้งค่า Azure instance ให้เป็น Kubectl context ดูรายละเอียดได้จากปุ่ม **Connect** ในหน้า cluster จะมี code snippet ให้ copy ไปวางใน terminal เพื่อเปลี่ยน context

## Clone configuration repository

Kubernetes กับ n8n ต้องใช้ไฟล์ config หลายไฟล์ สามารถ clone repo ตัวอย่างจาก [ที่นี่](https://github.com/n8n-io/n8n-kubernetes-hosting/tree/azure){:target=_blank .external-link}

รันคำสั่งนี้เพื่อ clone:

```shell
git clone https://github.com/n8n-io/n8n-kubernetes-hosting.git -b azure
```

แล้วเข้าไปที่โฟลเดอร์ที่ clone มา:

```shell
cd azure
```

## Configure Postgres

สำหรับการใช้งาน n8n ขนาดใหญ่ แนะนำให้ใช้ Postgres เป็น database backend

### Configure volume for persistent storage

เพื่อให้ข้อมูลไม่หายเวลามี pod restart, Postgres ต้องใช้ persistent volume ค่า default storage class ของ Azure กำหนดไว้ในไฟล์ `postgres-claim0-persistentvolumeclaim.yaml`

/// note | Specialized storage classes
ถ้าต้องการ storage class แบบพิเศษหรือประสิทธิภาพสูง อ่านรายละเอียดได้ที่ [Azure documentation](https://learn.microsoft.com/en-us/azure/aks/concepts-storage#storage-classes){:target="_blank" .external-link}
///
### Postgres environment variables

Postgres ต้องการ environment variable บางตัวใน container ตัวอย่างไฟล์ `postgres-secret.yaml` มี placeholder ให้แก้ไข

`postgres-deployment.yaml` จะใช้ค่าจากไฟล์นี้ส่งเข้า pod

## Configure n8n

### Create a volume for file storage

ไม่จำเป็นต้องมี persistent volume ก็รัน n8n ได้ แต่ถ้าอยากเก็บไฟล์ที่อัปโหลด หรือเก็บ [encryption key ของ n8n แบบ manual](/hosting/configuration/environment-variables/deployment.md) ระหว่าง restart ต้องใช้ persistent volume

ไฟล์ `n8n-claim0-persistentvolumeclaim.yaml` จะสร้าง volume นี้ และ deployment ของ n8n จะ mount volume ใน section `volumes` ของ `n8n-deployment.yaml`

```yaml
…
volumes:
  - name: n8n-claim0
    persistentVolumeClaim:
      claimName: n8n-claim0
…
```

### Pod resources

[Kubernetes lets you](https://kubernetes.io/docs/concepts/configuration/manage-resources-containers/){:target="_blank" .external-link} สามารถกำหนด resource ขั้นต่ำ/สูงสุดให้แต่ละ container ได้ ตัวอย่างในไฟล์ YAML ที่ clone มาจะมีแบบนี้ใน `resources` section ของ `n8n-deployment.yaml`:

```yaml
…
resources:
  requests:
    memory: "250Mi"
  limits:
    memory: "500Mi"
…    
```

กำหนดขั้นต่ำ 250mb ต่อ container, สูงสุด 500mb, ส่วน CPU ให้ Kubernetes จัดการเอง สามารถปรับค่าตามต้องการได้

--8<-- "_snippets/self-hosting/installation/suggested-pod-resources.md"

### Optional: Environment variables

สามารถตั้งค่า n8n เพิ่มเติมด้วย environment variable

สร้างไฟล์ `n8n-secret.yaml` ดูรายละเอียด environment variable ได้ที่ [Environment variables](/hosting/configuration/environment-variables/index.md)

## Deployments

deployment manifest 2 ไฟล์ (`n8n-deployment.yaml` กับ `postgres-deployment.yaml`) จะกำหนดรายละเอียดของ n8n กับ Postgres ใน Kubernetes

- ส่ง environment variable ที่กำหนดเข้าแต่ละ pod
- กำหนด container image ที่ใช้
- กำหนด resource limit
- กำหนด volume และ path ที่จะ mount
- กำหนดจำนวน pod และ restart policy (ตัวอย่างนี้ใช้ 1 pod ต่อ service สามารถปรับได้)

## Services

service manifest 2 ไฟล์ (`postgres-service.yaml` กับ `n8n-service.yaml`) จะ expose service ออกไปผ่าน Kubernetes load balancer ที่ port 5432 และ 5678 ตามลำดับ

## Send to Kubernetes cluster

deploy manifest ทั้งหมดเข้า cluster ด้วยคำสั่งนี้:

```shell
kubectl apply -f .
```

/// note | Namespace error
ถ้าเจอ error ว่าไม่เจอ namespace "n8n" ให้รันคำสั่งนี้ก่อน แล้วค่อยรัน apply อีกรอบ:

```shell
kubectl apply -f namespace.yaml
```
///


## Set up DNS

โดยปกติ n8n จะรันบน subdomain ให้สร้าง DNS record ชี้ subdomain ไปที่ IP ของ n8n service ดู IP ได้จาก **Services & ingresses** ของ cluster ใน column **External IP** ต้องเติม port "5678" ต่อท้าย URL ด้วย

/// note | Static IP addresses with AKS
อ่านวิธีใช้ static IP กับ AKS ได้ที่ [ที่นี่](https://learn.microsoft.com/en-us/azure/aks/static-ip){:target="_blank" .external-link}
///
## Delete resources

ถ้าต้องการลบ resource ที่สร้างไว้ ให้ใช้คำสั่ง:

```shell
kubectl delete -f .
```

## Next steps

--8<-- "_snippets/self-hosting/installation/server-setups-next-steps.md"
