# -*-coding:Utf-8 -*

'''Quelques bricoles pour que le code python 2 passe en python3
(et éventuellement l'inverse)
'''


try:
    dict.iteritems
except AttributeError:
    # Python 3
    def itervalues(d):
        return iter(d.values())
    def iteritems(d):
        return iter(d.items())
else:
    # Python 2
    def itervalues(d):
        return d.itervalues()
    def iteritems(d):
        return d.iteritems()
