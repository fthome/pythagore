# -*-coding:Utf-8 -*

import svgwrite
#from svglib.svglib import svg2rlg
#from reportlab.graphics import renderPDF
from pathlib import Path
from python2_3 import *

class table(object):
    '''Une table de pythagore est un puzzle 3D
        Elle est composée de blocs (qui sont des morceaux de tasseaux)
    '''
    def __init__(self, couleurs={}, longueur_tasseau = 400, largeur_tasseau = 22, largueur_espace = 8.5, longueur_unit = 4, longueur_spacer = 3, outfolder = ""):
        '''Initialisation
            tasseaux    :   liste de tasseaux
            couleurs    :   dict {facteur : couleur}
                                facteur : nombre
                                couleur : text (ex : 'red', '#59B840', )
            TODO : compléter
        '''
        self.tasseaux = {}
        self.couleurs = couleurs
        self.longueur_tasseau = longueur_tasseau
        self.largeur_tasseau = largeur_tasseau
        self.largueur_espace = largueur_espace
        self.longueur_unit = longueur_unit
        self.longueur_spacer = longueur_spacer
        self.outfolder = outfolder

    def add_tasseau(self, indice, tasseau):
        '''Ajoute un tasseau à la table
        indice  :   indice ex (1 ou 'un')
        '''
        self.tasseaux[indice] = tasseau
        tasseau.table = self
        tasseau.id = indice
        for bloc in tasseau.blocs:
            bloc.table = self
            bloc.tasseau = tasseau

    def test(self):
        '''Test la cohérance des données
        '''
        print("TEST des données :")
        blocs = []
        for tasseau in itervalues(self.tasseaux):
            blocs += tasseau.blocs
        blocs.sort(key = lambda bloc:(bloc.valeur, bloc.facteurs))
        print("Nb de blocs : %s"%len(blocs))
        error = 0
        # TEST des blocs
        for bloc in blocs:
            print(bloc)
            error += bloc.test()
        print("Erreurs dans la cohérance des données : %s"%error)
        return error == 0


    def genere(self, nom, tasseaux_ids):
        '''genère les fichiers des 4 faces des tasseaux correspondant aux indices
            nom             :   nom racine des fichiers générés
            tasseaux_ids    :   liste d'indices
        '''
        self.test()
        for face in range(4):
            print("face %s :"%face)
            file = Path(self.outfolder) /("%s_F%s.svg"%(nom,face+1))
            w = len(tasseaux_ids)*(self.largeur_tasseau + self.largueur_espace) - self.largueur_espace/2
            h = self.longueur_tasseau
            dwg = svgwrite.Drawing(str(file), ("%smm"%w,"%smm"%h), debug = True, profile = 'tiny', viewBox=(0,0,w,h))
            x = 0
            for tasseau_id in tasseaux_ids:
                svg_tasseau = self.tasseaux[tasseau_id].genere(dwg, face)
                dwg.add(dwg.use(svg_tasseau, insert = (x,0)))
                x += self.largeur_tasseau + self.largueur_espace
            dwg.save()
            # En fait la génération du pdf par svg2rlg ne fonctionne pas : les rectangles gris sont perdus! et mauvaise prise en charge des units (mm)
            # => on va utiliser un programme tiers (ie adobe illustrator)
            #drawing = svg2rlg(file)
            #renderPDF.drawToFile(drawing, "%s_F%s.pdf"%(nom,face+1))

    def couleur(self, facteur):
        '''Renvoi la couleur d'une face selon son facteur
        '''
        try:
            couleur = self.couleurs[facteur]
        except KeyError:
            couleur = self.couleurs[0]
        return couleur
