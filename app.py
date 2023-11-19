from flask import Flask, request, jsonify
import os
import librosa
import numpy as np
from sklearn.ensemble import RandomForestClassifier

app = Flask(__name__)

# Load your trained RandomForestClassifier model
model = RandomForestClassifier()

# Load the model weights from a file (replace 'your_model_weights.pkl' with your actual model file)
model.load('your_model_weights.pkl')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Get the audio data from the POST request
        audio_data = request.files['audio'].read()

        # Preprocess the audio data (you might need to adapt this based on your preprocessing logic)
        mfccs = extract_mfcc(audio_data)  # Replace with your actual preprocessing function

        # Make predictions using the loaded model
        prediction = model.predict(mfccs.reshape(1, -1))

        # Return the prediction as JSON
        return jsonify({'prediction': int(prediction[0])})

    except Exception as e:
        return jsonify({'error': str(e)})

if __name__ == '__main__':
    app.run(debug=True)
