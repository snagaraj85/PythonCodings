import face_recognition
import cv2
import numpy as np

# This is a super simple (but slow) example of running face recognition on live video from your webcam.
# There's a second example that's a little more complicated but runs faster.

# PLEASE NOTE: This example requires OpenCV (the `cv2` library) to be installed only to read from your webcam.
# OpenCV is *not* required to use the face_recognition library. It's only required if you want to run this
# specific demo. If you have trouble installing it, try any of the other demos that don't require it instead.

# Get a reference to webcam #0 (the default one)
video_capture = cv2.VideoCapture(0)

# Load a sample picture and learn how to recognize it.
rajan_image = face_recognition.load_image_file("images/Rajan.jpg")
rajan_face_encoding = face_recognition.face_encodings(rajan_image)[0]

# Load a second sample picture and learn how to recognize it.
renuka_image = face_recognition.load_image_file("images/Renuka.jpg")
renuka_face_encoding = face_recognition.face_encodings(renuka_image)[0]

# Load a third sample picture and learn how to recognize it.
rudhraesh_image = face_recognition.load_image_file("images/Rudhraesh.jpg")
rudhraesh_face_encoding = face_recognition.face_encodings(rudhraesh_image)[0]

# Load a third sample picture and learn how to recognize it.
ganesan_image = face_recognition.load_image_file("images/Ganesan.jpg")
ganesan_face_encoding = face_recognition.face_encodings(ganesan_image)[0]

# Load a third sample picture and learn how to recognize it.
usha_image = face_recognition.load_image_file("images/Usha.jpg")
usha_face_encoding = face_recognition.face_encodings(usha_image)[0]

# Load a third sample picture and learn how to recognize it.
aarthi_image = face_recognition.load_image_file("images/Aarthi.jpg")
aarthi_face_encoding = face_recognition.face_encodings(aarthi_image)[0]

# Load a third sample picture and learn how to recognize it.
sarvaesh_image = face_recognition.load_image_file("images/Sarvaesh.jpg")
sarvaesh_face_encoding = face_recognition.face_encodings(sarvaesh_image)[0]

# Load a third sample picture and learn how to recognize it.
balaji_image = face_recognition.load_image_file("images/Balaji.jpg")
balaji_face_encoding = face_recognition.face_encodings(balaji_image)[0]

# Create arrays of known face encodings and their names
known_face_encodings = [
    rajan_face_encoding,
    renuka_face_encoding,
    rudhraesh_face_encoding,
    ganesan_face_encoding,
    usha_face_encoding,
    aarthi_face_encoding,
    sarvaesh_face_encoding,
    balaji_face_encoding
    ]
known_face_names = [
    "Rajan",
    "Renuka",
    "Rudhraesh",
    "Ganesan",
    "Usha",
    "Aarthi",
    "Sarvaesh"
    "Balaji"
]

while True:
    # Grab a single frame of video
    ret, frame = video_capture.read()

    # Convert the image from BGR color (which OpenCV uses) to RGB color (which face_recognition uses)
    rgb_frame = frame[:, :, ::-1]

    # Find all the faces and face enqcodings in the frame of video
    face_locations = face_recognition.face_locations(rgb_frame)
    face_encodings = face_recognition.face_encodings(rgb_frame, face_locations)

    # Loop through each face in this frame of video
    for (top, right, bottom, left), face_encoding in zip(face_locations, face_encodings):
        # See if the face is a match for the known face(s)
        matches = face_recognition.compare_faces(known_face_encodings, face_encoding)

        name = "Unknown"

        # If a match was found in known_face_encodings, just use the first one.
        # if True in matches:
        #     first_match_index = matches.index(True)
        #     name = known_face_names[first_match_index]

        # Or instead, use the known face with the smallest distance to the new face
        face_distances = face_recognition.face_distance(known_face_encodings, face_encoding)
        best_match_index = np.argmin(face_distances)
        if matches[best_match_index]:
            name = known_face_names[best_match_index]

        # Draw a box around the face
        cv2.rectangle(frame, (left + 10, top + 10), (right + 10, bottom + 10), (0, 0, 255), 2)

        # Draw a label with a name below the face
        cv2.rectangle(frame, (left + 15, bottom - 20), (right, bottom), (0, 0, 255), cv2.FILLED)
        font = cv2.FONT_HERSHEY_DUPLEX
        cv2.putText(frame, name, (left + 20, bottom - 5), font, 0.5, (255, 255, 255), 1)

    # Display the resulting image
    cv2.imshow('Video', frame)

    # Hit 'q' on the keyboard to quit!
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release handle to the webcam
video_capture.release()
cv2.destroyAllWindows()
