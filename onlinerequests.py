import requests

API_KEY = 'QqNV1Cx0hFpUowUNFJBgOAkYrGCEM5I0KQfarcDz'

HOST = f'https://api.freecurrencyapi.com/v1/latest?apikey={API_KEY}&currencies=EUR%2CUSD%2CGBP%2CRUB'

response = requests.get(HOST)

print(response.json())