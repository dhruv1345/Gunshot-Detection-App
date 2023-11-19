from twilio.rest import Client
import geocoder
from ml_code import gunshot_detected

# Twilio credentials (replace with your own)
account_sid = 'AC95bab185bcf9f84cdc53f08769f67f15'
auth_token = '690d10d0b4846c4a510ec7a4f08cb413'
twilio_phone_number = '+14436029264'
your_phone_number = '+919958324711'

# Google Maps API key (replace with your own)
google_maps_api_key = 'AIzaSyAatKDFob7NtGfNUY1YEyLndOVXsSLqnuY'

def send_sms(message, phone_number):
    client = Client(account_sid, auth_token)

    message = client.messages.create(
        body=message,
        from_=twilio_phone_number,
        to=phone_number
    )

    print(f"SMS sent with SID: {message.sid}")

def get_current_location():
    # Use an IP geolocation service to get an approximate location
    location = geocoder.ip('me')

    # Extract latitude and longitude
    latitude, longitude = location.latlng

    return latitude, longitude

def get_location_address(latitude, longitude):
    # Use Google Maps API to get the location address
    g = geocoder.google([latitude, longitude], method='reverse', key=google_maps_api_key)
    return g.address

# Replace these values with your actual Twilio and Google Maps API credentials
account_sid = 'AC95bab185bcf9f84cdc53f08769f67f15'
auth_token = '690d10d0b4846c4a510ec7a4f08cb413'
twilio_phone_number = '+14436029264'
your_phone_number = '+919958324711'
google_maps_api_key = 'AIzaSyAatKDFob7NtGfNUY1YEyLndOVXsSLqnuY'

# Define a threshold for gunshot detection (replace with your actual detection logic)
# gunshot_detected = True

if gunshot_detected:
    # Get current location
    latitude, longitude = get_current_location()

    # Get location address
    location_address = get_location_address(latitude, longitude)

    # Send SMS with gunshot alert and location
    sms_message = f"Gunshot detected at {location_address} (Latitude: {latitude}, Longitude: {longitude})!"
    send_sms(sms_message, your_phone_number)
else:
    print("No gunshot detected.")
    latitude, longitude = get_current_location()

    # Get location address
    location_address = get_location_address(latitude, longitude)
    sms_message = f"No Gunshot detected at {location_address} (Latitude: {latitude}, Longitude: {longitude})!"
    send_sms(sms_message, your_phone_number)
