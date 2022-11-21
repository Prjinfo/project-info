from art import text2art, tprint, art 
from colorama import Fore
print(text2art("|TP Python|"))
k=k_=k__=0
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
        print(Fore.RED + '1)Execute')
        print(Fore.GREEN + 'chosse correcte value:')
        k__=int(input())
