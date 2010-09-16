import sys
sys.path.append('./gruffy')
from line import Line
from bar import Bar
from side_bar import SideBar

g = Line()
g = Bar()
g = SideBar()
g.theme_greyscale()
g.title = "Gruffy's Graph"

g.data("Apples", [1, 2, 3, 4, 4, 3])
g.data("Oranges", [4, 8, 7, 9, 8, 9])
g.data("Watermelon", [2, 3, 1, 5, 6, 8])
g.data("Peaches", [9, 9, 10, 8, 7, 9])

g.labels = {0: '2003', 2: '2004', 4: '2005'}

g.write('py_graph.png')
