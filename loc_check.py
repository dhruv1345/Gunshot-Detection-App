import geocoder

google_maps_api_key = 'AIzaSyAatKDFob7NtGfNUY1YEyLndOVXsSLqnuY'

def get_location_address(latitude, longitude):
    g = geocoder.google([latitude, longitude], method='reverse', key=google_maps_api_key)
    print(g)  # Print the complete reverse geocoding response
    return g.address

# Example usage
latitude = 37.422408
longitude = -122.084068
location_address = get_location_address(latitude, longitude)
print(f"Reverse geocoded address: {location_address}")
