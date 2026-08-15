import unittest
from digital_door_locker import DigitalDoorLocker


class TestDigitalDoorLocker(unittest.TestCase):

    def setUp(self):
        self.locker = DigitalDoorLocker()

    def test_initial_status(self):
        self.assertEqual(
            self.locker.status(),
            "STATUS: DOOR LOCKED"
        )

    def test_correct_pin_unlocks_door(self):
        result = self.locker.enter_pin("1234")

        self.assertEqual(
            result,
            "CORRECT PIN: Door unlocked successfully."
        )

        self.assertFalse(self.locker.is_locked)

    def test_wrong_pin(self):
        result = self.locker.enter_pin("1111")

        self.assertEqual(
            result,
            "INCORRECT PIN: 2 attempt(s) remaining."
        )

    def test_system_blocks_after_three_wrong_attempts(self):
        self.locker.enter_pin("1111")
        self.locker.enter_pin("2222")
        result = self.locker.enter_pin("3333")

        self.assertEqual(
            result,
            "INCORRECT PIN: Maximum attempts reached. System blocked."
        )

        self.assertTrue(self.locker.is_blocked)

    def test_lock_door(self):
        self.locker.enter_pin("1234")
        result = self.locker.lock_door()

        self.assertEqual(
            result,
            "DOOR LOCKED SUCCESSFULLY."
        )

        self.assertTrue(self.locker.is_locked)

    def test_change_pin(self):
        result = self.locker.change_pin("1234", "5678")

        self.assertEqual(
            result,
            "PIN CHANGED SUCCESSFULLY."
        )

        self.locker.enter_pin("5678")

        self.assertFalse(self.locker.is_locked)

    def test_invalid_new_pin(self):
        result = self.locker.change_pin("1234", "123")

        self.assertEqual(
            result,
            "ERROR: New PIN must contain exactly 4 digits."
        )


if __name__ == "__main__":
    unittest.main()
  
