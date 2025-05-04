### Metadata Filter (ตัวกรอง Metadata)

มีให้ใช้งานในโหมด **Get Many** เมื่อค้นหาข้อมูล ใช้ตัวเลือกนี้เพื่อจับคู่กับ metadata ที่เกี่ยวข้องกับเอกสาร

นี่คือการ query แบบ `AND` หากคุณระบุฟิลด์ตัวกรอง metadata มากกว่าหนึ่งฟิลด์ ทุกฟิลด์จะต้องตรงกันทั้งหมด

เมื่อแทรกข้อมูล metadata จะถูกตั้งค่าโดยใช้ document loader อ้างอิง [Default Data Loader](/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.documentdefaultdataloader.md) สำหรับข้อมูลเพิ่มเติมเกี่ยวกับการโหลดเอกสาร
