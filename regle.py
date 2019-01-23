# -*-coding:Utf-8 -*

import primesieve

class regle(object):
    ''' Une regle est un morceau de tasseau
    Elle est défini par
        * une valeur de debut
        * une valeur de fin

        Note : il pourrait y avoir un mécanisme d'héritage avec les blocs....
    '''

    def __init__(self, debut, fin):
        '''Initialisation
            - debut     :    valeur de debut de la régle (coté 1...100)
            - fin       :    valeur de fin de la régle (coté 1...100)
        '''
        self.debut = debut
        self.fin = fin
        self.valeur = None
        #test que les facteurs sont bien des facteurs
        assert self.debut< self.fin, "Erreur dans la définition de la regle."
        self.tasseau = None

    @property
    def table(self):
        return self.__table
    @table.setter
    def table(self, table):
        self.__table = table
        self.valeur = (self.fin - self.debut + 1) * self.table.largeur_tasseau / self.table.longueur_unit

    def __str__(self):
        #return "bloc_%s"%(self.indice)
        return "Regle %s-%s"%(self.debut, self.fin)

    def sort_key(self):
            return self.debut

    def test(self):
        '''test la cohérence des données
        '''
        return 0

    def genere(self, dwg, face):
        '''Return un objet svgwrite : une face du bloc
        '''
        print("%s-face %s"%(str(self),face))
        # Create the group
        g = dwg.defs.add(dwg.g())
        largeur = self.table.largeur_tasseau + self.table.largueur_espace / 2

        if face == 4:
            y = 0
            # rectangle gris pour les nombre premiers
            for i in range(self.debut,self.fin+1):
                if i in primesieve.primes(100):
                    g.add(dwg.rect( \
                            (0,y), \
                            (largeur, self.table.largeur_tasseau), \
                            fill=self.table.couleur('premier') \
                            ))
                y += self.table.largeur_tasseau

        if face in [1,2,4]:
            # Graduation largeur de tasseau
            y = 0
            for i in range(self.debut,self.fin):
                y += self.table.largeur_tasseau
                g.add(dwg.line((0,y),(largeur,y), stroke='black', stroke_width=0.5))

        if face == 1:
            # Text de la face 1
            y = self.table.largeur_tasseau / 2
            for i in range(self.debut,self.fin):
                params = {'insert':(largeur / 2 ,y) , 'text_anchor' : 'middle','font_size':8, 'rotate' : "90"}
                if i%5==0:
                    params['font_weight'] = 'bold'
                g.add(dwg.text(str(i),**params))
                y += self.table.largeur_tasseau
        if face == 3:
            #Une regle en unités
            y=0
            for i in range((self.debut-1)*self.table.largeur_tasseau/self.table.longueur_unit,
                            self.fin*self.table.largeur_tasseau/self.table.longueur_unit):
                y += self.table.longueur_unit
                if i%10==0:
                    # Si dizaine : ligne découpée + nombre
                    largeur_ligne = self.table.largueur_espace / 4 + self.table.largeur_tasseau / 5
                    if i%100==0:
                        params = {'stroke':'black', 'stroke_width':1}
                    else:
                        params = {'stroke':'black', 'stroke_width':0.5}
                    g.add(dwg.line((0,y),(largeur_ligne,y), **params))
                    g.add(dwg.line((largeur - largeur_ligne,y),(largeur,y), **params))
                    params = {'insert':(largeur / 2 ,y) , 'text_anchor' : 'middle','font_size':8, 'rotate' : "180"}
                    if i%100==0:
                        params['font_weight'] = 'bold'
                    g.add(dwg.text(str(i),**params))
                else:
                    g.add(dwg.line((0,y),(largeur,y), stroke='black', stroke_width=0.5))
        return g
