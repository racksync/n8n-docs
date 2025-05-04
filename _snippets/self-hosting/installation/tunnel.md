## n8n กับ Tunnel

/// danger
Use this for local development and testing. It isn't safe to use it in production.
///

ในการใช้ Webhook สำหรับ Trigger node ของบริการภายนอก เช่น GitHub นั้น n8n จะต้องสามารถเข้าถึงได้จากเว็บ n8n มีบริการ [tunnel service](https://github.com/localtunnel/localtunnel) ที่สามารถเปลี่ยนเส้นทางคำขอ (Redirect requests) จาก Server ของ n8n ไปยัง Instance n8n ในเครื่องของคุณได้
