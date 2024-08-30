# Face Recognition Attendance System

## Overview

The Face Recognition Attendance System is a Python-based application designed to streamline student attendance management. It integrates advanced facial detection and recognition algorithms to accurately identify students, ensuring an efficient and automated attendance process.

## Features

* Facial Detection & Recognition: Utilizes state-of-the-art algorithms to detect and recognize student faces with high accuracy.
* Real-time Attendance: Automatically logs student attendance in real-time upon successful recognition.
* Secure Data Storage: Uses Firebase for secure and scalable storage of attendance data.
* User-friendly Interface: Simple and intuitive interface for both administrators and students.

## Technologies Used

* Programming Language: Python
* Libraries: OpenCV, NumPy, dlib, face_recognition
* Database: Firebase Realtime Database
* Other Tools: Firebase Admin SDK

## How It Works

1. Capture & Store Faces: The system captures images of students’ faces and stores them as encodings in Firebase.
2. Real-time Recognition: When a student stands in front of the camera, the system detects and recognizes their face using the stored encodings.
3. Attendance Logging: Upon successful recognition, the student’s attendance is automatically logged in the Firebase Realtime Database.

## Future Enhancements

* Multi-camera Support: Expand the system to support multiple cameras across different locations.
* Attendance Reports: Generate detailed attendance reports for administrators.
* Mobile Integration: Develop a companion mobile app for students to view their attendance records.

## Contributors
* [Jayni Joshi](https://github.com/jayni07)
