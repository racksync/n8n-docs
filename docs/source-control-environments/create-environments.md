---
#https://www.notion.so/n8n/Frontmatter-432c2b8dff1f43d4b1c8d20075510fe4
title: Tutorial - สร้าง Environments ด้วย Source control
description: วิธีใช้ฟีเจอร์ source control ของ n8n เพื่อสร้าง environments
contentType: tutorial
---

# Tutorial: Create environments with source control

--8<-- "_snippets/source-control-environments/feature-availability.md"

tutorial นี้จะพาคุณตั้งค่า environments แบบ end-to-end คุณจะสร้าง environment สองอัน: development กับ production โดยใช้ GitHub เป็น Git provider (ถ้าใช้ provider อื่นก็คล้ายๆ กัน)

n8n สร้างฟีเจอร์ environments บน Git ซึ่งเป็นซอฟต์แวร์ version control คุณจะเชื่อม n8n instance กับ Git branch แล้วใช้ pattern push-pull เพื่อย้ายงานระหว่าง environments ควรเข้าใจ environments กับ Git มาก่อน ถ้าอยากอ่านเพิ่มดูที่:

* [Environments in n8n](/source-control-environments/understand/environments.md): จุดประสงค์ของ environments และวิธีการทำงานใน n8n
* [Git and n8n](/source-control-environments/understand/git.md): concept ของ Git และ source control ใน n8n

## Choose your source control pattern

ก่อนจะ setup source control กับ environments คุณต้องวางแผน environments กับความสัมพันธ์กับ Git branch n8n รองรับ [Branch patterns](/source-control-environments/understand/patterns.md) หลายแบบ สำหรับ environments ให้เลือกว่าจะใช้ multi-instance multi-branch หรือ multi-instance single-branch tutorial นี้จะสอนทั้งสองแบบ

--8<-- "_snippets/source-control-environments/one-direction.md"

### Multiple instances, multiple branches

![Diagram](/_images/source-control-environments/vc-multi-multi.png)

--8<-- "_snippets/source-control-environments/multi-instance-multi-branch-pros-cons.md"


### Multiple instances, one branch

![Diagram](/_images/source-control-environments/vc-multi-one.png)

--8<-- "_snippets/source-control-environments/multi-instance-one-branch-pros-cons.md"

## Set up your repository

เลือก pattern เสร็จแล้ว ให้ setup GitHub repository

=== "Multi-branch"

    1. [Create a new repository](https://docs.github.com/en/repositories/creating-and-managing-repositories/creating-a-new-repository){:target=_blank .external-link}
	    * ให้ repository เป็น private เว้นแต่คุณอยากให้ workflow, tag, variable, credential stub ของคุณเปิดเผยต่อสาธารณะ
	    * สร้าง repository พร้อม README เพื่อจะได้สร้าง branch ได้ทันที
    1. สร้าง branch ชื่อ `production` กับ `development` ดูวิธีที่ [Creating and deleting branches within your repository](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/creating-and-deleting-branches-within-your-repository){:target=_blank .external-link}
			

=== "Single-branch"

    [Create a new repository](https://docs.github.com/en/repositories/creating-and-managing-repositories/creating-a-new-repository){:target=_blank .external-link}

      * ให้ repository เป็น private เว้นแต่คุณอยากให้ workflow, tag, variable, credential stub ของคุณเปิดเผยต่อสาธารณะ  
      * สร้าง repository พร้อม README จะได้ branch `main` ไว้เชื่อมต่อ
		

## Connect your n8n instances to your repository

สร้าง n8n instance สองอัน อันหนึ่งสำหรับ development อีกอันสำหรับ production

### Configure Git in n8n

--8<-- "_snippets/source-control-environments/configure-git-in-n8n.md"

### Set up a deploy key

ตั้งค่า SSH access โดยสร้าง deploy key ให้ repository โดยใช้ SSH key จาก n8n ต้องให้สิทธิ์ write ดูวิธีที่ [GitHub | Managing deploy keys](https://docs.github.com/en/authentication/connecting-to-github-with-ssh/managing-deploy-keys){:target=_blank .external-link}

### Connect n8n and configure your instance

=== "Multi-branch"

    1. ที่ **Settings** > **Environments** ใน n8n ให้เลือก **Connect** เพื่อเชื่อมกับ Git repository
    1. ที่ **Instance settings** เลือก branch ที่จะใช้กับ n8n instance นี้ เชื่อม production branch กับ production instance, development branch กับ development instance
    1. production instance เท่านั้น: เลือก **Protected instance** เพื่อป้องกันไม่ให้ user แก้ workflow ใน instance นี้
    1. เลือก **Save settings**

=== "Single-branch"

    1. ที่ **Settings** > **Environments** ใน n8n ให้เลือก **Connect**
	  1. ที่ **Instance settings** เลือก main branch
    1. production instance เท่านั้น: เลือก **Protected instance** เพื่อป้องกันไม่ให้ user แก้ workflow ใน instance นี้
    1. เลือก **Save settings**

## Push work from development

ใน development instance ให้สร้าง workflow, tag, variable, credential ขึ้นมาสักหน่อย

--8<-- "_snippets/source-control-environments/push.md"

## Pull work to production

ตอนนี้งานของคุณอยู่ใน GitHub แล้ว ถ้าใช้ multi-branch จะอยู่ใน development branch ถ้าใช้ single-branch จะอยู่ใน main

=== "Multi-branch"

    1. ใน GitHub ให้สร้าง pull request เพื่อ merge development เข้า production
    1. merge pull request
    1. ที่ production instance ให้เลือก **Pull** <span class="inline-image">![Pull icon](/_images/source-control-environments/pull-icon.png){.off-glb}</span> ในเมนูหลัก

=== "Single-branch"

    ที่ production instance ให้เลือก **Pull** <span class="inline-image">![Pull icon](/_images/source-control-environments/pull-icon.png){.off-glb}</span> ในเมนูหลัก

--8<-- "_snippets/source-control-environments/push-pull-menu-state.md"

### Optional: Use a GitHub Action to automate pulls

ถ้าไม่อยาก login เข้า production instance เพื่อ pull งานเอง สามารถใช้ [GitHub Action](https://docs.github.com/en/actions/creating-actions/about-custom-actions){:target=_blank .external-link} กับ [n8n API](/api/index.md) เพื่อ pull อัตโนมัติทุกครั้งที่ push งานใหม่เข้า production หรือ main branch

--8<-- "_snippets/source-control-environments/github-action.md"


## Next steps

อ่านต่อเกี่ยวกับ:

* [Environments in n8n](/source-control-environments/understand/environments.md) และ [Git and n8n](/source-control-environments/understand/git.md)
* [Source control patterns](/source-control-environments/understand/patterns.md)
* [Variables](/code/variables.md) ที่นำกลับมาใช้ซ้ำได้ และ [Managing variables using the API](/source-control-environments/using/manage-variables.md) ตอนใช้ source control
