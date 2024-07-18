# import tkinter as tk
# from tkinter import filedialog,messagebox
# from code_prediction import train_model, predict, send_sms, get_current_location, get_location_address
# from PIL import Image, ImageTk

# # Global variable to store the trained model
# rf_model = None

# # Twilio credentials and other settings
# account_sid = 'AC95bab185bcf9f84cdc53f08769f67f15'
# auth_token = '690d10d0b4846c4a510ec7a4f08cb413'
# twilio_phone_number = '+14436029264'
# your_phone_number = '+919958324711'
# google_maps_api_key = 'AIzaSyAatKDFob7NtGfNUY1YEyLndOVXsSLqnuY'



# def train_and_load_model():
#     global rf_model
    
#     # Create a Toplevel window for the dialog box
#     dialog_window = tk.Toplevel(window)
#     dialog_window.title("Training Model")

#     # Display a message in the dialog box
#     message_label = tk.Label(dialog_window, text="Training the model. Please wait...", font=("Times", 12))
#     message_label.pack(pady=20)

#     try:
#         # Train the model
#         rf_model = train_model()

#         # Display a success message in the dialog box
#         message_label.config(text="Model trained successfully!")
#     except Exception as e:
#         # Display an error message in the dialog box if training fails
#         message_label.config(text=f"Error during training: {str(e)}")

#     # Schedule the closing of the dialog box after 2000 milliseconds (2 seconds)
#     dialog_window.after(2000, dialog_window.destroy)

#     # Print a message in the console
#     print("Model trained.")

# def upload_and_predict():
#     if rf_model is None:
#         messagebox.showerror("Error", "Model not trained. Please train the model first.")
#         return

#     file_path = filedialog.askopenfilename(filetypes=[("WAV files", "*.wav")])
#     if file_path:
#         try:
#             prediction = predict(rf_model, file_path)
#             result_message = "Gunshot detected!" if prediction else "No gunshot detected!"
#             print("No Gunshot Detected!")

#             # Display a dialog box with the result
#             messagebox.showinfo("Prediction Result", result_message)

#             if prediction:
#                 # Gunshot detected, send SMS
#                 print("Gunshot detected. Sending SMS...")

#                 # Replace this with your actual location logic
#                 latitude, longitude = get_current_location()
#                 location_address = get_location_address(latitude, longitude)

#                 sms_message = f"Gunshot detected at {location_address} (Latitude: {latitude}, Longitude: {longitude})!"
#                 sms_sid = send_sms(sms_message, your_phone_number)

#                 # Display a dialog box with the SMS SID
#                 messagebox.showinfo("SMS Sent", f"SMS sent with SID displayed below")
#                 # print("SMS SID:", sms_sid)

#         except Exception as e:
#             messagebox.showerror("Error", f"Error predicting audio: {str(e)}")

# # Create the main window
# window = tk.Tk()
# window.title("ML Algorithm for Gunshot Detection")
# window.geometry("375x500") 

# # Add a label
# label = tk.Label(window, text="Gunshot Detection App", font=("Helvetica", 16))
# label.pack(pady=8)

# additional_text = tk.Label(window, text="Based on Signal Processing & Audio Analysis", font=("Times", 12))
# additional_text.pack(pady=(8), fill=tk.X)

# image_path = "C:\\Users\\gupta\\OneDrive\\Desktop\\ML_project_final\\jiit_image.png"  # Replace with the path to your PNG image
# img = tk.PhotoImage(file=image_path)
# img_label = tk.Label(window, image=img)
# img_label.pack(pady=8)


# # Button to train and load the model
# train_button = tk.Button(window, text="Train Model", command=train_and_load_model,bg="green", fg="white", padx=10, pady=5)
# train_button.pack(pady=(0,10))

# # Button to upload and predict
# predict_button = tk.Button(window, text="Upload and Predict", command=upload_and_predict,bg="green", fg="white", padx=10, pady=5)
# predict_button.pack(pady=5)

# additional_text = tk.Label(window, text="This project will help in reducing street crimes \n & to reduce time required to \n catch of culprits", font=("Times", 13))
# additional_text.pack(pady=(10), fill=tk.X)

# # Start the Tkinter event loop
# window.mainloop()



#code 2




# import tkinter as tk
# from tkinter import filedialog, messagebox
# from code_prediction import train_model, predict, send_sms, get_current_location, get_location_address
# from PIL import Image, ImageTk

# # Global variable to store the trained model
# rf_model = None

# # Twilio credentials and other settings
# account_sid = 'AC95bab185bcf9f84cdc53f08769f67f15'
# auth_token = '690d10d0b4846c4a510ec7a4f08cb413'
# twilio_phone_number = '+14436029264'
# your_phone_number = '+919958324711'
# google_maps_api_key = 'AIzaSyAatKDFob7NtGfNUY1YEyLndOVXsSLqnuY'

# def train_and_load_model():
#     global rf_model

#     # Create a Toplevel window for the dialog box
#     dialog_window = tk.Toplevel(window)
#     dialog_window.title("Training Model")

#     # Display a message in the dialog box
#     message_label = tk.Label(dialog_window, text="Training the model. Please wait...", font=("Times", 12))
#     message_label.pack(pady=20)

#     try:
#         # Train the model
#         rf_model = train_model()

#         # Display a success message in the dialog box
#         message_label.config(text="Model trained successfully!")
#     except Exception as e:
#         # Display an error message in the dialog box if training fails
#         message_label.config(text=f"Error during training: {str(e)}")

#     # Schedule the closing of the dialog box after 2000 milliseconds (2 seconds)
#     dialog_window.after(2000, dialog_window.destroy)

#     # Print a message in the console
#     print("Model trained.")

# def upload_and_predict(window):  # Pass window as an argument
#     global rf_model  # Make sure to use the global variable

#     if rf_model is None:
#         # If the model is not trained, train it first
#         try:
#             train_and_load_model()
#         except Exception as e:
#             messagebox.showerror("Error", f"Error training the model: {str(e)}")
#             return

#     # Continue with the prediction logic
#     file_path = filedialog.askopenfilename(filetypes=[("WAV files", "*.wav")])
#     if file_path:
#         try:
#             prediction = predict(rf_model, file_path)
#             result_message = "Gunshot detected!" if prediction else "No gunshot detected!"
#             print(result_message)

#             # Display a dialog box with the result
#             messagebox.showinfo("Prediction Result", result_message)

#             if prediction:
#                 # Gunshot detected, send SMS
#                 print("Gunshot detected. Sending SMS...")

#                 # Replace this with your actual location logic
#                 latitude, longitude = get_current_location()
#                 location_address = get_location_address(latitude, longitude)

#                 sms_message = f"Gunshot detected at {location_address} (Latitude: {latitude}, Longitude: {longitude})!"
#                 sms_sid = send_sms(sms_message, your_phone_number)

#                 # Display a dialog box with the SMS SID
#                 messagebox.showinfo("SMS Sent", f"SMS sent with SID displayed below")

#         except Exception as e:
#             messagebox.showerror("Error", f"Error predicting audio: {str(e)}")

# # Create the main window
# window = tk.Tk()
# window.title("ML Algorithm for Gunshot Detection")
# window.geometry("375x500") 

# # Add a label
# label = tk.Label(window, text="Gunshot Detection App", font=("Helvetica", 16))
# label.pack(pady=8)

# # Additional text labels, image, and buttons go here...
# additional_text = tk.Label(window, text="Based on Signal Processing & Audio Analysis", font=("Times", 12))
# additional_text.pack(pady=(8), fill=tk.X)

# image_path = "C:\\Users\\gupta\\OneDrive\\Desktop\\ML_project_final\\jiit_image.png"  # Replace with the path to your PNG image
# img = tk.PhotoImage(file=image_path)
# img_label = tk.Label(window, image=img)
# img_label.pack(pady=8)


# # Button to upload and predict
# predict_button = tk.Button(window, text="Upload and Predict", command=lambda: upload_and_predict(window), bg="green", fg="white", padx=10, pady=5)
# predict_button.pack(pady=5)

# additional_text = tk.Label(window, text="This project will help in reducing street crimes \n & to reduce time required to \n catch of culprits", font=("Times", 13))
# additional_text.pack(pady=(20), fill=tk.X)

# # Start the Tkinter event loop
# window.mainloop()


#code 3


# import tkinter as tk
# from tkinter import ttk,filedialog, messagebox
# from code_prediction import train_model, predict, send_sms, get_current_location, get_location_address
# from PIL import Image, ImageTk

# # Global variable to store the trained model
# rf_model = None

# account_sid = 'AC95bab185bcf9f84cdc53f08769f67f15'
# auth_token = '690d10d0b4846c4a510ec7a4f08cb413'
# twilio_phone_number = '+14436029264'
# your_phone_number = '+919958324711'
# google_maps_api_key = 'AIzaSyAatKDFob7NtGfNUY1YEyLndOVXsSLqnuY'

# def train_and_load_model():
#     global rf_model

#     # Create a Toplevel window for the dialog box
#     dialog_window = tk.Toplevel(window)
#     dialog_window.title("Training Model")

#     # Display a message in the dialog box
#     message_label = tk.Label(dialog_window, text="Training the model. Please wait...", font=("Times", 12))
#     message_label.pack(pady=20)

#     try:
#         # Train the model
#         rf_model = train_model()

#         # Display a success message in the dialog box
#         message_label.config(text="Model trained successfully!")
#     except Exception as e:
#         # Display an error message in the dialog box if training fails
#         message_label.config(text=f"Error during training: {str(e)}")

#     # Schedule the closing of the dialog box after 2000 milliseconds (2 seconds)
#     dialog_window.after(2000, dialog_window.destroy)

#     # Print a message in the console
#     print("Model trained.")

# def upload_and_predict():
#     global rf_model  # Make sure to use the global variable

#     # Continue with the audio file selection
#     file_path = filedialog.askopenfilename(filetypes=[("WAV files", "*.wav")])
#     if file_path:
#         try:
#             # Check if the model is trained, if not, train it
#             if rf_model is None:
#                 train_and_load_model()

#             # Predict using the trained model
#             prediction = predict(rf_model, file_path)
#             result_message = "Gunshot detected!" if prediction else "No gunshot detected!"
#             print(result_message)

#             # Display a dialog box with the result
#             messagebox.showinfo("Prediction Result", result_message)

#             if prediction:
#                 # Gunshot detected, send SMS
#                 print("Gunshot detected. Sending SMS...")

#                 # Replace this with your actual location logic
#                 latitude, longitude = get_current_location()
#                 location_address = get_location_address(latitude, longitude)

#                 sms_message = f"Gunshot detected at {location_address} (Latitude: {latitude}, Longitude: {longitude})!"
#                 sms_sid = send_sms(sms_message, your_phone_number)

#                 # Display a dialog box with the SMS SID
#                 messagebox.showinfo("SMS Sent", f"SMS sent with SID displayed below")

#         except Exception as e:
#             messagebox.showerror("Error", f"Error processing audio: {str(e)}")

# # Create the main window
# window = tk.Tk()
# window.title("ML Algorithm for Gunshot Detection")
# window.geometry("375x500") 

# # Add a label
# label = tk.Label(window, text="Gunshot Detection App", font=("Helvetica", 16))
# label.pack(pady=8)

# # Additional text labels, image, and buttons go here...
# additional_text = tk.Label(window, text="Based on Signal Processing & Audio Analysis", font=("Times", 12))
# additional_text.pack(pady=(8), fill=tk.X)

# image_path = "C:\\Users\\gupta\\OneDrive\\Desktop\\ML_project_final\\jiit_image.png"  # Replace with the path to your PNG image
# img = tk.PhotoImage(file=image_path)
# img_label = tk.Label(window, image=img)
# img_label.pack(pady=8)

# # Additional text labels, image, and buttons go here...

# # Button to upload and predict
# predict_button = tk.Button(window, text="Upload and Predict", command=upload_and_predict, bg="green", fg="white", padx=10, pady=5)
# predict_button.pack(pady=5)

# additional_text = tk.Label(window, text="This project will help in reducing street crimes \n & to reduce time required to \n catch of culprits", font=("Times", 13))
# additional_text.pack(pady=(20), fill=tk.X)

# # Start the Tkinter event loop
# window.mainloop()


# code 4


# import tkinter as tk
# from tkinter import ttk, filedialog, messagebox
# from code_prediction import train_model, predict, send_sms, get_current_location, get_location_address
# from PIL import Image, ImageTk

# # Global variable to store the trained model
# rf_model = None

# account_sid = 'AC95bab185bcf9f84cdc53f08769f67f15'
# auth_token = '690d10d0b4846c4a510ec7a4f08cb413'
# twilio_phone_number = '+14436029264'
# your_phone_number = '+919958324711'
# google_maps_api_key = 'AIzaSyAatKDFob7NtGfNUY1YEyLndOVXsSLqnuY'

# def train_and_load_model():
#     global rf_model

#     # Create a Toplevel window for the dialog box
#     dialog_window = tk.Toplevel(window)
#     dialog_window.title("Training Model")

#     # Display a message in the dialog box
#     message_label = tk.Label(dialog_window, text="Training the model. Please wait...", font=("Times", 12))
#     message_label.pack(pady=10)

#     # Add a progress bar for the loading animation
#     progress_bar = ttk.Progressbar(dialog_window, mode='indeterminate', length=200)
#     progress_bar.pack(pady=10)
#     progress_bar.start()

#     try:
#         # Train the model
#         rf_model = train_model()

#         # Display a success message in the dialog box
#         message_label.config(text="Model trained successfully!")
#     except Exception as e:
#         # Display an error message in the dialog box if training fails
#         message_label.config(text=f"Error during training: {str(e)}")

#     # Stop the progress bar
#     progress_bar.stop()

#     # Schedule the closing of the dialog box after 2000 milliseconds (2 seconds)
#     dialog_window.after(2000, dialog_window.destroy)

#     # Print a message in the console
#     print("Model trained.")

# def upload_and_predict():
#     global rf_model  # Make sure to use the global variable

#     # Continue with the audio file selection
#     file_path = filedialog.askopenfilename(filetypes=[("WAV files", "*.wav")])
#     if file_path:
#         try:
#             # Check if the model is trained, if not, train it
#             if rf_model is None:
#                 train_and_load_model()

#             # Predict using the trained model
#             prediction = predict(rf_model, file_path)
#             result_message = "Gunshot detected!" if prediction else "No gunshot detected!"
#             print(result_message)

#             # Display a dialog box with the result
#             messagebox.showinfo("Prediction Result", result_message)

#             if prediction:
#                 # Gunshot detected, send SMS
#                 print("Gunshot detected. Sending SMS...")

#                 # Replace this with your actual location logic
#                 latitude, longitude = get_current_location()
#                 location_address = get_location_address(latitude, longitude)

#                 sms_message = f"Gunshot detected at {location_address} (Latitude: {latitude}, Longitude: {longitude})!"
#                 sms_sid = send_sms(sms_message, your_phone_number)

#                 # Display a dialog box with the SMS SID
#                 messagebox.showinfo("SMS Sent", f"SMS sent with SID displayed below")

#         except Exception as e:
#             messagebox.showerror("Error", f"Error processing audio: {str(e)}")

# # Create the main window
# window = tk.Tk()
# window.title("ML Algorithm for Gunshot Detection")
# window.geometry("375x500") 

# # Add a label
# label = tk.Label(window, text="Gunshot Detection App", font=("Helvetica", 16))
# label.pack(pady=8)

# # Additional text labels, image, and buttons go here...
# additional_text = tk.Label(window, text="Based on Signal Processing & Audio Analysis", font=("Times", 12))
# additional_text.pack(pady=(8), fill=tk.X)

# image_path = "C:\\Users\\gupta\\OneDrive\\Desktop\\ML_project_final\\jiit_image.png"  # Replace with the path to your PNG image
# img = tk.PhotoImage(file=image_path)
# img_label = tk.Label(window, image=img)
# img_label.pack(pady=8)

# # Additional text labels, image, and buttons go here...

# # Button to upload and predict
# predict_button = tk.Button(window, text="Upload and Predict", command=upload_and_predict, bg="green", fg="white", padx=10, pady=5)
# predict_button.pack(pady=5)

# additional_text = tk.Label(window, text="This project will help in reducing street crimes \n & to reduce time required to \n catch of culprits", font=("Times", 13))
# additional_text.pack(pady=(20), fill=tk.X)

# # Start the Tkinter event loop
# window.mainloop()


#code 5


import tkinter as tk
from tkinter import ttk, filedialog, messagebox
from code_prediction import train_model, predict, send_sms, get_current_location, get_location_address
from PIL import Image, ImageTk
import webbrowser


# Global variable to store the trained model
rf_model = None


account_sid = 'AC95bab185bcf9f84cdc53f08769f67f15'
auth_token = '690d10d0b4846c4a510ec7a4f08cb413'
twilio_phone_number = '+16503380253'
your_phone_number = '+919958324711'
google_maps_api_key = 'AIzaSyAatKDFob7NtGfNUY1YEyLndOVXsSLqnuY'

def train_and_load_model():
    global rf_model

    # Create a Toplevel window for the dialog box
    dialog_window = tk.Toplevel(window)
    dialog_window.title("Training Model")

    # Display a message in the dialog box
    message_label = tk.Label(dialog_window, text="Training the model. Please wait...", font=("Times", 12))
    message_label.pack(pady=10)

    # Add a progress bar for the loading animation
    progress_bar = ttk.Progressbar(dialog_window, mode='indeterminate', length=200)
    progress_bar.pack(pady=10)
    progress_bar.start()

    try:
        # Train the model
        rf_model = train_model()

        # Display a success message in the dialog box
        message_label.config(text="Model trained successfully!")
    except Exception as e:
        # Display an error message in the dialog box if training fails
        message_label.config(text=f"Error during training: {str(e)}")

    # Force an update of the GUI
    dialog_window.update_idletasks()

    # Stop the progress bar
    progress_bar.stop()

    # Schedule the closing of the dialog box after 2000 milliseconds (2 seconds)
    dialog_window.after(2000, dialog_window.destroy)

    # Print a message in the console
    print("Model trained.")

def upload_and_predict():
    global rf_model  # Make sure to use the global variable

    # Continue with the audio file selection
    file_path = filedialog.askopenfilename(filetypes=[("WAV files", "*.wav")])
    if file_path:
        try:
            # Check if the model is trained, if not, train it
            if rf_model is None:
                train_and_load_model()

            # Predict using the trained model
            prediction = predict(rf_model, file_path)
            result_message = "Gunshot detected!" if prediction else "No gunshot detected!"
            print(result_message)

            # Display a dialog box with the result
            messagebox.showinfo("Prediction Result", result_message)

            if prediction:
                # Gunshot detected, send SMS
                print("Gunshot detected. Sending SMS...")

                # Replace this with your actual location logic
                latitude, longitude = get_current_location()
                location_address = get_location_address(latitude, longitude)

                sms_message = f"Gunshot detected at Jaypee Institute of Information Technology (Latitude: {latitude}, Longitude: {longitude})!"
                sms_sid = send_sms(sms_message, your_phone_number)

                # Display a dialog box with the SMS SID
                messagebox.showinfo("SMS Sent", f"SMS sent with SID displayed below")

        except Exception as e:
            messagebox.showerror("Error", f"Error processing audio: {str(e)}")


def open_colab_notebook():
    # Replace the URL with the link to your Google Colab notebook
    notebook_url = "https://colab.research.google.com/drive/1yEcGkBbHc6P_e_3MBe8BrXw37V2xa_eY?usp=sharing"
    webbrowser.open_new(notebook_url)

# Create the main window
window = tk.Tk()
window.title("ML Algorithm for Gunshot Detection")
window.geometry("375x500") 

# Add a label
label = tk.Label(window, text="Gunshot Detection App", font=("Helvetica", 16))
label.pack(pady=8)

# Additional text labels, image, and buttons go here...
additional_text = tk.Label(window, text="Based on Signal Processing & Audio Analysis", font=("Times", 12))
additional_text.pack(pady=(8), fill=tk.X)

image_path = "C:\\Users\\gupta\\OneDrive\\Desktop\\ML_project_final\\jiit_image.png"  # Replace with the path to your PNG image
img = tk.PhotoImage(file=image_path)
img_label = tk.Label(window, image=img)
img_label.pack(pady=5)

colab_button = tk.Button(window, text="Audio Features Plots", bg="green", fg="white", padx=10, pady=2,command=open_colab_notebook)
colab_button.pack(pady=5)

# Button to upload and predict
predict_button = tk.Button(window, text="Upload and Predict", command=upload_and_predict, bg="green", fg="white", padx=10, pady=5)
predict_button.pack(pady=5)

additional_text = tk.Label(window, text="This project will help in reducing street crimes \n & to reduce time required \n catching culprits", font=("Times", 12))
additional_text.pack(pady=(20), fill=tk.X)

window.mainloop()

# #code new

# import tkinter as tk
# from tkinter import ttk, filedialog, messagebox, simpledialog
# from code_prediction import train_model, predict, send_sms, get_current_location, get_location_address
# from PIL import Image, ImageTk

# # Global variable to store the trained model
# rf_model = None

# account_sid = 'AC95bab185bcf9f84cdc53f08769f67f15'
# auth_token = '690d10d0b4846c4a510ec7a4f08cb413'
# twilio_phone_number = '+14436029264'
# your_phone_number = '+919958324711'
# google_maps_api_key = 'AIzaSyAatKDFob7NtGfNUY1YEyLndOVXsSLqnuY'

# class AnalyzingDialog(simpledialog.Dialog):
#     def body(self, master):
#         tk.Label(master, text="Analyzing... Please wait.").pack()
#         return None

# def train_and_load_model():
#     global rf_model

#     # Display a dialog box with the "Analyzing..." message
#     # analyzing_dialog = simpledialog.Dialog(window, title="Analyzing", text="Analyzing... Please wait.")
    
#     analyzing_dialog = AnalyzingDialog(window, title="Analyzing")

#     # Train the model
#     try:
#         rf_model = train_model()

#         # Display a success message in the dialog box
#         analyzing_dialog.withdraw()  # Close the analyzing dialog
#         messagebox.showinfo("Model Trained", "Model trained successfully!")

#     except Exception as e:
#         # Display an error message in the dialog box if training fails
#         analyzing_dialog.withdraw()  # Close the analyzing dialog
#         messagebox.showerror("Error", f"Error during training: {str(e)}")

#     # Print a message in the console
#     print("Model trained.")

# def upload_and_predict():
#     global rf_model  # Make sure to use the global variable

#     # Continue with the audio file selection
#     file_path = filedialog.askopenfilename(filetypes=[("WAV files", "*.wav")])
#     if file_path:
#         try:
#             # Display a dialog box with the "Analyzing..." message
#             # analyzing_dialog = simpledialog.Dialog(window, title="Analyzing", text="Analyzing... Please wait.")
#             analyzing_dialog = AnalyzingDialog(window, title="Analyzing")

#             # Check if the model is trained, if not, train it
#             if rf_model is None:
#                 train_and_load_model()
#                 analyzing_dialog.withdraw()  # Close the analyzing dialog

#             # Predict using the trained model
#             prediction = predict(rf_model, file_path)
#             result_message = "Gunshot detected!" if prediction else "No gunshot detected!"
#             print(result_message)

#             # Display a dialog box with the result
#             messagebox.showinfo("Prediction Result", result_message)

#             if prediction:
#                 # Gunshot detected, send SMS
#                 print("Gunshot detected. Sending SMS...")

#                 # Replace this with your actual location logic
#                 latitude, longitude = get_current_location()
#                 location_address = get_location_address(latitude, longitude)

#                 sms_message = f"Gunshot detected at {location_address} (Latitude: {latitude}, Longitude: {longitude})!"
#                 sms_sid = send_sms(sms_message, your_phone_number)

#                 # Display a dialog box with the SMS SID
#                 messagebox.showinfo("SMS Sent", f"SMS sent with SID displayed below")

#         except Exception as e:
#             messagebox.showerror("Error", f"Error processing audio: {str(e)}")

# # Create the main window
# window = tk.Tk()
# window.title("ML Algorithm for Gunshot Detection")
# window.geometry("375x500") 

# # Add a label
# label = tk.Label(window, text="Gunshot Detection App", font=("Helvetica", 16))
# label.pack(pady=8)

# # Additional text labels, image, and buttons go here...
# additional_text = tk.Label(window, text="Based on Signal Processing & Audio Analysis", font=("Times", 12))
# additional_text.pack(pady=(8), fill=tk.X)

# image_path = "C:\\Users\\gupta\\OneDrive\\Desktop\\ML_project_final\\jiit_image.png"  # Replace with the path to your PNG image
# img = tk.PhotoImage(file=image_path)
# img_label = tk.Label(window, image=img)
# img_label.pack(pady=8)

# # Additional text labels, image, and buttons go here...

# # Button to upload and predict
# predict_button = tk.Button(window, text="Upload and Predict", command=upload_and_predict, bg="green", fg="white", padx=10, pady=5)
# predict_button.pack(pady=5)

# additional_text = tk.Label(window, text="This project will help in reducing street crimes \n & to reduce time required to \n catch culprits", font=("Times", 13))
# additional_text.pack(pady=(20), fill=tk.X)

# window.mainloop()