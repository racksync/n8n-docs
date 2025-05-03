---
#https://www.notion.so/n8n/Frontmatter-432c2b8dff1f43d4b1c8d20075510fe4
title: ตั้งค่า Source control
description: เชื่อมต่อ n8n กับ Git provider ของคุณ
contentType: howto
---

# Set up source control for environments

เชื่อม Git repository กับ n8n instance แล้วตั้งค่า source control

n8n ใช้ source control เพื่อรองรับ environments ดูรายละเอียดที่ [Environments in n8n](/source-control-environments/understand/environments.md)

## Prerequisites

ถ้าจะใช้ source control กับ n8n คุณต้องมี Git repository ที่รองรับ SSH access

เอกสารนี้สมมติว่าคุณคุ้นเคยกับ Git และ Git provider ของคุณ

## Step 1: Set up your repository and branches

สำหรับ setup ใหม่:

1. สร้าง repository ใหม่สำหรับใช้กับ n8n
1. สร้าง branch ที่ต้องใช้ เช่น ถ้าจะมี environment แยก test กับ production ให้สร้าง branch สำหรับแต่ละอัน

ถ้าอยากตัดสินใจว่า use case ของคุณควรมี branch อะไรบ้าง ดูที่ [Branch patterns](/source-control-environments/understand/patterns.md)

## Step 2: Configure Git in n8n

--8<-- "_snippets/source-control-environments/configure-git-in-n8n.md"

## Step 3: Set up a deploy key

ตั้งค่า SSH access โดยสร้าง deploy key ให้ repository โดยใช้ SSH key จาก n8n ต้องให้สิทธิ์ write ด้วย

แต่ละ Git provider จะมีขั้นตอนต่างกัน ดูวิธีได้ที่:

* [GitHub | Managing deploy keys](https://docs.github.com/en/authentication/connecting-to-github-with-ssh/managing-deploy-keys){:target=_blank .external-link}
* [GitLab | Deploy keys](https://docs.gitlab.com/ee/user/project/deploy_keys/){:target=_blank .external-link}

## Step 4: Connect n8n and configure your instance

1. ที่ **Settings** > **Environments** ใน n8n ให้เลือก **Connect** เพื่อเชื่อมกับ Git repository
1. ที่ **Instance settings** เลือก branch ที่จะใช้กับ n8n instance นี้
1. **Optional**: เลือก **Protected instance** เพื่อป้องกันไม่ให้ user แก้ workflow ใน instance นี้ เหมาะกับ production instance
1. **Optional**: เลือกสี custom ให้ instance สีนี้จะโชว์ในเมนูข้างปุ่ม push/pull source control ช่วยให้ user รู้ว่าอยู่ instance ไหน
1. เลือก **Save settings**

