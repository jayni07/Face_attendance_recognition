import cv2
import face_recognition
import pickle
import os
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
from firebase_admin import storage

cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred, {
    'databaseURL': "https://faceattendancerealtime-bad92-default-rtdb.firebaseio.com/",
    'storageBucket': "faceattendancerealtime-bad92.appspot.com"
})

# importing student images in the list
folderPath = 'images'
PathList = os.listdir(folderPath)
print("Path List ", PathList)
imgList = []
studentIds = []
for path in PathList:
    imgList.append(cv2.imread(os.path.join(folderPath, path)))

    # to remove jpg from the image
    print(os.path.splitext(path)[0])
    studentIds.append(os.path.splitext(path)[0])

    fileName = f'{folderPath}/{path}'
    bucket = storage.bucket()
    blob = bucket.blob(fileName)
    blob.upload_from_filename(fileName)

print(studentIds)


def findEncodings(imagesList):
    encodeList = []
    for img in imagesList:
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        encode = face_recognition.face_encodings(img)[0]
        encodeList.append(encode)

    return encodeList


print("encoding started..... might take few minutes!")
encodeListKnown = findEncodings(imgList)
# Not working
print(encodeListKnown)
encodeListKnownIds = [encodeListKnown, studentIds]
print("encoding complete")

file = open("EncodeFile.p", 'wb')
pickle.dump(encodeListKnownIds, file)
file.close()
print("file saved")
