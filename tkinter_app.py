import tkinter as tk
from tkinter import filedialog,messagebox
from code_prediction import train_model, predict, send_sms, get_current_location, get_location_address
from PIL import Image, ImageTk

# Global variable to store the trained model
rf_model = None

# Twilio credentials and other settings
account_sid = 'AC95bab185bcf9f84cdc53f08769f67f15'
auth_token = '690d10d0b4846c4a510ec7a4f08cb413'
twilio_phone_number = '+14436029264'
your_phone_number = '+919958324711'
google_maps_api_key = 'AIzaSyAatKDFob7NtGfNUY1YEyLndOVXsSLqnuY'

# def train_and_load_model():
#     global rf_model
#     # Train the model and load it into the global variable
#     rf_model = train_model()
#     print("Model trained and loaded.")

def train_and_load_model():
    global rf_model
    
    # Create a Toplevel window for the dialog box
    dialog_window = tk.Toplevel(window)
    dialog_window.title("Training Model")

    # Display a message in the dialog box
    message_label = tk.Label(dialog_window, text="Training the model. Please wait...", font=("Times", 12))
    message_label.pack(pady=20)

    try:
        # Train the model
        rf_model = train_model()

        # Display a success message in the dialog box
        message_label.config(text="Model trained successfully!")
    except Exception as e:
        # Display an error message in the dialog box if training fails
        message_label.config(text=f"Error during training: {str(e)}")

    # Schedule the closing of the dialog box after 2000 milliseconds (2 seconds)
    dialog_window.after(2000, dialog_window.destroy)

    # Print a message in the console
    print("Model trained.")

def upload_and_predict():
    if rf_model is None:
        messagebox.showerror("Error", "Model not trained. Please train the model first.")
        return

    file_path = filedialog.askopenfilename(filetypes=[("WAV files", "*.wav")])
    if file_path:
        try:
            prediction = predict(rf_model, file_path)
            result_message = "Gunshot detected!" if prediction else "No gunshot detected."

            # Display a dialog box with the result
            messagebox.showinfo("Prediction Result", result_message)

            if prediction:
                # Gunshot detected, send SMS
                print("Gunshot detected. Sending SMS...")

                # Replace this with your actual location logic
                latitude, longitude = get_current_location()
                location_address = get_location_address(latitude, longitude)

                sms_message = f"Gunshot detected at {location_address} (Latitude: {latitude}, Longitude: {longitude})!"
                sms_sid = send_sms(sms_message, your_phone_number)

                # Display a dialog box with the SMS SID
                messagebox.showinfo("SMS Sent", f"SMS sent with SID displayed below")
                # print("SMS SID:", sms_sid)

        except Exception as e:
            messagebox.showerror("Error", f"Error predicting audio: {str(e)}")

# Create the main window
window = tk.Tk()
window.title("ML Algorithm for Gunshot Detection")
window.geometry("375x500") 

# Add a label
label = tk.Label(window, text="Gunshot Detection App", font=("Helvetica", 16))
label.pack(pady=8)

additional_text = tk.Label(window, text="Based on Signal Processing & Audio Analysis", font=("Times", 12))
additional_text.pack(pady=(8), fill=tk.X)

image_path = "C:\\Users\\gupta\\OneDrive\\Desktop\\ML_project_final\\jiit_image.png"  # Replace with the path to your PNG image
img = tk.PhotoImage(file=image_path)
img_label = tk.Label(window, image=img)
img_label.pack(pady=8)


# Button to train and load the model
train_button = tk.Button(window, text="Train Model", command=train_and_load_model,bg="green", fg="white", padx=10, pady=5)
train_button.pack(pady=(0,10))

# Button to upload and predict
predict_button = tk.Button(window, text="Upload and Predict", command=upload_and_predict,bg="green", fg="white", padx=10, pady=5)
predict_button.pack(pady=5)

additional_text = tk.Label(window, text="This project will help in reducing street crimes \n & to reduce time required to \n catch of culprits", font=("Times", 13))
additional_text.pack(pady=(10), fill=tk.X)

# Start the Tkinter event loop
window.mainloop()
