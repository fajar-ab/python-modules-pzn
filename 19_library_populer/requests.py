import requests

# GET requests sederhana
response = requests.get("https://jsonplaceholder.typicode.com/posts/1")

if response.status.code == 200:
    data = response.json()
    print(data)
else:
    print("Error:", response.status.code)
