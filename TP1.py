#Exo cours 

#Exercice4

'''def fonction(c,n):
    return c*n
print(fonction('c',8))'''

#Exercice 5

'''def fonction(c,d,n,m):
    return c*n + d*m
print(fonction('c','d',8,8))'''

#Exercice 6
1.
def fonction(ch,n):
    if n=0:
    for i in range(n):
        print(ch)
    else:
        print("n doit être suprérieur") 
2.
def fonction(ch,n):
    if n>0:
        for i in range(1,n+1):
            print(f"{i}.{ch}")
    else:
    
        print("n doit être suprérieur")
fonction(12,8)#Ceci est un exemple
#Exercice 7

def fonction(c,n):
    if n>0:
        for i in range(1,n+1):
            print(c * i)
    else:
    
        print("n doit être suprérieur")
fonction("c",5)#Ceci est un exemple
#Exercice 8

def premiere_occ(ch,c):
    if len(ch):
        k=0
        for i in range(len(ch)):
            if ch[i]== c:
                k=k+1
        return k
    else: 
        return "valeur vide"
print(premiere_occ('abfvghsjvvvv','v')) #Ceci est un exemple

#Exercice 9

def nb_occurence(ch,c):
    if len(ch):
        k=0
        for i in range(len(ch)):
            if ch[i]== c:
                k=k+1
        return k
    else: 
        return "valeur vide"
print(nb_occurence('abfvghsjvvvv','v'))

#Exercice 10

def sous_chaine(ch1,ch2):
    if ch1 in ch2:
        return True 
    else:
        return False
print(sous_chaine("hi","hibro"))

#Exercice 11
1.
ch = ''
for = k in range (1,5) :
    if k % 2 == 1: #this exercice isn't finish

#Exercice 12
1. 
def triple_six(ch):
    return "666" in ch
print(triple_six("aaaa666666ad"))
2.
def triple_six_exact(ch):
    n=len(ch)
    if ch[0:3]=="666" and (n<=3 or ch[3]!="6"):
        return True
    elif ch[n-3:n]=="666" and ch[n-3]!= "6":
        return True
    for k in range (1,n-3):
        if ch[k:k+3]=="666" and ch[k-1]!= 6 and ch[k+3]!= 6:
            return True
    return False
print(triple_six_exact("aaaa666666ad"))

#Exercice 13

2.
def mirroir2(ch):
    inv=''
    for e in ch:
        inv = e+inv
    return inv
def palindrome(ch):
    return ch == mirroir2(ch)
print (palindrome('kayak'))

3.1

def supprimer_espaces(chaine):
    return chaine.replace(" ", "")

# Exemple d'utilisation
texte = "Ceci est un texte avec des espaces"
texte_sans_espaces = supprimer_espaces(texte)
print(texte_sans_espaces)  # Output: Ceciestuntexteavecdesespaces

3.2

def supprimer_espaces(ch):
    return ch.replace(" ", "")

# Exemple d'utilisation
texte = "et la marine va venir a malte"
texte_sans_espaces = supprimer_espaces(texte)
print(texte_sans_espaces)  
def mirroir2(texte_sans_espaces):
    inv=''
    for e in texte_sans_espaces:
        inv = e+inv
    return inv
def palindrome(texte_sans_espaces):
    return texte_sans_espaces == mirroir2(texte_sans_espaces)
print (palindrome(texte_sans_espaces)
