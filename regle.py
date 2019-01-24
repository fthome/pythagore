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
        #test que les facteurs sont bien des facteurs
        assert self.debut< self.fin, "Erreur dans la définition de la regle."
        self.tasseau = None
        self.valeur = None

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
            Les régles doivent être à la fois d'une longueur multiple de la largeur des tasseaux (ok par construction),
            Mais aussi d'une longueur multiple de la longueur des unités et début et fin doivent co-incider avec graduation.
        '''
        if ((self.debut-1)*self.table.largeur_tasseau)%self.table.longueur_unit ==0 \
            and (self.fin*self.table.largeur_tasseau)%self.table.longueur_unit == 0:
            return 0
        else:
            print("Erreur dans %s : la longueur n'est pas un multiple des unités."%(self, ))
            return 1

    def genere(self, dwg, face):
        '''Return un objet svgwrite : une face du bloc
            - dwg       :   main drawing
            - face      :   0-3
        '''
        print("%s-face %s"%(str(self),face))
        # Create the group
        g = dwg.defs.add(dwg.g())
        largeur = self.table.largeur_tasseau + self.table.largueur_espace / 2

        if face == 3:
            y = 0
            # rectangle gris pour les nombre premiers
            for i in range(self.debut,self.fin+1):
                if i>10 and i in primesieve.primes(100):
                    g.add(dwg.rect( \
                            (0,y), \
                            (largeur, self.table.largeur_tasseau), \
                            fill=self.table.couleur('premier') \
                            ))
                y += self.table.largeur_tasseau

        if face in [0,1,3]:
            # Graduation largeur de tasseau
            y = 0
            for i in range(self.debut,self.fin):
                y += self.table.largeur_tasseau
                g.add(dwg.line((0,y),(largeur,y), stroke='black', stroke_width=0.5))

        if face in [0,3]:
            # Text de la face 1 et 4
            y = self.table.largeur_tasseau / 2
            for i in range(self.debut,self.fin):
                params = {'insert':(largeur / 2 ,y) , 'text_anchor' : 'middle','font_size':8, 'transform' : "rotate(90,%s,%s)"%(largeur / 2 ,y)}#'rotate':[90]} 
                if i%5==0:
                    params['font_weight'] = 'bold'
                g.add(dwg.text(str(i),**params))
                y += self.table.largeur_tasseau
        if face == 2:
            #Une regle en unités
            y=0
            for i in range((self.debut-1)*self.table.largeur_tasseau/self.table.longueur_unit+1,
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
                    params = {'insert':(largeur / 2 ,y+3) , 'text_anchor' : 'middle','font_size':8, 'rotate' : '0'}
                    if i%100==0:
                        params['font_weight'] = 'bold'
                    g.add(dwg.text(str(i),**params))
                else:
                    g.add(dwg.line((0,y),(largeur,y), stroke='black', stroke_width=0.5))
        return g
