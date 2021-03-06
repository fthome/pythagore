# -*-coding:Utf-8 -*

class tasseau(object):
    ''' Un tasseau est un objet d'une table de pythagore
        composé de plusieurs blocs
    '''
    def __init__(self, blocs = []):
        self.blocs = blocs
        self.table = None
        self.id = None

    def __str__(self):
        return "tasseau_%s"%self.id

    def genere(self,dwg, face):
        '''Return un objet svgwrite : une face du tasseau
        '''
        print(str(self))
        g = dwg.defs.add(dwg.g())
        y = 0
        largeur = self.table.largeur_tasseau + self.table.largueur_espace / 2
        for bloc in self.blocs:
            # Bloc
            g_bloc = bloc.genere(dwg, face)
            g.add(dwg.use(g_bloc, insert = (0,y)))
            y += bloc.valeur * self.table.longueur_unit
            # Séparateur
            if y < self.table.longueur_tasseau - self.table.longueur_spacer:
                g.add(dwg.rect((0,y),(largeur,self.table.longueur_unit),fill=self.table.couleur('spacer')))
                y += self.table.longueur_spacer
        # On termine le tasseau en gris
        if y < self.table.longueur_tasseau:
            g.add(dwg.rect((0,y),(largeur, self.table.longueur_tasseau - y),fill=self.table.couleur('spacer')))
        return g
