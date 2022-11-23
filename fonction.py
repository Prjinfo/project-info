from PIL import Image
import matplotlib.pyplot as plt
import numpy as np

#Q4
def image_noire(h,l):                                                                
 return  np.zeros((h,l))
#Q5
def image_blanch(h,l):                                                                
 return  np.ones((h,l))
#Q6
def creerImgBlancNoir(h,l):
   base=np.zeros((h,l))
   for i in range(h):
    for j in range(l):
     base[i, j]=(i+j)%2
   return base
#Q7
def negatif(nom_de_image,h,l):
 base=np.zeros((h,l))
 img=Image.open(nom_de_image)
 for i in range(h):
    for j in range(l):
     if img.getpixel((i,j))==0:
      base[i,j]=1
     else:   
      base[i,j]=0
 return base

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
################# Ouvrir une image jpg ou bmp on retourne une matrice
def ouvrirImage(nom_de_image):
 img=plt.imread(nom_de_image)
 return img
