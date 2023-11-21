import os
import librosa
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from twilio.rest import Client
import geocoder

# Twilio credentials
account_sid = 'AC95bab185bcf9f84cdc53f08769f67f15'
auth_token = '690d10d0b4846c4a510ec7a4f08cb413'
twilio_phone_number = '+14436029264'
your_phone_number = '+919958324711'
google_maps_api_key = 'AIzaSyAatKDFob7NtGfNUY1YEyLndOVXsSLqnuY'

# Initialize and train a Random Forest model
def train_model():
    # Path to the dataset folder
    dataset_dir = "C:\\Users\\gupta\\OneDrive\\Desktop\\ML_project_final\\All _sounds"

    # Load the dataset of gunshot sounds and extract MFCC features
    features = []
    labels = []

    for folder in ["train", "test"]:
        for label in ["gunshots", "nongunshot"]:
            label_folder = os.path.join(dataset_dir, folder, label)
            for filename in os.listdir(label_folder):
                if filename.endswith(".wav"):
                    file_path = os.path.join(label_folder, filename)
                    mfccs = extract_mfcc(file_path)
                    features.append(mfccs)
                    labels.append(0 if "nongunshot" in filename else 1)  # Assign 1 to gunshot and 0 to non-gunshot

    # Flatten the features for the Random Forest classifier
    flattened_features = [mfcc.flatten() for mfcc in features]

    # Convert to numpy array
    X = np.array(flattened_features)
    y = np.array(labels)

    # Initialize and train a Random Forest model
    rf = RandomForestClassifier(n_estimators=100, random_state=42)  # Adjust parameters as needed
    rf.fit(X, y)

    return rf

# Function to extract MFCC features from an audio file
def extract_mfcc(audio_path):
    audio, sample_rate = librosa.load(audio_path)
    fixed_length = 2 * sample_rate  # Adjust as needed
    if len(audio) < fixed_length:
        audio = np.pad(audio, (0, fixed_length - len(audio)))
    else:
        audio = audio[:fixed_length]

    mfccs = librosa.feature.mfcc(y=audio, sr=sample_rate, n_mfcc=13)
    return mfccs.T

# Function to predict the label for the recorded audio
def predict(rf, recorded_audio_path):
    recorded_mfccs = extract_mfcc(recorded_audio_path)

    # Flatten the recorded audio features
    recorded_mfcc_flattened = recorded_mfccs.flatten()

    # Predict the label for the recorded audio
    prediction = rf.predict([recorded_mfcc_flattened])

    return prediction[0] == 1  # Return True if it's a gunshot, False otherwise

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

# Define a threshold for gunshot detection (replace with your actual detection logic)
def main():
    # Train the model
    rf_model = train_model()

    # Example audio path
    recorded_audio_path = "C:\\Users\\gupta\\OneDrive\\Desktop\\ML_project_final\\song.wav"

    # Predict
    gunshot_detected = predict(rf_model, recorded_audio_path)

    if gunshot_detected:
        print("Gunshot detected and SMS generated.")
        latitude, longitude = get_current_location()
        location_address = get_location_address(latitude, longitude)
        sms_message = f"Gunshot detected at Jaypee Institute of Information Technology (Latitude: {latitude}, Longitude: {longitude})!"
        send_sms(sms_message, your_phone_number)
    else:
        print("No gunshot detected and SMS generated.")
        latitude, longitude = get_current_location()
        location_address = get_location_address(latitude, longitude)
        sms_message = f"No Gunshot detected at Jaypee Institute of Information Technology (Latitude: {latitude}, Longitude: {longitude})!"
        send_sms(sms_message, your_phone_number)

if __name__ == "__main__":
    main()
