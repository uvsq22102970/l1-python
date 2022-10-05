#temps[0] : jours, temps[1]: heures, temps[2]: minutes, temps[3]: secondes
def tempsEnSeconde(temps): 
    """ Renvoie la valeur en seconde de temps donné comme jour, heure, minute, seconde."""
    jours_s=temps[0]*24*3600
    heure_s=temps[1]*3600
    min_s= temps[2]*60
    tot= min_s+heure_s+jours_s+temps[3]
    return tot

print(tempsEnSeconde((3,23,1,34)))

def secondeEnTemps(seconde):
    """Renvoie le temps (jour, heure, minute, seconde) qui correspond au nombre de seconde passé en argument"""
    pass
    jours = seconde // 86400
    reste = seconde % 86400

    heures = reste // 3600
    reste = reste % 3600

    minutes = reste // 60
    reste = reste % 60

    return(jours, heures, minutes, reste)

temps = secondeEnTemps(100000)
print(temps[0],"jours",temps[1],"heures",temps[2],"minutes",temps[3],"secondes")



def demandeTemps(): 
    """Demande à l'utilisateur un nombre de jours, d'heures, de minutes et de secondes"""
    jours = -1
    heures = -1
    minutes = -1
    secondes = -1

    while (jours < 0 or jours >= 24):
        jours = int(input("entrer un nombre de jours"))

    while (heures < 0 or heures >= 60):
        heures = int(input("entrer un nombre d'heures"))

    while (minutes < 0 or heures >= 60):
        minutes = int(input("entrer un nombre de minutes"))

    while (secondes < 0 or secondes >= 60)



afficheTemps(demandeTemps())