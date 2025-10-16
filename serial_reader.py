import serial
import time

def main():
    # Configuration - modify these parameters as needed
    PORT = '/dev/cu.PL2303G-USBtoUART210'  # Change based on your system
    BAUD_RATE = 9600       # Match your device's configuration

    try:
        # Initialize serial connection
        ser = serial.Serial(
            port=PORT,
            baudrate=BAUD_RATE,
            bytesize=serial.EIGHTBITS,
            parity=serial.PARITY_NONE,
            stopbits=serial.STOPBITS_ONE,
            timeout=1,
            rtscts=False,  # Disable hardware flow control
            dsrdtr=False   # Disable DTR/DSR flow control
        )
        print(f"Connected to {PORT} at {BAUD_RATE} baud")
        print("Waiting for data... (Press Ctrl+C to exit)")

        # Read and display data
        while True:
            if ser.in_waiting > 0:
                # Read raw bytes first to see what we're getting
                raw_data = ser.read(ser.in_waiting)
                print(f"Raw bytes ({len(raw_data)}): {raw_data}")
                # Try to decode as ASCII
                try:
                    decoded = raw_data.decode('ascii', errors='replace')
                    print(f"Decoded: {decoded}")
                except Exception as e:
                    print(f"Decode error: {e}")
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
