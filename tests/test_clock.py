import datetime
import unittest

from bin.lib import _clock


class ClockHelpersTest(unittest.TestCase):
    def setUp(self):
        self.moment = datetime.datetime(2026, 1, 2, 3, 4, 5, 678901)

    def test_components(self):
        self.assertEqual(_clock.hour(self.moment), 3)
        self.assertEqual(_clock.minute(self.moment), 4)
        self.assertEqual(_clock.mint(self.moment), 4)  # deprecated alias
        self.assertEqual(_clock.sec(self.moment), 5)

    def test_timestamp_is_zero_padded(self):
        self.assertEqual(_clock.timestamp(moment=self.moment), "03:04:05")

    def test_timestamp_custom_format(self):
        self.assertEqual(_clock.timestamp("%Y-%m-%d %H:%M", self.moment), "2026-01-02 03:04")

    def test_now_utc_is_aware(self):
        self.assertIsNotNone(_clock.now(utc=True).tzinfo)

    def test_now_local_is_naive(self):
        self.assertIsNone(_clock.now().tzinfo)


if __name__ == "__main__":
    unittest.main()
