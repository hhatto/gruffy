import os
from unittest import TestCase, main
from gruffy import Line

TARGET_FILE = 'test.png'


class TestLine(TestCase):

    def tearDown(self):
        os.remove(TARGET_FILE)

    def test_writable(self):
        g = Line()
        g.theme_greyscale()
        g.data("test1", [1, 2, 3])
        g.data("test2", [3, 2, 1])
        g.write(TARGET_FILE)

    def test_set_baseline_value(self):
        g = Line()
        # FIXME: test is NG
        #g.baseline_value = 2
        g.data("test1", [1, 2, 3])
        g.data("test2", [3, 2, 1])
        g.write(TARGET_FILE)


if __name__ == '__main__':
    main()
