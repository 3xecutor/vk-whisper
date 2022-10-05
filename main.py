import requests
r= requests.get('https://vk.com')
print(r.status_code)