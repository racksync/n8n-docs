---
#https://www.notion.so/n8n/Frontmatter-432c2b8dff1f43d4b1c8d20075510fe4
title: OpenAI Audio operations 
description: Documentation for the Audio operations in OpenAI node in n8n, a workflow automation platform. Includes details of operations and configuration, and links to examples and credentials information.
contentType: [integration, reference]
priority: critical
---

# OpenAI Audio operations

ใช้ operation นี้เพื่อสร้างเสียง หรือถอดความ/แปลไฟล์เสียงใน OpenAI. ดูข้อมูลเพิ่มเติมที่ [OpenAI](/integrations/builtin/app-nodes/n8n-nodes-langchain.openai/index.md).

## Generate Audio

ใช้ operation นี้เพื่อสร้างเสียงจากข้อความ prompt.

Enter these parameters:
- **Credential to connect with**: สร้างหรือเลือก [OpenAI credential](/integrations/builtin/credentials/openai.md) ที่มีอยู่แล้ว.
- **Resource**: เลือก **Audio**.
- **Operation**: เลือก **Generate Audio**.
- **Model**: เลือก Model ที่ต้องการใช้สร้างเสียง. ดูรายละเอียดเพิ่มเติมที่ [TTS | OpenAI](https://platform.openai.com/docs/models/tts){:target=_blank .external-link}.
    - **TTS-1**: ใช้สำหรับความเร็ว.
    - **TTS-1-HD**: ใช้สำหรับคุณภาพที่สูงกว่า.
- **Text Input**: ระบุข้อความที่ต้องการแปลงเป็นเสียง. ความยาวสูงสุด 4096 ตัวอักษร.
- **Voice**: เลือกเสียงที่จะใช้สร้างเสียง. ฟังตัวอย่างได้ที่ [Text to speech guide | OpenAI](https://platform.openai.com/docs/guides/text-to-speech/quickstart){:target=_blank .external-link}.

### Options

- **Response Format**: เลือกรูปแบบของการตอบกลับเสียง เช่น **MP3** (ค่าเริ่มต้น), **OPUS**, **AAC**, **FLAC**, **WAV**, หรือ **PCM**.
- **Audio Speed**: ระบุความเร็วของเสียงที่สร้าง โดยมีค่าระหว่าง `0.25` ถึง `4.0` (ค่าเริ่มต้นคือ `1`).
- **Put Output in Field**: ค่าเริ่มต้นคือ `data`. ระบุชื่อฟิลด์สำหรับเก็บข้อมูล binary.

ดูรายละเอียดเพิ่มเติมที่ [Create speech | OpenAI](https://platform.openai.com/docs/api-reference/audio/createSpeech){:target=_blank .external-link}.

## Transcribe a Recording

ใช้ operation นี้เพื่อถอดความเสียงเป็นข้อความ. การอัปโหลดไฟล์เสียงมีจำกัดสูงสุด 25 MB. ค่าเริ่มต้น model คือ `whisper-1`.

Enter these parameters:
- **Credential to connect with**: สร้างหรือเลือก [OpenAI credential](/integrations/builtin/credentials/openai.md) ที่มีอยู่แล้ว.
- **Resource**: เลือก **Audio**.
- **Operation**: เลือก **Transcribe a Recording**.
- **Input Data Field Name**: ค่าเริ่มต้นคือ `data`. ระบุชื่อ property แบบ binary ที่มีไฟล์เสียง (รองรับฟอร์แมท: `.flac`, `.mp3`, `.mp4`, `.mpeg`, `.mpga`, `.m4a`, `.ogg`, `.wav`, หรือ `.webm`).

### Options

- **Language of the Audio File**: ระบุภาษาของไฟล์เสียงแบบ [ISO-639-1](https://en.wikipedia.org/wiki/List_of_ISO_639_language_codes){:target=_blank .external-link} เพื่อเพิ่มความแม่นยำ.
- **Output Randomness (Temperature)**: ค่าเริ่มต้นคือ `1.0`. ปรับความสุ่มของผลลัพธ์ในช่วง `0.0` ถึง `1.0`. แนะนำเริ่มที่ประมาณ `0.7`.

ดูรายละเอียดเพิ่มเติมที่ [Create transcription | OpenAI](https://platform.openai.com/docs/api-reference/audio/createTranscription){:target=_blank .external-link}.

## Translate a Recording

ใช้ operation นี้เพื่อแปลเสียงเป็นภาษาอังกฤษ. ขนาดไฟล์เสียงจำกัดสูงสุด 25 MB. ค่าเริ่มต้น model คือ `whisper-1`.

Enter these parameters:
- **Credential to connect with**: สร้างหรือเลือก [OpenAI credential](/integrations/builtin/credentials/openai.md) ที่มีอยู่แล้ว.
- **Resource**: เลือก **Audio**.
- **Operation**: เลือก **Translate a Recording**.
- **Input Data Field Name**: ค่าเริ่มต้นคือ `data`. ระบุชื่อ property แบบ binary ที่มีไฟล์เสียงในฟอร์แมท: `.flac`, `.mp3`, `.mp4`, `.mpeg`, `.mpga`, `.m4a`, `.ogg`, `.wav`, หรือ `.webm`.

### Options

- **Output Randomness (Temperature)**: ค่าเริ่มต้นคือ `1.0`. ปรับความสุ่มของผลลัพธ์ โดยมีช่วง `0.0` ถึง `1.0`. แนะนำเริ่มประมาณ `0.7`.

ดูรายละเอียดเพิ่มเติมที่ [Create transcription | OpenAI](https://platform.openai.com/docs/api-reference/audio/createTranscription){:target=_blank .external-link}.

## Common issues

For common errors or issues and suggested resolution steps, refer to [Common Issues](/integrations/builtin/app-nodes/n8n-nodes-langchain.openai/common-issues.md).
