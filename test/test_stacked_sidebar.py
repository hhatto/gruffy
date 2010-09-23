from gruffy.stacked_sidebar import StackedSideBar

g = StackedSideBar()

g.data("test1", [1, 2, 3])
g.data("test2", [3, 2, 1])
g.write('gruffy_stacked_sidebar.png')
