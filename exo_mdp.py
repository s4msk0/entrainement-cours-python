def verif_mdp():
    mdp_correct = "1234" #Ceci est un exemple
    tentative = 0
    max_tentative = 5

    while tentative < max_tentative:
        mot_de_passe = input("Entrez le mot de passe : ")
    
        if mot_de_passe == mdp_correct:
            print("mode passe correct, Accès autorisé.")
            return True
    
        else: 
            tentative += 1
            print(f"Mot de passe incorrect, veullez le saisir. Tentatives restantes : {max_tentative - tentative}")
   
    print("Tentative dépassé, Accès refusé.")
    return False      


verif_mdp()


   