from array import array
from PIL import Image
import matplotlib.pyplot as plt
import numpy as np
import cv2 as cv
#Q13

def inverser(img):
   hoteur = img.shape[0] ###image vide
   largeur = img.shape[1] ###image vide
   channels = img.shape[2] ###image vide
   size = (hoteur,largeur,channels)
   newimg = np.zeros(size,np.uint8)
   for x in range(0,hoteur):
       for y in range(0,largeur):
           for c in range(0,channels):
              newimg[x,y,c] = 255 - img[x,y,c]
   return newimg
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
 for i in range(h-1):
    for j in range(l-1):
     if img.getpixel((i,j))==0:
      base[i,j]=1
     else:   
      base[i,j]=0
 return base

def main():
   Inputimg = cv.imread("test.jpg")
   inverseimg = inverser(Inputimg)
   imgplot = plt.imshow(inverseimg)
   plt.show()
#############Q14
def flipH():
   Inputimg = cv.imread("test.jpg")
   flipvertical = cv.flip(Inputimg,0) ## 0 est verticale flip
   imgplot = plt.imshow(flipvertical)
   plt.show()
###Q15
def poserv(img1, img2):
    hoteur1 = img1.shape[0]
    largeur1 = img1.shape[1]
    channels1= img1.shape[2]
    hoteur2 = img2.shape[0]
    largeur2 = img2.shape[1]
    channels2 = img2.shape[2]
    N = 10 
    Nhoteur = hoteur1 + hoteur1 + N
    if(largeur1 > largeur2):
        Nlargeur = largeur1
    else:
        Nlargeur = largeur2
    Nimage = np.zeros((Nhoteur,Nlargeur,channels1),np.uint8)
    for x in( 0,hoteur1):
        for y in (0,largeur1):
            for c in (0,channels1):
                Nimage[x,y,c]= img1[x,y,c]
    for x in (0,hoteur2):
        for y in (0,largeur2):
            for c in (0,channels2):
                Nimage[x,(hoteur1+N),c] = img2[x,y,c]
    return Nimage
def main2():
    img1 = cv.imread("test.jpg")
    img2 = cv.imread("test.jpg")
    Nimage  = poserv(img1,img2)
    imgplot = plt.imshow(Nimage)
    plt.show()

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

######Q11
def profondeur(img):
    t2=ouvrirImage(img)
    max=t2[0,0,0]
    for i in range(len(t2)):
        for j in range(len(t2[i])):
            for z in range(len(t2[i,j])):
                if t2[i,j,z]>max:
                    max=t2[i,j,z]
    return max
############Q9:
def luminance(img):
    t = ouvrirImage(img) #ouvrirImage(img), retourne la matrice d'une image.
    s = 0
    for i in range(len(t)):
        for j in range(len(t[i])):
            for z in range(len(t[i,j])):
                s += t[i, j, z]
    n=len(t[i,j])*len(t[i]) #il s'agit d'une matrice carree,donc le nombre d'elemnt de la matrice est le nombre d'element de la sous liste multiplie par le nombre de liste.
    m=s/n #moyenne pour une matrice normale
    return m
###########Q10:
def constract(img):
    t1 = ouvrirImage(img)
    s1 = 0
    m=luminance(img)
    for i in range(len(t1)-1):
        for j in range(len(t1[i])-1):
            for z in range(len(t1[i, j])-1):
                s1 = s1 + t1[i, j,z]**2 - 2*m*t1[i,j,z] + m**2
    n = len(t1[i, j]) * len(t1[i]) #il s'agit d'une matrice carree,donc le nombre d'elemnt de la matrice est le nombre d'element de la sous liste multiplie par le nombre de liste
    res = s1 / n
    return res
########Q12
def ouvrirImage(nom_de_image):
    img=plt.imread(nom_de_image) 
    return img #retourne la matrice d'une image
