import requests
from django.shortcuts import render
from .models import City
from .forms import CityForm

# Create your views here.
def index(request):
	keyid = '8b7f212f6824671399d1206caaf28f9e'
	url = 'https://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid=' + keyid

	if(request.method == 'POST'):
		form = CityForm(request.POST)
		form.save()

	form = CityForm()

	cities = City.objects.all()

	all__cities = []

	for city in cities:
		res = requests.get(url.format(city.name)).json()	

		city_info = {
			'city': city.name,
			'temp': res["main"]["temp"],
			'icon': res["weather"][0]["icon"]
		}

		all__cities.append(city_info)
	

	context = {
		'all_info': all__cities,
		'form': form
	}

	return render(request, 'weather/index.html', context)