from gruffy.stacked_bar import StackedBar

g = StackedBar()

g.data("test1", [1, 2, 3])
g.data("test2", [3, 2, 1])
g.write('gruffy_stacked_bar.png')
