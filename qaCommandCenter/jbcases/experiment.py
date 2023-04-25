# # import module
# from PIL import Image, ImageChops
#
# # assign images
# img1 = Image.open("1.jpg")
# img2 = Image.open("2.jpg")
#
# # finding difference
# diff = ImageChops.difference(img1, img2)
#
# # showing the difference
# diff.show()

import cv2

# load images
image1 = cv2.imread("test1.png")
image2 = cv2.imread("test2.png")

# compute difference
difference = cv2.subtract(image1, image2)

# color the mask red
Conv_hsv_Gray = cv2.cvtColor(difference, cv2.COLOR_BGR2GRAY)
ret, mask = cv2.threshold(Conv_hsv_Gray, 0, 255,cv2.THRESH_BINARY_INV |cv2.THRESH_OTSU)
difference[mask != 255] = [0, 0, 255]

# add the red mask to the images to make the differences obvious
image1[mask != 255] = [0, 0, 255]
image2[mask != 255] = [0, 0, 255]

# store images
cv2.imwrite('diffOverImage1.png', image1)
cv2.imwrite('diffOverImage2.png', image1)
cv2.imwrite('diff.png', difference)