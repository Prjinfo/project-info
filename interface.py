import matplotlib.pyplot as plt
from art import text2art, tprint, art 
from colorama import Fore
import numpy as np
def image_noire(h,l):                                                                
 return  np.zeros((h,l))

def AfficherImg(img):
 plt.axis("off")
 plt.imshow(img, interpolation="nearest")
 plt.show()

print(text2art("|TP Python|"))
x_=y_=k=k_=k__=0
while (k !=1 and k!=2 and k!=3 and k!=4):
 print(Fore.RED + '1)Partie 1')
 print(Fore.RED + '2)Partie 2')
 print(Fore.RED + '3)Partie 3')
 print(Fore.RED + '4)Partie 4')
 print(Fore.GREEN + 'chosse correcte value:')
 k=int(input())
 if k==1 :
   while(k_!=1 and k_!=2 and k_!=3 and k_!=4): 
     print(Fore.RED + '1)Question 4. Créer une image noir')
     print(Fore.RED + '2)Question 5. Créer une image blanche')
     print(Fore.RED + '3)Question 6. Créer une image noir et blanc')
     print(Fore.RED + '4)Question 7. Négatif')
     print(Fore.GREEN + 'chosse correcte value:')
     k_=int(input())
     if k_==1 :
      while(k__!=1 and k__!=2):
        print(Fore.RED + '1)Print source code')
        print(Fore.RED + '2)Execute')
        print(Fore.GREEN + 'chosse correcte value:')
        k__=int(input())
        if k__==1:
          print(Fore.YELLOW +"import numpy as np\ndef image_noire(h,l):\n return  np.zeros((h,l))")
        else :
          x_:int(input("rentrer hauteur de photo"))
          y_:int(input("rentrer largeur de photo"))
          immg=image_noire(x_,y_)
          AfficherImg(immg)
