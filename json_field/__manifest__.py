{
    "name": "Json field",
    "version": "15.0.0.0.1",
    "category": "Field type",
    "author": "Article714",
    "license": "LGPL-3",
    "website": "https://www.article714.org",
    "summary": """ """,
    "depends": ["base", "web"],
    "assets": {
        "web.assets_backend": [
            "json_field/static/src/js/json_field.js",
            "json_field/static/lib/ajv.min.js",
            "json_field/static/src/scss/json_field.scss",
        ],
        "web.assets_qweb": [
            "json_field/static/src/xml/json_field.xml",
        ],
    },
    "installable": True,
    "images": [],
    "application": True,
}
