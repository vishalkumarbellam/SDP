import os
import cv2
import numpy as np
import torch
from facenet_pytorch import InceptionResnetV1

def capture_face(username):
    # Initialize the camera
    cap = cv2.VideoCapture(0)

    # Capture the face image
    while True:
        ret, frame = cap.read()
        cv2.imshow('Capture Face', frame)

        # Press 'q' to capture the face image
        if cv2.waitKey(1) & 0xFF == ord('q'):
            file_path = f'Captured-Faces/{username}/{username}_face_image.jpg'
            cv2.imwrite(file_path, frame)
            break

    # Release the camera and close the window
    cap.release()
    cv2.destroyAllWindows()

def detect_faces(image_path, face_cascade):
    # Load the face image
    face_image = cv2.imread(image_path)

    # Convert the image to grayscale
    gray = cv2.cvtColor(face_image, cv2.COLOR_BGR2GRAY)

    # Perform face detection
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

    if len(faces) == 0:
        print("No face found in the captured image!")
        return None

    # Extract the first face coordinates
    (x, y, w, h) = faces[0]

    # Extract the face region from the image
    face_roi = gray[y:y + h, x:x + w]

    return face_roi

def encode_face(face_roi, resnet_model):
    # Convert the grayscale face ROI to a 3-channel image
    face_roi_rgb = cv2.cvtColor(face_roi, cv2.COLOR_GRAY2RGB)

    # Resize the face ROI for face embedding
    face_roi_rgb = cv2.resize(face_roi_rgb, (160, 160))

    # Normalize the face ROI
    face_roi_rgb = (face_roi_rgb / 255.0 - 0.5) * 2.0

    # Transpose the dimensions of the face ROI array
    face_roi_rgb = np.transpose(face_roi_rgb, (2, 0, 1))

    # Generate face embeddings using FaceNet model
    face_encoding = resnet_model(torch.tensor(face_roi_rgb[np.newaxis, :, :, :]).float())

    return face_encoding.detach().numpy()

def match_faces(encoded_face, match_faces_folder, threshold=0.7):
    for filename in os.listdir(match_faces_folder):
        if filename.endswith('.npy'):
            match_face = np.load(os.path.join(match_faces_folder, filename))
            distance = np.linalg.norm(encoded_face - match_face)
            if distance < threshold:
                return True
    return False

def save_face_embedding(face_embedding, filename):
    # Save the face embedding to a file
    np.save(filename, face_embedding)

def save_face_image(face_image, filename):
    # Save the face image to a file
    cv2.imwrite(filename, face_image)

def main(userid):
    # Load the FaceNet model
    resnet_model = InceptionResnetV1(pretrained='vggface2').eval()

    # Load the Haar cascade classifier for face detection
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

    # Capture the face image

    user_folder = f'Captured-Faces/{userid}'

    if os.path.exists(user_folder):
        # User already exists, match the captured face with the stored faces
        print(f"Matching face for user: {userid}")
        capture_face(userid)
        matching_face_roi = detect_faces(f'{user_folder}/{userid}_face_image.jpg', face_cascade)
        if matching_face_roi is not None:
            matching_face = encode_face(matching_face_roi, resnet_model)
            if match_faces(matching_face, user_folder):
                return("Match found!")
            else:
                return("Match not found!")
    else:
        # New user, capture the face image and store it
        print(f"Capturing face for new user: {userid}")
        os.makedirs(user_folder)
        capture_face(userid)
        captured_face_roi = detect_faces(f'{user_folder}/{userid}_face_image.jpg', face_cascade)
        if captured_face_roi is not None:
            captured_face = encode_face(captured_face_roi, resnet_model)
            save_face_embedding(captured_face, f'{user_folder}/{userid}_captured_face_embedding.npy')
            save_face_image(captured_face_roi, f'{user_folder}/{userid}_captured_face_image.jpg')
        return ("New User Registered")