from gruffy import AccumulatorBar

g = AccumulatorBar()
g.title = "Gruffy's Graph"

g.data("add", [10, 50, 150, 20])

g.hide_legend = True
g.labels = {0: '2003', 1: '2004', 2: '2005', 3: '2006'}
g.transparent = 0.7
g.y_axis_increment = 50
g.maximum_value = 300

g.write('gruffy-accumulatorbar.png')
