import pyrebase
import os
from zipfile import ZipFile 
import requests
import base64
import io
from PIL import Image
config = {
  "apiKey": "AIzaSyC35TZ5fCp_duJkk-CJZhFBWj5vOJUCew4",
  "authDomain": "parkar-2ab66.firebaseapp.com",
  "projectId": "parkar-2ab66",
  "storageBucket": "parkar-2ab66.appspot.com",
  "messagingSenderId": "636129511176",
  "appId": "1:636129511176:web:185a7c464ad450417c4ebd",
  "measurementId": "G-6G9GFZED38",
  "databaseURL": ""
}

firebase = pyrebase.initialize_app(config)
storage = firebase.storage()

path_on_cloud = "Annotation Data/annotations.zip"
storage.child(path_on_cloud).download("C:/Users/mazen/OneDrive/Documents/AUC/Thesis/Middleware/Roboflow Annotation","annotations.zip")
flag = True
while flag:
  if os.path.exists("C:/Users/mazen/OneDrive/Documents/AUC/Thesis/Middleware/annotations.zip"):
    print("FILES EXTRACTED Before")
    with ZipFile("C:/Users/mazen/OneDrive/Documents/AUC/Thesis/Middleware/annotations.zip", 'r') as zipObj:
      zipObj.extractall("C:/Users/mazen/OneDrive/Documents/AUC/Thesis/Middleware/Roboflow Annotation/extracted files")
      print("FILES EXTRACTED")
      flag = False

# ------------------------------------------------------------------------------------------------------------------------------

import os
for filename in os.listdir("C:/Users/mazen/OneDrive/Documents/AUC/Thesis/Middleware/Roboflow Annotation/extracted files/."):
    if filename.endswith(".jpg") or filename.endswith(".png"):
      print(filename)

      # Load Image with PIL
      image = Image.open("C:/Users/mazen/OneDrive/Documents/AUC/Thesis/Middleware/Roboflow Annotation/extracted files/"+filename).convert("RGB")

      # Convert to JPEG Buffer
      buffered = io.BytesIO()
      image.save(buffered, quality=90, format="JPEG")

      # Base 64 Encode
      img_str = base64.b64encode(buffered.getvalue())
      img_str = img_str.decode("ascii")



      # Construct the URL
      upload_url = "".join([
          "https://api.roboflow.com/dataset/uploading-test/upload",
          "?api_key=" + "WhB0ITMP8ShDnIGhvNad",
          "&name=" +str("C:/Users/mazen/OneDrive/Documents/AUC/Thesis/Middleware/Roboflow Annotation/extracted files/"+filename),
          "&split=train"
      ])

      # POST to the API
      r = requests.post(upload_url, data=img_str, headers={
          "Content-Type": "application/x-www-form-urlencoded"
      })

      # Output result
      print(r.json())

      img_id = r.json()['id']

      annotation_filename = os.path.splitext("C:/Users/mazen/OneDrive/Documents/AUC/Thesis/Middleware/Roboflow Annotation/extracted files/"+filename)[0]+'.txt'
      print(annotation_filename)

      # Read Annotation as String
      annotation_str = open(annotation_filename, "r").read()

      # Construct the URL
      upload_url = "".join([
          "https://api.roboflow.com/dataset/uploading-test/annotate/" + img_id,
          "?api_key=" + "WhB0ITMP8ShDnIGhvNad",
          "&name=", annotation_filename
      ])

      # POST to the API
      r = requests.post(upload_url, data=annotation_str, headers={
          "Content-Type": "text/plain"
      })

      # Output result
      print(r.json())



  

