from gruffy import Bezier

g = Bezier()
g.title = "Gruffy's Graph"

g.data("Apples", [1, 290, 300])
g.data("Oranges", [1, 8, 350])

g.labels = {0: '2003', 1: '2004', 2: '2005'}
g.transparent = 0.7

g.write('gruffy-bezier.png')
