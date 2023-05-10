from django.shortcuts import render
from django.shortcuts import render
import json
import urllib.request


def index(request):
        if request.method == 'POST':
            city = request.POST.get("city")
            if city:
                api_key = "164fec96a27b97680ee442e489ce3f06"
                url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&units=metric&appid={api_key}"
                response = urllib.request.urlopen(url)
                data = json.loads(response.read())
                temperature = data["main"]["temp"]
                description = data["weather"][0]["description"]
                return render(request, "index.html", {"city": city, "temperature": temperature, "description": description})
            else:
                return render(request, "index.html")


    
    
       
        #         city = request.POST['city']
        #         source = urllib.request.urlopen(
        #             f'http://api.openweathermap.org/data/2.5/weather?q={city}&units=imperial&appid=164fec96a27b97680ee442e489ce3f06'
        #         ).read()

        #         list_of_data = json.loads(source)
        #         data = {
        #             "country_code": str(list_of_data['sys']['country']),
        #             "coordinate": str(list_of_data['coord']['lon']) + ' '
        #                         + str(list_of_data['coord']['lat']),
        #             "temp": str(list_of_data['main']['temp']) + 'k',
    #             "pressure": str(list_of_data['main']['pressure']),
        #             "humidity": str(list_of_data['main']['humidity']),
        #         }
        # else:
        #         data ={}
    
    
