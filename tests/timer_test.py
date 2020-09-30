import unittest

from scripts.timer import Timer


class StatusManagerTest(unittest.TestCase):

    def test_shouldReturnTotalTimeGreaterThanZeroWhenStartingAndStoppingTimer(self):

        timer = Timer()
        timer.start()

        timer.stop()

        self.assertTrue(timer.get_time() > 0)

    def test_shouldReturnTotalTimeGreaterThanZeroWhenStartingTimer(self):

        timer = Timer()
        timer.start()

        self.assertTrue(timer.get_time() > 0)

    def test_shouldReturnTotalTimeZeroWhenGettingTotalTimeWithoutStartingTimer(self):

        timer = Timer()

        self.assertEqual(timer.get_time(), 0.0)
