import requests

response = requests.get('https://www.lamudi.com.mx/nuevo-leon/casa/for-sale/',headers={'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36'})
print(type(response))
print(response.status_code )

