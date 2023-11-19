import librosa
import librosa.display
import matplotlib.pyplot as plt
import numpy as np

# Load the gunshot sound (replace 'gunshot.wav' with your actual file)
gunshot_path = 'C:\\Users\\gupta\\OneDrive\\Desktop\\ML_project_final\\gunshot.wav'
y, sr = librosa.load(gunshot_path)

# Extract MFCC features
mfccs = librosa.feature.mfcc(y=y, sr=sr, n_mfcc=13)

# Display the MFCCs
plt.figure(figsize=(10, 4))
librosa.display.specshow(mfccs, x_axis='time')
plt.colorbar()
plt.title('MFCC Features of Gunshot Sound')
plt.xlabel('Time')
plt.ylabel('MFCC Coefficients')
plt.show()
