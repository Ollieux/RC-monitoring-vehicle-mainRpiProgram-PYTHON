import time
import cv2
import imutils
import numpy as np


if __name__ == '__main__':

    # fire_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'fire_detection.xml')
    fire_cascade = cv2.CascadeClassifier('fire_detection.xml')

    cap = cv2.VideoCapture(0)
    # cap = cv2.VideoCapture('http://192.168.1.31:8081/')

    _width = 320#176##240
    _height = 240#144##160

    cap.set(cv2.CAP_PROP_FRAME_WIDTH, _width)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, _height)

    # cap.set(cv2.CAP_PROP_FPS, 10)

    print("width: ", cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    print("height: ", cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    # print("fps: ", cap.get(cv2.CAP_PROP_FPS))

    # fps, st, frames_to_count, cnt = (0, 0, 30, 0)

    while(True):
        ret, frame = cap.read()

        # frame = cv2.resize(frame, (_width, _height))

        # frame = cv2.rotate(frame, cv2.ROTATE_90_CLOCKWISE)
        frame = cv2.rotate(frame, cv2.ROTATE_90_COUNTERCLOCKWISE)

        # frame = imutils.resize(frame, width=_width, height=_height)
        # frame = imutils.rotate_bound(frame, 90)
        # #frame = imutils.rotate(frame, 90)

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        fire = fire_cascade.detectMultiScale(gray, 1.3, 5)

        for (x, y, w, h) in fire:
            # cv2.rectangle(frame, (x - 20, y - 20),(x + w + 20, y + h + 20), (255, 0, 0), 2)
            cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)
            # roi_gray = gray[y:y + h, x:x + w]
            # roi_color = frame[y:y + h, x:x + w]
            print('fire is detected')

        #  print("fps: ", cap.get(cv2.CAP_PROP_FPS))
        # frame = cv2.putText(frame, 'FPS: ' + str(fps), (10, 40), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)
        cv2.imshow('frame', frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

        # if cnt == frames_to_count:
        #     try:
        #         fps = round(frames_to_count / (time.time() - st))
        #         st = time.time()
        #         cnt = 0
        #         print(fps)
        #     except:
        #         pass
        # cnt += 1

    cap.release()
    cv2.DestroyAllWindows()