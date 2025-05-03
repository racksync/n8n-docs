---
title: ข้อมูลยืนยันตัวตน Netscaler ADC
description: เอกสารสำหรับการยืนยันตัวตน Netscaler ADC. ใช้ข้อมูลเหล่านี้เพื่อยืนยันตัวตน Netscaler ADC ใน n8n.
contentType: [integration, reference]
---

# Netscaler ADC credentials

คุณสามารถใช้ credentials เหล่านี้เพื่อยืนยันตัวตนใน nodes ต่อไปนี้:

* [Netscaler ADC node](/integrations/builtin/app-nodes/n8n-nodes-base.netscaleradc.md)

## Prerequisites

ติดตั้ง [NetScaler/Citrix ADC appliance](https://docs.netscaler.com/en-us/citrix-adc/current-release/getting-started-with-citrix-adc){:target=_blank .external-link}

## Supported authentication methods

- Basic auth

## Related resources

อ้างอิง [Netscaler ADC's 14.1 NITRO API documentation](https://developer-docs.netscaler.com/en-us/adc-nitro-api/current-release){:target=_blank .external-link} สำหรับข้อมูลเพิ่มเติมเกี่ยวกับบริการนี้

## Using basic auth

ในการกำหนดค่า credential นี้ คุณจะต้องมี:

* **URL**: ป้อน URL ของ instance NetScaler/Citrix ADC ของคุณ
* **Username**: ป้อนชื่อผู้ใช้ NetScaler/Citrix ADC ของคุณ
* **Password**: ป้อนรหัสผ่าน NetScaler/Citrix ADC ของคุณ

อ้างอิง [Performing Basic Netscaler ADC Operations](https://developer-docs.netscaler.com/en-us/adc-nitro-api/current-release/performing-basic-netscaler-operations){:target=_blank .external-link} สำหรับข้อมูลเพิ่มเติม
