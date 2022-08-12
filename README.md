# CanSat telemetry receiver
![Program](https://github.com/Yarosvet/cansat_telemetry/raw/main/screenshot.png)

CanSat2022 telemetry receiver for my sattellite.
# Receiver
Receiver based on Arduino and nRf24l01 2.4Ghz radio module. See *rx_serial.py* to understand how does it work and change it to make this programm working with your own receiver.
Connect the Arduino board to PC through USB, then choose arduino in the device list and set the Serial port number.
# Run
```bash
pip3 install -r requiremets.txt
python3 main.py
```
