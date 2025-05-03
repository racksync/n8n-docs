---
#https://www.notion.so/n8n/Frontmatter-432c2b8dff1f43d4b1c8d20075510fe4
title: ข้อมูลรับรอง Discord
description: เอกสารข้อมูลรับรอง Discord ใช้ข้อมูลนี้เพื่อยืนยันตัวตน Discord ใน n8n
contentType: [integration, reference]
priority: high
---

# Discord credentials

คุณสามารถใช้ credentials นี้เพื่อเชื่อมต่อกับ node เหล่านี้:

- [Discord](/integrations/builtin/app-nodes/n8n-nodes-base.discord/index.md)

## Prerequisites

- สมัคร [Discord](https://www.discord.com/){:target=_blank .external-link} ให้เรียบร้อยก่อน
- สำหรับ Bot และ OAuth2 credentials:
    - [ตั้งค่า local developer environment ของคุณ](https://discord.com/developers/docs/quick-start/getting-started#step-0-project-setup){:target=_blank .external-link}
    - [สร้าง application และ bot user](https://discord.com/developers/docs/quick-start/getting-started#step-1-creating-an-app){:target=_blank .external-link}
- สำหรับ webhook credentials [สร้าง webhook](https://support.discord.com/hc/en-us/articles/228383668-Intro-to-Webhooks){:target=_blank .external-link}

## Supported authentication methods

- Bot
- OAuth2
- Webhook

ไม่แน่ใจว่าควรใช้วิธีไหน? ดูคำแนะนำเพิ่มเติมได้ที่ [Choose an authentication method](#choose-an-authentication-method)

## Related resources

ดูรายละเอียดเพิ่มเติมเกี่ยวกับการใช้งาน API ได้ที่ [Discord's Developer documentation](https://discord.com/developers/docs/intro){:target=_blank .external-link}

## Using bot

ใช้วิธีนี้หากคุณต้องการเพิ่ม bot ไปยัง Discord server ของคุณโดยใช้ bot token แทน OAuth2

ถ้าจะตั้งค่า credentials นี้ คุณต้องมี:

- **Bot Token**: สร้างขึ้นเมื่อคุณสร้าง application พร้อม bot

วิธีสร้าง application พร้อม bot และสร้าง **Bot Token**:

1. หากยังไม่มี ให้สร้าง app ใน [developer portal](https://discord.com/developers/applications?new_application=true){:target=_blank .external-link}
2. ป้อน **Name** สำหรับ app ของคุณ
3. เลือก **Create**
4. เลือก **Bot** จากเมนูด้านซ้าย
5. ใต้ **Token** เลือก **Reset Token** เพื่อสร้าง bot token ใหม่
6. คัดลอก token และเพิ่มลงใน n8n credential ของคุณ
7. ใน **Bot > Privileged Gateway Intents** เพิ่ม privileged intents ที่คุณต้องการให้ bot ของคุณมี ดูข้อมูลเพิ่มเติมเกี่ยวกับ privileged intents ได้ที่ [Configuring your bot](https://discord.com/developers/docs/quick-start/getting-started#configuring-your-bot){:target=_blank .external-link}
    - n8n แนะนำให้เปิดใช้งาน **SERVER MEMBERS INTENT: Required for your bot to receive events listed under GUILD_MEMBERS**
8. ใน **Installation > Installation Contexts** เลือก installation contexts ที่คุณต้องการให้ bot ของคุณใช้:
    - เลือก **Guild Install** สำหรับ app ที่ติดตั้งบน server (พบบ่อยที่สุดสำหรับผู้ใช้ n8n)
    - เลือก **User Install** สำหรับ app ที่ติดตั้งโดยผู้ใช้ (พบน้อยกว่าสำหรับผู้ใช้ n8n แต่อาจมีประโยชน์สำหรับการทดสอบ)
    - ดูข้อมูลเพิ่มเติมเกี่ยวกับ installation contexts เหล่านี้ได้ที่เอกสาร [Choosing installation contexts](https://discord.com/developers/docs/quick-start/getting-started#choosing-installation-contexts){:target=_blank .external-link} ของ Discord
9. ใน **Installation > Install Link** เลือก **Discord Provided Link** หากยังไม่ได้เลือกไว้
10. ยังคงอยู่ที่หน้า **Installation** ในส่วน **Default Install Settings** เลือก `applications.commands` และ `bot` scopes ดูข้อมูลเพิ่มเติมเกี่ยวกับ scopes เหล่านี้และ scopes อื่นๆ ได้ที่เอกสาร [Scopes](https://discord.com/developers/docs/topics/oauth2#shared-resources-oauth2-scopes){:target=_blank .external-link} ของ Discord
11. เพิ่ม permissions ในหน้า **Bot > Bot Permissions** ดูข้อมูลเพิ่มเติมได้ที่เอกสาร [Permissions](https://discord.com/developers/docs/topics/permissions){:target=_blank .external-link} ของ Discord n8n แนะนำให้เลือก permissions เหล่านี้สำหรับ [Discord](/integrations/builtin/app-nodes/n8n-nodes-base.discord/index.md) node:
    - Manage Roles
    - Manage Channels
    - Read Messages/View Channels
    - Send Messages
    - Create Public Threads
    - Create Private Threads
    - Send Messages in Threads
    - Send TTS Messages
    - Manage Messages
    - Manage Threads
    - Embed Links
    - Attach Files
    - Read Message History
    - Add Reactions
12. เพิ่ม app ไปยัง server หรือ test server ของคุณ:
    1. ไปที่ **Installation > Install Link** และคัดลอก link ที่แสดงอยู่
    2. วาง link ในเบราว์เซอร์ของคุณแล้วกด Enter
    1. เลือก **Add to server** ในหน้าต่างการติดตั้ง
    1. เมื่อ app ของคุณถูกเพิ่มไปยัง server แล้ว คุณจะเห็นมันใน member list

ขั้นตอนเหล่านี้สรุปฟังก์ชันพื้นฐานที่จำเป็นในการตั้งค่า n8n credential ของคุณ ดูข้อมูลเพิ่มเติมเกี่ยวกับการสร้าง app ได้ที่คู่มือ [Discord Creating an App](https://discord.com/developers/docs/quick-start/getting-started#step-1-creating-an-app){:target=_blank .external-link} โดยเฉพาะ:

- [Fetching your credentials](https://discord.com/developers/docs/quick-start/getting-started#fetching-your-credentials){:target=_blank .external-link} สำหรับการนำ credentials ของ app เข้าสู่ local developer environment ของคุณ
- [Handling interactivity](https://discord.com/developers/docs/quick-start/getting-started#step-3-handling-interactivity){:target=_blank .external-link} สำหรับข้อมูลเกี่ยวกับการตั้งค่า public endpoints สำหรับคำสั่ง `/slash` แบบโต้ตอบ

## Using OAuth2

ใช้วิธีนี้หากคุณต้องการเพิ่ม bot ไปยัง Discord servers โดยใช้ OAuth2 flow ซึ่งทำให้กระบวนการง่ายขึ้นสำหรับผู้ที่ติดตั้ง app ของคุณ

ถ้าจะตั้งค่า credentials นี้ คุณต้องมี:

- **Client ID**
- **Client Secret**
- เลือกว่าจะส่ง **Authentication** ใน **Header** หรือ **Body**
- **Bot Token**

สำหรับรายละเอียดเกี่ยวกับการสร้าง application พร้อม bot และการสร้าง token ให้ทำตามขั้นตอนเดียวกับใน [Using bot](#using-bot) ด้านบน

จากนั้น:

1. คัดลอก **Bot Token** ที่คุณสร้างขึ้นและเพิ่มลงใน n8n credential
2. เปิดหน้า **OAuth2** ใน Discord application ของคุณเพื่อเข้าถึง **Client ID** และสร้าง **Client Secret** เพิ่มข้อมูลเหล่านี้ลงใน n8n credential ของคุณ
3. จาก n8n คัดลอก **OAuth Redirect URL** และเพิ่มลงใน Discord application ใน **OAuth2 > Redirects** อย่าลืมบันทึกการเปลี่ยนแปลงเหล่านี้

## Using webhook

ถ้าจะตั้งค่า credentials นี้ คุณต้องมี:

- **Webhook URL**: สร้างขึ้นเมื่อคุณสร้าง webhook

หากต้องการรับ Webhook URL คุณต้องสร้าง webhook และคัดลอก URL ที่สร้างขึ้น:

1. เปิด **Server Settings** ของ Discord และเปิดแท็บ **Integrations**
2. เลือก **Create Webhook** เพื่อสร้าง webhook ใหม่
3. ตั้ง **Name** ที่สื่อความหมายให้กับ webhook ของคุณ
3. เลือก **avatar** ถัดจาก **Name** เพื่อแก้ไขหรืออัปโหลด avatar ใหม่
4. ใน dropdown **CHANNEL** เลือก channel ที่ webhook ควรโพสต์ไป
5. เลือก **Copy Webhook URL** เพื่อคัดลอก Webhook URL ป้อน URL นี้ใน n8n credential ของคุณ

ดูข้อมูลเพิ่มเติมได้ที่เอกสาร [Discord Making a Webhook documentation](https://support.discord.com/hc/en-us/articles/228383668-Intro-to-Webhooks){:target=_blank .external-link}

## Choose an authentication method

การติดตั้งที่ง่ายที่สุดคือ **webhook** คุณสร้างและเพิ่ม webhooks ไปยัง channel เดียวบน Discord server Webhooks สามารถโพสต์ข้อความไปยัง channel ได้ ไม่จำเป็นต้องมี bot user หรือ authentication แต่ไม่สามารถฟังหรือตอบสนองต่อคำขอหรือคำสั่งของผู้ใช้ได้ หากคุณต้องการวิธีที่ตรงไปตรงมาในการส่งข้อความไปยัง channel โดยไม่จำเป็นต้องมีการโต้ตอบหรือข้อเสนอแนะ ให้ใช้ webhook

**bot** เป็นขั้นตอนที่โต้ตอบได้มากกว่า webhook คุณเพิ่ม bots ไปยัง Discord server (เรียกว่า `guild` ในเอกสาร Discord API) หรือไปยังบัญชีผู้ใช้ Bots ที่เพิ่มไปยัง server สามารถโต้ตอบกับผู้ใช้ในทุก channels ของ server ได้ สามารถจัดการ channels ส่งและดึงข้อความ ดึงรายชื่อผู้ใช้ทั้งหมด และเปลี่ยน roles ของพวกเขาได้ หากคุณต้องการสร้าง workflow ที่โต้ตอบได้ ซับซ้อน หรือหลายขั้นตอน ให้ใช้ bot

**OAuth2** โดยพื้นฐานแล้วคือ **bot** ที่ใช้ OAuth2 flow แทนที่จะใช้เพียง bot token เช่นเดียวกับ bots คุณเพิ่มสิ่งเหล่านี้ไปยัง Discord server หรือบัญชีผู้ใช้ Credentials เหล่านี้มีฟังก์ชันการทำงานเช่นเดียวกับ bots แต่สามารถทำให้การติดตั้ง bot บน server ของคุณง่ายขึ้น

