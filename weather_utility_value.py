from datetime import datetime, timezone
values = {"coord": {"lon": 3.75, "lat": 6.5833},
          "weather": [{"id": 803, "main": "Clouds", "description": "broken clouds", "icon": "04d"}],
          "base": "stations",
          "main": {"temp": 304.33, "feels_like": 308.13, "temp_min": 304.33, "temp_max": 304.33, "pressure": 1006, "humidity": 59, "sea_level": 1006, "ground_level": 1006},
          "visibility": 10000,
          "wind": {"speed": 5.05, "deg": 197, "gust": 6.2},
          "clouds": {"all": 59},
          "dt": 1679156754,
          "sys": {"type": 1, "id": 1185, "country": "NG", "sunrise": 1679118622, "sunset": 1679162163},
          "timezone": 3600, "id": 2332453,
          "name": "Lagos",
          "cod": 200}
# print(values)

# get value of icon


# def get_value_of_icon():
#     value = values["weather"][0]["icon"]
#     return value


# print(get_value_of_icon())


# def get_value_of_gust():
#     value = values["wind"]["gust"]
#     return value


# print(get_value_of_gust())


# def get_value_of_pressure():
#     value = values["main"]["pressure"]
#     return value


# print(get_value_of_pressure())


# def get_value_of_sunrise():
#     value = values["sys"]["sunrise"]
#     return value


# print(get_value_of_sunrise())


def get_sunrise_readable_time():
    sunrise = datetime.fromtimestamp(1679162163)
    return sunrise


print(get_sunrise_readable_time())
