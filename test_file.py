import requests

response = requests.get("http://127.0.0.1:5000/1B")

open('downloaded_file.txt', 'wb') .write(response.content)
print("File downloaded successfully.")

