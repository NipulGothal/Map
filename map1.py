import folium
import pandas as pd


df= pd.read_csv("val.txt")
#print(df)
lat = list(df["LAT"])
lon= list(df["LON"])
eal =list(df["ELEV"])

def color_change(el):
   if el<1000:
      return "green"
   elif 1000<= el <3000 :
      return "blue"
   else :
      return "red"
   
map=folium.Map(location=[80,-180],zoom_start=3,tiles="Mapbox Bright")#lag= -90 to 90 / long= -180 to 180
fgv=folium.FeatureGroup(name="Volcanoes")

for la,ln,el in zip(lat,lon,eal):
   fgv.add_child(folium.Marker(location=[la,ln],popup=str(el)+"m",tooltip="click on it"))#input(enter the name)/,icon=folium.Icon(color=color_change(el)

fgg=folium.FeatureGroup(name="Population")

   
fgg.add_child(folium.GeoJson(data=open('world.json','r',encoding='utf-8-sig').read(),
style_function=lambda x:{'fillColor':'blue' if x['properties']['POP2005']<10000000
else 'green' if 10000000 <= x['properties']['POP2005']<20000000 else 'red'}))



   
map.add_child(fgv)
map.add_child(fgg)
#map.add_child(folium.LayerControl())
map.save("maprr.html")
