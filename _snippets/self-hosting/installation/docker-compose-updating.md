หากคุณรัน n8n โดยใช้ไฟล์ Docker Compose ให้ทำตามขั้นตอนเหล่านี้เพื่ออัปเดต n8n:

```sh
# Pull latest version
docker compose pull

# Stop and remove older version
docker compose down

# Start the container
docker compose up -d
```
