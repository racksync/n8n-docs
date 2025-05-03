---
#https://www.notion.so/n8n/Frontmatter-432c2b8dff1f43d4b1c8d20075510fe4
title: ติดตั้ง Private Nodes
description: วิธีติดตั้ง node ที่สร้างเองแบบ private ใน n8n instance
contentType: howto
---

# Install private nodes

คุณสามารถสร้าง node ของตัวเองและติดตั้งใน n8n instance ของคุณได้โดยไม่ต้อง publish ขึ้น npm เหมาะสำหรับ node ที่ใช้ภายในบริษัทหรือองค์กรเท่านั้น

## Install your node in a Docker n8n instance

ถ้าคุณรัน n8n ด้วย Docker คุณต้องสร้าง Docker image ที่มี node ของคุณติดตั้งอยู่ใน n8n

1. สร้างไฟล์ Dockerfile แล้ววางโค้ดจาก [Dockerfile นี้](https://github.com/n8n-io/n8n/blob/master/docker/images/n8n/Dockerfile)

	ตัวอย่าง Dockerfile จะหน้าตาประมาณนี้:

	```Dockerfile
	FROM node:16-alpine

	ARG N8N_VERSION

	RUN if [ -z "$N8N_VERSION" ] ; then echo "The N8N_VERSION argument is missing!" ; exit 1; fi

	# Update everything and install needed dependencies
	RUN apk add --update graphicsmagick tzdata git tini su-exec

	# Set a custom user to not have n8n run as root
	USER root

	# Install n8n and the packages it needs to build it correctly.
	RUN apk --update add --virtual build-dependencies python3 build-base ca-certificates && \
		npm config set python "$(which python3)" && \
		npm_config_user=root npm install -g full-icu n8n@${N8N_VERSION} && \
		apk del build-dependencies \
		&& rm -rf /root /tmp/* /var/cache/apk/* && mkdir /root;


	# Install fonts
	RUN apk --no-cache add --virtual fonts msttcorefonts-installer fontconfig && \
		update-ms-fonts && \
		fc-cache -f && \
		apk del fonts && \
		find  /usr/share/fonts/truetype/msttcorefonts/ -type l -exec unlink {} \; \
		&& rm -rf /root /tmp/* /var/cache/apk/* && mkdir /root

	ENV NODE_ICU_DATA /usr/local/lib/node_modules/full-icu

	WORKDIR /data

	COPY docker-entrypoint.sh /docker-entrypoint.sh
	ENTRYPOINT ["tini", "--", "/docker-entrypoint.sh"]

	EXPOSE 5678/tcp
	```

2. Compile โค้ด custom node ของคุณ (`npm run build` ถ้าใช้ nodes starter) แล้ว copy โฟลเดอร์ **node** และ **credential** จากใน **dist** ไปไว้ใน `~/.n8n/custom/` ของ container เพื่อให้ Docker มองเห็น node เหล่านี้

3. ดาวน์โหลดไฟล์ [docker-entrypoint.sh](https://github.com/n8n-io/n8n/blob/master/docker/images/n8n/docker-entrypoint.sh) แล้ววางไว้ใน directory เดียวกับ Dockerfile

4. Build Docker image ของคุณ:

	```Dockerfile
	# เปลี่ยน <n8n-version-number> เป็นเวอร์ชัน n8n ที่ต้องการ เช่น N8N_VERSION=0.177.0
	docker build --build-arg N8N_VERSION=<n8n-version-number> --tag=customizedn8n .
	```

ตอนนี้คุณก็สามารถใช้ node ของคุณใน Docker ได้แล้ว

## Install your node in a global n8n instance

ถ้าคุณติดตั้ง n8n แบบ global ให้แน่ใจว่าคุณติดตั้ง node ของคุณไว้ใน n8n ด้วย n8n จะค้นหา module และโหลดให้อัตโนมัติ
