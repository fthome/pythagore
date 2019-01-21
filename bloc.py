# -*-coding:Utf-8 -*

class bloc(object):
    ''' Un bloc est un morceau de tasseau
    Il est défini par
        * une valeur totale
        * pour chacune de ses faces
            * un facteur qui correspond au chiffre qui sera affiché
    '''

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


    def __str__(self):
        #return "bloc_%s"%(self.indice)
        return "Bloc %s-%s"%(self.valeur, self.facteurs)

    def __cmp__(self, other):
        return cmp((self.valeur, self.facteurs),(other.valeur, other.facteurs))

    def test(self):
        '''test la cohérence des données
            bloc(valeur,[f1,f2,f3,f4])
            - nb de facteur : 4
            - f1*f2 == f3xf4 = valeur
        '''
        error = 0
        if len(self.facteurs)!=4:
            print("%s n'a pas 4 facteurs!"%self)
            error +=1
        if self.valeur != self.facteurs[0] * self.facteurs[1]:
            print("%s : erreur %s != %s * %s!"%(self,self.valeur, self.facteurs[0], self.facteurs[1]))
            error +=1
        if self.valeur != self.facteurs[2] * self.facteurs[3]:
            print("%s : erreur %s != %s * %s!"%(self,self.valeur, self.facteurs[2], self.facteurs[3]))
            error +=1
        return error

    def genere(self, dwg, face):
        '''Return un objet svgwrite : une face du bloc
        '''
        print("%s-face %s"%(str(self),face))
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
        # Text (sauf pour facteur == 1)
        if self.facteurs[face] > 1:
            y = 0
            for i in range(self.valeur / self.facteurs[face]):
                y_text = y+self.facteurs[face]*self.table.longueur_unit/2 + 2
                text = dwg.text(str(self.facteurs[face]),insert=(largeur / 2 ,y_text) , text_anchor = 'middle',font_size=8)
                if self.facteurs[face] in [6,9]:
                    point = dwg.circle((largeur/2, y_text + 3), 1, fill = "black")
                    g.add(point)
                g.add(text)
                y += self.table.longueur_unit*self.facteurs[face]
        return g
