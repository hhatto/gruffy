import os
from unittest import TestCase, main
from gruffy import StackedSideBar

TARGET_FILE = 'test.png'


class TestStackedArea(TestCase):

    def tearDown(self):
        os.remove(TARGET_FILE)

    def test_writable(self):
        g = StackedSideBar()
        g.data("test1", [1, 2, 3])
        g.data("test2", [3, 2, 1])
        g.write(TARGET_FILE)

if __name__ == '__main__':
    main()
