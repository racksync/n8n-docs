---
#https://www.notion.so/n8n/Frontmatter-432c2b8dff1f43d4b1c8d20075510fe4
title: สร้าง AI chat agent ด้วย n8n
description: เรียนรู้วิธีสร้าง AI workflows ด้วย n8n
type: tutorial
---

# Build an AI chat agent with n8n

ยินดีต้อนรับสู่บทแนะนำเบื้องต้นสำหรับการสร้าง AI workflows ด้วย n8n ไม่ว่าคุณจะเคยใช้ n8n มาก่อนหรือเพิ่งเริ่มต้น ที่นี่เราจะแสดงให้เห็นว่าส่วนประกอบต่างๆ ของ AI workflows ทำงานร่วมกันอย่างไร และจะสร้าง AI-powered chat agent ที่ใช้งานได้จริง ซึ่งคุณสามารถปรับแต่งได้ตามต้องการ

!["Screenshot of the completed workflow"](/_images/advanced-ai/ai-intro01.png)

หลายคนรู้สึกว่าการเรียนรู้สิ่งใหม่ๆ ผ่านวิดีโอนั้นง่ายกว่า บทแนะนำนี้อ้างอิงจากวิดีโอยอดนิยมของ n8n ที่ลิงก์ไว้ด้านล่าง จะดูวิดีโอหรืออ่านขั้นตอนที่นี่ หรือทั้งสองอย่างก็ได้!

<iframe width="560" height="315" src="https://www.youtube.com/embed/yzvLfHb0nqE?si=7ruaUEycFcoQbYsD" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

### What you will need

- **n8n**: สำหรับบทแนะนำนี้ แนะนำให้ใช้บริการ [n8n cloud](/manage-cloud/overview.md) - มีช่วงทดลองใช้ฟรีสำหรับผู้ใช้ใหม่! ถ้าต้องการ self-hosted ดูที่ [installation pages](/hosting/installation/docker.md)
- **Credentials for a chat model**: บทแนะนำนี้ใช้ OpenAI แต่คุณสามารถใช้ DeepSeek, Google Gemini, Groq, Azure และอื่นๆ ได้ง่ายๆ (ดู [sub-nodes documentation](/integrations/builtin/cluster-nodes/sub-nodes/index.md) สำหรับรายละเอียด)

### What you will learn

- AI concepts ใน n8n
- วิธีใช้ AI Agent node
- การทำงานกับ Chat input
- การเชื่อมต่อกับ AI models
- การปรับแต่ง input
- การสังเกตการณ์ conversation
- การเพิ่ม persistence

## AI concepts in n8n

ถ้าคุณคุ้นเคยกับ AI อยู่แล้ว ข้ามส่วนนี้ได้เลย นี่คือแนะนำพื้นฐานเกี่ยวกับ AI concepts และวิธีนำไปใช้ใน n8n workflows

[AI agent](/glossary.md#ai-agent) สร้างขึ้นบน [Large Language Models (LLMs)](/glossary.md#large-language-model-llm) ซึ่งสร้างข้อความตาม input โดยเดาคำถัดไป LLMs จะประมวลผล input เพื่อสร้าง output เท่านั้น แต่ AI agents จะเพิ่มฟังก์ชันที่เน้นเป้าหมาย สามารถใช้ [tools](/glossary.md#ai-tool), ประมวลผล output ของตัวเอง และตัดสินใจเพื่อทำงานให้เสร็จหรือแก้ปัญหา

ใน n8n, AI agent จะแสดงเป็น node ที่มีการเชื่อมต่อพิเศษบางอย่าง

| Feature             | LLM                        | AI Agent                           |
|---------------------|----------------------------|------------------------------------|
| Core Capability     | Text generation            | Goal-oriented task completion      |
| Decision-Making     | None                       | Yes                                |
| Uses Tools/APIs     | No                         | Yes                                |
| Workflow Complexity | Single-step                | Multi-step                         |
| Scope               | Generates language         | Performs complex, real-world tasks |
| Example             | LLM generating a paragraph | An agent scheduling an appointment |

การนำ AI agent มาเป็น node ทำให้ n8n รวมขั้นตอนที่ขับเคลื่อนด้วย AI กับ programming แบบปกติได้อย่างมีประสิทธิภาพ ตัวอย่างเช่น งานง่ายๆ อย่างการตรวจสอบ email address ไม่จำเป็นต้องใช้ AI แต่ถ้าเป็นงานซับซ้อน เช่น ประมวลผล _content_ ของอีเมล หรือจัดการ multimodal inputs (เช่น รูปภาพ, เสียง) นี่คือจุดเด่นของ AI agent

## 1. Create a new workflow

--8<-- "_snippets/try-it-out/new-workflow.md"

## 2. Add a trigger node

ทุก workflow ต้องมีจุดเริ่มต้น ใน n8n สิ่งนี้เรียกว่า ['trigger nodes'](/glossary.md#trigger-node-n8n) สำหรับ workflow นี้ เราจะเริ่มด้วย chat node

 1. เลือก **Add first step** หรือกด ++tab++ เพื่อเปิด node menu

 1. ค้นหา **Chat Trigger** n8n จะแสดงรายการ nodes ที่ตรงกับการค้นหา

 1. เลือก **Chat Trigger** เพื่อเพิ่ม node ลงบน canvas n8n จะเปิด node ให้

 1. ปิดหน้าต่างรายละเอียด node (เลือก **Back to canvas**) เพื่อกลับไปที่ canvas

??? explanation "More about the Chat Trigger node..."
    trigger node จะสร้าง output เมื่อมี event ที่ทำให้มัน trigger ในกรณีนี้ เราต้องการให้สามารถพิมพ์ข้อความเพื่อให้ workflow ทำงานได้ ใน production, trigger นี้สามารถเชื่อมต่อกับ public chat interface ที่ n8n มีให้ หรือฝังในเว็บอื่นก็ได้ สำหรับ workflow ง่ายๆ นี้ เราจะใช้ local chat interface ที่มีมาให้ จึงไม่ต้องตั้งค่าอะไรเพิ่ม

[[ workflowDemo("file:////advanced-ai/tutorials/chat_01.json") ]]

## 3. Add an AI Agent Node

AI Agent node คือหัวใจของการเพิ่ม AI ให้ workflow ของคุณ

 1. เลือก **Add node** <span class="inline-image">![Add node icon](/_images/try-it-out/add-node-small.png){.off-glb}</span> ที่ connector ของ trigger node เพื่อเปิด node search

 1. เริ่มพิมพ์ "AI" แล้วเลือก **AI agent** node เพื่อเพิ่ม

 1. จะเห็นหน้าต่างแก้ไขของ **AI agent** แสดงขึ้นมา
 
 1. มีบาง field ที่เปลี่ยนได้ แต่เพราะเราใช้ **Chat Trigger** node ค่าเริ่มต้นของ source และ prompt specification ไม่ต้องเปลี่ยน

[[ workflowDemo("file:////advanced-ai/tutorials/chat_02.json") ]]

## 4. Configure the node
  
AI agents ต้องการ chat model เพื่อประมวลผล prompt ที่เข้ามา

1. เพิ่ม chat model โดยคลิกปุ่มบวก <span class="inline-image">![Add node icon](/_images/try-it-out/add-node-small.png){.off-glb}</span> ใต้ **Chat Model** connection บน **AI Agent** node (เป็น connection แรกด้านล่าง node)

1. จะมี search dialog ปรากฏขึ้น กรองเฉพาะ 'Language Models' ซึ่งเป็น models ที่ n8n รองรับ ในบทนี้เราจะใช้ **OpenAI Chat Model**

1. เลือก **OpenAI Chat model** จากลิสต์ จะเชื่อมต่อกับ **AI Agent** node และเปิด node editor หนึ่งใน parameter ที่เปลี่ยนได้คือ 'Model' สำหรับบัญชี OpenAI แบบฟรี จะใช้ได้แค่ 'gpt-4o-mini'

??? explanation "Which chat model?"
    อย่างที่กล่าวไป LLM คือส่วนที่สร้างข้อความตาม prompt ที่ได้รับ LLMs ต้องถูกสร้างและ train ซึ่งปกติใช้ทรัพยากรสูง LLMs ต่างกันอาจมีความสามารถหรือความถนัดต่างกัน ขึ้นกับข้อมูลที่ใช้ train

## 5. Add credentials (if needed)

เพื่อให้ n8n ติดต่อกับ chat model ได้ ต้องมี [credentials](/credentials/index.md) (ข้อมูล login เพื่อเข้าถึงบัญชีบริการออนไลน์อื่น) ถ้าคุณตั้งค่า credentials สำหรับ OpenAI ไว้แล้ว จะเห็นใน credentials selector เลย ถ้ายังไม่มี ใช้ selector เพื่อเพิ่ม credential ใหม่ได้

![image showing the credentials dialog for OpenAI](/_images/advanced-ai/ai-tutorial-credentials.png)

1. ถ้าต้องการเพิ่ม credential ใหม่ คลิกข้อความ 'Select credential' จะมีตัวเลือกเพิ่ม credential ใหม่
   ![Screenshot showing create a new credential button](/_images/advanced-ai/ai-tutorial-create-credential.png)

1. credential นี้ต้องการแค่ API key ตอนเพิ่ม credential ใดๆ ให้ดูข้อความด้านขวา ในกรณีนี้จะมีลิงก์ไปยังบัญชี OpenAI เพื่อดึง API key

1. API key คือสตริงยาวๆ อันเดียว แค่นี้ก็พอสำหรับ credential นี้ คัดลอกจากเว็บ OpenAI แล้ววางในช่อง **API key**

??? explanation "Keeping your credentials safe"
    Credentials คือข้อมูลส่วนตัวที่ออกโดยแอปหรือบริการเพื่อยืนยันตัวตนคุณ และอนุญาตให้เชื่อมต่อหรือแชร์ข้อมูลระหว่างแอป/บริการกับ n8n node ประเภทข้อมูลที่ต้องใช้จะแตกต่างกันไปตามแอป/บริการ ควรระวังเรื่องการแชร์หรือเปิดเผย credentials นอก n8n

## 6. Test the node

ตอนนี้ node เชื่อมกับ **Chat Trigger** และ chat model แล้ว เราสามารถทดสอบ workflow ส่วนนี้ได้

1. คลิกปุ่ม 'Chat' ใกล้ด้านล่าง canvas จะเปิดหน้าต่าง chat ทางซ้ายและ AI agent logs ทางขวา

1. พิมพ์ข้อความแล้วกด ++enter++ จะเห็น response จาก chat model ใต้ข้อความของคุณ

1. หน้าต่าง log จะแสดง input และ output ของ AI Agent
   ![image showing a chat session in progress](/_images/advanced-ai/ai-intro-chat.png)

??? explanation "Accessing the logs..."
    คุณสามารถดู logs ของ AI node ได้แม้ไม่ได้ใช้ chat interface แค่เปิด **AI Agent** node แล้วคลิกแท็บ **Logs** ในแผงขวา
	![screenshot showing the Logs tab in the AIAgent](/_images/advanced-ai/ai-intro-logs.png)

## 7. Changing the prompt

logs ในขั้นตอนก่อนเผยให้เห็น system prompt ซึ่งเป็นข้อความเริ่มต้นที่ **AI Agent** ใช้เตรียม chat model จาก log จะเห็นว่าเป็น "You are a helpful assistant" แต่เราสามารถเปลี่ยน prompt นี้เพื่อปรับพฤติกรรม chat model ได้

1. เปิด **AI Agent** node ที่ด้านล่างจะมีส่วน 'Options' และ selector 'Add Option' ใช้เลือก 'System message'

1. จะเห็น system message แสดงขึ้นมา นี่คือ priming prompt เดิมที่เห็นใน logs เปลี่ยน prompt เป็นอย่างอื่นเพื่อเตรียม chat model ในแบบที่ต่างออกไป เช่น "You are a brilliant poet who always replies in rhyming couplets"

1. ปิด node แล้วกลับไปที่ chat window ลองพิมพ์ข้อความอีกครั้งจะเห็นว่า output เปลี่ยนไป
   ![image showing changed text for chat, now it rhymes; if you can believe that](/_images/advanced-ai/ai-intro-poet.png)

## 8. Adding persistence

chat model ตอนนี้ตอบกลับได้ดี แต่ยังมีบางอย่างขาดไปซึ่งจะเห็นได้เมื่อคุณลองคุยกับมัน

1. ใช้ chat แล้วบอกชื่อคุณกับ chat model เช่น "Hi there, my name is Nick"

1. รอให้ตอบ แล้วพิมพ์ "What's my name?" AI จะไม่สามารถบอกชื่อคุณได้ ไม่ว่ามันจะขอโทษแค่ไหน เหตุผลคือเราไม่ได้บันทึก context AI Agent ไม่มี [memory](/glossary.md#ai-memory)
   ![image showing a conversation illustrating the above](/_images/advanced-ai/ai-intro-memory.png)

1. เพื่อให้ AI Agent จำสิ่งที่เกิดขึ้นในการสนทนาได้ ต้องเพิ่ม memory ให้ node นี้ บน canvas คลิก <span class="inline-image">![Add node icon](/_images/try-it-out/add-node-small.png){.off-glb}</span> ที่ด้านล่างของ **AI Agent** node ที่เขียนว่า "Memory"

1. จากแผงที่ขึ้นมา เลือก "Simple Memory" จะใช้ memory จาก instance ที่รัน n8n ซึ่งปกติพอสำหรับงานง่ายๆ ค่าเริ่มต้น 5 interactions ก็เพียงพอ แต่จำไว้ว่าตัวเลือกนี้อยู่ตรงไหนเผื่ออยากเปลี่ยนทีหลัง

1. ลองคุยแบบเดิมอีกครั้ง จะเห็นว่า AI Agent จำชื่อคุณได้แล้ว

## 9. Saving the workflow

ก่อนออกจาก workflow editor อย่าลืมกด save ไม่งั้นการเปลี่ยนแปลงทั้งหมดจะหาย

1. คลิกปุ่ม "Save" มุมขวาบนของ editor workflow จะถูกบันทึกไว้ กลับมาใช้งานหรือเพิ่มฟีเจอร์ใหม่ได้ภายหลัง

## Congratulations!

คุณได้เริ่มต้นสร้าง workflow ที่มีประโยชน์และมีประสิทธิภาพด้วย AI แล้ว ในบทนี้เราได้ดูส่วนประกอบพื้นฐานของ AI workflow, เพิ่ม **AI Agent** และ chat model, ปรับ prompt ให้ได้ output ที่ต้องการ และเพิ่ม memory เพื่อให้ chat จำ context ระหว่างข้อความได้

[[ workflowDemo("file:////advanced-ai/tutorials/chat_complete.json") ]]

## Next steps

ตอนนี้คุณเห็นวิธีสร้าง AI workflow พื้นฐานแล้ว ยังมีแหล่งข้อมูลอีกมากมายให้ต่อยอด และตัวอย่าง workflow ที่จะช่วยให้คุณมีไอเดียต่อไป:

* เรียนรู้เพิ่มเติมเกี่ยวกับ AI concepts และดูตัวอย่างใน [Examples and concepts](/advanced-ai/examples/introduction.md)
* เรียกดู AI [Workflow templates](https://n8n.io/workflows/?categories=25){:target=_blank .external-link}
* ดูวิธี [enhance the AI agent with tools](/advanced-ai/examples/understand-tools.md)
