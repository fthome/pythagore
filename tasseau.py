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

    def tgenere(self, dwg, face):
        '''Return un objet svgwrite
        '''
        svg_tasseau = dwg.defs.add(dwg.g(id=str(self)))
        svg_tasseau.add(dwg.rect((self.table.largueur_espace,0),(self.table.largeur_tasseau ,self.table.longueur_tasseau)))
        return svg_tasseau

    def genere(self,dwg, face):
        '''Return un objet svgwrite : une face du tasseau
        '''
        g = dwg.defs.add(dwg.g())
        y = 0
        for bloc in self.blocs:
            g_bloc = bloc.genere(dwg, face)
            g.add(dwg.use(g_bloc, insert = (0,y)))
            y += bloc.valeur * self.table.longueur_unit
            g.add(dwg.rect((0,y),(self.table.largeur_tasseau + self.table.largueur_espace / 2,self.table.longueur_unit),fill=self.table.couleur('spacer')))
            y += self.table.longueur_spacer
        return g
