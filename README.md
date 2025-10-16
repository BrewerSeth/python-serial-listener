## 📄 README.md

# Serial Terminal Reader

A simple Python application that reads data from a serial port and displays it in the terminal.

## 📦 Requirements
- Python 3.x
- `pyserial` library (install with `pip install pyserial`)

## 🚀 Usage
1. Modify the `PORT` and `BAUD_RATE` variables in `serial_reader.py` to match your hardware
2. Run the script:
```bash
python serial_reader.py
```
3. Data will be displayed in the terminal as it arrives

## 🔧 Configuration
Edit these parameters in the script:
```python
PORT = '/dev/ttyUSB0'      # Change based on your system
BAUD_RATE = 9600           # Match your device's configuration
```

## 📌 Notes
- Common ports:
  - Linux: `/dev/ttyUSB0`, `/dev/ttyACM0`
  - Windows: `COM3`, `COM4`
  - Mac: `/dev/cu.usbmodem1411`
- Press `Ctrl+C` to exit the program


Remeber to use the virtual environment

``` bash
source venv/bin/activate
```