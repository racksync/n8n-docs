Slack มีฟีเจอร์ **token rotation** ที่คุณสามารถเปิดใช้งานสำหรับ bot token และ user token ได้ ซึ่งจะทำให้ token ทุกตัวหมดอายุหลังจาก 12 ชั่วโมง แม้ว่าฟีเจอร์นี้อาจมีประโยชน์สำหรับการทดสอบ แต่ n8n credentials ที่ใช้ token ซึ่งเปิดใช้งานฟีเจอร์นี้จะใช้งานไม่ได้หลังจากหมดอายุ หากคุณต้องการใช้ Slack credentials ของคุณใน production ฟีเจอร์นี้จะต้อง **ปิด** อยู่

หากต้องการตรวจสอบว่าแอป Slack ของคุณเปิดใช้งาน token rotation หรือไม่ โปรดดูที่ [Slack API Documentation | Token Rotation](https://api.slack.com/authentication/rotation){:target=_blank .external-link}

/// note | หากแอปของคุณใช้ token rotation
โปรดทราบ หากแอป Slack ของคุณใช้ token rotation คุณจะไม่สามารถปิดใช้งานได้อีก คุณจำเป็นต้องสร้างแอป Slack ใหม่โดยปิดใช้งาน token rotation แทน
///
