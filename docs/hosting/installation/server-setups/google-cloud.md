---
#https://www.notion.so/n8n/Frontmatter-432c2b8dff1f43d4b1c8d20075510fe4
contentType: tutorial
---

# Hosting n8n on Google Cloud

คู่มือนี้จะสอนวิธีติดตั้ง n8n แบบ self-host บน Google Cloud (GCP) โดยใช้ n8n กับ Postgres เป็น database backend และใช้ Kubernetes จัดการ resource ต่าง ๆ และ reverse proxy

## Prerequisites

- [gcloud command line tool](https://cloud.google.com/sdk/gcloud/){:target="_blank" .external-link}
- [gke-gcloud-auth-plugin](https://cloud.google.com/blog/products/containers-kubernetes/kubectl-auth-changes-in-gke){:target="_blank" .external-link} (ต้องติดตั้ง gcloud CLI ก่อน)

--8<-- "_snippets/self-hosting/warning.md"

--8<-- "_snippets/self-hosting/installation/latest-next-version.md"

## Hosting options

Google Cloud มีหลายวิธีให้ deploy n8n เช่น Cloud Run, Compute Engine, หรือ Kubernetes Engine

คู่มือนี้จะใช้ Google Kubernetes Engine (GKE) ซึ่งเหมาะกับการ scale ตามความต้องการ

ส่วนใหญ่จะใช้ Google Cloud UI แต่จะใช้ [gcloud command line tool](https://cloud.google.com/sdk/gcloud/){:target="_blank" .external-link} ได้เหมือนกัน

## Create project

GCP แนะนำให้สร้าง project แยกสำหรับแต่ละงาน สร้าง project ใหม่สำหรับ n8n ได้จาก Google Cloud Console เลือก project dropdown แล้วกด **NEW PROJECT** จากนั้นเลือก project ที่สร้างไว้

## Enable the Kubernetes Engine API

GKE ไม่ได้เปิดไว้ตั้งแต่แรก ให้ค้นหา "Kubernetes" ในช่องค้นหาด้านบน แล้วเลือก "Kubernetes Engine" จากผลลัพธ์

กด **ENABLE** เพื่อเปิด Kubernetes Engine API สำหรับ project นี้

## Create a cluster

ไปที่ [GKE service page](https://console.cloud.google.com/kubernetes/list/overview){:target=_blank .external-link} เลือก **Clusters** > **CREATE** ให้เลือกแบบ "Standard" (n8n ใช้กับ "Autopilot" ไม่ได้) ตั้งค่าตามต้องการแล้วสร้าง cluster

## Set Kubectl context

ขั้นตอนต่อไปต้องตั้งค่า GCP instance ให้เป็น Kubectl context ดูรายละเอียดได้จากหน้า cluster แล้วกด **CONNECT** จะมี code snippet ให้ copy ไปวางใน gcloud CLI เพื่อเปลี่ยน context

## Clone configuration repository

Kubernetes กับ n8n ต้องใช้ไฟล์ config หลายไฟล์ สามารถ clone repo ตัวอย่างจาก [ที่นี่](https://github.com/n8n-io/n8n-kubernetes-hosting/tree/gcp){:target=_blank .external-link}

รันคำสั่งนี้เพื่อ clone:

```shell
git clone https://github.com/n8n-io/n8n-kubernetes-hosting.git -b gcp
```

แล้วเข้าไปที่โฟลเดอร์ที่ clone มา:

```shell
cd n8n-kubernetes-hosting
```

## Configure Postgres

สำหรับการใช้งาน n8n ขนาดใหญ่ แนะนำให้ใช้ Postgres เป็น database backend

### Create a volume for persistent storage

เพื่อให้ข้อมูลไม่หายเวลามี pod restart, Postgres ต้องใช้ persistent volume บน GCP ต้องใช้ Storage Class เฉพาะ ดูรายละเอียดได้ที่ [คู่มือนี้](https://cloud.google.com/architecture/deploying-highly-available-postgresql-with-gke){:target="_blank" .external-link} แต่ไฟล์ `storage.yaml` ใน repo จะสร้างให้ ตัวอย่างเช่น:

```yaml
…
allowedTopologies:
  - matchLabelExpressions:
      - key: failure-domain.beta.kubernetes.io/zone
        values:
          - us-central1-b
          - us-central1-c
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

[Kubernetes lets you](https://kubernetes.io/docs/concepts/configuration/manage-resources-containers/) สามารถกำหนด resource ขั้นต่ำ/สูงสุดให้แต่ละ container ได้ ตัวอย่างในไฟล์ YAML ที่ clone มาจะมีแบบนี้ใน `resources` section ของ `n8n-deployment.yaml` และ `postgres-deployment.yaml`:

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

โดยปกติ n8n จะรันบน subdomain ให้สร้าง DNS record ชี้ subdomain ไปที่ IP ของ n8n service ดู IP ได้จาก **Services & Ingress** ของ cluster ใน column **Endpoints**

/// note | GKE and IP addresses
อ่านรายละเอียดการใช้ reserved IP กับ GKE ได้ที่ [GKE tutorial](https://cloud.google.com/kubernetes-engine/docs/tutorials/configuring-domain-name-static-ip#configuring_your_domain_name_records){:target="_blank" .external-link}
///
## Delete resources

ถ้าต้องการลบ resource ที่สร้างไว้ ให้ใช้คำสั่ง:

```shell
kubectl delete -f .
```

## Next steps

--8<-- "_snippets/self-hosting/installation/server-setups-next-steps.md"
