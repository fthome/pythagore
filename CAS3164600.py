# -*-coding:Utf-8 -*
from table import *
from tasseau import *
from bloc import *
from regle import *



'''Programme principale pour générer une table de pythogore
La description de la table se fait ici

Usage python table_de_pythagore.py
'''
couleurs = {
    1 : '#FDE900', # Jaune*	C5 M0 J98 N0
    2 : '#00ACE8', # Bleu*	C83 M2 J0 N0
    3 : '#AF6D35', # Marron*	C33 M61 J87 N6
    4 : 'white', # Blanc*	C0 M0 J0 N0
    5 : '#E20613', # Rouge*	C0 M100 J100 N1
    6 : '#000000', #Noir*	C0 M0 J0 N100
    7 : '#FF69B3', #Rose*	C3 M88 J0 N0
    8 : '#FF8618',  # Orange*	C0 M65 J100 N5
    9 : '#934F99', # Violet*	C51 M78 J1 N0
    10 : '#6CB52D', #Vert*	C63 M0 J100 N0
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

bloc_10 = bloc(10,[10]*4, no_graduation = True)
bloc_9 = bloc(9,[9]*4, no_graduation = True)
bloc_8 = bloc(8,[8]*4, no_graduation = True)
bloc_7 = bloc(7,[7]*4, no_graduation = True)
bloc_6 = bloc(6,[6]*4, no_graduation = True)
bloc_5 = bloc(5,[5]*4, no_graduation = True)
bloc_4 = bloc(4,[4]*4, no_graduation = True)
bloc_3 = bloc(3,[3]*4, no_graduation = True)
bloc_2 = bloc(2,[2]*4, no_graduation = True)
bloc_1 = bloc(1,[1]*4, no_graduation = True)

CAS3164600.add_tasseau(1, tasseau(blocs=[bloc_10, bloc_5]))
CAS3164600.add_tasseau(2, tasseau(blocs=[bloc_10, bloc_5]))
CAS3164600.add_tasseau(3, tasseau(blocs=[bloc_9, bloc_6, bloc_2]))
CAS3164600.add_tasseau(4, tasseau(blocs=[bloc_9, bloc_6, bloc_2]))
CAS3164600.add_tasseau(5, tasseau(blocs=[bloc_8, bloc_7, bloc_2]))
CAS3164600.add_tasseau(6, tasseau(blocs=[bloc_8, bloc_7, bloc_2]))
CAS3164600.add_tasseau(7, tasseau(blocs=[bloc_4]*2+[bloc_3]*3))
CAS3164600.add_tasseau(8, tasseau(blocs=[bloc_1]*10+[bloc_2]))
# On imprime 9 tasseaux à la fois :
CAS3164600.genere('CAS3164600_', list(range(1,9)))
