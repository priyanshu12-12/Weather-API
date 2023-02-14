from django.shortcuts import render
import json
import urllib.request
api='73ba75da689beaa68377836815fdfd95'

    # city='Ranchi'
    # url='https://api.openweathermap.org/data/2.5/weather?q=city & appid=api'
def index(request):
	if request.method == 'POST':
		city = request.POST.get('city', 'True')
		source = urllib.request.urlopen('http://api.openweathermap.org/data/2.5/weather?q='+city+'&appid=73ba75da689beaa68377836815fdfd95').read()

		list_of_data = json.loads(source)

		data = {
            'city':city,
			"country_code": str(list_of_data['sys']['country']),
			"coordinate": str(list_of_data['coord']['lon']) + ' '
						+ str(list_of_data['coord']['lat']),
			"temp": str(round(list_of_data['main']['temp']-273.15, 2)) + 'C',
			"pressure": str(list_of_data['main']['pressure']),
			"humidity": str(list_of_data['main']['humidity']),
		}
		print(data)
	else:
		data ={}
	return render(request, "home.html", data)
