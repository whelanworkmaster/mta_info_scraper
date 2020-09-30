import unittest

from scripts.timer import Timer


class StatusManagerTest(unittest.TestCase):

    def test_shouldReturnTimer(self):

        timer = Timer()
        timer.start()

        timer.stop()

        print(timer.get_time())
