import time

import cv2

def video_processing():
    cap = cv2.VideoCapture(0)
    down_points = (640, 480)
    i = 0
    while True:
        ret, frame = cap.read()
        if not ret:
            break

        frame = cv2.resize(frame, down_points, interpolation=cv2.INTER_LINEAR)
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        gray = cv2.GaussianBlur(gray, (21, 21), 0)
        ret, thresh = cv2.threshold(gray, 80, 255, cv2.THRESH_BINARY_INV)

        contours, hierarchy = cv2.findContours(
            thresh,
            cv2.RETR_EXTERNAL,
            cv2.CHAIN_APPROX_SIMPLE
        )

        if len(contours) > 0:
            c = max(contours, key=cv2.contourArea)
            (x, y), r = cv2.minEnclosingCircle(c)
            
            x = int(x)
            y = int(y)
            center = (x, y)
            r=int(r)

            cv2.circle(frame, center, r, (0, 255, 0), 2)
            
            if x>w and y>h and x<640-w and y<480-h:
                
                frame[y-h:y+h, x-w:x+w] = img

            if x<=320:
                print("Слева")
            else:
                print("Справа")

        cv2.imshow('frame', frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

        time.sleep(0.1)
        i += 1

    cap.release()

img = cv2.imread("fly64.png")
w = img.shape[1]//2
h = img.shape[0]//2

if __name__ == '__main__':
    video_processing()

# cv2.waitKey(0)
# cv2.destroyAllWindows()