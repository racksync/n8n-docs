---
#https://www.notion.so/n8n/Frontmatter-432c2b8dff1f43d4b1c8d20075510fe4
title: การเขียน Code ด้วย AI
description: ใช้ GPT สร้าง code ใน Code node
contentType: explanation
---

# AI coding with GPT

ไม่มีให้บริการบน self-hosted

ไม่รองรับ Python
///

## Use AI in the Code node

--8<-- "_snippets/code/ai-how-to.md"

## Usage limits

ในช่วงทดลองใช้งาน ไม่มีข้อจำกัดในการใช้งาน หาก n8n ทำให้ฟีเจอร์นี้เป็นแบบถาวร อาจมีข้อจำกัดการใช้งานเป็นส่วนหนึ่งของระดับราคาของคุณ

## Feature limits

การนำ ChatGPT มาใช้ใน n8n มีข้อจำกัดดังต่อไปนี้:

*   AI เขียนโค้ดที่จัดการข้อมูลจาก n8n workflow คุณไม่สามารถขอให้มันดึงข้อมูลจากแหล่งอื่นได้
*   AI ไม่รู้จักข้อมูลของคุณ รู้เพียงแค่ schema ดังนั้นคุณต้องบอกสิ่งต่างๆ เช่น วิธีค้นหาข้อมูลที่คุณต้องการดึง หรือวิธีตรวจสอบค่า null
*   Nodes ก่อนหน้า Code node ต้องทำงานและส่งข้อมูลไปยัง Code node ก่อนที่คุณจะรัน AI query ของคุณ
*   ไม่ทำงานกับ data schemas ขาเข้าขนาดใหญ่
*   อาจมีปัญหาหากมี nodes จำนวนมากก่อนหน้า code node

## Writing good prompts

<!-- vale off -->

การเขียน prompts ที่ดีจะเพิ่มโอกาสในการได้โค้ดที่เป็นประโยชน์กลับมา

เคล็ดลับทั่วไปบางประการ:

*   ให้ตัวอย่าง: หากเป็นไปได้ ให้ตัวอย่างผลลัพธ์ที่คาดหวัง สิ่งนี้ช่วยให้ AI เข้าใจการแปลงหรือตรรกะที่คุณต้องการได้ดีขึ้น
*   อธิบายขั้นตอนการประมวลผล: หากมีขั้นตอนการประมวลผลหรือตรรกะเฉพาะที่ควรนำไปใช้กับข้อมูล ให้ระบุตามลำดับ ตัวอย่างเช่น: "ขั้นแรก กรองผู้ใช้ทุกคนที่อายุต่ำกว่า 18 ปี จากนั้น จัดเรียงผู้ใช้ที่เหลือตามนามสกุล"
*   หลีกเลี่ยงความคลุมเครือ: แม้ว่า AI จะเข้าใจคำสั่งต่างๆ แต่การมีความชัดเจนและตรงไปตรงมาจะช่วยให้คุณได้โค้ดที่แม่นยำที่สุด แทนที่จะพูดว่า "Get the older users" คุณอาจพูดว่า "Filter users who are 60 years and above"
*   ระบุให้ชัดเจนว่าคุณคาดหวังอะไรเป็นผลลัพธ์ คุณต้องการให้ข้อมูลถูกแปลง, กรอง, รวม หรือจัดเรียง? ให้รายละเอียดมากที่สุดเท่าที่จะทำได้

และคำแนะนำเฉพาะสำหรับ n8n:

*   คิดถึงข้อมูลขาเข้า: ตรวจสอบให้แน่ใจว่า ChatGPT รู้ว่าคุณต้องการเข้าถึงข้อมูลส่วนใด และข้อมูลขาเข้าหมายถึงอะไร คุณอาจต้องบอก ChatGPT เกี่ยวกับความพร้อมใช้งานของ built-in methods and variables ของ n8n
*   ประกาศการโต้ตอบระหว่าง nodes: หากตรรกะของคุณเกี่ยวข้องกับข้อมูลจากหลาย nodes ให้ระบุว่าควรโต้ตอบกันอย่างไร "Merge the output of 'Node A' with 'Node B' based on the 'userID' property" หากคุณต้องการให้ข้อมูลมาจาก nodes บางตัว หรือไม่สนใจ nodes อื่นๆ ให้ระบุให้ชัดเจน: "Only consider data from the 'Purchases' node and ignore the 'Refunds' node."
*   ตรวจสอบให้แน่ใจว่าผลลัพธ์เข้ากันได้กับ n8n โปรดดู [Data structure](/data/data-structure.md) สำหรับข้อมูลเพิ่มเติมเกี่ยวกับโครงสร้างข้อมูลที่ n8n ต้องการ

### Example prompts

ตัวอย่างเหล่านี้แสดงช่วงของ prompts และ tasks ที่เป็นไปได้

#### Example 1: Find a piece of data inside a second dataset

หากต้องการลองตัวอย่างด้วยตัวเอง [download the example workflow](/_workflows/ai-code/find-a-piece-of-data.json) และ import เข้าไปใน n8n

ใน Code node ที่สาม ป้อน prompt นี้:

> The slack data contains only one item. The input data represents all Notion users. Sometimes the person property that holds the email can be null. I want to find the notionId of the Slack user and return it.

ลองดูโค้ดที่ AI สร้างขึ้น

นี่คือ JavaScript ที่คุณต้องการ:

```js
const slackUser = $("Mock Slack").all()[0];
const notionUsers = $input.all();
const slackUserEmail = slackUser.json.email;

const notionUser = notionUsers.find(
  (user) => user.json.person && user.json.person.email === slackUserEmail
);

return notionUser ? [{ json: { notionId: notionUser.json.id } }] : [];
```

#### Example 2: Data transformation

หากต้องการลองตัวอย่างด้วยตัวเอง [download the example workflow](/_workflows/ai-code/data-transformation.json) และ import เข้าไปใน n8n

ใน Code node **Join items** ป้อน prompt นี้:

> Return a single line of text that has all usernames listed with a comma. Each username should be enquoted with a double quotation mark.

ลองดูโค้ดที่ AI สร้างขึ้น

นี่คือ JavaScript ที่คุณต้องการ:

```js
const items = $input.all();
const usernames = items.map((item) => `"${item.json.username}"`);
const result = usernames.join(", ");
return [{ json: { usernames: result } }];
```

#### Example 3: Summarize data and create a Slack message

หากต้องการลองตัวอย่างด้วยตัวเอง [download the example workflow](/_workflows/ai-code/summarize-data.json) และ import เข้าไปใน n8n

ใน Code node **Summarize** ป้อน prompt นี้:

> Create a markdown text for Slack that counts how many ideas, features and bugs have been submitted. The type of submission is saved in the property_type field. A feature has the property "Feature", a bug has the property "Bug" and an idea has the property "Bug". Also, list the five top submissions by vote in that message. Use "<url|text>" as markdown for links.

ลองดูโค้ดที่ AI สร้างขึ้น

นี่คือ JavaScript ที่คุณต้องการ:

```js
const submissions = $input.all();

// Count the number of ideas, features, and bugs
let ideaCount = 0;
let featureCount = 0;
let bugCount = 0;

submissions.forEach((submission) => {
  switch (submission.json.property_type[0]) {
    case "Idea":
      ideaCount++;
      break;
    case "Feature":
      featureCount++;
      break;
    case "Bug":
      bugCount++;
      break;
  }
});

// Sort submissions by votes and take the top 5
const topSubmissions = submissions
  .sort((a, b) => b.json.property_votes - a.json.property_votes)
  .slice(0, 5);

let topSubmissionText = "";
topSubmissions.forEach((submission) => {
  topSubmissionText += `<${submission.json.url}|${submission.json.name}> with ${submission.json.property_votes} votes\n`;
});

// Construct the Slack message
const slackMessage = `*Summary of Submissions*\n
Ideas: ${ideaCount}\n
Features: ${featureCount}\n
Bugs: ${bugCount}\n
Top 5 Submissions:\n
${topSubmissionText}`;

return [{ json: { slackMessage } }];
```

<!-- vale on -->

### Reference incoming node data explicitly

หากข้อมูลขาเข้าของคุณมีฟิลด์ซ้อนกัน การใช้ dot notation เพื่ออ้างอิงถึงฟิลด์เหล่านั้นสามารถช่วยให้ AI เข้าใจว่าคุณต้องการข้อมูลใด

!["Screenshot of an n8n code node, highlighting how to reference data with dot notation in an AI query"](/_images/code/ai-code/reference-data-dot-notation.png)

หากต้องการลองตัวอย่างด้วยตัวเอง [download the example workflow](/_workflows/ai-code/reference-incoming-data-explicitly.json) และ import เข้าไปใน n8n

ใน Code node ที่สอง ป้อน prompt นี้:

> The data in "Mock data" represents a list of people. For each person, return a new item containing personal_info.first_name and work_info.job_title.

นี่คือ JavaScript ที่คุณต้องการ:

```js
const items = $input.all();
const newItems = items.map((item) => {
  const firstName = item.json.personal_info.first_name;
  const jobTitle = item.json.work_info.job_title;
  return {
    json: {
      firstName,
      jobTitle,
    },
  };
});
return newItems;
```

### Related resources

Pluralsight มีคู่มือสั้นๆ เกี่ยวกับ [How to use ChatGPT to write code](https://www.pluralsight.com/blog/software-development/how-use-chatgpt-programming-coding){:target=_blank .external-link} ซึ่งรวมถึงตัวอย่าง prompts

## Fixing the code

โค้ดที่สร้างโดย AI อาจทำงานได้โดยไม่ต้องแก้ไขใดๆ แต่คุณอาจต้องแก้ไข คุณจำเป็นต้องตระหนักถึง [Data structure](/data/data-structure.md) ของ n8n คุณอาจพบว่า built-in methods and variables ของ n8n มีประโยชน์
