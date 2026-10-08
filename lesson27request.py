import requests

# r = requests.get(url="https://cbu.uz/uz/arkhiv-kursov-valyut/json/")


# print(r.status_code)
# print(r.json()[:3])

# for i in r.json()[:3]:
#     print(f" {i['Rate']} - {i['Ccy']}")


"""
1 dolar - 11778.45 sum
1 euro - ...
1 rubl - ...
"""
#
# url = "https://api.open-meteo.com/v1/forecast"
# params = {
#     "latitude": 41.31,          # Toshkent
#     "longitude": 69.28,
#     "current_weather": True
# }
# r = requests.get(url, params=params)
#
# print(r.json()["current_weather"]["temperature"],"- gradus selsida")


# post qilish

url = "https://jsonplaceholder.typicode.com/posts"
url_update = "https://jsonplaceholder.typicode.com/posts/2"

data = {
    "title": "salom",
    "body": "Examples use the Fetch API, but any HTTP client works.",
    "userId": 1
}

r = requests.post(url=url, data=data)
r2 = requests.put(url=url_update, data=data)
print(r.status_code)
print(r.json())

print(r2.status_code)
print(r2.json())


