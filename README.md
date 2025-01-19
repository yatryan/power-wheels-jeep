# Power Wheels Jeeps - Raspberry Pi Pico with OTA Updates

This project uses **Raspberry Pi Pico microcontrollers** to handle communication, sensor management, and over-the-air (OTA) firmware updates for two **Power Wheels Jeeps**. The motor control is managed by external motor drivers, while the Picos handle tasks such as reading sensor data, coordinating with wireless modules, and enabling the OTA update process.

## Features
- **Dual Raspberry Pi Pico Setup**: Two Picos manage communication, sensors, and OTA updates for each Jeep.
- **OTA Firmware Updates**: Each Pico automatically checks for new firmware on boot and updates itself over-the-air (OTA).
- **Sensor and Communication Management**: The Picos manage data from sensors (e.g., battery voltage, speed, temperature) and communicate with external devices (e.g., remote control, motor driver). (TBD)
- **Modular Motor Control**: Motor drivers control the motors based on input from the Raspberry Pi Picos (via GPIO or communication protocol). (TBD)

## Components
- **Hardware**:
  - 2x Raspberry Pi Pico W
  - **Motor Driver Modules** (e.g., L298N, VNH2SP30) to control Power Wheels motors. (TBD) 
  - Sensors for various parameters (e.g., battery voltage, temperature, speed). (TBD)
  - Power supply for Raspberry Pi Picos and motor drivers.
- **Software**:
  - MicroPython for Raspberry Pi Pico.
  - Custom OTA update mechanism using a server or cloud service.

## Setup

### 1. Hardware Assembly
- **Motor Control**: Connect the motor drivers to the Power Wheels motors according to the motor driver's documentation. The Raspberry Pi Pico will not control the motors directly but will send commands (e.g., PWM, serial commands) to the motor driver.
- **Sensors**: Connect various sensors to the Raspberry Pi Pico GPIO pins to read data such as battery voltage, temperature, and speed.
- **Wireless Module**: Connect an ESP8266/ESP32 or similar wireless module to the Raspberry Pi Pico to facilitate OTA updates. This module will communicate with a central server to check for new firmware versions.

### 2. Installing CircuitPython / MicroPython
1. Download and install **CircuitPython** or **MicroPython** for Raspberry Pi Pico from the [official websites](https://circuitpython.org/board/raspberry_pi_pico/).
2. Flash the firmware to the Pico using the drag-and-drop method.

### 3. Flash the Firmware
Clone the repository and flash the firmware to your Raspberry Pi Pico:

```bash
git clone https://github.com/yatryan/power-wheels-jeep.git
cp -r power-wheels-jeep/* /Volumes/CIRCUITPY/
```

> Created by ChatGPT