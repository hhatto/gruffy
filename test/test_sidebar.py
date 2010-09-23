from gruffy import SideBar

g = SideBar()
g.theme_pastel()
g.theme_greyscale()

g.data("test1", [1, 2, 3])
g.data("test2", [3, 2, 1])
g.write('gruffy_sidebar.png')
