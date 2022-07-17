import cv2
cap = cv2.VideoCapture(1)
cap.set(3,1366) # you can set here the window size
cap.set(4,768)
while True:
    success, img = cap.read()
    cv2.imshow('camera', img)
    if cv2.waitKey(10) == ord('q'):
        break # press 'Q' key to close the window
cv2.waitKey(1)
