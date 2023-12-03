import pyrebase
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
path_on_cloud="Annotation Data/annotations.zip"
pathlocal="C:/Users/mazen/OneDrive/Documents/AUC/Thesis/Imagees/annotations.zip"
storage.child(path_on_cloud).put(pathlocal)