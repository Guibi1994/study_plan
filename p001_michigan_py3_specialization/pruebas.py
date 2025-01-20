1 + 1

import requests

url = requests.get("https://github.com/Guibi1994")
print(url.text.count(""))
