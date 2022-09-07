import folium
from geopy.geocoders import Nominatim
import json


def logins_to_map(data, m):
    for activity in data['account_activity']:
        geoloc= geolocator.geocode(activity["city"])
        long_lat = geoloc.latitude, geoloc.longitude
        color="green"
        if "Windows" in activity["user_agent"]:
            color = "blue"
        popup_text = activity["action"] + " by the following ip address:\n" + activity["ip_address"]
        folium.Marker(
            location=long_lat,
            popup=popup_text,
            icon=folium.Icon(color=color, icon='facebook', prefix='fa'),
        ).add_to(m)


if __name__ == '__main__':
    m = folium.Map(
        location=[50.89, 10.61],
        zoom_start=6,
    )
    germany = f"4_niedrig.geo.json"
    with open("loginsample.json", "r") as read_file:
        data = json.load(read_file)
    facebook_logins = f"/home/sve/Downloads/pg/loginsample.json"
    folium.GeoJson(germany, name="geojson").add_to(m)
    geolocator = Nominatim(user_agent="GeojsonPG")
    logins_to_map(data, m)
    m.save("index.html")



