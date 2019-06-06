from tap_kit.streams import Stream

class AssetsStream(Stream):

    stream = 'assets'

    meta_fields = dict(
        key_properties=['id'],
        replication_method='incremental',
        selected_by_default=False
    )

    schema = {
        "properties": {
              "copyright": {
                "type": [
                    "null",
                    "string"
                    ]
              },
              "type": {
                "type": [
                    "null",
                    "string"
                    ]
              },
              "idHash": {
                "type": [
                    "null",
                    "string"
                    ]
              },
              "id": {
                "type": [
                    "null",
                    "string"
                    ]
              },
              "height": {
                "type": [
                    "null",
                    "integer"
                    ]
              },
              "archive": {
                "type": [
                    "null",
                    "integer"
                    ]
              },
              "tags": {
                "type": [
                    "null",
                    "array"
                ]
              },
              "datePublished": {
                "type": [
                    "null",
                    "string"
                    ],
                "format": "date-time"
              },
              "fileSize": {
                "type": [
                    "null",
                    "integer"
                    ]
              },
              "brandId": {
                "type": [
                    "null",
                    "string"
                    ]
              },
              "name": {
                "type": [
                    "null",
                    "string"
                    ]
              },
              "extension": {
                "type": [
                    "null",
                    "array"
                ]
              },
              "description": {
                "type": [
                    "null",
                    "string"
                    ]
              },
              "userCreated": {
                "type": [
                    "null",
                    "string"
                    ]
              },
              "dateCreated": {
                "type": [
                    "null",
                    "string"
                    ],
                "format": "date-time"
              },
              "isPublic": {
                "type": [
                    "null",
                    "integer"
                    ]
              },
              "propertyOptions": {
                "type": [
                    "null",
                    "array"
                ]
              },
              "orientation": {
                "type": [
                    "null",
                    "string"
                    ]
              },
              "dateModified": {
                "type": [
                    "null",
                    "string"
                    ],
                "format": "date-time"
              },
              "width": {
                "type": [
                    "null",
                    "integer"
                    ]
              },
              "watermarked": {
                "type": [
                    "null",
                    "integer"
                    ]
              },
              "limited": {
                "type": [
                    "null",
                    "integer"
                    ]
              },
              "thumbnails": {
                "type": [
                    "null",
                    "object"
                ],
                "properties": {
                    "mini": {
                        "type": [
                            "null",
                            "string"
                        ]
                    },
                    "webimage": {
                        "type": [
                            "null",
                            "string"
                        ]
                    },
                    "thul": {
                        "type": [
                            "null",
                            "string"
                        ]
                    }
                }
              },
              "property_wenumber": {
                "type": [
                    "null",
                    "array"
                ]
              },
              "property_filetype": {
                "type": [
                    "null",
                    "array"
                ]
              },
              "property_usagerights": {
                "type": [
                    "null",
                    "array"
                ]
              },
              "property_market": {
                "type": [
                    "null",
                    "array"
                ]
              },
              "property_marketingreference": {
                "type": [
                    "null",
                    "array"
                ]
              },
              "property_assetsubtype": {
                "type": [
                    "null",
                    "array"
                ]
              },
              "property_bestofphotography": {
                "type": [
                    "null",
                    "array"
                ]
              },
              "property_assettype": {
                "type": [
                    "null",
                    "array"
                ]
              },
              "property_visibleto": {
                "type": [
                    "null",
                    "array"
                ]
              },
              "property_state": {
                "type": [
                    "null",
                    "array"
                ]
              },
              "property_country": {
                "type": [
                    "null",
                    "array"
                ]
            }
        }
    }
