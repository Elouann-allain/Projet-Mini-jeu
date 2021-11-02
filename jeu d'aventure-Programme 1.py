"""
Programme réalisé par Allain Elouann, 1G4
"""
#desciption des pièces en fonction du numéro
def decrireLaPiece(piece):
    cleTrouve='N'
    if piece==1:
        print("vous vous trouvez dans l'ENTRÉE")
    elif piece==2:
        print("vous vous trouvez dans le PETIT SALON")
    elif piece==3:
        print("vous vous trouvez dans le SALON")
    elif piece==4:
        print("vous vous trouvez dans la SALLE À MANGER")
    elif piece==5:
        print("vous vous trouvez dans la CUISINE")
    elif piece==6:
        print("vous vous trouvez dans la CHAMBRE 1")
        print("Il y a une pièce cachée qui n'est accéssible que si vous avez trouvé la clé")
    elif piece==7:
        print("vous vous trouvez dans la CHAMBRE 2")
    elif piece==8:
        print("vous vous trouvez dans la BIBLIOTHÈQUE")
    elif piece==9:
        print("vous vous trouvez dans le BUREAU et vous venez de trouver la clé de la pièce cachée")
        cleTrouve='O'
    elif piece==10:
        print("vous vous trouvez dans l'ARRIÈRE CUISINE")
    elif piece==11:
        print("vous vous trouvez dans le GRENIER qui est la pièce cachée.")
        print("vous avez réussi le jeu. Merci d'avoir joué")
    return cleTrouve

#la fonction decision ou "machine a état" permettant de se déplacer ou non en fonction de la pièce ou l'on se situe
def decision(direction,piece,cleTrouve):
    print("Vous désirez allez dans la direction",nomDirection(direction))
    memorisePiece=piece
    #S : le personnage désire aller au sud
    if direction=='s':
        if piece==1:
            piece=8
        elif piece==2:
            piece=7
        elif piece==3:
            piece=6
        elif piece==4:
            piece=5
        elif piece==5:
            piece=10
        elif piece==6 and cleTrouve=='O':
            piece=11
        elif piece==8:
            piece=9
    #N : le personnage désire aller au nord
    elif direction=='n':
        if piece==8:
            piece=1
        elif piece==7:
            piece=2
        elif piece==6:
            piece=3
        elif piece==5:
            piece=4
        elif piece==9:
            piece=8
        elif piece==10:
            piece=5
        elif piece==11:
            piece=6
    #E : le personnage désire aller à l'est
    elif direction=='e':
        if piece==4:
            piece=3
        elif piece==3:
            piece=2
        elif piece==2:
            piece=1
        elif piece==5:
            piece=6
        elif piece==6:
            piece=7
        elif piece==7:
            piece=8
    #O : le personnage désire aller à l'ouest
    elif direction=='o':
        if piece==1:
            piece=2
        elif piece==2:
            piece=3
        elif piece==3:
            piece=4
        elif piece==6:
            piece=5
        elif piece==7:
            piece=6
        elif piece==8:
            piece=7
    if memorisePiece==piece:
        print("Deplacement impossible")
    return piece

#Cette fonction donne le nom complet de la direction
def nomDirection(direction):
    switch={
    'n':'NORD',
    's':'SUD',
    'o':'OUEST',
    'e':'EST'
    }
    return switch.get(direction,direction+' = Direction inconnue')

#programme principal
dansQuellePieceEstLePersonnage=1   #variable très explicite
cleTrouve='N'
presenceCle='N'
menu='0'
while menu!='q':
    cleTrouve=decrireLaPiece(dansQuellePieceEstLePersonnage)
    if cleTrouve=='O':
        presenceCle='O'
    print("Ou désirez-vous aller? -------------------------------------")
    print("n : Nord")
    print("s : Sud")
    print("e : Est")
    print("o : Ouest")
    print("q : quitter")
    print("------------------------------------------------------------")
    menu=input("votre choix ?")
    dansQuellePieceEstLePersonnage=decision(menu,dansQuellePieceEstLePersonnage,presenceCle)

print("Au revoir")