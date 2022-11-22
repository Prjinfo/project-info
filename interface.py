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
          os.remove("image_.png")
          image = Image.new('RGB', (x_,y_))
          image.save("image_.png", "PNG")
          array_img(immg)
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
          os.remove("image_.png")
          image = Image.new('RGB', (x_,y_))
          image.save("image_.png", "PNG")
          array_img(immg)
        elif k__==3:
          menu()
menu()
