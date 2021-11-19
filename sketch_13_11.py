import cv2

# function to display image
def display(img):
    cv2.imshow("Image", img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


img = cv2.imread(".\gandhiji.jpg")
# 1. convert image to grayscale
gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# 2. invert the image
inverted_img = 255-gray_img

# 3. apply gaussian blur
blur_image = cv2.GaussianBlur(inverted_img, (121,221), 0)

# 4. sketch
sketch = cv2.divide(blur_image, inverted_img, scale=256.0)
display(sketch)