import phonenumbers,sys
import opencage
import folium
import get_num
from opencage.geocoder import OpenCageGeocode
from phonenumbers import geocoder,carrier

if len(sys.argv) == 2:
    number = sys.argv[1]
else:
    number = get_num.num

try:
    pepnumber = phonenumbers.parse(number,"PH")
    location = geocoder.description_for_number(pepnumber,"en")
    print(location)
    service_pro = phonenumbers.parse(number)
    print(carrier.name_for_number(service_pro,"en"))
except phonenumbers.phonenumberutil.NumberParseException as e:
    sys.exit(f"Error parsing phone number: {e}")

key = '7e924ecafb434c0d907f37432d04608b'

geocoder = OpenCageGeocode(key)
query = str(location)
results = geocoder.geocode(query)

try:
    latitude = results[0]["geometry"]["lat"]
    longitude = results[0]["geometry"]["lng"]
except IndexError:
    sys.exit("Cannot find PhoneNumber in the map")

print(latitude,longitude)

mymap = folium.Map(location=[latitude,longitude],zoom_start=9)
folium.Marker([latitude,longitude],popup=location).add_to(mymap)

mymap.save("location.html")

