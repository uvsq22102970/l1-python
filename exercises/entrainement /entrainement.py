import getpass

def get_joueur ():
    joueur_1 = input("Veuillez entrer le nom du joueur 1:")
    joueur_2 = input("Veuillez entrer le nom du joueur 2:")

    while len(joueur_1) == 0 or len(joueur_2) == 0:
        joueur_1 = input("Veuillez entrer un nom correct pour le joueur 1:")
        joueur_2 = input("Veuillez entrer un nom correct pour le joueur 2:")

    return joueur_1, joueur_2

def propose_mot (noms_joueurs, tour):

    mot = getpass.getpass("Quel mot" + noms_joueurs[tour%2] + "va devoir deviner ?")

    mot_clair = []
    mot_cache = []

    for lettre in mot: 
        mot_clair.append(lettre)
        mot_cache.append("_")
    
    return(mot_clair, mot_cache)

def check_lettre(etat_mot, lettre):

    i = 0
    correct = False
    for l in etat_mot[0]:
        if l == lettre:
            etat_mot[1][i] = lettre
            correct = True
        i += 1

    return correct


def check_mot(mot_clair , mot_propose):

    i = 0
    correct = True 

    for lettre in mot_propose:
        if mot_clair[i] == lettre:
            correct = False

    return correct 



def propose(etat_mot, noms_joueurs, tour,  liste_proposition, nb_vie):

    proposition = input(noms_joueurs[tour%2] + "propose une lettre ou un mot: ")

    correct = 0

    while len(proposition) != 1 or not len(proposition) != len(etat_mot[0]):
        proposition = input("Veuillez proposer une lettre ou un mot:")

    if len(proposition) == 1:
        if proposition in liste_proposition:
            print("Vous avez déjà proposé cette lettre")
            propose(etat_mot, noms_joueurs, tour, liste_proposition, nb_vie)
        else: 
            if check_lettre(etat_mot, proposition):
                correct = 1
            liste_proposition.append(proposition)
    else:
        if check_mot():
            correct = 2

    return correct

def affiche_mot(mot):
    print(mot)

def test_fin_de_jeu (etat_mot, correct, nb_vie):
    if correct == 0: #Le joueur s'est trompé 
        nb_vie -= 1
        return False, nb_vie
        
    elif correct == 1: #Le joueur a deviné une lettre
        if etat_mot[0] == etat_mot [1]:
            return True 
        else: 
            return False
    else: #Le joueur a deviné le mot
        return True 

def lancer_jeu(tour, joueurs):

    tour = 0
    nb_vie = 10
    liste_proposition = []

    etat_mot = propose_mot(joueurs, tour)

    while True:
        print(nb_vie)
        correct = propose(etat_mot, joueurs, tour, liste_proposition, nb_vie)

        if test_fin_de_jeu(etat_mot, correct, nb_vie):
            print("Bravo vous avez deviné le mot: ", etat_mot[0])
            break
        else: 
            print("Vous vous êtes trompés.")
            if nb_vie == 0:
                print("Perdu vous n'avez plus de vie !")
                break
            else: 
                print("Il vous reste", nb_vie, "!")


joueurs= get_joueur ()

for tour in range(10):
    lancer_jeu(tour)