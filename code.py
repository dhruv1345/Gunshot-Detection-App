import os
import librosa
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split

# Path to the dataset folder
dataset_dir = "C:\\Users\\gupta\\OneDrive\\Desktop\\ML_project_final\\All _sounds"

print("Test gun files:", len("C:\\Users\\gupta\\OneDrive\\Desktop\\ML_project_final\\All _sounds\\test\\gunshots"))
print("Test nongun files:", len("C:\\Users\\gupta\\OneDrive\\Desktop\\ML_project_final\\All _sounds\\test\\nongunshot"))
print("Train gun files:", len("C:\\Users\\gupta\\OneDrive\\Desktop\\ML_project_final\\All _sounds\\train\\gunshots"))
print("Train nongun files:", len("C:\\Users\\gupta\\OneDrive\\Desktop\\ML_project_final\\All _sounds\\train\\nongunshot"))



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

# print(labels)
print(len(labels))

# Convert to numpy array
X = np.array(flattened_features)
y = np.array(labels)

# Initialize and train a Random Forest model
rf = RandomForestClassifier(n_estimators=100, random_state=42)  # Adjust parameters as needed
rf.fit(X, y)

# Load and process the recorded audio

# import pyaudio
# import wave

# # Configure audio settings
# FORMAT = pyaudio.paInt16
# CHANNELS = 1  # Mono audio
# RATE = 44100  # Sample rate (samples per second)
# RECORD_SECONDS = 10  # Duration of recording in seconds
# OUTPUT_FILENAME = "recorded_audio.wav"  # Output file name

# # Initialize PyAudio
# audio = pyaudio.PyAudio()

# # Create an audio stream
# stream = audio.open(format=FORMAT, channels=CHANNELS, rate=RATE, input=True, frames_per_buffer=1024)

# print("Recording...")

# frames = []

# # Record audio for the specified duration
# for _ in range(0, int(RATE / 1024 * RECORD_SECONDS)):
#     data = stream.read(1024)
#     frames.append(data)

# print("Recording complete.")

# # Stop and close the audio stream
# stream.stop_stream()
# stream.close()

# # Terminate PyAudio
# audio.terminate()

# # Save the recorded audio as a .wav file
# with wave.open(OUTPUT_FILENAME, 'wb') as wf:
#     wf.setnchannels(CHANNELS)
#     wf.setsampwidth(audio.get_sample_size(FORMAT))
#     wf.setframerate(RATE)
#     wf.writeframes(b''.join(frames))

# print(f"Audio saved as {OUTPUT_FILENAME}")



# recorded_audio_path = "/content/drive/MyDrive/sounds/test/gunshots/gunshot 8 (71).wav"  
# recorded_audio_path = "C:\\Users\\gupta\\Downloads\\gunshot.wav"

recorded_audio_path = "C:\\Users\\gupta\\OneDrive\\Desktop\\ML_project_final\\song.wav"

# recorded_audio_path = "/content/drive/MyDrive/sounds/test/nongunshot/nongunshot 105029-7-2-9.wav"

recorded_mfccs = extract_mfcc(recorded_audio_path)



# Flatten the recorded audio features
recorded_mfcc_flattened = recorded_mfccs.flatten()



# Predict the label for the recorded audio
prediction = rf.predict([recorded_mfcc_flattened])

if prediction[0] == 1:
    print("The recorded audio is identified as a gunshot.")
else:
    print("The recorded audio is not identified as a gunshot.")
    
    