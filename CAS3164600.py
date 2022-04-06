# -*-coding:Utf-8 -*
from table import *
from tasseau import *
from bloc import *
from regle import *



'''Programme principale pour générer une table de pythogore
La description de la table se fait ici

Usage python table_de_pythagore.py
'''

'''
Barre 1	10	Jaune*	C5 M0 J98 N0
Barre 2	5	Bleu*	C83 M2 J0 N0
Barre 3	3	Marron*	C33 M61 J87 N6
Barre 4	2	Blanc*	C0 M0 J0 N0
Barre 5	2	Rouge*	C0 M100 J100 N1
Barre 6	2	Noir*	C0 M0 J0 N100
Barre 7	2	Rose*	C3 M88 J0 N0
Barre 8	2	Orange*	C0 M88 J99 N0
Barre 9	2	Violet*	C85 M81 J0 N1
Barre 10	2	Vert*	C63 M0 J100 N0

'''
couleurs = {
    1 : '#F2FF05', # Jaune*	C5 M0 J98 N0
    2 : '#2BFAFF', # Bleu*	C83 M2 J0 N0
    3 : '#9C5412', # Marron*	C33 M61 J87 N6
    4 : 'white', # Blanc*	C0 M0 J0 N0
    5 : '#FC0000', # Rouge*	C0 M100 J100 N1
    6 : '#000000', #Noir*	C0 M0 J0 N100
    7 : '#F71FFF', #Rose*	C3 M88 J0 N0
    8 : '#FF1F03',  # Orange*	C0 M88 J99 N0
    9 : '#242EFC', # Violet*	C85 M81 J0 N1
    10 : '#5EFF00', #Vert*	C63 M0 J100 N0
    0 : 'white', # valeur par defaut
    'spacer' : "grey",
    'premier' : "#C0C0C0" # pour nombre premier : gris clair
}

CAS3164600  = table( \
                    couleurs = couleurs,
                    longueur_tasseau = 400, # en mm
                    largeur_tasseau = 22, # en mm
                    largueur_espace = 8.5, # Correspond à l'interval en mm entre deux tasseaux dans le gabarit
                    longueur_unit = 22, # Correspond à la hauteur en mm de 1
                    longueur_spacer = 3, #Correspond à l'épaisseur de la lame de scie
                    outfolder = "SVG"
                    )

CAS3164600.add_tasseau(1, tasseau(blocs=[
                        bloc(10,[10]*4, no_graduation = True),
                        bloc(5,[5]*4, no_graduation = True)
                    ]))
CAS3164600.add_tasseau(2, tasseau(blocs=[
                        bloc(9,[9]*4, no_graduation = True),
                        bloc(6,[6]*4, no_graduation = True)
                    ]))
CAS3164600.add_tasseau(3, tasseau(blocs=[
                        bloc(8,[8]*4, no_graduation = True),
                        bloc(7,[7]*4, no_graduation = True)
                    ]))
CAS3164600.add_tasseau(4, tasseau(blocs=[
                        bloc(4,[4]*4, no_graduation = True),
                        bloc(3,[3]*4, no_graduation = True),
                        bloc(2,[2]*4, no_graduation = True),
                        bloc(5,[5]*4, no_graduation = True)
                    ]))
CAS3164600.add_tasseau(5, tasseau(blocs=[
                        bloc(4,[4]*4, no_graduation = True),
                        bloc(3,[3]*4, no_graduation = True),
                        bloc(3,[3]*4, no_graduation = True),
                        bloc(2,[2]*4, no_graduation = True),
                        bloc(2,[2]*4, no_graduation = True),
                        bloc(2,[2]*4, no_graduation = True),
                    ]))
CAS3164600.add_tasseau(6, tasseau(blocs=[
                        bloc(2,[2]*4, no_graduation = True),
                        bloc(1,[1]*4, no_graduation = True),
                        bloc(1,[1]*4, no_graduation = True),
                        bloc(1,[1]*4, no_graduation = True),
                        bloc(1,[1]*4, no_graduation = True),
                        bloc(1,[1]*4, no_graduation = True),
                        bloc(1,[1]*4, no_graduation = True),
                        bloc(1,[1]*4, no_graduation = True),
                        bloc(1,[1]*4, no_graduation = True),
                        bloc(1,[1]*4, no_graduation = True),
                        bloc(1,[1]*4, no_graduation = True),
                    ]))
# On imprime 9 tasseaux à la fois :
CAS3164600.genere('CAS3164600_', list(range(1,7)))
