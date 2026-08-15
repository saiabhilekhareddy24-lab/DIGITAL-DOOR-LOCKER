class DigitalDoorLocker:
    def __init__(self, correct_pin="1234", max_attempts=3):
        self.correct_pin = correct_pin
        self.max_attempts = max_attempts
        self.attempts = 0
        self.is_locked = True
        self.is_blocked = False

    def enter_pin(self, pin):
        """Check the entered PIN and unlock the door if correct."""

        if self.is_blocked:
            return "SYSTEM BLOCKED: Too many incorrect attempts."

        if not self.is_locked:
            return "DOOR ALREADY UNLOCKED."

        if pin == self.correct_pin:
            self.is_locked = False
            self.attempts = 0
            return "CORRECT PIN: Door unlocked successfully."

        self.attempts += 1
        remaining = self.max_attempts - self.attempts

        if self.attempts >= self.max_attempts:
            self.is_blocked = True
            return "INCORRECT PIN: Maximum attempts reached. System blocked."

        return f"INCORRECT PIN: {remaining} attempt(s) remaining."

    def lock_door(self):
        """Lock the door again."""

        if self.is_blocked:
            return "SYSTEM BLOCKED: Door cannot be operated."

        self.is_locked = True
        return "DOOR LOCKED SUCCESSFULLY."

    def change_pin(self, old_pin, new_pin):
        """Change the current PIN."""

        if self.is_blocked:
            return "SYSTEM BLOCKED: PIN cannot be changed."

        if old_pin != self.correct_pin:
            return "ERROR: Old PIN is incorrect."

        if not new_pin.isdigit() or len(new_pin) != 4:
            return "ERROR: New PIN must contain exactly 4 digits."

        self.correct_pin = new_pin
        return "PIN CHANGED SUCCESSFULLY."

    def status(self):
        """Return the current door status."""

        if self.is_blocked:
            return "STATUS: SYSTEM BLOCKED"

        if self.is_locked:
            return "STATUS: DOOR LOCKED"

        return "STATUS: DOOR UNLOCKED"


def main():
    locker = DigitalDoorLocker()

    print("=" * 40)
    print("       DIGITAL DOOR LOCKER")
    print("=" * 40)

    while True:
        print("\n1. Enter PIN")
        print("2. Lock Door")
        print("3. Change PIN")
        print("4. Check Status")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            pin = input("Enter 4-digit PIN: ")
            print(locker.enter_pin(pin))

        elif choice == "2":
            print(locker.lock_door())

        elif choice == "3":
            old_pin = input("Enter old PIN: ")
            new_pin = input("Enter new 4-digit PIN: ")
            print(locker.change_pin(old_pin, new_pin))

        elif choice == "4":
            print(locker.status())

        elif choice == "5":
            print("Thank you for using Digital Door Locker.")
            break

        else:
            print("INVALID CHOICE: Please select 1-5.")


if __name__ == "__main__":
    main()
      
