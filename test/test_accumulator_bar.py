import os
from unittest import TestCase, main
from gruffy import AccumulatorBar

TARGET_FILE = 'test.png'


class TestAccumulatorBar(TestCase):

    def tearDown(self):
        os.remove(TARGET_FILE)

    def test_writable(self):
        g = AccumulatorBar()
        g.theme_pastel()
        g.theme_greyscale()

        g.data("test1", [1, 2, 3])
        g.write(TARGET_FILE)

if __name__ == '__main__':
    main()
