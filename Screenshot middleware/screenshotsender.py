import pyrebase
import os

# Configuration Key Necessary for Connection to Firebase Storage
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
# Connecting to Firebase Storage
firebase = pyrebase.initialize_app(config)
storage = firebase.storage()

# folder path
dir_path = r'C:/Users/mazen/OneDrive/Documents/AUC/Thesis/Middleware/Screenshot middleware/screenshots'
count = 0

# Iterate directory
for path in os.listdir(dir_path):
    # check if current path is a file
    if os.path.isfile(os.path.join(dir_path, path)):
        count += 1



print('File count:', count)


for fileCount in range(count):
  path_on_cloud=f"Number Plate Images/frame_{fileCount}.jpg"
  pathlocal=f"C:/Users/mazen/OneDrive/Documents/AUC/Thesis/Middleware/Screenshot middleware/screenshots/frame_{fileCount}.jpg"
  print(f"frame_{fileCount}.jpg")
  storage.child(path_on_cloud).put(pathlocal)
