import requests

url= "http://shibe.online/api/shibes?count=2&urls=true&httpsUrls=true"
url2 = "https://api.deepl.com/v2/usage?auth_key=d9e30146-60e6-403c-d630-8d80c5df0652"
response = requests.get(url2)
# Print the status code of the response.
print(response.status_code)
print(response.text)


