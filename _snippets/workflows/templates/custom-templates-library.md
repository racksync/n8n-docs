ใน environment variables ของคุณ ตั้งค่า `N8N_TEMPLATES_HOST` เป็น base URL ของ API ของคุณ

### Endpoints

API ของคุณต้องมี endpoints และโครงสร้างข้อมูลเหมือนกับของ n8n

Endpoints คือ:

| Method | Path |
| ------ | ---- |
| GET | /templates/workflows/`<id>` |
| GET | /templates/search |
| GET | /templates/collections/`<id>` |
| GET | /templates/collections |
| GET | /templates/categories |
| GET | /health |

### Query parameters

Endpoint `/templates/search` ยอมรับ query parameters ต่อไปนี้:

| Parameter  | Type                                         | คำอธิบาย                                      |
|------------|----------------------------------------------|--------------------------------------------------|
| `page`     | integer                                      | หน้าของผลลัพธ์ที่จะส่งคืน                    |
| `rows`     | integer                                      | จำนวนผลลัพธ์สูงสุดที่จะส่งคืนต่อหน้า |
| `category` | comma-separated list of strings (categories) | หมวดหมู่ที่จะค้นหาภายใน                  |
| `search`   | string                                       | คำค้นหา                                 |

Endpoint `/templates/collections` ยอมรับ query parameters ต่อไปนี้:

| Parameter  | Type                                         | คำอธิบาย                     |
|------------|----------------------------------------------|---------------------------------|
| `category` | comma-separated list of strings (categories) | หมวดหมู่ที่จะค้นหาภายใน |
| `search`   | string                                       | คำค้นหา                |

### Data schema

คุณสามารถสำรวจโครงสร้างข้อมูลของรายการใน response object ที่ส่งคืนโดย endpoints ได้ที่นี่:

??? note "แสดง `workflow` item data schema"
	```json title="Workflow item data schema"
	{
	  "$schema": "http://json-schema.org/draft-07/schema#",
	  "title": "Generated schema for Root",
	  "type": "object",
	  "properties": {
	    "id": {
	      "type": "number"
	    },
	    "name": {
	      "type": "string"
	    },
	    "totalViews": {
	      "type": "number"
	    },
	    "price": {},
	    "purchaseUrl": {},
	    "recentViews": {
	      "type": "number"
	    },
	    "createdAt": {
	      "type": "string"
	    },
	    "user": {
	      "type": "object",
	      "properties": {
	        "username": {
	          "type": "string"
	        },
	        "verified": {
	          "type": "boolean"
	        }
	      },
	      "required": [
	        "username",
	        "verified"
	      ]
	    },
	    "nodes": {
	      "type": "array",
	      "items": {
	        "type": "object",
	        "properties": {
	          "id": {
	            "type": "number"
	          },
	          "icon": {
	            "type": "string"
	          },
	          "name": {
	            "type": "string"
	          },
	          "codex": {
	            "type": "object",
	            "properties": {
	              "data": {
	                "type": "object",
	                "properties": {
	                  "details": {
	                    "type": "string"
	                  },
	                  "resources": {
	                    "type": "object",
	                    "properties": {
	                      "generic": {
	                        "type": "array",
	                        "items": {
	                          "type": "object",
	                          "properties": {
	                            "url": {
	                              "type": "string"
	                            },
	                            "icon": {
	                              "type": "string"
	                            },
	                            "label": {
	                              "type": "string"
	                            }
	                          },
	                          "required": [
	                            "url",
	                            "label"
	                          ]
	                        }
	                      },
	                      "primaryDocumentation": {
	                        "type": "array",
	                        "items": {
	                          "type": "object",
	                          "properties": {
	                            "url": {
	                              "type": "string"
	                            }
	                          },
	                          "required": [
	                            "url"
	                          ]
	                        }
	                      }
	                    },
	                    "required": [
	                      "primaryDocumentation"
	                    ]
	                  },
	                  "categories": {
	                    "type": "array",
	                    "items": {
	                      "type": "string"
	                    }
	                  },
	                  "nodeVersion": {
	                    "type": "string"
	                  },
	                  "codexVersion": {
	                    "type": "string"
	                  }
	                },
	                "required": [
	                  "categories"
	                ]
	              }
	            }
	          },
	          "group": {
	            "type": "string"
	          },
	          "defaults": {
	            "type": "object",
	            "properties": {
	              "name": {
	                "type": "string"
	              },
	              "color": {
	                "type": "string"
	              }
	            },
	            "required": [
	              "name"
	            ]
	          },
	          "iconData": {
	            "type": "object",
	            "properties": {
	              "icon": {
	                "type": "string"
	              },
	              "type": {
	                "type": "string"
	              },
	              "fileBuffer": {
	                "type": "string"
	              }
	            },
	            "required": [
	              "type"
	            ]
	          },
	          "displayName": {
	            "type": "string"
	          },
	          "typeVersion": {
	            "type": "number"
	          },
	          "nodeCategories": {
	            "type": "array",
	            "items": {
	              "type": "object",
	              "properties": {
	                "id": {
	                  "type": "number"
	                },
	                "name": {
	                  "type": "string"
	                }
	              },
	              "required": [
	                "id",
	                "name"
	              ]
	            }
	          }
	        },
	        "required": [
	          "id",
	          "icon",
	          "name",
	          "codex",
	          "group",
	          "defaults",
	          "iconData",
	          "displayName",
	          "typeVersion"
	        ]
	      }
	    }
	  },
	  "required": [
	    "id",
	    "name",
	    "totalViews",
	    "price",
	    "purchaseUrl",
	    "recentViews",
	    "createdAt",
	    "user",
	    "nodes"
	  ]
	}
	```

??? note "แสดง `category` item data schema"
	```json title="Category item data schema"
	{
	  "$schema": "http://json-schema.org/draft-07/schema#",
	  "type": "object",
	  "properties": {
	    "id": {
	      "type": "number"
	    },
	    "name": {
	      "type": "string"
	    }
	  },
	  "required": [
	    "id",
	    "name"
	  ]
	}
	```

??? note "แสดง `collection` item data schema"
	```json title="Collection item data schema"
	{
	  "$schema": "http://json-schema.org/draft-07/schema#",
	  "type": "object",
	  "properties": {
	    "id": {
	      "type": "number"
	    },
	    "rank": {
	      "type": "number"
	    },
	    "name": {
	      "type": "string"
	    },
	    "totalViews": {},
	    "createdAt": {
	      "type": "string"
	    },
	    "workflows": {
	      "type": "array",
	      "items": {
	        "type": "object",
	        "properties": {
	          "id": {
	            "type": "number"
	          }
	        },
	        "required": [
	          "id"
	        ]
	      }
	    },
	    "nodes": {
	      "type": "array",
	      "items": {}
	    }
	  },
	  "required": [
	    "id",
	    "rank",
	    "name",
	    "totalViews",
	    "createdAt",
	    "workflows",
	    "nodes"
	  ]
	}
	```

คุณยังสามารถสำรวจ endpoints ของ API ของ n8n แบบโต้ตอบได้:

[https://api.n8n.io/templates/categories](https://api.n8n.io/templates/categories)
[https://api.n8n.io/templates/collections](https://api.n8n.io/templates/collections)
[https://api.n8n.io/templates/search](https://api.n8n.io/templates/search)
[https://api.n8n.io/health](https://api.n8n.io/health)


คุณสามารถ [ติดต่อเรา](mailto:help@n8n.io) เพื่อขอรับการสนับสนุนเพิ่มเติม
