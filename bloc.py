# -*-coding:Utf-8 -*

class bloc(object):
    ''' Un bloc est un morceau de tasseau
    Il est défini par
        * une valeur totale
        * pour chacune de ses faces
            * un facteur qui correspond au chiffre qui sera affiché
    '''
    compteur = 0
    def __init__(self, valeur, facteurs):
        '''Initialisation
            valeur      :    valeur total du blocs
            facteurs    :   facteurs des 4 faces
        '''
        self.valeur = valeur
        self.facteurs = facteurs
        #test que les facteurs sont bien des facteurs
        for facteur in facteurs:
            assert self.valeur%facteur==0, "Erreur dans la définition de la table. %s n'est pas un bon facteur pour %s"%(facteur, self.valeur)
        self.table = None
        self.tasseau = None
        self.compteur +=1
        self.indice = self.compteur

    def __str__(self):
        return "bloc_%s"%(self.indice)

    def genere(self, dwg, face):
        '''Return un objet svgwrite : une face du bloc
        '''
        print("couleur : %s"%self.table.couleur(self.facteurs[face]))
        # Create the group
        g = dwg.defs.add(dwg.g())
        # Add rectangle
        largeur = self.table.largeur_tasseau + self.table.largueur_espace / 2
        g.add(dwg.rect( \
                (0,0), \
                (largeur, self.valeur*self.table.longueur_unit), \
                fill=self.table.couleur(self.facteurs[face]) \
                ))
        # Add graduation
        y = 0
        for i in range(self.valeur-1):# / self.facteurs[face]):
            y += self.table.longueur_unit
            if (i+1)%self.facteurs[face]==0:
                g.add(dwg.line((0,y),(largeur,y), stroke='black', stroke_width=0.5))
            else:
                largeur_ligne = self.table.largueur_espace / 4 + self.table.largeur_tasseau / 5
                g.add(dwg.line((0,y),(largeur_ligne,y), stroke='black', stroke_width=0.5))
                g.add(dwg.line((largeur - largeur_ligne,y),(largeur,y), stroke='black', stroke_width=0.5))
        # Text
        y = 0
        for i in range(self.valeur / self.facteurs[face]):
            print(self.facteurs[face])
            text = dwg.add(dwg.g(font_size=10))
            text.add(dwg.text(str(self.facteurs[face]),(largeur/2,y+self.facteurs[face]*self.table.longueur_unit/2)))
            g.add(text)
            y += self.table.longueur_unit*self.facteurs[face]
        return g
