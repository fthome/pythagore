# -*-coding:Utf-8 -*
from table import *
from tasseau import *
from bloc import *



'''C'est le main !
'''

couleurs = {
    1 : 'white',
    2 : 'yellow',
    3 : '#66ffff', #bleu clair
    4 : '#FBBA00', # orange clair
    5 : 'pink',
    6 : 'blue',
    7 : 'green',
    8 : '#EF7D00',  # orange foncé
    9 : 'violet',
    10 : 'red',
    0 : 'white', # valeur par defaut
    'spacer' : "grey"
}

ma_table = table(couleurs = couleurs)

ma_table.add_tasseau(1, tasseau(blocs=[
                        bloc(100,[10,10,10,50])
                    ]))
ma_table.add_tasseau(2, tasseau(blocs=[
                        bloc(90,[10,9,2,45]),
                        bloc(9,[3,3,1,9])
                    ]))
ma_table.genere('essai', [1,2])
