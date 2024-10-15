#Exercice 6
1.
def est_isocele(a,b,c):
    if(a==b or b==c or a==c):
        return (True)
    else:
        return (False)
print(est_isocele(3,4,5)) #Ceci est un exemple


2.
def est_rectange(a,b,c):
    if(a+b==c):
        return (True)
    else:
        return (False)
print(est_rectange(3,4,5)) #Ceci est un exemple


#Exercice 7
def lpp(a,b):
    if a>b:
        return b 
    else:
        return a 
print (lpp(0,9)) #Ceci est un exemple


#Exercice 8
def valeur_absolue(x):
    if x<0:
        return x*(-1)
    else:
        return x
print (valeur_absolue(-182)) #Ceci est un exemple


#Exercice 9
def est_entier(x):
    if x==(int) :
        return (True)
    else:
        return (False)
print (est_entier(4.28)) #Ceci est un exemple


#Exercice 10
def est_pair(n):
    if n%2==0:
        return True
    else:
        return False
print(est_pair(0)) #Ceci est un exemple


#Exercice 11
1.
def intervalle1(x):
    if x>-2 and x<=3:
        return (True)
    else:
        return (False)
print(intervalle1(9)) #Ceci est un exemple
print(intervalle1(-9)) #Ceci est un exemple
print(intervalle1(-1)) #Ceci est un exemple
print(intervalle1(2)) #Ceci est un exemple


#Exercice 12
def signe(x):
    if x>0:
        return 'positif'
    elif x<0:
        return 'negatif'
    else:
        return 'nul'
    
print(signe(-7)) #Ceci est un exemple


#Exercice 13
def est_bissextile(n):
    if((n%4==0 and n%100!=0)or(n%400==0)):
        return True
    else:
        return False
print(est_bissextile(2400)) #Ceci est un exemple

#Exercice 14

def prout(S):
    S=0
    for i in range(1,10):
        S=S+i**2
    return S 
print(prout(4))

#Exercice 15

def somme_puissance_trois(n):
    S = 0
    for i in range(4,n+1):
        S = S+3**i
    return S
print (somme_puissance_trois(7)) #Ceci est un exemple 

#Exercice 16

def sigma(n,p):
    S=0
    for k in range (1,n+1):
        S=S+k**p 
    return S 
print (sigma(2,3)) #Ceci est un exemple

#Exercice 17
1.
def mult_7(n):
    S=0
    for i in range(1,n+1):
        if i%7==0:
            S=S+1
    return S
print(mult_7(31)) #Ceci est un exemple
2.
def mult_7pas_3_5(n):
    S=0
    for i in range(1,n+1):
        if i%7==0 and i%5!=0 and i%3!=0:
            S=S+1
    return S
print(mult_7pas_3_5(31)) #Ceci est un exemple 

#Exercice 18

def est_parfait(n):
    sum=0
    for i in range (1,n+1):
        if n%i==0:
            sum += i
    return sum == 2*n 
print(est_parfait(3))

#Exercice 19

def factorielle (n):
    fact = 1 
    for i in range(1,n+1):
        fact = fact*i 
    return fact
print(factorielle(3)) #Ceci est un exemple
