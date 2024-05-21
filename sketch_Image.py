import cv2

imagePath = 'C:/Users/Pc/Downloads/Captain America.jpg'
image = cv2.imread(imagePath)
grey_img = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
invert = cv2.bitwise_not(grey_img)
blur = cv2.GaussianBlur(invert,(21,21),0)
interconverted = cv2.bitwise_not(blur)
sketch = cv2.divide(grey_img, interconverted, scale=256.0)


cv2.imwrite("sketch.png", sketch)