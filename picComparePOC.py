import cv2
import imutils
from imgcompare import is_equal, image_diff_percent

#get the images you want to compare.
original = cv2.imread("1.jpg")
new = cv2.imread("2.jpg")
#resize the images to make them small in size. A bigger size image may take a significant time
#more computing power and time
original = imutils.resize(original, height = 600)
new = imutils.resize(new, height = 600)

#create a copy of original image so that we can store the
#difference of 2 images in the same on
diff = original.copy()
cv2.absdiff(original, new, diff)

# converting the difference into grayscale images
gray = cv2.cvtColor(diff, cv2.COLOR_BGR2GRAY)

# increasing the size of differences after that we can capture them all
for i in range(0, 3):
    dilated = cv2.dilate(gray.copy(), None, iterations=i + 1)


(T, thresh) = cv2.threshold(dilated, 3, 255, cv2.THRESH_BINARY)

# now we have to find contours in the binarized image
cnts = cv2.findContours(thresh, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
cnts = imutils.grab_contours(cnts)


for c in cnts:
    # nicely fiting a bounding box to the contour
    (x, y, w, h) = cv2.boundingRect(c)
    cv2.rectangle(new, (x, y), (x + w, y + h), (0, 255, 0), 2)

    # remove comments from below 2 lines if you want to
    # for viewing the image press any key to continue
    # simply write the identified changes to the disk
cv2.imwrite("testchanges.png", new)

is_same = is_equal('test1.png', 'test2.png', tolerance=32)
percentage = image_diff_percent('test1.png', 'test2.png')
print(is_same)
print(percentage)