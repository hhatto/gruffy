from gruffy import Area

g = Area(800)
g.title = "Gruffy's Graph"

g.theme_pastel()
g.transparent = True
g.data("Apples", [1, 2, 3, 4, 4, 3])
g.data("Oranges", [4, 8, 7, 9, 8, 9])
g.data("Watermelon", [2, 3, 1, 5, 6, 8])
g.data("Peaches", [9, 9, 10, 8, 7, 9])
g.labels = {0: '2003', 2: '2004', 4: '2005.09'}

g.additional_line_values = True

g.write()
