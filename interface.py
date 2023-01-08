import imageio.v2 as imageio
from fonction import *
from art import text2art, tprint, art 
from colorama import Fore
def printchoix():
 print(Fore.RED + '1)Print source code')
 print(Fore.RED + '2)Execute')
 print(Fore.RED + '3)Menu')
 print(Fore.GREEN + 'chosse correcte value:')
print(text2art("|Project Python|"))
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
          print(Fore.YELLOW +"--------------------------------------------------------------------")
          print(Fore.YELLOW +"import numpy as np\ndef image_noire(h,l):\n return  np.zeros((h,l))")
          print(Fore.YELLOW +"--------------------------------------------------------------------")
          menu()
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
          print(Fore.YELLOW +"--------------------------------------------------------------------")
          print(Fore.YELLOW +"import numpy as np\ndef image_blanch(h,l):\n return  np.ones((h,l))")
          print(Fore.YELLOW +"--------------------------------------------------------------------")
          menu()
        elif k__==2 :
#          x_=int(input("rentrer hauteur de photo"))
#          y_=int(input("rentrer largeur de photo"))
          immg=white_image()
          image = Image.fromarray(immg)
          image.show()
        elif k__==3:
          menu()
     elif k_==3:
       while(k__!=1 and k__!=2 and k__!=3):
        printchoix()
        k__=int(input())
        if k__==1:
         print(Fore.YELLOW +"--------------------------------------------------------------------")
         print(Fore.YELLOW +"def creerImgBlancNoir(h,l):\n base=np.zeros((h,l))\n for i in range(h):\n  for j in range(l):\n   base[i, j]=(i+j)%2\n return base")
         print(Fore.YELLOW +"--------------------------------------------------------------------")
         menu()
        elif k__==2:
#          x_=int(input("rentrer hauteur de photo"))
#          y_=int(input("rentrer largeur de photo"))
          immg=creerImgBlancNoir()
          image = Image.fromarray(immg)
          image.show()
        elif k__==3:
         menu()
     elif k_==4:
      while(k__!=1 and k__!=2 and k__!=3):
        printchoix()
        k__=int(input())
        if k__==1:
         print(Fore.YELLOW +"--------------------------------------------------------------------")
         print(Fore.YELLOW +"def negatif(nom_de_image,h,l):\n base=np.zeros((h,l))\n img=Image.open(nom_de_image)\n for i in range(h):\n    for j in range(l):\n     if img.getpixel((i,j))==0:\n      base[i,j]=1\n     else:   \n      base[i,j]=0\n return base")
         print(Fore.YELLOW +"--------------------------------------------------------------------")
         menu()
        elif k__==2:
          negative()
        elif k__==3:
         menu()
     elif k_==5:
      menu() 
  if k==3:
   while(k_!=1 and k_!=2 and k_!=3 and k_!=4 and k_!=5 ): 
     print(Fore.RED + '1)Question 13. Écrire une fonction inverser')
     print(Fore.RED + '2)Question 14. Écrire une fonction flipH')
     print(Fore.RED + '3)Question 15. Écrire une fonction poserV')
     print(Fore.RED + '4)Question 16. Écrire une fonction poserH')
     print(Fore.RED + '5)Menu')
     print(Fore.GREEN + 'chosse correcte value:')
     k_=int(input())
     if k_==1 :
      while(k__!=1 and k__!=2 and k__!=3):
        printchoix()
        k__=int(input())
        if k__==1:
         print(Fore.YELLOW +"--------------------------------------------------------------------")
         print(Fore.YELLOW +"def inverser(img):\n   hoteur = img.shape[0]\n   largeur = img.shape[1]\n   channels = img.shape[2]\n   size = (hoteur,largeur,channels)\n   newimg = np.zeros(size,np.uint8)\n   for x in range(0,hoteur):\n       for y in range(0,largeur):\n           for c in range(0,channels):\n              newimg[x,y,c] = 255 - img[x,y,c]\n   return newimg ")
         print(Fore.YELLOW +"--------------------------------------------------------------------")
         menu()
        elif k__==2:
         main()
        elif k__==3:
         menu()
     if k_==2 :
      while(k__!=1 and k__!=2 and k__!=3): 
       printchoix()
       k__=int(input())
       if k__==1:
        print(Fore.YELLOW +"--------------------------------------------------------------------")
        print(Fore.YELLOW +"def flipH(img):\n   Inputimg = cv.imread(img)\n   flipvertical = cv.flip(Inputimg,0)\n   cv.imwrite('flipverticale.jpg',flipvertical)")
        print(Fore.YELLOW +"--------------------------------------------------------------------")
        menu()
       elif k__==2:
         flipH()
       elif k__==3:
         menu()
     if k_==3 :
      while(k__!=1 and k__!=2 and k__!=3): 
       printchoix()
       k__=int(input())
       if k__==1:
        print(Fore.YELLOW +"--------------------------------------------------------------------")
        print(Fore.YELLOW +" def poserv(img1, img2):\n    hoteur1 = img1.shape[0]\n    largeur1 = img1.shape[1]\n    channels1= img1.shape[2]\n    hoteur2 = img2.shape[0]\n    largeur2 = img2.shape[1]\n    channels2 = img2.shape[2]\n     N = 10 \n    Nhoteur = hoteur1 + hoteur1 + N\n    if(largeur1 > largeur2):\n        Nlargeur = largeur1\n    else:\n        Nlargeur = largeur2\n    Nimage = np.zeros((Nhoteur,Nlargeur,channels1),np.uint8)\n    for x in( 0,hoteur1):\n        for y in (0,largeur1):\n            for c in (0,channels1):\n                Nimage[x,y,c]= img1[x,y,c]\n    for x in (0,hoteur2):\n        for y in (0,largeur2):\n            for c in (0,channels2):\n                Nimage[x,(hoteur1+N),c] = img2[x,y,c]\n    return Nimage")
        print(Fore.YELLOW +"--------------------------------------------------------------------")
        menu()
       elif k__==2:
         poserV()
       elif k__==3:
         menu()
     if k_==4:
      while(k__!=1 and k__!=2 and k__!=3): 
       printchoix()
       k__=int(input())
       if k__==1:
        print(Fore.YELLOW +"--------------------------------------------------------------------")
        print(Fore.YELLOW +"def poserv(img1, img2):\n    hoteur1 = img1.shape[0]\n    largeur1 = img1.shape[1]\n    channels1= img1.shape[2]\n    hoteur2 = img2.shape[0]\n    largeur2 = img2.shape[1]\n    channels2 = img2.shape[2]\n     N = 10 \n    Nhoteur = hoteur1 + hoteur1 + N\n    if(largeur1 > largeur2):\n        Nlargeur = largeur1\n    else:\n        Nlargeur = largeur2\n    Nimage = np.zeros((Nhoteur,Nlargeur,channels1),np.uint8)\n    for x in( 0,hoteur1):\n        for y in (0,largeur1):\n            for c in (0,channels1):\n                Nimage[x,y,c]= img1[x,y,c]\n    for x in (0,hoteur2):\n        for y in (0,largeur2):\n            for c in (0,channels2):\n                Nimage[x,(hoteur1+N),c] = img2[x,y,c]\n    return Nimage")
        print(Fore.YELLOW +"--------------------------------------------------------------------")
        menu()
       elif k__==2:
         main2()   
       elif k__==3:
         menu()
     elif k_==5:
      menu() 
  elif k==2:
   while(k_!=1 and k_!=2 and k_!=3 and k_!=4 and k_!=5): 
    print(Fore.RED + '1)Question 9. La luminance')
    print(Fore.RED + '2)Question 10.La contraste')
    print(Fore.RED + '3)Question 11.La profendeur')
    print(Fore.RED + '4)Question 12.La Matrice dune image')
    print(Fore.RED + '5)Menu')
    print(Fore.GREEN + 'chosse correcte value:')
    k_=int(input())
    if k_==3 :
     while(k__!=1 and k__!=2 and k__!=3):
      printchoix()
      k__=int(input())
      if k__==1:
       print(Fore.YELLOW +"--------------------------------------------------------------------")
       print(Fore.YELLOW +"def profondeur(img):\n    t2=array(ouvrirImage(img),dtype=int)\n    max=t2[0,0,0]\n    for i in range(len(t2)):\n        for j in range(len(t2[i])):\n            for z in range(len(t2[i,j])):\n                if t2[i,j,z]>max:\n                    max=t2[i,j,z]\n    return max")
       print(Fore.YELLOW +"--------------------------------------------------------------------")
       menu()
      elif k__==2:
       print(profondeur("test.jpg"))
      elif k__==3:
         menu()
    elif k_==1 : 
     while(k__!=1 and k__!=2 and k__!=3):
      printchoix()
      k__=int(input())
      if k__==1:
       print(Fore.YELLOW +"--------------------------------------------------------------------")
       print(Fore.YELLOW +"def luminance(img):\n    t = array(ouvrirImage(img), dtype=int)\n    s = 0\n    for i in range(len(t)):\n        for j in range(len(t[i])):\n            for z in range(len(t[i,j])):\n                s += t[i, j, z]\n    n=len(t[i,j])*len(t[i])\n    m=s/n\n    return m") 
       print(Fore.YELLOW +"--------------------------------------------------------------------")
       menu()
      elif k__==2:
       print(luminance("test.jpg"))
      elif k__==3:
         menu()
    elif k_==2 : 
     while(k__!=1 and k__!=2 and k__!=3):
      printchoix()    
      k__=int(input())
      if k__==1:
       print(Fore.YELLOW +"--------------------------------------------------------------------")
       print(Fore.YELLOW +"def constract(img):\n    t1 = array(ouvrirImage(img), dtype=int)\n    s1 = 0\n    m=luminance(img)\n    for i in range(len(t1)-1):\n        for j in range(len(t1[i])-1):\n            for z in range(len(t1[i, j])-1):\n                s1 = s1 + t1[i, j,z]**2 - 2*m*t1[i,j,z] + m**2\n    n = len(t1[i, j]) * len(t1[i])\n    res = s1 / n\n    return res")
       print(Fore.YELLOW +"--------------------------------------------------------------------")
       menu()
      elif k__==2:
       print(constract("test.jpg"))
      elif k__==3:
         menu()
    elif k_==4 : 
     while(k__!=1 and k__!=2 and k__!=3):
      printchoix()    
      k__=int(input())
      if k__==1:
       print(Fore.YELLOW +"--------------------------------------------------------------------")
       print(Fore.YELLOW +"def ouvrirImage(nom_de_image):\n    img=plt.imread(nom_de_image)\n    return img")
       print(Fore.YELLOW +"--------------------------------------------------------------------")
       menu()
      elif k__==2:
       print(ouvrirImage("test.jpg"))
      elif k__==3:
         menu()
    elif k__==5:
     menu()
  elif k==4:
   while(k_!=1 and k_!=2 and k_!=3 and k_!=4 and k_!=5): 
    print(Fore.RED + '1)Question 22')
    print(Fore.RED + '2)Question 23')
    print(Fore.RED + '3)Question 24 Ecrire une fonction initImageRGB')
    print(Fore.RED + '4)Question 25 Ecrire une fonction def symetrie')
    print(Fore.RED + '5)Question 26 Ecrire une fonction def grayscale')
    print(Fore.RED + '6)Menu')
    print(Fore.GREEN + 'chosse correcte value:')
    k_=int(input())
    if k_==1 : 
     while(k__!=1 and k__!=2 and k__!=3):
      printchoix()
      k__=int(input())    
      if k__==1 or k__==2 :
       print(Fore.YELLOW +"--------------------------------------------------------------------")
       print(Fore.YELLOW +"M[0][1][1]=50\n M[1][0][1]=255\n M[2][1][0]=25")
       print(Fore.YELLOW +"--------------------------------------------------------------------")
       menu()
      elif k__==3:
       menu()
    elif k_==2 :   
     while(k__!=1 and k__!=2 and k__!=3):
      printchoix()    
      k__=int(input())
      if k__==1 or k__==2 :
       print(Fore.YELLOW +"--------------------------------------------------------------------")
       print(Fore.YELLOW +"on sait que chaque pixel est représenté par 3 octets donc lea quantité de mémoire nécéssaire pour stocker cette image est:\n n*p*3 = 3*6*3 = 54o = 432 bits")
       print(Fore.YELLOW +"--------------------------------------------------------------------")
       menu()
      elif k__==3:
       menu()
    elif k_==3 :   
     while(k__!=1 and k__!=2 and k__!=3):
      printchoix()    
      k__=int(input())
      if k__==1  :
       print(Fore.YELLOW +"--------------------------------------------------------------------")
       print(Fore.YELLOW + "def initImageRGB(imageRGB):\n imageRGB = []\n for x in range(0, 3):\n imageRGB.append([])\n for y in range(0,6):\n  imageRGB[x].append([]) \n  for z in range(0,3):\n   i=randrange(0,255)\n   imageRGB[x][y].append(i)\n return imageRGB")
       print(Fore.YELLOW +"--------------------------------------------------------------------")
       menu()
      elif k__==2:
       print(initImageRGB("test.jpg"))
      elif k__==3:
       menu()
    elif k_==4: 
     while(k__!=1 and k__!=2 and k__!=3 and k__!=4):
      print(Fore.RED + '1)Print source code')
      print(Fore.RED + '2)Execute')
      print(Fore.RED + '3)Execution {horizontal}')
      print(Fore.RED + '4)menu')
      print(Fore.GREEN + 'chosse correcte value:')
      k__=int(input())
      if k__==1  :
       print(Fore.YELLOW +"--------------------------------------------------------------------")
       print(Fore.YELLOW+"Img = imageio.imread(cttm1.jpg).tolist()\nplt.figure()\nplt.imshow(Img)\nplt.show()\ndef Symetrie(Img):\n n=len(Img)\n p = len(Img[0])\n Z =[[0 for j in range(p)] for i in range(n)]\n for i in range(n):\n  for j in range(p):\n   Z[i][j]=Img[i][p-1-j]\n return Z\n==================\nfigurplSymetrie2(Img):\n n=len(Img)\n p = len(Img[0])\n Z =[[0 for j in range(p)] for i in range(n)]\n for i in range(n):\n  for j in range(p):\n   Z[i][j]=Img[n-1-i][j]\n  return Z")
       print(Fore.YELLOW +"--------------------------------------------------------------------")
       menu()
      elif k__==2:
       main3()
      elif k__==3:
       main4()
      elif k__==4:
       menu()
    elif k_==5 :   
     while(k__!=1 and k__!=2 and k__!=3):
      printchoix()    
      k__=int(input())
      if k__==1  :
       print(Fore.YELLOW +"--------------------------------------------------------------------")
       print(Fore.YELLOW + "def grayscale(imageRGB):\n GrayImg=[[0]*len(Img[0])\n for i in range(len(Img))]\n  for i in range(len(Img)):\n   for j in range(len(Img[0])):\nGrayImg[i][j]=(Img[i][j][2]+Img[i][j][0]+Img[i][j][1])//3")
       print(Fore.YELLOW +"--------------------------------------------------------------------")
       menu()
      elif k__==2:
       Img = imageio.imread("test.jpg").tolist()
       grayscale(Img)
      elif k__==3:
       menu()
    elif k_==6:
     menu()

menu()
