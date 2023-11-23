from geopy.geocoders import Nominatim

# Create a geolocator object
geolocator = Nominatim(user_agent="gunshot_detection_app")

# Example: Convert an address to coordinates (Geocoding)
location = geolocator.geocode("Example Street, City, Country")
print("Coordinates:", (location.latitude, location.longitude))

# Example: Convert coordinates to an address (Reverse Geocoding)
address = geolocator.reverse((location.latitude, location.longitude))
print("Address:", address.address)
