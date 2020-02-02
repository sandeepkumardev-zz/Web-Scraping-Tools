import requests
import pandas as pd
from bs4 import BeautifulSoup

page = requests.get('https://forecast.weather.gov/MapClick.php?lat=34.09979000000004&lon=-118.32721499999997')
soup = BeautifulSoup(page.content, 'html.parser')
week = soup.find(id="seven-day-forecast-body")
# print(week)

items = week.find_all(class_ = "tombstone-container")
#print(items[0])

# for i in range(10):
#     print(items[i].find(class_="period-name").get_text())
#     print(items[i].find(class_="short-desc").get_text())
#     print(items[i].find(class_="temp").get_text())
#     print()

period_name = [item.find(class_="period-name").get_text() for item in items]
period_desc = [item.find(class_="short-desc").get_text() for item in items]
period_temp = [item.find(class_="temp").get_text() for item in items]
# print(period_name)
# print(period_desc)
# print(period_temp)


weather_stuff = pd.DataFrame(
    {"period name": period_name,
     "period description": period_desc,
     "period temp": period_temp
     }
)

print(weather_stuff)

weather_stuff.to_csv("result.csv")