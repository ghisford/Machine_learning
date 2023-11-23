import requests
import tkinter as tk
from tkinter import filedialog

# Set the API endpoint URL
url = 'https://predict-cqs4o8zwng-km.a.run.app/predict'

# Create a function to select a video file
def select_video_file():
    root = tk.Tk()
    root.withdraw()  # Hides the root window

    # Prompt the user to select a video file
    file_path = filedialog.askopenfilename(filetypes=[("Video Files", "*.mp4")])

    return file_path

# Get the path to the video file
video_path = select_video_file()

# Open the video file binary and send it a request
with open(video_path, 'rb') as file:
    response = requests.post(url, files={'file': file}, verify=False)

# Print the response from the API
print(response.content)
