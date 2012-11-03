from gruffy import Bar

g = Bar()
g.title = "Gruffy's Graph"

g.data("Apples", [1, 2, 3, 4, 4, 3])
g.data("Oranges", [4, 8, 7, 9, 8, 9])
g.data("Watermelon", [2, 3, 1, 5, 6, 8])
g.data("Peaches", [9, 9, 10, 8, 7, 9])

g.labels = {0: '2003', 2: '2004', 4: '2005'}
g.transparent = 0.7
g.additional_line_values = True

g.write('gruffy.png')
