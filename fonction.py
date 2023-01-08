from random import randrange
from array import array
from PIL import Image
import matplotlib.pyplot as plt
import numpy as np
from numpy import *
import cv2 as cv
from PIL import ImageFilter
import imageio.v2 as imageio
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
def main():
    img1 = cv.imread("test.jpg")
    Nimage  = inverser(img1)
    imgplot = plt.imshow(Nimage)
    plt.show()
#Q4
def image_noire(h,l):                                                                
 return  np.zeros((h,l))
#Q5
def white_image():
 img = np.zeros([100,100,3],dtype=np.uint8)
 img.fill(255) 
 return img
#Q6
def creerImgBlancNoir():
   base=white_image()
   for i in range(len(base)):
    for j in range(len(base[i])):
     base[i,j]=(i+j)%2
   return base
#Q7
def negative(): 
 img = Image.open("index.jpg");
 img.show()
 for i in range(0, img.size[0]-1):
    for j in range(0, img.size[1]-1):
        pixelColorVals = img.getpixel((i,j));
        redPixel    = 255 - pixelColorVals[0]; # Negate red pixel
        greenPixel  = 255 - pixelColorVals[1]; # Negate green pixel
        bluePixel   = 255 - pixelColorVals[2]; # Negate blue pixel
        img.putpixel((i,j),(redPixel, greenPixel, bluePixel))
 img.show()
#############Q14
def flipH():
   Inputimg = cv.imread("test.jpg")
   flipvertical = cv.flip(Inputimg,0) ## 0 est verticale flip
   imgplot = plt.imshow(flipvertical)
   plt.show()
###Q15
def poserV():
 img1=cv.imread("lion.jpeg")
 img2=cv.imread("lolaa.jpeg")
 imgV = Image(img1.shape[0] + img2.shape[0], img1.shape[1], img1.shape[2])
 for i in range(img1.shape[0]):
  for j in range(img1.shape[1]):
   imgV.m[i, j] = img1.m[i, j]
 for i in range(img2.shape[0]):
  for j in range(img2.shape[1]):
   imgV.m[img1.shape[1] + i, j] = img2.m[i, j]
 imgplot = plt.imshow(imgV)
 imgv.show()


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

#####Q24:
def initImageRGB(imageRGB):
      imageRGB = []
      for x in range(0,3):
             imageRGB.append([])
             for y in range(0,6):
                   imageRGB[x].append([])
                   for z in range(0,3):
                         i=randrange(0,255)
                         imageRGB[x][y].append(i)
      return imageRGB
######Q26
def grayscale(Img):
        GrayImg=[[0]*len(Img[0]) for i in range(len(Img))]#initialiser la matrice 2D en 0
        for i in range(len(Img)):
              for j in range(len(Img[0])):
                    GrayImg[i][j]=(Img[i][j][2]+Img[i][j][0]+Img[i][j][1])//3 #implémenter la mztrice avec la moyenne de chaque pixel
        arr = array(GrayImg, dtype=uint8)
        new_image = Image.fromarray(arr) #convertir la matrice en image
        plt.axis("off")
        plt.imshow(new_image, cmap = "gray")
        plt.show()
######Q27
def Symetrie(Img):
#*Renvoie une image symétrique de Img par un axe vertical
     n=len(Img)  # nombre de lignes dans Ing
     p = len(Img[0])  # nombre de colonnes dans Ing
     Z =[[0 for j in range(p)] for i in range(n)]  # Z la matrice nulle
     for i in range(n):
            for j in range(p):
                  Z[i][j]=Img[i][p-1-j]
     return Z
def main3():
 Img = imageio.imread("index.jpg").tolist()
 plt.figure()
 plt.imshow(Img)
 plt.show()
 k=Symetrie(Img)
 plt.figure()
 plt.imshow(k)
 plt.show()
def Symetrie2(Img):
#*Renvoie une image symétrique de Img par un axe horizontale
     n=len(Img)  # nombre de lignes dans Ing
     p = len(Img[0])  # nombre de colonnes dans Ing
     Z =[[0 for j in range(p)] for i in range(n)]  # Z la matrice nulle
     for i in range(n):
            for j in range(p):
                  Z[i][j]=Img[n-1-i][j]
     return Z
def main4(): 
 Img = imageio.imread("index.jpg").tolist()
 plt.figure()
 plt.imshow(Img)
 plt.show()  
 k=Symetrie2(Img)
 plt.figure()
 plt.imshow(k)
 plt.show()  
              
