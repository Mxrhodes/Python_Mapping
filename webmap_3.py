# want to use the volcano txt file to generate markers fo map
import folium
import pandas as pd

#original map obj can stay put
map4 = folium.Map(location=[40.897934, -73.885948], zoom_start=15, tiles='Stamen Terrain')

# lets read the csv file into python, store it in variable df
df = pd.read_csv('Volcanoes.txt')

# create a for loop to use file data to creat markers
# we have 2 iterators in this loop, put in a zip function
# read as iterator, then where is df to 'grab; that iterators value
for lat,lon,name in zip(df['LAT'], df['LON'], df['NAME']):
    folium.Marker(location=[lat, lon], popup = name, icon = folium.Icon(icon = 'cloud')).add_to(map4)
    print("Complete")
print(map4.save('test4.html'))