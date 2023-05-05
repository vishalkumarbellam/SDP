import cv2

def captureFace():
    vc=cv2.VideoCapture(0)

    while True:

        ret,frame=vc.read()

        if ret:
            cv2.imshow("video",frame)

        if cv2.waitKey(1) & 0xFF ==ord('q'):
            break

    vc.release()
    cv2.destroyAllWindows