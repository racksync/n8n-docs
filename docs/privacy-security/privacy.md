---
#https://www.notion.so/n8n/Frontmatter-432c2b8dff1f43d4b1c8d20075510fe4
description: นโยบายความเป็นส่วนตัวของ n8n
tags:
  - gdpr
  - data collection
  - pid
  - payment processor
hide:
  - tags
contentType: explanation
---

<!-- vale off -->

# Privacy

หน้านี้อธิบายแนวปฏิบัติด้านความเป็นส่วนตัวของข้อมูลของ n8n

## GDPR

### Data processing agreement

สำหรับ n8n เวอร์ชัน Cloud, n8n ถือเป็นทั้ง Controller และ Processor ตามที่กำหนดโดย GDPR ในฐานะ Processor, n8n ใช้ นโยบายและแนวปฏิบัติที่รักษาความปลอดภัยข้อมูลส่วนบุคคลที่คุณส่งไปยังแพลตฟอร์ม และรวม [Data Processing Agreement](https://n8n.io/legal/#data){:target=_blank .external-link} เป็นส่วนหนึ่งของ [Terms of Service](https://n8n.io/legal/#terms){:target=_blank .external-link} มาตรฐานของบริษัท

n8n Data Processing Agreement รวมถึง [Standard Contractual Clauses (SCCs)](https://ec.europa.eu/info/law/law-topic/data-protection/international-dimension-data-protection/standard-contractual-clauses-scc_en){:target=_blank .external-link} สิ่งเหล่านี้ชี้แจงว่า n8n จัดการข้อมูลของคุณอย่างไร และอัปเดตนโยบาย GDPR ของ n8n ให้ครอบคลุมมาตรฐานล่าสุดที่กำหนดโดยคณะกรรมาธิการยุโรป

คุณสามารถดูรายชื่อ sub-processors ของ n8n ได้ [ที่นี่](https://n8n.io/legal/#subprocessors){:target=_blank .external-link}

/// note | Self-hosted n8n
สำหรับเวอร์ชัน self-hosted, n8n ไม่ใช่ทั้ง Controller หรือ Processor เนื่องจากเราไม่ได้จัดการข้อมูลของคุณ
///
### Submitting a GDPR deletion request

ส่งอีเมลไปที่ privacy@n8n.io เพื่อขอให้ลบข้อมูล

### Sub-processors

นี่คือรายชื่อ sub-processors ที่ได้รับอนุญาตให้ประมวลผลข้อมูลลูกค้าสำหรับบริการของ n8n n8n ตรวจสอบการควบคุมความปลอดภัยและกฎระเบียบที่เกี่ยวข้องของ sub-processor แต่ละรายเพื่อการปกป้องข้อมูลส่วนบุคคล

| Sub-processor name | Contact details | Geographic location of processing |
| ------------------ | --------------- | --------------------------------- |
| Microsoft Azure | Microsoft Azure <br /> 1 Microsoft Way <br /> Redmond <br /> WA 98052 <br /> USA <br /> Contact information: https://privacy.microsoft.com/en-GB/privacystatement#mainhowtocontactusmodule | Germany (West Central Region) |
| Hetzner Online | Hetzner Online GmbH <br /> Industriestr. 25 <br /> 91710 Gunzenhausen <br /> Germany <br /> data-protection@hetzner.com | Germany |

สมัครรับข้อมูล [ที่นี่](https://n8n-community.typeform.com/to/FdeRxSkH?typeform-source=n8n.io){:target=_blank .external-link} เพื่อรับการอัปเดตเมื่อ n8n เพิ่มหรือเปลี่ยนแปลง sub-processor

### GDPR for self-hosted users

--8<-- "_snippets/privacy-security/gdpr-self-hosted.md"



## Data collection

n8n เก็บรวบรวมข้อมูลการใช้งานและประสิทธิภาพที่เลือกสรร เพื่อช่วยวินิจฉัยปัญหาและปรับปรุงแพลตฟอร์ม อ่านเกี่ยวกับวิธีที่ n8n จัดเก็บและประมวลผลข้อมูลนี้ใน [privacy policy](https://n8n.io/legal/#privacy){:target=_blank .external-link}

ข้อมูลที่รวบรวมจะแตกต่างกันใน n8n แบบ self-hosted และ n8n Cloud

### Data collection in self-hosted n8n

n8n ระมัดระวังในการรักษาข้อมูล self-hosted ให้เป็นนิรนามและหลีกเลี่ยงการเก็บข้อมูลที่ละเอียดอ่อน

#### What n8n collects

- รหัสข้อผิดพลาดและข้อความของ executions ที่ล้มเหลว (ไม่รวมข้อมูล payload ใดๆ และไม่ใช่สำหรับ custom nodes)
- รายงานข้อผิดพลาดสำหรับ app crashes และปัญหา API
- กราฟของ workflow (ประเภทของ nodes ที่ใช้และวิธีเชื่อมต่อ)
- จาก node parameters:
    - 'resource' และ 'operation' ที่ node ถูกตั้งค่าไว้ (ถ้ามี)
    - สำหรับ HTTP request nodes, โดเมน, path และ method (โดยข้อมูลส่วนบุคคลจะถูกทำให้เป็นนิรนาม)
- ข้อมูลเกี่ยวกับการรัน workflow (workflow executions):
    - สถานะ (Status)
    - User ID ของผู้ใช้ที่รัน execution
    - ครั้งแรกที่ workflow โหลดข้อมูลจากแหล่งภายนอก
    - การรัน workflow ใน production (ที่ไม่ใช่ manual) ครั้งแรกที่สำเร็จ
- โดเมนของ webhook calls หากระบุ (ไม่รวม subdomain)
- รายละเอียดเกี่ยวกับวิธีการใช้ UI (เช่น การนำทาง, การค้นหาใน nodes panel)
- ข้อมูลการวินิจฉัย (Diagnostic information):
    - เวอร์ชัน n8n
    - การตั้งค่าที่เลือก:
        - DB_TYPE
        - N8N_VERSION_NOTIFICATIONS_ENABLED
        - N8N_DISABLE_PRODUCTION_MAIN_PROCESS
        - [Execution variables](/hosting/configuration/environment-variables/executions.md)
    - OS, RAM และ CPUs
    - Anonymous instance ID
 - IP address

#### What n8n doesn't collect

n8n ไม่เก็บข้อมูลส่วนตัวหรือข้อมูลที่ละเอียดอ่อน เช่น:

- ข้อมูลที่สามารถระบุตัวตนได้ (Personally identifiable information) (ยกเว้น IP address)
- ข้อมูล Credential
- Node parameters (ยกเว้น 'resource' และ 'operation')
- Execution data
- การตั้งค่าที่ละเอียดอ่อน (เช่น endpoints, ports, DB connections, username/password)
- Error payloads

#### How collection works

ข้อมูลส่วนใหญ่จะถูกส่งไปยัง n8n เมื่อมี events เกิดขึ้น จำนวนการรัน workflow และ instance pulse จะถูกส่งเป็นระยะ (ทุก 6 ชั่วโมง)

#### Opting out of telemetry

การเก็บข้อมูล Telemetry เปิดใช้งานโดยค่าเริ่มต้น หากต้องการปิดใช้งาน คุณสามารถกำหนดค่าตัวแปรสภาพแวดล้อมต่อไปนี้

หากต้องการยกเลิกการเก็บข้อมูล telemetry events:

```bash
export N8N_DIAGNOSTICS_ENABLED=false
```

หากต้องการยกเลิกการตรวจสอบเวอร์ชันใหม่ของ n8n:

```bash
export N8N_VERSION_NOTIFICATIONS_ENABLED=false
```

ดู [configuration](/hosting/configuration/configuration-methods.md) สำหรับข้อมูลเพิ่มเติมเกี่ยวกับวิธีการตั้งค่าตัวแปรสภาพแวดล้อม

### Data collection in n8n Cloud

n8n Cloud เก็บรวบรวมทุกอย่างที่ระบุไว้ใน [Data collection in self-hosted n8n](#data-collection-in-self-hosted-n8n)

นอกจากนี้ ใน n8n Cloud, n8n ใช้ [PostHog](https://posthog.com/){:target=_blank .external-link} เพื่อติดตาม events และแสดงภาพการใช้งาน รวมถึงการใช้ session recordings Session recordings ประกอบด้วยข้อมูลที่ผู้ใช้เห็นบนหน้าจอ ยกเว้นค่า credential ทีมผลิตภัณฑ์ของ n8n ใช้ข้อมูลนี้เพื่อปรับปรุงผลิตภัณฑ์ การบันทึกทั้งหมดจะถูกลบหลังจาก 21 วัน

### AI in n8n

เพื่อให้ความช่วยเหลือที่ดียิ่งขึ้น n8n ได้รวมฟีเจอร์ที่ขับเคลื่อนด้วย AI ซึ่งใช้ประโยชน์จาก Large Language Models (LLMs)

#### How n8n uses AI

เพื่อช่วยเหลือและปรับปรุงประสบการณ์ผู้ใช้ n8n อาจส่งข้อมูล context เฉพาะไปยัง LLMs ข้อมูล context นี้จำกัดเฉพาะข้อมูลเกี่ยวกับ workflow ปัจจุบันเท่านั้น n8n ไม่ส่งค่าใดๆ จากฟิลด์ credential หรือ output data จริงไปยังบริการ AI ข้อมูลจะไม่ถูกรวม ใช้ หรือเก็บรักษาเพื่อฝึกโมเดลของบริการ AI ข้อมูลใดๆ จะถูกลบหลังจาก 30 วัน

#### When n8n shares data

ข้อมูลจะถูกส่งไปยังบริการ AI เฉพาะเมื่อ workspaces ได้เลือกใช้ assistant เท่านั้น Assistant เปิดใช้งานโดยค่าเริ่มต้นสำหรับผู้ใช้ n8n Cloud เมื่อ workspace เลือกใช้ assistant ข้อมูลเฉพาะของ node จะถูกส่งเฉพาะในระหว่างการโต้ตอบโดยตรงและเซสชันที่ใช้งานอยู่กับ AI assistant เท่านั้น เพื่อให้แน่ใจว่าจะไม่มีการแชร์ข้อมูลที่ไม่จำเป็นเกิดขึ้น

#### What n8n shares

- **General Workflow Information**: ซึ่งรวมถึงรายละเอียดเกี่ยวกับ nodes ที่มีอยู่ใน workflow ของคุณ, จำนวน items ปัจจุบันใน workflow และว่า workflow นั้น active หรือไม่
- **Input & Output Schemas of Nodes**: ซึ่งรวมถึง schema ของ nodes ทั้งหมดที่มีข้อมูลขาเข้าและ output schema ของ node ที่เกี่ยวข้อง เราไม่ส่งค่าข้อมูลจริงของ schema
- **Node Configuration**: ซึ่งรวมถึง operations, options และ settings ที่เลือกใน node ที่อ้างอิง
- **Code and Expressions**: ซึ่งรวมถึง code หรือ expressions ใดๆ ใน node ที่เกี่ยวข้องเพื่อช่วยในการดีบักปัญหาที่อาจเกิดขึ้นและการปรับให้เหมาะสม

#### What n8n doesn't share

- **Credentials**: ค่าใดๆ ของฟิลด์ credential ของ nodes ของคุณ
- **Output Data**: ข้อมูลจริงที่ประมวลผลโดย workflows ของคุณ
- **Sensitive Information**: ข้อมูลที่สามารถระบุตัวตนได้หรือข้อมูลที่ละเอียดอ่อนอื่นๆ ที่อาจกระทบต่อความเป็นส่วนตัวหรือความปลอดภัยของคุณที่คุณไม่ได้ระบุไว้อย่างชัดเจนใน node parameters หรือ code ของคุณใน [Code Node](/integrations/builtin/core-nodes/n8n-nodes-base.code/index.md)

### Documentation telemetry

เอกสารของ n8n (เว็บไซต์นี้) ใช้ cookies เพื่อจดจำการเข้าชมซ้ำและความชอบของคุณ รวมถึงเพื่อวัดประสิทธิภาพของเอกสารของ n8n และว่าผู้ใช้พบสิ่งที่พวกเขากำลังค้นหาหรือไม่ ด้วยความยินยอมของคุณ คุณกำลังช่วยให้ n8n ทำให้เอกสารของเราดีขึ้น

[Change cookie settings](#__consent){ .md-button }

## Retention and deletion of personal identifiable data

PID (personal identifiable data) คือข้อมูลที่เป็นส่วนตัวของคุณและจะระบุตัวตนของคุณในฐานะบุคคล

### n8n Cloud

#### PID retention

n8n เก็บข้อมูลไว้ตราบเท่าที่จำเป็นเพื่อให้บริการหลักเท่านั้น

สำหรับ n8n Cloud, n8n จัดเก็บ workflow code, credentials และข้อมูลอื่นๆ ของคุณไว้อย่างไม่มีกำหนด จนกว่าคุณจะเลือกที่จะลบหรือปิดบัญชีของคุณ แพลตฟอร์มจัดเก็บ execution data ตามกฎการเก็บรักษา (retention rules) ในบัญชีของคุณ

n8n ลบ internal application logs ส่วนใหญ่และ logs ที่ผูกกับ subprocessors ภายใน 90 วัน บริษัทเก็บรักษาชุดย่อยของ logs ไว้นานขึ้นในกรณีที่จำเป็นสำหรับการสืบสวนด้านความปลอดภัย

#### PID deletion

หากคุณเลือกที่จะลบบัญชี n8n ของคุณ, n8n จะลบข้อมูลลูกค้าและข้อมูล event ทั้งหมดที่เกี่ยวข้องกับบัญชีของคุณ n8n ลบข้อมูลลูกค้าใน backups ภายใน 90 วัน

### Self-hosted

ผู้ใช้ Self-hosted ควรมีนโยบาย PID และกระบวนการลบข้อมูลของตนเอง โปรดดู [What you can do](/privacy-security/what-you-can-do.md) สำหรับข้อมูลเพิ่มเติม

## Payment processor

n8n ใช้ Paddle.com ในการประมวลผลการชำระเงิน เมื่อคุณสมัครแผนชำระเงิน Paddle จะส่งและจัดเก็บรายละเอียดวิธีการชำระเงินของคุณตามนโยบายความปลอดภัยของพวกเขา n8n ไม่เก็บข้อมูลใดๆ เกี่ยวกับวิธีการชำระเงินของคุณ

<!-- vale on -->
