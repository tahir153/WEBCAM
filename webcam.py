import cv2
cap = cv2.VideoCapture(0)
while True:
    success, img = cap.read()
    cv2.imshow('camera', img)
    if cv2.waitKey(10) == ord('q'):
        break
cv2.waitKey(1)