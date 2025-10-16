"""
Serial Port Sender - Test Script for Windows
Sends test messages through a serial port to verify cable connection.
"""

import serial
import time
import sys

# Configuration
PORT = 'COM3'  # Change this to your Windows COM port (check Device Manager)
BAUD_RATE = 9600
TIMEOUT = 1

def main():
    print(f"Attempting to open serial port {PORT} at {BAUD_RATE} baud...")

    try:
        ser = serial.Serial(PORT, BAUD_RATE, timeout=TIMEOUT)
        print(f"Successfully opened {PORT}")
        print("Sending test messages... (Press Ctrl+C to stop)")
        print("-" * 50)

        counter = 0
        while True:
            counter += 1
            message = f"Test message #{counter} from Windows\n"
            ser.write(message.encode('utf-8'))
            print(f"Sent: {message.strip()}")
            time.sleep(2)

    except serial.SerialException as e:
        print(f"Error: Could not open serial port {PORT}")
        print(f"Details: {e}")
        print("\nTroubleshooting:")
        print("1. Check Device Manager to find the correct COM port")
        print("2. Make sure no other program is using the port")
        print("3. Verify the serial cable is connected")
        sys.exit(1)

    except KeyboardInterrupt:
        print("\n\nStopping...")
        ser.close()
        print("Serial port closed.")
        sys.exit(0)

if __name__ == "__main__":
    main()
