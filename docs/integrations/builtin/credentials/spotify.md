---
#https://www.notion.so/n8n/Frontmatter-432c2b8dff1f43d4b1c8d20075510fe4
title: Spotify credentials
description: Documentation for Spotify credentials. Use these credentials to authenticate Spotify in n8n, a workflow automation platform.
contentType: [integration, reference]
priority: medium
---

# Spotify credentials

คุณสามารถใช้ credentials นี้เพื่อยืนยันตัวตนกับ node ต่อไปนี้:

- [Spotify](/integrations/builtin/app-nodes/n8n-nodes-base.spotify.md)

## Supported authentication methods

- OAuth2

## Related resources

ดูข้อมูลเพิ่มเติมเกี่ยวกับบริการนี้ได้ที่ [Spotify's Web API documentation](https://developer.spotify.com/documentation/web-api){:target=_blank .external-link}

## Using OAuth2

--8<-- "_snippets/integrations/builtin/credentials/cloud-oauth-button.md"

ถ้าคุณ [self-hosting](/hosting/index.md) n8n คุณจะต้องมีบัญชี [Spotify Developer](https://developer.spotify.com/){:target=_blank .external-link} เพื่อสร้าง Spotify app:

1. เปิด [Spotify developer dashboard](https://developer.spotify.com/dashboard){:target=_blank .external-link}
2. เลือก **Create an app**
3. กรอก **App name** เช่น `n8n integration`
4. กรอก **App description**
5. คัดลอก **OAuth Redirect URL** จาก n8n แล้วนำไปใส่ใน **Redirect URI** ของ Spotify app
6. ติ๊กถูกเพื่อยอมรับ Spotify Terms of Service และ Branding Guidelines
7. กด **Create** จะเข้าสู่หน้า **App overview**
8. คัดลอก **Client ID** แล้วนำไปใส่ใน n8n credential
9. คัดลอก **Client Secret** แล้วนำไปใส่ใน n8n credential
10. กด **Connect my account** แล้วทำตามขั้นตอนบนหน้าจอเพื่อ authorize credential

ดูข้อมูลเพิ่มเติมได้ที่ [Spotify Apps](https://developer.spotify.com/documentation/web-api/concepts/apps){:target=_blank .external-link}
