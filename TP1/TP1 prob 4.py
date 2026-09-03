# emilie blanchard
# 2025-09-03
# v 1.0
# reponse probleme 4 : Gestion des notes d'un groupe

#Entrées
note_1 = int(input("Entrer la note 1"))
note_2 = int(input("Entrer la note 2"))
note_3 = int(input("Entrer la note 3"))
note_4 = int(input("Entrer la note 4"))
nb_echec = 0
#Traitements
notes = [note_1, note_2, note_3, note_4]
for note in notes :
    if note < 60 :
        nb_echec = nb_echec + 1
total = note_1 + note_2 + note_3 + note_4
moy = total/4
if moy % 1 == 0:
    moy = int(moy)
#Sorties
print("Notes:", note_1,",",note_2,",",note_3,",",note_4)
print("Moyenne:",moy)
print("Échec(s):",nb_echec)