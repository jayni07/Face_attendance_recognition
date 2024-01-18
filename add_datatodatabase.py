import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred, {
    'databaseURL': "https://faceattendancerealtime-bad92-default-rtdb.firebaseio.com/"
})

ref = db.reference('students')
data = {
    '100':
        {
            "Name": "Jayni Joshi",
            "Major": "CS",
            "Starting_year": "2021",
            "Total_attendance": 6,
            "Standing": "6",
            "Year": 2,
            "last_attendance_time": "2022-06-04 00:54:34"
        },
    '101':
        {
            "Name": "Shobhit Tomer",
            "Major": "CS",
            "Starting_year": "2021",
            "Total_attendance": 6,
            "Standing": "7",
            "Year": 2,
            "last_attendance_time": "2022-06-04 00:55:34"
        },
    '102':
        {
            "Name": "Tanikesh Sharma",
            "Major": "CS",
            "Starting_year": "2021",
            "Total_attendance": 7,
            "Standing": "3",
            "Year": 2,
            "last_attendance_time": "2022-06-04 00:56:34"
        },
    '103':
        {
            "Name": "Bhavya Jalap",
            "Major": "CS",
            "Starting_year": "2021",
            "Total_attendance": 7,
            "Standing": "3",
            "Year": 2,
            "last_attendance_time": "2022-06-04 00:56:34"
        }

}

for key, value in data.items():
    ref.child(key).set(value)
