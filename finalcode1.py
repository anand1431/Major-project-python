
import cv2
from matplotlib import pyplot as plt
path = r'C:\AI\apple.png' # Reading the image from the path
img = cv2.imread(path,cv2.IMREAD_UNCHANGED)
print('image_shape:',img.shape) #shape of original image
 
scale_percent = 200 #fixing scaling percent 
width = int(img.shape[1] * scale_percent / 100)  #scaling the width
height = int(img.shape[0] * scale_percent / 100) #scaling the height

dim = (width, height)#dimension of resized image
print(dim) 
# resize image
resized = cv2.resize(img, dim, interpolation = cv2.INTER_CUBIC) #upscaling using bicubic interpolation
print('Resized Dimensions : ',resized.shape)
plt.title('Original Img')  #title for original image
cv2.imshow("Original image",img)   #Plotting original image
plt.title('Resized Img')   #title for Resized image
cv2.imshow("Resized image", resized) #toshow the Resized image
cv2.waitKey(0) #display the window infinitely
cv2.destroyAllWindows() #destroyAllWindows() simply destroys all the windows we created