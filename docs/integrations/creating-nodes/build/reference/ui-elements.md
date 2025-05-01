---
#https://www.notion.so/n8n/Frontmatter-432c2b8dff1f43d4b1c8d20075510fe4
contentType: reference
---

# Node user interface elements

n8n มีชุด UI component ที่เตรียมไว้ให้ (อิงจากไฟล์ JSON) เพื่อให้ผู้ใช้สามารถกรอกข้อมูลได้หลายประเภท UI element เหล่านี้สามารถใช้ใน n8n ได้เลย

## String

การตั้งค่าพื้นฐาน:

```typescript
{
	displayName: Name, // The value the user sees in the UI
	name: name, // The name used to reference the element UI within the code
	type: string,
	required: true, // Whether the field is required or not
	default: 'n8n',
	description: 'The name of the user',
	displayOptions: { // the resources and operations to display this element with
		show: {
			resource: [
				// comma-separated list of resource names
			],
			operation: [
				// comma-separated list of operation names
			]
		}
	},
}
```

![String](/_images/integrations/creating-nodes/string.png)

String field สำหรับกรอก password:

```typescript
{
	displayName: 'Password',
	name: 'password',
	type: 'string',
	required: true,
	typeOptions: {
		password: true,
	},
	default: '',
	description: `User's password`,
	displayOptions: { // the resources and operations to display this element with
		show: {
			resource: [
				// comma-separated list of resource names
			],
			operation: [
				// comma-separated list of operation names
			]
		}
	},
}
```

![Password](/_images/integrations/creating-nodes/password.png)

String field ที่มีหลายบรรทัด:

```typescript
{
	displayName: 'Description',
	name: 'description',
	type: 'string',
	required: true,
	typeOptions: {
		rows: 4,
	},
	default: '',
	description: 'Description',
	displayOptions: { // the resources and operations to display this element with
		show: {
			resource: [
				// comma-separated list of resource names
			],
			operation: [
				// comma-separated list of operation names
			]
		}
	},
}
```

![Multiple rows](/_images/integrations/creating-nodes/multiple-rows.png)

### Support drag and drop for data keys

ผู้ใช้สามารถลากและวางค่าข้อมูล (data value) เพื่อ map ไปยัง field ต่างๆ ได้ การ drag & drop จะสร้าง [expression](/glossary.md#expression-n8n) เพื่อโหลดค่าข้อมูลนั้น n8n รองรับฟีเจอร์นี้อัตโนมัติ

คุณต้องเพิ่ม option พิเศษเพื่อรองรับการ drag & drop data key:

* `requiresDataPath: 'single'`: สำหรับ field ที่ต้องการ string เดียว
* `requiresDataPath: 'multiple'`: สำหรับ field ที่รับค่าหลาย string (comma-separated)

ดูตัวอย่างได้ที่ [Compare Datasets node code](https://github.com/n8n-io/n8n/blob/master/packages/nodes-base/nodes/CompareDatasets/CompareDatasets.node.ts){:target=_blank .external-link}

## Number

Number field ที่รองรับทศนิยม:

```typescript
{
	displayName: 'Amount',
	name: 'amount',
	type: 'number',
	required: true,
	typeOptions: {
		maxValue: 10,
		minValue: 0,
		numberPrecision: 2,
	},
	default: 10.00,
	description: 'Your current amount',
	displayOptions: { // the resources and operations to display this element with
		show: {
			resource: [
				// comma-separated list of resource names
			],
			operation: [
				// comma-separated list of operation names
			]
		}
	},
}
```

![Decimal](/_images/integrations/creating-nodes/decimal.png)

## Collection

ใช้ type `collection` เมื่อคุณต้องการแสดง field ที่เป็น option เสริม

```typescript
{
	displayName: 'Filters',
	name: 'filters',
	type: 'collection',
	placeholder: 'Add Field',
	default: {},
	options: [
		{
			displayName: 'Type',
			name: 'type',
			type: 'options',
			options: [
				{
					name: 'Automated',
					value: 'automated',
				},
				{
					name: 'Past',
					value: 'past',
				},
				{
					name: 'Upcoming',
					value: 'upcoming',
				},
			],
			default: '',
		},
	],
	displayOptions: { // the resources and operations to display this element with
		show: {
			resource: [
				// comma-separated list of resource names
			],
			operation: [
				// comma-separated list of operation names
			]
		}
	},
}
```

![Collection](/_images/integrations/creating-nodes/collection.png)

## DateTime

type `dateTime` จะมี date picker ให้เลือกวันเวลา

```typescript
{
	displayName: 'Modified Since',
	name: 'modified_since',
	type: 'dateTime',
	default: '',
	description: 'The date and time when the file was last modified',
	displayOptions: { // the resources and operations to display this element with
		show: {
			resource: [
				// comma-separated list of resource names
			],
			operation: [
				// comma-separated list of operation names
			]
		}
	},
}
```

![DateTime](/_images/integrations/creating-nodes/datetime.png)

## Boolean

type `boolean` จะเพิ่ม toggle สำหรับเลือก true หรือ false

```typescript
{
	displayName: 'Wait for Image',
	name: 'waitForImage',
	type: 'boolean',
	default: true, // Initial state of the toggle
	description: 'Whether to wait for the image or not',
	displayOptions: { // the resources and operations to display this element with
		show: {
			resource: [
				// comma-separated list of resource names
			],
			operation: [
				// comma-separated list of operation names
			]
		}
	},
}
```

![Boolean](/_images/integrations/creating-nodes/boolean.png)

## Color

type `color` จะมีตัวเลือกสีให้เลือก

```typescript
{
	displayName: 'Background Color',
	name: 'backgroundColor',
	type: 'color',
	default: '', // Initially selected color
	displayOptions: { // the resources and operations to display this element with
		show: {
			resource: [
				// comma-separated list of resource names
			],
			operation: [
				// comma-separated list of operation names
			]
		}
	},
}
```

![Color](/_images/integrations/creating-nodes/color.png)

## Options

type `options` จะเพิ่ม list ตัวเลือก ผู้ใช้เลือกได้ 1 ค่า

```typescript
{
	displayName: 'Resource',
	name: 'resource',
	type: 'options',
	options: [
		{
			name: 'Image',
			value: 'image',
		},
		{
			name: 'Template',
			value: 'template',
		},
	],
	default: 'image', // The initially selected option
	description: 'Resource to consume',
	displayOptions: { // the resources and operations to display this element with
		show: {
			resource: [
				// comma-separated list of resource names
			],
			operation: [
				// comma-separated list of operation names
			]
		}
	},
}
```

![Options](/_images/integrations/creating-nodes/options.png)

## Multi-options

type `multiOptions` จะเพิ่ม list ตัวเลือก ผู้ใช้เลือกได้มากกว่า 1 ค่า

```typescript
{
	displayName: 'Events',
	name: 'events',
	type: 'multiOptions',
	options: [
		{
			name: 'Plan Created',
			value: 'planCreated',
		},
		{
			name: 'Plan Deleted',
			value: 'planDeleted',
		},
	],
	default: [], // Initially selected options
	description: 'The events to be monitored',
	displayOptions: { // the resources and operations to display this element with
		show: {
			resource: [
				// comma-separated list of resource names
			],
			operation: [
				// comma-separated list of operation names
			]
		}
	},
}
```

![Multi-options](/_images/integrations/creating-nodes/multioptions.png)

## Filter

ใช้ component นี้เพื่อ evaluate, match หรือ filter ข้อมูลที่เข้ามา

นี่คือตัวอย่างโค้ดจาก If node ของ n8n ซึ่งแสดงการใช้ filter component ร่วมกับ [collection](#collection) component ที่ผู้ใช้สามารถตั้งค่า behavior ของ filter ได้

```typescript
{
	displayName: 'Conditions',
	name: 'conditions',
	placeholder: 'Add Condition',
	type: 'filter',
	default: {},
	typeOptions: {
		filter: {
			// Use the user options (below) to determine filter behavior
			caseSensitive: '={{!$parameter.options.ignoreCase}}',
			typeValidation: '={{$parameter.options.looseTypeValidation ? "loose" : "strict"}}',
		},
	},
},
{
	displayName: 'Options',
	name: 'options',
	type: 'collection',
	placeholder: 'Add option',
	default: {},
	options: [
		{
			displayName: 'Ignore Case',
			description: 'Whether to ignore letter case when evaluating conditions',
			name: 'ignoreCase',
			type: 'boolean',
			default: true,
		},
		{
			displayName: 'Less Strict Type Validation',
			description: 'Whether to try casting value types based on the selected operator',
			name: 'looseTypeValidation',
			type: 'boolean',
			default: true,
		},
	],
}
```

![Filter](/_images/integrations/creating-nodes/filter.png)

## Assignment collection (drag and drop)

ใช้ component drag & drop เมื่อคุณต้องการให้ผู้ใช้กรอก name และ value ได้ด้วยการลากเพียงครั้งเดียว

```typescript
{
	displayName: 'Fields to Set',
	name: 'assignments',
	type: 'assignmentCollection',
	default: {},
},
```

ดูตัวอย่างได้ที่ [Edit Fields (Set) node](https://github.com/n8n-io/n8n/tree/0faeab1228e26d69a2a93bdb2f89523cca1e4036/packages/nodes-base/nodes/Set/v2){:target=_blank .external-link}:

![A gif showing the drag and drop action, as well as changing a field to fixed](/_images/integrations/builtin/core-nodes/set/drag-drop-fixed-toggle.gif)

## Fixed collection

ใช้ type `fixedCollection` เพื่อจัดกลุ่ม field ที่เกี่ยวข้องกัน

```typescript
{
	displayName: 'Metadata',
	name: 'metadataUi',
	placeholder: 'Add Metadata',
	type: 'fixedCollection',
	default: '',
	typeOptions: {
		multipleValues: true,
	},
	description: '',
	options: [
		{
			name: 'metadataValues',
			displayName: 'Metadata',
			values: [
				{
					displayName: 'Name',
					name: 'name',
					type: 'string',
					default: 'Name of the metadata key to add.',
				},
				{
					displayName: 'Value',
					name: 'value',
					type: 'string',
					default: '',
					description: 'Value to set for the metadata key.',
				},
			],
		},
	],
	displayOptions: { // the resources and operations to display this element with
		show: {
			resource: [
				// comma-separated list of resource names
			],
			operation: [
				// comma-separated list of operation names
			]
		}
	},
}
```

![Fixed collection](/_images/integrations/creating-nodes/fixed-collection.png)

## Resource locator

![Resource locator](/_images/integrations/creating-nodes/resource-locator.png)

Resource locator element ช่วยให้ผู้ใช้หา resource เฉพาะใน service ภายนอก เช่น card หรือ label ใน Trello

ตัวเลือกที่มีให้:

* ID
* URL
* List: ให้ผู้ใช้เลือกหรือค้นหาจาก list ที่เตรียมไว้ ตัวเลือกนี้ต้องเขียนโค้ดเพิ่มเพื่อ populate list และ handle การค้นหา

คุณสามารถเลือกว่าจะให้มี type ไหนบ้าง

ตัวอย่าง:

```typescript
{
	displayName: 'Card',
	name: 'cardID',
	type: 'resourceLocator',
	default: '',
	description: 'Get a card',
	modes: [
		{
			displayName: 'ID',
			name: 'id',
			type: 'string',
			hint: 'Enter an ID',
			validation: [
				{
					type: 'regex',
					properties: {
						regex: '^[0-9]',
						errorMessage: 'The ID must start with a number',
					},
				},
			],
			placeholder: '12example',
			// How to use the ID in API call
			url: '=http://api-base-url.com/?id={{$value}}',
		},
		{
			displayName: 'URL',
			name: 'url',
			type: 'string',
			hint: 'Enter a URL',
			validation: [
				{
					type: 'regex',
					properties: {
						regex: '^http',
						errorMessage: 'Invalid URL',
					},
				},
			],
			placeholder: 'https://example.com/card/12example/',
			// How to get the ID from the URL
			extractValue: {
				type: 'regex',
				regex: 'example.com/card/([0-9]*.*)/',
			},
		},
		{
			displayName: 'List',
			name: 'list',
			type: 'list',
			typeOptions: {
				// You must always provide a search method
				// Write this method within the methods object in your base file
				// The method must populate the list, and handle searching if searchable: true
				searchListMethod: 'searchMethod',
				// If you want users to be able to search the list
				searchable: true,
				// Set to true if you want to force users to search
				// When true, users can't browse the list
				// Or false if users can browse a list
				searchFilterRequired: true,
			},
		},
	],
	displayOptions: {
		// the resources and operations to display this element with
		show: {
			resource: [
				// comma-separated list of resource names
			],
			operation: [
				// comma-separated list of operation names
			],
		},
	},
},
```

ดูตัวอย่างจริงได้ที่:

* ดู [`CardDescription.ts`](https://github.com/n8n-io/n8n/blob/master/packages/nodes-base/nodes/Trello/CardDescription.ts){:target=_blank .external-link} และ [`Trello.node.ts`](https://github.com/n8n-io/n8n/blob/master/packages/nodes-base/nodes/Trello/Trello.node.ts){:target=_blank .external-link} ใน Trello node ของ n8n สำหรับตัวอย่าง list ที่มี search และ `searchFilterRequired: true`
* ดู [`GoogleDrive.node.ts`](https://github.com/n8n-io/n8n/blob/master/packages/nodes-base/nodes/Google/Drive/GoogleDrive.node.ts){:target=_blank .external-link} สำหรับตัวอย่างที่ผู้ใช้สามารถ browse หรือ search ได้

## Resource mapper

ถ้า node ของคุณทำ insert, update หรือ upsert คุณต้องส่งข้อมูลในรูปแบบที่ service รองรับ ปกติจะใช้ Set node ก่อน node ที่จะส่งข้อมูล เพื่อแปลงข้อมูลให้ตรง schema ของ service แต่ resource mapper UI component จะช่วยให้ map ข้อมูลใน node ได้เลยโดยไม่ต้องใช้ Set node และยัง validate ข้อมูลกับ schema ที่กำหนดใน node ได้ด้วย

/// note | Mapping and matching
Mapping คือการตั้งค่าข้อมูล input ที่จะใช้เป็น value ตอน update row ส่วน Matching คือการใช้ชื่อ column เพื่อระบุ row ที่จะ update
///

```js
{
	displayName: 'Columns',
	name: 'columns', // The name used to reference the element UI within the code
	type: 'resourceMapper', // The UI element type
	default: {
		// mappingMode can be defined in the component (mappingMode: 'defineBelow')
		// or you can attempt automatic mapping (mappingMode: 'autoMapInputData')
		mappingMode: 'defineBelow',
		// Important: always set default value to null
		value: null,
	},
	required: true,
	// See "Resource mapper type options interface" below for the full typeOptions specification
	typeOptions: {
		resourceMapper: {
			resourceMapperMethod: 'getMappingColumns',
			mode: 'update',
			fieldWords: {
				singular: 'column',
				plural: 'columns',
			},
			addAllFields: true, 
			multiKeyMatch: true,
			supportAutoMap: true,
			matchingFieldsLabels: {
				title: 'Custom matching columns title',
				description: 'Help text for custom matching columns',
				hint: 'Below-field hint for custom matching columns',
			},
		},
	},
},
```

ดูตัวอย่างจริงได้ที่ [Postgres node (version 2)](https://github.com/n8n-io/n8n/tree/master/packages/nodes-base/nodes/Postgres/v2){:target=_blank .external-link} สำหรับ database schema

ดูตัวอย่างจริงที่ [Google Sheets node (version 2)](https://github.com/n8n-io/n8n/tree/master/packages/nodes-base/nodes/Google/Sheet/v2){:target=_blank .external-link} สำหรับ schema-less service

### Resource mapper type options interface

section `typeOptions` ต้อง implement interface นี้:

```js
export interface ResourceMapperTypeOptions {
	// The name of the method where you fetch the schema
	// Refer to the Resource mapper method section for more detail
	resourceMapperMethod: string;
	// Choose the mode for your operation
	// Supported modes: add, update, upsert
	mode: 'add' | 'update' | 'upsert';
	// Specify labels for fields in the UI
	fieldWords?: { singular: string; plural: string };
	// Whether n8n should display a UI input for every field when node first added to workflow
	// Default is true
	addAllFields?: boolean;
	// Specify a message to show if no fields are fetched from the service 
	// (the call is successful but the response is empty)
	noFieldsError?: string;
	// Whether to support multi-key column matching
	// multiKeyMatch is for update and upsert only
	// Default is false
	// If true, the node displays a multi-select dropdown for the matching column selector
	multiKeyMatch?: boolean;
	// Whether to support automatic mapping
	// If false, n8n hides the mapping mode selector field and sets mappingMode to defineBelow
	supportAutoMap?: boolean;
	// Custom labels for the matching columns selector
	matchingFieldsLabels?: {
		title?: string;
		description?: string;
		hint?: string;
	};
}
```

### Resource mapper method

method นี้จะมี logic เฉพาะ node สำหรับดึง schema ของข้อมูล ทุก node ต้อง implement logic สำหรับดึง schema และตั้งค่า UI field ตาม schema

ต้อง return ค่าเป็นไปตาม interface `ResourceMapperFields`:

```js
interface ResourceMapperField {
	// Field ID as in the service
	id: string;
	// Field label
	displayName: string;
	// Whether n8n should pre-select the field as a matching field
	// A matching field is a column used to identify the rows to modify
	defaultMatch: boolean;
	// Whether the field can be used as a matching field
	canBeUsedToMatch?: boolean;
	// Whether the field is required by the schema
	required: boolean;
	// Whether to display the field in the UI
	// If false, can't be used for matching or mapping
	display: boolean;
	// The data type for the field
	// These correspond to UI element types
	// Supported types: string, number, dateTime, boolean, time, array, object, options
	type?: FieldType;
	// Added at runtime if the field is removed from mapping by the user
	removed?: boolean;
	// Specify options for enumerated types
	options?: INodePropertyOptions[];
}
```

ดูตัวอย่างจริงที่ [Postgres resource mapping method](https://github.com/n8n-io/n8n/blob/master/packages/nodes-base/nodes/Postgres/v2/methods/resourceMapping.ts){:target=_blank .external-link} และ [Google Sheets resource mapping method](https://github.com/n8n-io/n8n/blob/master/packages/nodes-base/nodes/Google/Sheet/v2/methods/resourceMapping.ts){:target=_blank .external-link}

## JSON

```typescript
{
	displayName: 'Content (JSON)',
	name: 'content',
	type: 'json',
	default: '',
	description: '',
	displayOptions: { // the resources and operations to display this element with
		show: {
			resource: [
				// comma-separated list of resource names
			],
			operation: [
				// comma-separated list of operation names
			]
		}
	},
}
```

![JSON](/_images/integrations/creating-nodes/json.png)

## HTML

HTML editor ให้ผู้ใช้สร้าง HTML template ใน workflow ได้ Editor รองรับ HTML มาตรฐาน, CSS ใน `<style>`, และ expression ใน `{{}}` ผู้ใช้สามารถเพิ่ม `<script>` เพื่อดึง JavaScript เพิ่มเติมได้ n8n จะไม่รัน JavaScript นี้ตอน workflow ทำงาน

```js
{
	displayName: 'HTML Template', // The value the user sees in the UI
	name: 'html', // The name used to reference the element UI within the code
	type: 'string',
	typeOptions: {
		editor: 'htmlEditor',
	},
	default: placeholder, // Loads n8n's placeholder HTML template
	noDataExpression: true, // Prevent using an expression for the field
	description: 'HTML template to render',
},
```

ดูตัวอย่างจริงที่ [`Html.node.ts`](https://github.com/n8n-io/n8n/blob/master/packages/nodes-base/nodes/Html/Html.node.ts){:target=_blank .external-link}

## Notice

แสดงกล่องเหลืองพร้อม hint หรือข้อมูลเสริม ดูแนวทางการเขียน hint ที่ดีได้ที่ [Node UI design](/integrations/creating-nodes/plan/node-ui-design.md)

```js
{
  displayName: 'Your text here',
  name: 'notice',
  type: 'notice',
  default: '',
},
```
![Notice](/_images/integrations/creating-nodes/notice.png)

## Hints

hint มี 2 แบบ: parameter hint และ node hint

* Parameter hint คือข้อความสั้นใต้ input field
* Node hint เป็นตัวเลือกที่ยืดหยุ่นกว่า [Notice](#notice) ใช้แสดง hint ยาวๆ ใน input panel, output panel หรือ node details view

### Add a parameter hint

เพิ่ม parameter `hint` ใน UI element:

```ts
{
	displayName: 'URL',
	name: 'url',
	type: 'string',
	hint: 'Enter a URL',
	...
}
```

### Add a node hint

กำหนด hint ของ node ใน property `hints` ใน node `description`:

```ts
description: INodeTypeDescription = {
	...
	hints: [
		{
			// The hint message. You can use HTML.
			message: "This node has many input items. Consider enabling <b>Execute Once</b> in the node\'s settings.",
			// Choose from: info, warning, danger. The default is 'info'.
			// Changes the color. info (grey), warning (yellow), danger (red)
			type: 'info',
			// Choose from: inputPane, outputPane, ndv. By default n8n displays the hint in both the input and output panels.
			location: 'outputPane',
			// Choose from: always, beforeExecution, afterExecution. The default is 'always'
			whenToDisplay: 'beforeExecution',
			// Optional. An expression. If it resolves to true, n8n displays the message. Defaults to true.
			displayCondition: '={{ $parameter["operation"] === "select" && $input.all().length > 1 }}'
		}
	]
	...
}
```

### Add a dynamic hint to a programmatic-style node

ใน node แบบ programmatic-style สามารถสร้างข้อความ hint แบบ dynamic ที่มีข้อมูลจากการ execute node ได้ (ต้อง execute ก่อนถึงจะแสดงได้)

```ts
if (operation === 'select' && items.length > 1 && !node.executeOnce) {
    // Expects two parameters: NodeExecutionData and an array of hints
	return new NodeExecutionOutput(
		[returnData],
		[
			{
				message: `This node ran ${items.length} times, once for each input item. To run for the first item only, enable <b>Execute once</b> in the node settings.`,
				location: 'outputPane',
			},
		],
	);
}
return [returnData];
```

ดูตัวอย่างจริงของ dynamic hint ใน programmatic-style node ได้ที่ [Split Out node code](https://github.com/n8n-io/n8n/blob/master/packages/nodes-base/nodes/Transform/SplitOut/SplitOut.node.ts#L266){:target=_blank .external-link}
