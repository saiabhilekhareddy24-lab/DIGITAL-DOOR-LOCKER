 Digital Door Locker System
Introduction
The Digital Door Locker System is a Python-based security system that simulates an electronic door lock using a PIN/password mechanism.

The system allows a user to enter a PIN to unlock the door. If the correct PIN is entered, the door is unlocked. If an incorrect PIN is entered three times, the system becomes blocked.
Features
PIN-based door unlocking
Door locking
PIN changing
Door status checking
Maximum three incorrect attempts
Automatic system blocking after three incorrect attempts
Input validation
Automated unit testing
Technologies Used
Python 3
Object-Oriented Programming
Python unittest framework
Default PIN
1234

Project Structure
digital-door-locker/
│
├── digital_door_locker.py
├── test_door_locker.py
├── README.md
├── requirements.txt
└── output.txt
How to Run
Install Python 3 on your computer.

Open the project directory in a terminal and run:

python digital_door_locker.py

The following menu will appear:

1. Enter PIN
2. Lock Door
3. Change PIN
4. Check Status
5. Exit
6. How to Run Tests
Run:

python -m unittest test_door_locker.py -v

The test bench checks:

Initial door status
Correct PIN
Incorrect PIN
Three failed attempts
Door locking
PIN changing
Invalid PIN
Working Principle
The system starts with the door locked.

The user enters a four-digit PIN.

Working Principle
The system starts with the door locked.

The user enters a four-digit PIN.

Correct PIN
If the entered PIN matches the stored PIN:

CORRECT PIN: Door unlocked successfully.
Incorrect PIN
If the PIN is incorrect, the number of remaining attempts is displayed.

After three consecutive incorrect attempts, the system is blocked.

INCORRECT PIN: Maximum attempts reached. System blocked.
Future Improvements
The project can be expanded by connecting it to actual hardware such as:

Arduino
Raspberry Pi
Keypad
Servo motor
LCD display
Buzzer
RFID reader
Fingerprint sensor
Conclusion
The Digital Door Locker System demonstrates how Python can be used to implement a basic electronic security system. It uses PIN authentication, attempt limitations, door status management, and automated testing.
