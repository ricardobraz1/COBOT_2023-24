import cv2

video = cv2.VideoCapture()

ip = "http://10.224.1.5:8080/video"

video.open(ip)

while True:
    check, img = video.read()
    cv2.imshow("img", img)
    cv2.waitKey(1)