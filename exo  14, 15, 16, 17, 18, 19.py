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
