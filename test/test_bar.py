import os
from unittest import TestCase, main
from gruffy import Bar

TARGET_FILE = 'test.png'


class TestBar(TestCase):

    def tearDown(self):
        os.remove(TARGET_FILE)

    def test_writable(self):
        g = Bar()
        g.data("test1", [1, 2, 3])
        g.write(TARGET_FILE)

if __name__ == '__main__':
    main()
