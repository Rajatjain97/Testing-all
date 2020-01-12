import cv2

cap = cv2.VideoCapture(0)

while True:
	face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_alt.xml")
	ret,frame = cap.read() # it returns 1. whether frame is captured, 2. and returns the captured frame
	gray_frame = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)


	if ret == False:
		continue

	faces = face_cascade.detectMultiScale(gray_frame,1.3,5)

	for (x,y,w,h) in faces:
		cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2)

	cv2.imshow('Video Frame',frame)
	# wait for user input - q then loop will stop

	key_pressed = cv2.waitKey(1) & 0xFF # waitKey waits for a pressed key
	if key_pressed == ord('q'):
		break

cap.release()
cv2.destroyAllWindows()