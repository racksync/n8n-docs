---
#https://www.notion.so/n8n/Frontmatter-432c2b8dff1f43d4b1c8d20075510fe4
contentType: tutorial
---

# Hosting n8n on Amazon Web Services

คู่มือนี้จะสอนวิธีติดตั้ง n8n แบบ self-host บน Amazon Web Services (AWS) โดยใช้ n8n กับ Postgres เป็น database backend และใช้ Kubernetes จัดการ resource ต่าง ๆ และ reverse proxy

## Hosting options

AWS มีหลายวิธีให้เลือก deploy n8n เช่น EC2 (virtual machine) หรือ EKS (Kubernetes)

คู่มือนี้จะใช้ [EKS](https://aws.amazon.com/eks/){:target=_blank .external-link} ซึ่งเหมาะกับการ scale ตามความต้องการ

## Prerequisites

ขั้นตอนในคู่มือนี้จะใช้ทั้ง AWS UI และ [eksctl CLI tool สำหรับ EKS](https://eksctl.io){:target=_blank .external-link}

นอกจากนี้ต้อง [ติดตั้ง AWS CLI tool](https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html){:target=_blank .external-link} และ [ตั้งค่า authentication](https://docs.aws.amazon.com/cli/latest/userguide/cli-configure-quickstart.html){:target=_blank .external-link} ด้วย

--8<-- "_snippets/self-hosting/warning.md"

--8<-- "_snippets/self-hosting/installation/latest-next-version.md"

## Create a cluster

ใช้ eksctl สร้าง cluster โดยระบุชื่อและ region:

```shell
eksctl create cluster --name n8n --region <your-aws-region>
```

อาจใช้เวลาสักพัก

เมื่อสร้างเสร็จ eksctl จะตั้งค่า kubectl context ให้ใช้ cluster นี้โดยอัตโนมัติ

## Clone configuration repository

Kubernetes กับ n8n ต้องใช้ไฟล์ config หลายไฟล์ สามารถ clone repo ตัวอย่างจาก [ที่นี่](https://github.com/n8n-io/n8n-kubernetes-hosting/tree/aws){:target=_blank .external-link}

รันคำสั่งนี้เพื่อ clone:

```shell
git clone https://github.com/n8n-io/n8n-kubernetes-hosting.git -b aws
```

แล้วเข้าไปที่โฟลเดอร์ที่ clone มา:

```shell
cd n8n-kubernetes-hosting
```

## Configure Postgres

สำหรับการใช้งาน n8n ขนาดใหญ่ แนะนำให้ใช้ Postgres เป็น database backend

### Configure volume for persistent storage

เพื่อให้ข้อมูลไม่หายเวลามี pod restart, Postgres ต้องใช้ persistent volume ค่า default storage class ของ AWS คือ [gp2](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/general-purpose.html#EBSVolumeTypes_gp2){:target=_blank .external-link} ซึ่งกำหนดไว้ในไฟล์ `postgres-claaim0-persistentvolumeclaim.yaml`

```yaml
…
spec:
  storageClassName: gp2
  accessModes:
    - ReadWriteOnce
…
```

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

[Kubernetes](https://kubernetes.io/docs/concepts/configuration/manage-resources-containers/){:target=_blank .external-link} สามารถกำหนด resource ขั้นต่ำ/สูงสุดให้แต่ละ container ได้ ตัวอย่างในไฟล์ YAML ที่ clone มาจะมีแบบนี้ใน `resources` section ของ `n8n-deployment.yaml`:

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

deploy manifest ทั้งหมดเข้า cluster ด้วยคำสั่งนี้ในโฟลเดอร์ `n8n-kubernetes-hosting`:

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

โดยปกติ n8n จะรันบน subdomain ให้สร้าง DNS record ชี้ subdomain ไปที่ static address ของ instance

ดู address ของ n8n service ได้โดย:

1. เปิด **Clusters** ใน **Amazon Elastic Kubernetes Service** บน AWS console
2. เลือกชื่อ cluster ที่ต้องการ
3. ไปที่แท็บ **Resources** แล้วเลือก **Service and networking** > **Services**
4. เลือก **n8n** service แล้ว copy ค่า **Load balancer URLs** ใช้ค่านี้ตามด้วย port 5678 ตั้ง DNS

/// note | Use HTTP
คู่มือนี้ใช้ HTTP ใน service ที่กำหนดไว้ (เช่นใน `n8n-deployment.yaml`) แต่ถ้าคลิก **Load balancer URLs** ใน EKS จะพาไปที่ HTTPS ซึ่งจะ error ให้เปลี่ยนเป็น HTTP ตอนเข้าใช้งาน n8n
///
## Delete resources

ถ้าต้องการลบ setup นี้ สามารถลบ resource ที่สร้างไว้ด้วยคำสั่ง:

```shell
kubectl delete -f .
```

## Next steps

--8<-- "_snippets/self-hosting/installation/server-setups-next-steps.md"
