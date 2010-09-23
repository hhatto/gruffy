from gruffy.base import Base

g = Base()
g.theme_keynote()
g.theme_django()
g.theme_pastel()
g.theme_greyscale()
g.theme_37signals()
g.theme_rails_keynote()
g.theme_odeo()

g.data("test1", [1, 2, 3])
g.data("test2", [3, 2, 1])
g.write()
