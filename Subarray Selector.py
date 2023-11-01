def soustableau(tab, x, y):
    for i in range(x, y + 1):
        print(tab[i])


while True :
    tab = []
    print("Entrez un tableau de 10 éléments :")
    for i in range(10):
        a = int(input(f"Entrez l'élément {i+1} : "))
        tab.append(a)

    x = int(input("Entrez l'indice de départ : "))
    y = int(input("Entrez l'indice de fin : "))

    soustableau(tab, x, y)

    reponse = input("Voulez-vous saisir une nouvelle liste? (Oui/Non) : ").lower()
    if reponse != "oui":
        break