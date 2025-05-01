---
#https://www.notion.so/n8n/Frontmatter-432c2b8dff1f43d4b1c8d20075510fe4
title: Copy work between environments
description: How to get changes from one environment into another.
contentType: howto
---

# Copy work between environments

ขั้นตอนการส่งงานจาก n8n instance หนึ่งไปอีกอันจะต่างกัน ขึ้นอยู่กับว่าคุณใช้ Git branch เดียวหรือหลาย branch

## Single branch

ถ้าคุณใช้ Git branch เดียว ขั้นตอน copy งานคือ:

1. push งานจาก instance หนึ่งไปที่ Git branch
1. login เข้าอีก instance เพื่อ pull งานจาก Git คุณสามารถ [automate pulls](#automatically-send-changes-to-n8n) ได้

## Multiple branches

ถ้าคุณมี Git branch มากกว่าหนึ่ง คุณต้อง merge branch ใน Git provider เพื่อ copy งานระหว่าง environments คุณไม่สามารถ copy งานตรงๆ ระหว่าง environments ใน n8n ได้

pattern ที่เจอบ่อยคือ:

1. ทำงานใน development instance
1. push งานไปที่ development branch ใน Git
1. merge development branch เข้า production branch ดูวิธี merge ได้ที่:
	* [GitHub: Creating a pull request](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/creating-a-pull-request){:target=_blank .external-link}
	* [GitLab: Creating merge requests](https://docs.gitlab.com/ee/user/project/merge_requests/creating_merge_requests.html){:target=_blank .external-link}
	* [Git: Basic branching and merging](https://git-scm.com/book/en/v2/Git-Branching-Basic-Branching-and-Merging){:target=_blank .external-link}
1. ใน production n8n instance ให้ pull การเปลี่ยนแปลง คุณสามารถ [automate pulls](#automatically-send-changes-to-n8n) ได้

## Automatically send changes to n8n

คุณสามารถ automate บางส่วนของการ copy งานได้ โดยใช้ endpoint `/source-control/pull` ของ API เรียก API หลัง merge เสร็จ:

```curl
curl --request POST \
	--location '<YOUR-INSTANCE-URL>/api/v1/source-control/pull' \
	--header 'Content-Type: application/json' \
	--header 'X-N8N-API-KEY: <YOUR-API-KEY>' \
	--data '{"force": true}'
```

แบบนี้คุณสามารถใช้ GitHub Action หรือ GitLab CI/CD เพื่อ pull งานเข้า production instance อัตโนมัติหลัง merge

--8<-- "_snippets/source-control-environments/github-action.md"

