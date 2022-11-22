from PIL import Image
import matplotlib.pyplot as plt
import numpy as np

#Q4
def image_noire(h,l):                                                                
 return  np.zeros((h,l))
#Q5
def image_blanch(h,l):                                                                
 return  np.ones((h,l))
#print image fonction
def AfficherImg(img):
 plt.axis("off")
 plt.imshow(img, interpolation="nearest")
 plt.show()
################ Sauvgarder une image sous forme jpg ou bmp
def saveImage(img):
 plt.imsave("image1.png",img)
####### transforme une matrice en image
def array_img(np_array):
  image = Image.open("image_.png") #creer un fichier .png 
  np_array = np.array(image)
  pil_image=Image.fromarray(np_array)
  pil_image.show()
