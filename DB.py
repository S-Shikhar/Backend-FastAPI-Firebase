import firebase_admin
from firebase_admin import credentials, db

cred = credentials.Certificate("fastapi-f1a2f-firebase-adminsdk-ywzue-59ff469fd9.json")  # Replace with the path to your service account JSON file
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://fastapi-f1a2f-default-rtdb.firebaseio.com/'  # Replace with your database URL
})

def get_db():
    return db
