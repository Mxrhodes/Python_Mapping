import folium

#Create the map object
map = folium.Map(location=[40.897934, -73.885948], zoom_start=7)
print(map)

#Need html file out of this obj - to create a map
# look in the Map method dir to see all avail methods to Map

print(map.save('test.html'))
#Look under your files for the surprise
# rt click on html file and open in browser

# change zoom to 15 and tiles = 'Stame Terrain' and recreate the html file

map2 = folium.Map(location=[40.897934, -73.885948], zoom_start=15, tiles ='Stamen Terrain')
print(map2)
print(map2.save('test2.html'))