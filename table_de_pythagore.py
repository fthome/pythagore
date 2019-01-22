# -*-coding:Utf-8 -*
from table import *
from tasseau import *
from bloc import *



'''Programme principale pour générer une table de pythogore
La description de la table se fait ici

Usage python3 table_de_pythagore.py
(python 3 pour génération pdf)
'''

couleurs = {
    1 : 'white',
    2 : '#FFE500', # yellow
    3 : '#A1DAF8', # bleu clair
    4 : '#FBBA00', # orange clair
    5 : '#EA528E', # pink
    6 : '#009DDF', # blue
    7 : '#76B82A', # vert
    8 : '#EF7D00',  # orange foncé
    9 : '#5488C7', # violet
    10 : '#E7344C', #rouge
    0 : 'white', # valeur par defaut
    'spacer' : "grey"
}

ma_table = table(couleurs = couleurs)

ma_table.add_tasseau(1, tasseau(blocs=[
                        bloc(100,[10,10,2,50])
                    ]))
ma_table.add_tasseau(2, tasseau(blocs=[
                        bloc(90,[10,9,2,45]),
                        bloc(9,[3,3,1,9])
                    ]))
ma_table.add_tasseau(3, tasseau(blocs=[
                        bloc(80,[10,8,2,40]),
                        bloc(10,[10,1,2,5]),
                        bloc(8,[8,1,2,4])
                    ]))
ma_table.add_tasseau(4, tasseau(blocs=[
                        bloc(70,[10,7,2,35]),
                        bloc(20,[10,2,2,10]),
                        bloc(8,[4,2,1,8])
                    ]))
ma_table.add_tasseau(5, tasseau(blocs=[
                        bloc(60,[10,6,2,30]),
                        bloc(30,[10,3,2,15]),
                        bloc(8,[2,4,1,8])
                    ]))
ma_table.add_tasseau(6, tasseau(blocs=[
                        bloc(50,[10,5,2,25]),
                        bloc(40,[10,4,2,20]),
                        bloc(8,[1,8,2,4])
                    ]))
ma_table.add_tasseau(7, tasseau(blocs=[
                        bloc(90,[9,10,2,45]),
                        bloc(9,[9,1,3,3])
                    ]))
ma_table.add_tasseau(8, tasseau(blocs=[
                        bloc(81,[9,9,3,27]),
                        bloc(18,[9,2,3,6])
                    ]))
ma_table.add_tasseau(9, tasseau(blocs=[
                        bloc(72,[9,8,2,36]),
                        bloc(27,[9,3,9,3])
                    ]))
ma_table.add_tasseau(10, tasseau(blocs=[
                        bloc(63,[9,7,3,21]),
                        bloc(36,[9,4,3,12])
                    ]))
ma_table.add_tasseau(11, tasseau(blocs=[
                        bloc(54,[9,6,2,27]),
                        bloc(45,[9,5,3,15])
                    ]))
ma_table.add_tasseau(12, tasseau(blocs=[
                        bloc(80,[8,10,2,40]),
                        bloc(15,[3,5,3,5]),
                        bloc(3,[3,1,3,1])
                    ]))
ma_table.add_tasseau(13, tasseau(blocs=[
                        bloc(72,[8,9,4,18]),
                        bloc(16,[8,2,4,4]),
                        bloc(10,[1,10,2,5])
                    ]))
ma_table.add_tasseau(14, tasseau(blocs=[
                        bloc(64,[8,8,2,32]),
                        bloc(24,[8,3,6,4]),
                        bloc(10,[5,2,1,10])
                    ]))
ma_table.add_tasseau(15, tasseau(blocs=[
                        bloc(56,[8,7,2,28]),
                        bloc(32,[8,4,2,16]),
                        bloc(9,[1,9,3,3])
                    ]))
ma_table.add_tasseau(16, tasseau(blocs=[
                        bloc(48,[8,6,2,24]),
                        bloc(40,[8,5,4,10]),
                        bloc(10,[2,5,1,10])
                    ]))
ma_table.add_tasseau(17, tasseau(blocs=[
                        bloc(70,[7,10,2,35]),
                        bloc(7,[7,1,7,1]),
                        bloc(20,[2,10,2,10])
                    ]))
ma_table.add_tasseau(18, tasseau(blocs=[
                        bloc(63,[7,9,3,21]),
                        bloc(14,[7,2,7,2]),
                        bloc(18,[2,9,3,6]),
                        bloc(2,[2,1,2,1])
                    ]))
ma_table.add_tasseau(19, tasseau(blocs=[
                        bloc(56,[7,8,4,14]),
                        bloc(21,[7,3,7,3]),
                        bloc(16,[2,8,4,4]),
                        bloc(4,[2,2,1,4])
                    ]))
ma_table.add_tasseau(20, tasseau(blocs=[
                        bloc(49,[7,7,7,7]),
                        bloc(28,[7,4,2,14]),
                        bloc(14,[2,7,2,7]),
                        bloc(6,[2,3,1,6])
                    ]))
ma_table.add_tasseau(21, tasseau(blocs=[
                        bloc(42,[7,6,2,21]),
                        bloc(30,[6,5,3,10]),
                        bloc(12,[2,6,3,4]),
                        bloc(12,[4,3,2,6])
                    ]))
ma_table.add_tasseau(22, tasseau(blocs=[
                        bloc(60,[6,10,2,30]),
                        bloc(6,[6,1,2,3]),
                        bloc(30,[3,10,2,15]),
                        bloc(1,[1,1,1,1])
                    ]))
ma_table.add_tasseau(23, tasseau(blocs=[
                        bloc(54,[6,9,3,18]),
                        bloc(12,[6,2,3,4]),
                        bloc(27,[3,9,3,9]),
                        bloc(4,[1,4,2,2])
                    ]))
ma_table.add_tasseau(24, tasseau(blocs=[
                        bloc(48,[6,8,3,16]),
                        bloc(18,[6,3,2,9]),
                        bloc(24,[3,8,2,12]),
                        bloc(6,[3,2,1,6])
                    ]))
ma_table.add_tasseau(25, tasseau(blocs=[
                        bloc(42,[6,7,3,14]),
                        bloc(24,[6,4,3,8]),
                        bloc(20,[5,4,10,2]),#
                        bloc(7,[1,7,1,7]),
                        bloc(3,[1,3,1,3])
                    ]))
ma_table.add_tasseau(26, tasseau(blocs=[
                        bloc(36,[6,6,4,9]),
                        bloc(35,[7,5,7,5]),
                        bloc(20,[4,5,2,10]),
                        bloc(6,[1,6,2,3])
                    ]))
ma_table.add_tasseau(27, tasseau(blocs=[
                        bloc(50,[5,10,2,25]),
                        bloc(5,[1,5,5,1]),
                        bloc(40,[4,10,2,20]),
                        bloc(2,[1,2,1,2])
                    ]))
ma_table.add_tasseau(28, tasseau(blocs=[
                        bloc(45,[5,9,3,15]),
                        bloc(36,[4,9,2,18]),
                        bloc(16,[4,4,2,8])
                    ]))
ma_table.add_tasseau(29, tasseau(blocs=[
                        bloc(40,[5,8,4,10]),
                        bloc(15,[5,3,3,5]),
                        bloc(32,[4,8,2,16]),
                        bloc(4,[4,1,2,2]),
                        bloc(5,[1,5,1,5])
                    ]))
ma_table.add_tasseau(30, tasseau(blocs=[
                        bloc(35,[5,7,5,7]),
                        bloc(21,[3,7,3,7]),
                        bloc(28,[4,7,2,14]),
                        bloc(12,[3,4,2,6])
                    ]))
ma_table.add_tasseau(31, tasseau(blocs=[
                        bloc(30,[5,6,3,10]),
                        bloc(25,[5,5,5,5]),
                        bloc(24,[4,6,2,12]),
                        bloc(18,[3,6,2,9])
                    ]))
# On imprime 9 tasseaux à la fois :
ma_table.genere('TABLE_1_', range(1,10))
ma_table.genere('TABLE_2_', range(10,19))
ma_table.genere('TABLE_3_', range(19,28))
ma_table.genere('TABLE_4_', range(28,32))
