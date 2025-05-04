1. เข้าถึง [Google Cloud Console - Library](https://console.cloud.google.com/apis/library){:target=_blank .external-link} ของคุณ ตรวจสอบให้แน่ใจว่าคุณอยู่ใน project ที่ถูกต้อง
	<figure markdown="span">
	![The project dropdown in the Google Cloud top navigation](/_images/integrations/builtin/credentials/google/google-cloud-project-dropdown.png)
	<figcaption>ตรวจสอบ project dropdown ในแถบนำทางด้านบนของ Google Cloud</figcaption>
	</figure>
1. ไปที่ **APIs & Services > Library**
1. ค้นหาและเลือก API ที่คุณต้องการเปิดใช้งาน ตัวอย่างเช่น สำหรับ Gmail node ให้ค้นหาและเปิดใช้งาน Gmail API
1. บาง integrations จำเป็นต้องใช้ API อื่นๆ หรือต้องการให้คุณขอสิทธิ์เข้าถึง:
	* Google Perspective: [Request API Access](https://developers.perspectiveapi.com/s/docs-get-started){:target=_blank .external-link}
	* Google Ads: รับ [Developer Token](https://developers.google.com/google-ads/api/docs/first-call/dev-token){:target=_blank .external-link}

    /// note | ต้องการ Google Drive API
	Integrations ต่อไปนี้ต้องการ Google Drive API รวมถึง API ของตัวเองด้วย:

	* Google Docs
	* Google Sheets
	* Google Slides
	///

    /// note | Google Vertex AI API
	นอกเหนือจาก Vertex AI API แล้ว คุณจะต้องเปิดใช้งาน [Cloud Resource Manager API](https://console.cloud.google.com/apis/api/cloudresourcemanager.googleapis.com/){:target=_blank .external-link} ด้วย

	///

1. เลือก **ENABLE**
