# emilie blanchard
# 2025-09-03
# v 1.0
# reponse probleme 3 : Guichet automatique

#entrees
solde_init = 500
montant = float(input("Entrez le montant a deposer ou retirer"))
reponse = (input("Est-ce un depot (oui/non)?"))
trans = "Depot"
#traitements
if montant % 1 == 0:
    montant = int(montant)
if reponse == "oui" :
    solde_new = solde_init + montant
elif reponse == "non" :
    trans= "Retrait"
    solde_new = solde_init - montant


#sorties
print("Solde initial:", solde_init, "$")
print(trans,":",montant, "$")
if solde_new < 0 :
    print("Transaction refusée")
else : print("Nouveau solde:", solde_new, "$")