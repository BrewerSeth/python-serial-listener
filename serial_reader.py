import serial
import time

def main():
    # Configuration - modify these parameters as needed
    PORT = '/dev/ttyUSB0'  # Change based on your system
    BAUD_RATE = 9600       # Match your device's configuration
    
    try:
        # Initialize serial connection
        ser = serial.Serial(PORT, BAUD_RATE, timeout=1)
        print(f"Connected to {PORT} at {BAUD_RATE} baud")
        
        # Read and display data
        while True:
            if ser.in_waiting > 0:
                data = ser.readline().decode('utf-8').strip()
                print(f"Received: {data}")
            time.sleep(0.1)
    
    except serial.SerialException as e:
        print(f"Error: Could not connect to {PORT}")
        print(f"Detail: {e}")
        print("Try checking:")
        print("1. That the device is properly connected")
        print("2. The correct COM port (try 'ls /dev/tty*' on Linux)")
        print("3. The baud rate matches your device's configuration")
    
    except KeyboardInterrupt:
        print("\nClosing serial connection...")
        ser.close()
        print("Done.")

if __name__ == "__main__":
    main()
