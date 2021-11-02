"""
Programme réalisé par Allain Elouann, 1G4
"""
import pygame

#initialisation graphique
pygame.init()
fenetre = pygame.display.set_mode((875, 510))
pygame.display.set_caption("jeu d'aventure")
font = pygame.font.Font('freesansbold.ttf', 20)
image1=pygame.image.load("vestibule.jpg")
image2=pygame.image.load("petit salon.jpg")
image3=pygame.image.load("salon.jpg")
image4=pygame.image.load("salle-a-manger.jpg")
image5=pygame.image.load("cuisine.jpg")
image6=pygame.image.load("chambre 1.jpg")
image7=pygame.image.load("chambre 2.jpg")
image8=pygame.image.load("bibliotheque.jpg")
image9=pygame.image.load("bureau.jpeg")
image10=pygame.image.load("arriere_cuisine.jpg")
image11=pygame.image.load("grenier.jpg")
text1 = font.render("Vous vous trouvez dans l'ENTRÉE.", True, (100, 225, 100))
text2 = font.render("Vous vous trouvez dans le PETIT SALON.", True, (105, 255, 200))
text3 = font.render("Vous vous trouvez dans le SALON.", True, (172, 230, 110))
text4 = font.render("Vous vous trouvez dans la SALLE À MANGER.", True, (255, 102, 178))
text5 = font.render("Vous vous trouvez dans la CUISINE.", True, (255, 0, 255))
text6a = font.render("Vous vous trouvez dans la CHAMBRE 1.", True, (255, 255, 0))
text6b = font.render("Il y a une pièce cachée qui n'est accéssible que si vous avez trouvé la clé.", True, (255, 255, 0))
text7 = font.render("Vous vous trouvez dans la CHAMBRE 2.", True, (255, 255, 0))
text8 = font.render("Vous vous trouvez dans la BIBLIOTHÈQUE.", True, (25, 25, 60))
text9 = font.render("Vous vous trouvez dans le BUREAU et vous venez de trouver la clé de la pièce cachée.", True, (0, 0, 0))
text10 = font.render("Vous vous trouvez dans l'ARRIÈRE CUISINE.", True, (205, 48, 60))
text11a = font.render("Vous vous trouvez dans le GRENIER qui est la pièce cachée.", True, (255, 255, 51))
text11b = font.render("Vous avez réussi le jeu !", True, (255, 255, 51))
text11c = font.render("Merci d'avoir joué(e).", True, (255, 67, 51))

def decrireLaPiece(piece):
    cleTrouve='N'
    if piece==1:
        fenetre.blit(image1,(0,0))
        fenetre.blit(text1,(0,350))
    elif piece==2:
        fenetre.blit(image2,(0,0))
        fenetre.blit(text2,(50,410))
    elif piece==3:
        fenetre.blit(image3,(0,0))
        fenetre.blit(text3,(100,330))
    elif piece==4:
        fenetre.blit(image4,(0,0))
        fenetre.blit(text4,(0,330))
    elif piece==5:
        fenetre.blit(image5,(0,0))
        fenetre.blit(text5,(200,390))
    elif piece==6:
        fenetre.blit(image6,(0,0))
        fenetre.blit(text6a,(20,350))
        fenetre.blit(text6b,(20,370))
    elif piece==7:
        fenetre.blit(image7,(0,0))
        fenetre.blit(text7,(200,20))
    elif piece==8:
        fenetre.blit(image8,(0,0))
        fenetre.blit(text8,(200,20))
    elif piece==9:
        cleTrouve='O'
        fenetre.blit(image9,(0,0))
        fenetre.blit(text9,(10,20))
    elif piece==10:
        fenetre.blit(image10,(0,0))
        fenetre.blit(text10,(200,300))
    elif piece==11:
        fenetre.blit(image11,(0,0))
        fenetre.blit(text11a,(40,35))
        fenetre.blit(text11b,(15,370))
        fenetre.blit(text11c,(15,390))
    return cleTrouve

def decision(direction,piece,cleTrouve):
    print("Vous désirez allez dans la direction",nomDirection(direction))
    memorisePiece=piece
    #N : le personnage désire aller au nord
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
    #S : le personnage désire aller au sud
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
loop=True
while loop==True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            loop = False            #fermeture de la fenetre (croix rouge)
        elif event.type == pygame.KEYDOWN:  #lecture du clavier
            dansQuellePieceEstLePersonnage=decision(event.unicode,dansQuellePieceEstLePersonnage,presenceCle)
            if event.key == pygame.K_ESCAPE or event.unicode == 'q': #touche q pour quitter
                loop = False
        cleTrouve=decrireLaPiece(dansQuellePieceEstLePersonnage)
        if cleTrouve=='O':
            presenceCle='O'
    # Actualisation de l'affichage
    pygame.display.flip()
pygame.quit()