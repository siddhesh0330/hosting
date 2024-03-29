import requests
response = requests.get("https://hosting-7d4p.onrender.com/1B")
open('downloaded_file.py', 'wb').write(response.content)


