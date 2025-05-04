* Split the data processed into smaller chunks. For example, instead of fetching 10,000 rows with each execution, process 200 rows with each execution.
* Avoid using the Code node where possible.
* Avoid manual executions when processing larger amounts of data.
* Split the workflow up into sub-workflows and ensure each sub-workflow returns a limited amount of data to its parent workflow.

การแบ่ง Workflow อาจดูขัดกับความรู้สึกในตอนแรก เพราะโดยปกติแล้วจะต้องเพิ่ม Node อย่างน้อยสองตัว: Node [Loop Over Items](/integrations/builtin/core-nodes/n8n-nodes-base.splitinbatches.md) เพื่อแบ่งรายการออกเป็นชุดย่อยๆ และ Node [Execute Workflow](/integrations/builtin/core-nodes/n8n-nodes-base.executeworkflow.md) เพื่อเริ่ม Sub-workflow

อย่างไรก็ตาม ตราบใดที่ Sub-workflow ของคุณทำงานหนักในแต่ละชุดข้อมูล (Batch) แล้วส่งคืนผลลัพธ์ชุดเล็กๆ กลับไปยัง Workflow หลัก วิธีนี้จะช่วยลดการใช้หน่วยความจำได้ เนื่องจาก Sub-workflow จะเก็บข้อมูลเฉพาะของ Batch ปัจจุบันไว้ในหน่วยความจำเท่านั้น หลังจากนั้นหน่วยความจำก็จะถูกคืนค่า
