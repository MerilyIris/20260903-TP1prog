# emilie blanchard
# 2025-09-03
# v 1.0
# reponse probleme 1 : Refuge animalier

#entrees
chien= int(input("Entrez le nombre de chiens:"))
chat= int(input("Entrez le nombre de chats:"))
lapin= int(input("Entrez le nombre de lapins:"))
#traitements
total= chien+chat+lapin
dom= max(chien,chat,lapin)
if dom == chien:
    esp_dom = "Chien"
elif dom == chat:
    esp_dom = "Chat"
elif dom == lapin:
    esp_dom = "Lapin"

#sorties
print("Chiens=",chien, "Chats=",chat, "Lapins=",lapin)
print("Total=",total)
print("Espèce dominante:",esp_dom)