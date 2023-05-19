import cv2
import face_recognition as fr

def captureFace():
    vc=cv2.VideoCapture(0)

    processFrame=True

    while True:

        ret,frame=vc.read()

        if ret:
            
            if processFrame:

                small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)

                rgb_small_frame = small_frame[:, :, ::-1]
        
                face_locations = fr.face_locations(rgb_small_frame)
                face_encodings = fr.face_encodings(rgb_small_frame, face_locations)

                return face_encodings
        
        else:
            print("camera not found")

        if cv2.waitKey(1) & 0xFF ==ord('q'):
            break

    vc.release()
    cv2.destroyAllWindows

captureFace()