from django.shortcuts import render
import requests

def index(request):
    appid = 'f703ca03191f7ce7d08884aeaea4ae0d'
    url = "https://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid=" + appid

    city = 'London'
    res = requests.get(url.format(city))
    print(res.text)
    return render(request,'weather/index.html')
