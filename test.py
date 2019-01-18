import svgwrite

dwg = svgwrite.Drawing(filename="toto.svg", size=(200, 200), debug=True)

g1=dwg.defs.add(dwg.g())
g1.add(dwg.rect(insert=(0,0),size=(10,10),fill="blue"))

g2=dwg.defs.add(dwg.g())
g2.add(dwg.rect(insert=(0,0),size=(20,20),fill="red"))


g1=dwg.use(g1, insert=(50,50))
dwg.add(g1)

g2=dwg.use(g2, insert=(100,100))
dwg.add(g2)

dwg.save()
