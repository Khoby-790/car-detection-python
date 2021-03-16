import cv2

car_image_source = "images/cars.png"

img = cv2.imread(car_image_source);

car_classifier = 'cars.xml'

gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# create trackers using classifiers using OpenCV
car_tracker = cv2.CascadeClassifier(car_classifier)


# detect cars
cars = car_tracker.detectMultiScale(gray_img)

# display the coordinates of different cars - multi dimensional array
print(cars)

# draw rectangle around the cars
for (x,y,w,h) in cars:
    cv2.rectangle(img, (x,y), (x+w, y+h), (0,255,0), 2)
    cv2.putText(img, 'Car', (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)


# Finally display the image with the markings
cv2.imshow('my detection',img)

# wait for the keystroke to exit
cv2.waitKey()