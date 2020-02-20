#Helping to create OpenMaps in Python
import folium
#Help to read data in Python
import pandas

#Reading a text file containing the data's of volcanoes present in USA
data = pandas.read_csv("Volcanoes_USA.txt")

#Making a list of lat and lon of the points
lat =  list(data["LAT"])
lon = list(data["LON"])

#Making the list to find the elevation of the volcanoes
elev = list(data["ELEV"])

#Creating a map object which starts from a particular point with zoom of 6
map = folium.Map(location = [20,-123],zoom_start = 6)

#Creating two feature group one for population and one for Volcanoes

fgpoint = folium.FeatureGroup(name = "My Map with Volcano Point")
fglayer = folium.FeatureGroup(name = "My Map with Population")

#iterating through the list
for lt,ln,el in zip(lat,lon,elev):
    if el < 1000:
        marker = "red"
        fgpoint.add_child(folium.CircleMarker(location = [lt,ln],radius = 6,popup = str(el)+"m", fill_color = marker, color = 'grey',fill_opacity=0.7))
    elif el > 1000 and el < 2000:
        marker = "cadetblue"
        fgpoint.add_child(folium.CircleMarker(location = [lt,ln],radius = 6,popup = str(el)+"m",fill_color = marker, color = 'grey',fill_opacity=0.7))
    else:
        marker = "orange"
        fgpoint.add_child(folium.CircleMarker(location = [lt,ln],radius = 6,popup = str(el)+"m",fill_color = marker, color = 'grey',fill_opacity=0.7 ))

fglayer.add_child(folium.GeoJson(data = (open("world.json", "r", encoding = "utf-8-sig").read()),
style_function = lambda x: {"fillColor":"green" if x["properties"]["POP2005"] < 10000000 else "orange" if 10000000 <= x["properties"]["POP2005"] < 20000000 else "red"}))


map.add_child(fgpoint)
map.add_child(fglayer)
map.add_child(folium.LayerControl())
map.save("Map1.html")
