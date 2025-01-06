# **main.json**

This JSON file serves as the configuration file for a
Citrus-supported repository. Below is a detailed breakdown of its structure and fields.

---

## **Root Structure**
```json
{
    "repository": {
        "name": "basic repo",
        "repo-id": "citrus-repo-example",
        "description": "description of this repository.",
        "repository-authors": ["p3til"],
        "icon-url": "/repo.ico",
        "single-app": false,
        "repository-apps": [ /* Array of apps */ ]
    }
}
```

## **App Structure**
```json
{
    "name": "someapp",
    "description": "This app doesn't exist, it is fake.",
    "authors": ["P3til"],
    "version": "v1",
    "catagory": "hidden",
    "icon": "/app.ico",
    "website-locked": {
        "active": false,
        "public-key": "",
        "url": "/apps/someapp/app.ico"
    },
    "installer": "/apps/someapp/main.bat"
}
```

# compile.py
This creates your README.md for github