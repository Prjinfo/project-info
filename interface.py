from fonction import *
from art import text2art, tprint, art 
from colorama import Fore
import os
def printchoix():
 print(Fore.RED + '1)Print source code')
 print(Fore.RED + '2)Execute')
 print(Fore.RED + '3)Menu')
 print(Fore.GREEN + 'chosse correcte value:')
print(text2art("|TP Python|"))
def menu():
 x_=y_=k=k_=k__=0
 while (k !=1 and k!=2 and k!=3 and k!=4):
  print(Fore.RED + '1)Partie 1')
  print(Fore.RED + '2)Partie 2')
  print(Fore.RED + '3)Partie 3')
  print(Fore.RED + '4)Partie 4')
  print(Fore.GREEN + 'chosse correcte value:')
  k=int(input())
  if k==1 :
   while(k_!=1 and k_!=2 and k_!=3 and k_!=4 and k_!=5): 
     print(Fore.RED + '1)Question 4. Créer une image noir')
     print(Fore.RED + '2)Question 5. Créer une image blanche')
     print(Fore.RED + '3)Question 6. Créer une image noir et blanc')
     print(Fore.RED + '4)Question 7. Négatif')
     print(Fore.RED + '5)Menu')
     print(Fore.GREEN + 'chosse correcte value:')
     k_=int(input())
     if k_==1 :
      while(k__!=1 and k__!=2 and k__!=3):
        printchoix()
        k__=int(input())
        if k__==1:
          print(Fore.YELLOW +"import numpy as np\ndef image_noire(h,l):\n return  np.zeros((h,l))")
        elif k__==2 :
          x_=int(input("rentrer hauteur de photo"))
          y_=int(input("rentrer largeur de photo"))
          immg=image_noire(x_,y_)
          image = Image.fromarray(immg)
          image.show()
        elif k__==3:
          menu()
     elif k_==2:
       while(k__!=1 and k__!=2 and k__!=3):
        printchoix()
        k__=int(input())
        if k__==1:
          print(Fore.YELLOW +"import numpy as np\ndef image_blanch(h,l):\n return  np.ones((h,l))")
        elif k__==2 :
          x_=int(input("rentrer hauteur de photo"))
          y_=int(input("rentrer largeur de photo"))
          immg=image_blanch(x_,y_)
          image = Image.fromarray(immg)
          image.show()
        elif k__==3:
          menu()
     elif k_==3:
       while(k__!=1 and k__!=2 and k__!=3):
        printchoix()
        k__=int(input())
        if k__==1:
         print(Fore.YELLOW +"def creerImgBlancNoir(h,l):\n base=np.zeros((h,l))\n for i in range(h):\n  for j in range(l):\n   base[i, j]=(i+j)%2\n return base")
        elif k__==2:
          x_=int(input("rentrer hauteur de photo"))
          y_=int(input("rentrer largeur de photo"))
          immg=creerImgBlancNoir(x_,y_)
          image = Image.fromarray(immg)
          image.show()
        elif k__==3:
         menu()
     elif k_==4:
      while(k__!=1 and k__!=2 and k__!=3):
        printchoix()
        k__=int(input())
        if k__==1:
         print(Fore.YELLOW +"def negatif(nom_de_image,h,l):\n base=np.zeros((h,l))\n img=Image.open(nom_de_image)\n for i in range(h):\n    for j in range(l):\n     if img.getpixel((i,j))==0:\n      base[i,j]=1\n     else:   \n      base[i,j]=0\n return base")
        elif k__==2:
          x_=int(input("rentrer hauteur de photo"))
          y_=int(input("rentrer largeur de photo"))
          immg=negatif("image_.png",x_,y_)
          image = Image.fromarray(immg)
          image.show()
        elif k__==3:
         menu()
     elif k_==5:
      menu() 
  if k==3:
   while(k_!=1 and k_!=2 and k_!=3 and k_!=4): 
     print(Fore.RED + '1)Question 13. Écrire une fonction inverser')
     print(Fore.RED + '2)Question 14. Écrire une fonction flipH')
     print(Fore.RED + '3)Question 15. Écrire une fonction poserH')
     print(Fore.RED + '4)Menu')
     print(Fore.GREEN + 'chosse correcte value:')
     k_=int(input())
     if k_==1 :
      while(k__!=1 and k__!=2 and k__!=3):
        printchoix()
        k__=int(input())
        if k__==1:
         print(Fore.YELLOW +"def inverser(img):\n   hoteur = img.shape[0]\n   largeur = img.shape[1]\n   channels = img.shape[2]\n   size = (hoteur,largeur,channels)\n   newimg = np.zeros(size,np.uint8)\n   for x in range(0,hoteur):\n       for y in range(0,largeur):\n           for c in range(0,channels):\n              newimg[x,y,c] = 255 - img[x,y,c]\n   return newimg ")
        elif k__==2:
         main()
        elif k__=3
         menu()

menu()
      
