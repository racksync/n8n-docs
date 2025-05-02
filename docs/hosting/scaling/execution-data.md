---
#https://www.notion.so/n8n/Frontmatter-432c2b8dff1f43d4b1c8d20075510fe4
contentType: howto
---

# Execution data

ขึ้นอยู่กับการตั้งค่า execution และปริมาณงาน database ของ n8n อาจโตจนเต็ม storage ได้

เพื่อป้องกันปัญหานี้ n8n แนะนำให้ไม่บันทึกข้อมูลที่ไม่จำเป็น และเปิดการลบ execution data เก่าอัตโนมัติ

ตั้งค่าด้วย [environment variables](/hosting/configuration/environment-variables/executions.md)

## Reduce saved data

/// note | Configuration at workflow level
ตั้งค่าเหล่านี้ได้ในแต่ละ workflow ด้วย [workflow settings](/workflows/settings.md)
///
คุณสามารถเลือกได้ว่า n8n จะบันทึก execution data แบบไหน เช่น บันทึกเฉพาะ execution ที่ error

```sh
# npm
# บันทึก execution ที่ error
export EXECUTIONS_DATA_SAVE_ON_ERROR=all

# บันทึก execution ที่สำเร็จ
export EXECUTIONS_DATA_SAVE_ON_SUCCESS=all

# ไม่บันทึก node progress ของแต่ละ execution
export EXECUTIONS_DATA_SAVE_ON_PROGRESS=false

# ไม่บันทึก execution ที่รันแบบ manual
export EXECUTIONS_DATA_SAVE_MANUAL_EXECUTIONS=false

```

```sh
# Docker
docker run -it --rm \
 --name n8n \
 -p 5678:5678 \
 -e EXECUTIONS_DATA_SAVE_ON_ERROR=all \
 -e EXECUTIONS_DATA_SAVE_ON_SUCCESS=none \
 -e EXECUTIONS_DATA_SAVE_ON_PROGRESS=true \
 -e EXECUTIONS_DATA_SAVE_MANUAL_EXECUTIONS=false \
 docker.n8n.io/n8nio/n8n
```

```yaml
# Docker Compose
n8n:
    environment:
      - EXECUTIONS_DATA_SAVE_ON_ERROR=all
      - EXECUTIONS_DATA_SAVE_ON_SUCCESS=none
      - EXECUTIONS_DATA_SAVE_ON_PROGRESS=true
      - EXECUTIONS_DATA_SAVE_MANUAL_EXECUTIONS=false
```

## Enable data pruning

คุณสามารถเปิดการลบ execution ที่เสร็จแล้วอัตโนมัติหลังเวลาที่กำหนด ถ้าไม่ตั้ง `EXECUTIONS_DATA_MAX_AGE` ค่า default คือ 336 ชั่วโมง (14 วัน)

คุณสามารถเลือกให้ลบ execution ก่อนถึงเวลาที่ตั้งไว้ โดยใช้ `EXECUTIONS_DATA_PRUNE_MAX_COUNT` เพื่อกำหนดจำนวน execution สูงสุดที่เก็บใน database ถ้าเกิน n8n จะลบ execution เก่าที่สุด ช่วยให้ database ทำงานเร็วขึ้น โดยเฉพาะถ้าใช้ SQLite ขนาด database อาจเกิน limit ที่ตั้งไว้ได้ถ้ามี execution ที่ยังไม่เสร็จ

```sh
# npm
# เปิดการลบ execution อัตโนมัติ
export EXECUTIONS_DATA_PRUNE=true

# จำนวนชั่วโมงหลัง execution ที่ n8n จะลบข้อมูล
export EXECUTIONS_DATA_MAX_AGE=168

# จำนวน execution ที่เก็บใน database
export EXECUTIONS_DATA_PRUNE_MAX_COUNT=50000
```

```sh
# Docker
docker run -it --rm \
 --name n8n \
 -p 5678:5678 \
 -e EXECUTIONS_DATA_PRUNE=true \
 -e EXECUTIONS_DATA_MAX_AGE=168 \
 docker.n8n.io/n8nio/n8n
```

```yaml
# Docker Compose
n8n:
    environment:
      - EXECUTIONS_DATA_PRUNE=true
      - EXECUTIONS_DATA_MAX_AGE=168
	  	- EXECUTIONS_DATA_PRUNE_MAX_COUNT=50000
```

/// note | SQLite
ถ้าใช้ n8n กับ SQLite database พื้นที่ disk ของข้อมูลที่ถูกลบจะไม่ถูกคืนทันทีแต่จะถูกใช้ซ้ำสำหรับ execution ใหม่ ถ้าอยากคืนพื้นที่ให้ตั้ง `DB_SQLITE_VACUUM_ON_STARTUP` [environment variable](/hosting/configuration/environment-variables/database.md#sqlite) หรือรัน [VACUUM](https://www.sqlite.org/lang_vacuum.html){:target=_blank .external-link} เอง
///

--8<-- "_snippets/self-hosting/scaling/binary-data-pruning.md"
