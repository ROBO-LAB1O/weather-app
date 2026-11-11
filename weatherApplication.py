import requests

def long_lat(city,url):
    url_=url

    params={
        "name" : city,
        "count" : 1,
        "language" : "en"
    }

    response=requests.get(url_, params=params)
    data=response.json()
    if "results" not in data:
        return None
    else: 
        place =data["results"][0]
        return place["longitude"],place["latitude"]

def get_weather(longitude,latitude,url):
    url_=url
    params={
        "latitude" : latitude,
        "longitude" : longitude,
        "current" : "temperature_2m,relative_humidity_2m,weather_code,wind_speed_10m"
    }
    response = requests.get(url_,params=params)
    return response.json()

geo_url= "https://geocoding-api.open-meteo.com/v1/search"

urltemp= "https://api.open-meteo.com/v1/forecast"

def main():
    while True :
        print("To exit or Application Press Enter!")
        city=input("Enter your choosen city: ").lower()
        coords=long_lat(city,geo_url)
        if city=="":
            print("----Thankyou for choosing our Application----")
            break
        
        if coords is None:
                print("City not found!")
        else:
            lon, lat=coords
            data = get_weather(lon,lat,urltemp)
            temp=data["current"]["temperature_2m"]
            humi=data["current"]["relative_humidity_2m"]
            weather_type=data["current"]["weather_code"]
            if weather_type==0:
                weather_desc="Clear Sky!"
            elif weather_type==1:
                weather_desc="Mainly clear"
            elif weather_type==45 or  weather_type==48:
                weather_desc="Fog"
            else:
                weather_desc="Unable to determine!"
            Wind_=data["current"]["wind_speed_10m"]

            print("==========Weather Application=========")

            print(f"City: {city.title()}")
            print(f"Temperature: {temp}")
            print(f"Weather: {weather_desc}*C")
            print(f"Humidity: {humi}%")
            print(f"Wind speed: {Wind_}km/h")

            print("=======================================")

if __name__=="__main__":
    main()