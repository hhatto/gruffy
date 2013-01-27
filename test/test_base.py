import os
from unittest import TestCase, main
from gruffy.base import Base

TARGET_FILE = 'test.png'


class TestBase(TestCase):

    def tearDown(self):
        os.remove(TARGET_FILE)

    def test_writable(self):
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
        g.write(TARGET_FILE)

if __name__ == '__main__':
    main()
