---
#https://www.notion.so/n8n/Frontmatter-432c2b8dff1f43d4b1c8d20075510fe4
contentType: howto
---

# White labelling

--8<-- "_snippets/embed-license.md"

White labelling n8n คือการปรับแต่ง frontend styling และ asset ต่างๆ ให้ตรงกับ brand ของคุณเอง วิธีนี้ต้องแก้ไข 2 package ใน source code ของ n8n [github.com/n8n-io/n8n](https://github.com/n8n-io/n8n){:target=_blank .external-link}:

* [packages/design-system](https://github.com/n8n-io/n8n/tree/master/packages/design-system){:target=_blank .external-link}: เป็น [storybook](https://storybook.js.org/){:target=_blank .external-link} design system ของ n8n ที่รวม CSS style และ Vue.js component
* [packages/editor-ui](https://github.com/n8n-io/n8n/tree/master/packages/editor-ui){:target=_blank .external-link}: เป็น frontend ของ n8n ที่ build ด้วย [Vue.js](https://vuejs.org/){:target=_blank .external-link} และ [Vite.js](https://vitejs.dev){:target=_blank .external-link}

## Prerequisites

เครื่องที่ใช้พัฒนาต้องติดตั้งสิ่งเหล่านี้:

--8<-- "_snippets/integrations/creating-nodes/prerequisites.md"

สร้าง fork ของ [repository n8n](https://github.com/n8n-io/n8n){:target=_blank .external-link} แล้ว clone repository ของคุณ

```shell
git clone https://github.com/<your-organization>/n8n.git n8n
cd n8n
```

ติดตั้ง dependency ทั้งหมด, build และ start n8n

```shell
npm install
npm run build
npm run start
```

ทุกครั้งที่แก้ไข code ต้อง build และ restart n8n ใหม่ ขณะพัฒนาใช้ `npm run dev` เพื่อ rebuild/restart อัตโนมัติทุกครั้งที่แก้ไข code

## Theme colors

ถ้าจะเปลี่ยนสี theme ให้เปิด [packages/design-system](https://github.com/n8n-io/n8n/tree/master/packages/design-system){:target=_blank .external-link} แล้วเริ่มที่ไฟล์:

- [packages/design-system/src/css/_tokens.scss](https://github.com/n8n-io/n8n/blob/master/packages/design-system/src/css/_tokens.scss){:target=_blank .external-link}
- [packages/design-system/src/css/_tokens.dark.scss](https://github.com/n8n-io/n8n/blob/master/packages/design-system/src/css/_tokens.dark.scss){:target=_blank .external-link}

ด้านบนของ `_tokens.scss` จะมีตัวแปร `--color-primary` เป็น HSL เช่นนี้:

```scss
@mixin theme {
	--color-primary-h: 6.9;
	--color-primary-s: 100%;
	--color-primary-l: 67.6%;
```

ตัวอย่างนี้เปลี่ยน primary color เป็น <span style="color:#0099ff">#0099ff</span> ถ้าจะ convert เป็น HSL ใช้ [color converter tool](https://www.w3schools.com/colors/colors_converter.asp){:target=_blank .external-link} ได้เลย

```scss
@mixin theme {
	--color-primary-h: 204;
	--color-primary-s: 100%;
	--color-primary-l: 50%;
```

![Example Theme Color Customization](/_images/embed/white-label/color-transition.gif)


## Theme logos

ถ้าจะเปลี่ยน logo asset ของ editor ให้ดูที่ [packages/editor-ui/public](https://github.com/n8n-io/n8n/tree/master/packages/editor-ui/public){:target=_blank .external-link} แล้วแทนที่ไฟล์เหล่านี้:

- favicon-16x16.png
- favicon-32x32.png
- favicon.ico
- n8n-logo.svg
- n8n-logo-collapsed.svg
- n8n-logo-expanded.svg

แทนที่ logo asset เหล่านี้ n8n จะใช้ใน Vue.js component หลายตัว เช่น:

* [MainSidebar.vue](https://github.com/n8n-io/n8n/blob/master/packages/editor-ui/src/components/MainSidebar.vue){:target=_blank .external-link}: โลโก้ด้านบน/ซ้ายใน sidebar หลัก
* [Logo.vue](https://github.com/n8n-io/n8n/blob/master/packages/editor-ui/src/components/Logo.vue): ใช้ซ้ำใน component อื่นๆ

ตัวอย่างนี้เปลี่ยน `n8n-logo-collapsed.svg` และ `n8n-logo-expanded.svg` เพื่ออัปเดตโลโก้ใน sidebar หลัก

![Example Logo Main Sidebar](/_images/embed/white-label/logo-main-sidebar.png)

ถ้า logo ของคุณต้องการขนาดหรือการจัดวางต่างจากเดิม สามารถแก้ SCSS style ด้านล่างของ [MainSidebar.vue](https://github.com/n8n-io/n8n/blob/master/packages/editor-ui/src/components/MainSidebar.vue){:target=_blank .external-link} ได้

```scss
.logoItem {
	display: flex;
	justify-content: space-between;
	height: $header-height;
	line-height: $header-height;
	margin: 0 !important;
	border-radius: 0 !important;
	border-bottom: var(--border-width-base) var(--border-style-base) var(--color-background-xlight);
	cursor: default;

	&:hover, &:global(.is-active):hover {
		background-color: initial !important;
	}

	* { vertical-align: middle; }
	.icon {
		height: 18px;
		position: relative;
		left: 6px;
	}

}
```

## Text localization

ถ้าจะเปลี่ยนข้อความเช่น `n8n` หรือ `n8n.io` ให้เป็น brand ของคุณเอง ให้แก้ไฟล์ internationalization ภาษาอังกฤษของ n8n: [packages/editor-ui/src/plugins/i18n/locales/en.json](https://github.com/n8n-io/n8n/blob/master/packages/editor-ui/src/plugins/i18n/locales/en.json){:target=_blank .external-link}

n8n ใช้ [Vue I18n](https://kazupon.github.io/vue-i18n/){:target=_blank .external-link} สำหรับแปลข้อความ UI ส่วนใหญ่ ถ้าจะค้นหาและแทนที่ข้อความใน `en.json` ใช้ [Linked locale messages](https://kazupon.github.io/vue-i18n/guide/messages.html#linked-locale-messages){:target=_blank .external-link} ได้

ตัวอย่างนี้เพิ่ม key `_brand.name` เพื่อ white label n8n ใน [AboutModal.vue](https://github.com/n8n-io/n8n/blob/master/packages/editor-ui/src/components/AboutModal.vue){:target=_blank .external-link}

```js
{
	"_brand.name": "My Brand",
	//replace n8n with link to _brand.name
	"about.aboutN8n": "About @:_brand.name",
	"about.n8nVersion": "@:_brand.name Version",
}
```

![Example About Modal Localization](/_images/embed/white-label/about-modal.png)

### Window title

ถ้าจะเปลี่ยน window title ของ n8n ให้เป็นชื่อ brand ของคุณ ให้แก้ไฟล์เหล่านี้:

- [packages/editor-ui/index.html](https://github.com/n8n-io/n8n/blob/master/packages/editor-ui/index.html){:target=_blank .external-link}
- [packages/editor-ui/src/components/mixins/titleChange.ts](https://github.com/n8n-io/n8n/blob/master/packages/editor-ui/src/components/mixins/titleChange.ts){:target=_blank .external-link}

ตัวอย่างนี้แทนที่ `n8n` และ `n8n.io` ด้วย `My Brand` ใน `index.html` และ `titleChange.ts`

```html
<!DOCTYPE html>
<html lang="en">
<head>
	<!-- Replace html title attribute -->
	<title>My Brand - Workflow Automation</title>
</head>
```

```typescript
$titleSet(workflow: string, status: WorkflowTitleStatus) {
	// replace n8n prefix
	window.document.title = `My Brand - ${icon} ${workflow}`;
},

$titleReset() {
	// replace n8n prefix
	document.title = `My Brand - Workflow Automation`;
},
```

![Example Window Title Localization](/_images/embed/white-label/window-title.png)




