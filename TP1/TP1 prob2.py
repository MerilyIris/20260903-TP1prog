# emilie blanchard
# 2025-09-03
# v 1.0
# reponse probleme 2 : Reservation camping

#le pourcentage pour les taxe n'était pas inclus dans la question, j'ai donc fait p_tx= (total-s_total/s_total
#   en inscrivant manuellement le total puisque le total dépend du résultat de p_tx
#   exemple avec le 3e résultat attendu; p_tx= (862.31-s_total)/s_total
#   puisque cela nécessitait un calcul, p_tx était dans traitement plutot que entrees

#entrees
nb_nuit= int(input("Entrez le nombre de nuits : "))
cout= float(input("Entrez le coût par nuit: "))
p_tx= 0.14974
#traitements
if cout % 1 == 0:
    cout = int(cout)
s_total= nb_nuit * cout
taxe= s_total * p_tx
total=round(s_total + taxe,2)
#sorties
print(nb_nuit,"nuits à",cout,"$")
print("Sous-total:",s_total,"$")
print("Total avec taxes:",total,"$")