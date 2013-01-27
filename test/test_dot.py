import os
from unittest import TestCase, main
from gruffy import Dot

TARGET_FILE = 'test.png'


class TestDot(TestCase):

    def tearDown(self):
        os.remove(TARGET_FILE)

    def test_writable(self):
        g = Dot()
        g.data("test1", [1, 2, 3])
        g.data("test2", [3, 2, 1])
        g.write(TARGET_FILE)

if __name__ == '__main__':
    main()
