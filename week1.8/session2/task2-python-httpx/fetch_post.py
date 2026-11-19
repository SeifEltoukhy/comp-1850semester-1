"""
Task 2: Fetch and display a post Using GET Request
"""

import httpx

def fetch_json(url):
    response = httpx.get(url)
    print( response.status_code)

    if response.status_code == 200:
        return response.json()  
    else:
        print("Error:", response.status_code)
        return None
    
if __name__ == "__main__":
    data = fetch_json("https://httpbin.io/json")
    if data is not None:
        print(data)

url = "https://httpbin.io/json"

response = httpx.get(url)   # httpx object, get() method, returns a response object

print(response.json())      # response object, json() method
