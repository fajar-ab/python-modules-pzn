import requests

# GET request sederhana
response = requests.get("https://jsonplaceholder.typicode.com/posts/1")

if response.status_code == 200:  
    data = response.json()
    print("title -> ", data["title"])
    print("body: ", data["body"])
else:
    print("Error:", response.status_code)