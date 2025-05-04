/// note | Parameter resolution in sub-nodes (การประมวลผล Parameter ใน sub-nodes)
Sub-nodes มีพฤติกรรมแตกต่างจาก node อื่นๆ เมื่อประมวลผลหลายรายการโดยใช้ expression

Node ส่วนใหญ่ รวมถึง root node จะรับ input กี่รายการก็ได้ ประมวลผลรายการเหล่านี้ และส่ง output ออกมา คุณสามารถใช้ expression เพื่ออ้างอิงถึง input item และ node จะประมวลผล expression สำหรับแต่ละ item ตามลำดับ ตัวอย่างเช่น หากมี input เป็นค่า `name` ห้ารายการ expression `{{ $json.name }}` จะถูกประมวลผลเป็นแต่ละชื่อตามลำดับ

ใน sub-nodes expression จะถูกประมวลผลเป็น item แรกเสมอ ตัวอย่างเช่น หากมี input เป็นค่า `name` ห้ารายการ expression `{{ $json.name }}` จะถูกประมวลผลเป็นชื่อแรกเสมอ
///