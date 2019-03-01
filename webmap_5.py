# cleaning our code by adding a function
import folium
import pandas as pd

map4 = folium.Map(location=[40.897934, -73.885948], zoom_start=15, tiles='Stamen Terrain')
df = pd.read_csv('Volcanoes.txt')

def color(elev):
    if elev in range(0,1000):
        col = 'green'
    elif elev in range(1000, 1999):
        col = 'blue'
    elif elev in range(2000, 2999):
        col = 'orange'
    else:
        col = 'red'
    return col

for lat,lon,name,elev in zip(df['LAT'], df['LON'], df['NAME'], df['ELEV']):
    folium.Marker(location=[lat, lon], popup=name, icon = folium.Icon(color = color(elev), icon = 'cloud')).add_to(map4)
print(map4.save('test6.html'))
