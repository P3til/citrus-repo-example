import json
import base64

with open("main.json", "r") as json_file:
    data = json.load(json_file)

repository = data["repository"]
repo_name = repository["name"]
repo_id = repository["repo-name"]
repo_description = repository["description"]
repo_icon_url = repository["icon-url"]
repo_author = repository["repository-authors"][0]
apps = repository["apps"]

apps_table = ""
app_authors = ""
for app in apps:

    app_name = app["name"]
    app_image = f'<img src="./apps/{app_name}/{app["icon"]}" width="50" height="50">'
    app_version = app["version"]
    app_category = app["catagory"]
    for author in app["authors"]:
        app_authors += f"{author}{app["authors"][app["authors"].__len__()-1] != author and ', ' or ''}"

    apps_table += f"|{app_image}|**{app_name}**|{app_version}|{app_authors}|{app_category}|\n"

readme_content = f"""
![Repository Icon]({repo_icon_url})

# {repo_name}
{repo_description}

### Includes:
|**Icon**|**App** [^1]|**Version** [^2]|**Author** [^3]|**Category** [^4]|
|-|-|-|-|-|
{apps_table}

## Opening through Citrus:
Open Repository through Citrus!
```
Citrus://repository/{repo_id}/
```

Or click the blue + icon and paste in the URL slot:
```
https://github.com/repository/{repo_id}/
```

[^1]: **App Tab:** The app name of which is being installed.

[^2]: **Version:** The version the app is on.

[^3]: **Author:** The person who made the app.

[^4]: **Category:** The type of app it is being installed. (Games, Productivity, etc.)

###### Created by [**{repo_author}**](https://github.com/{repo_author}).
"""
version = "{\"client\":\"citrus\"}::v.2" ## Version 1.1 ##

with open(".citrusversion", "w") as version_file:
    version_file.write(base64.b64encode(version.encode("utf-8")).decode("utf-8"))

with open("README.md", "w") as readme_file:
    readme_file.write(readme_content)
