# Valorant Airsoft Gun Project

This project integrates a custom airsoft gun setup with the game Valorant, providing real-time feedback by physically shooting the user whenever they take damage in-game. The system uses a combination of computer vision, an ESP32 microcontroller, and a relay to control the airsoft gun.

## Overview

The Valorant Airsoft Gun project combines hardware and software to deliver an immersive and intense gaming experience. By leveraging Python's OpenCV (cv2) library, the system continuously analyzes the Valorant game feed to detect when the player is shot. Upon detecting damage, a command is sent via Bluetooth to an ESP32 microcontroller, which then triggers a relay to control the airsoft gun, shooting the user in sync with the in-game events.

## Features

- **Real-Time Damage Detection**: Uses OpenCV to analyze the game screen and detect when the player takes damage.
- **Bluetooth Integration**: Communicates with the ESP32 microcontroller via Bluetooth to control the airsoft gun.
- **Relay-Controlled Firing**: The ESP32 uses a relay to control the power supply from the airsoft gun battery to the DC motor, effectively firing the gun when triggered.
- **Single Power Source**: Both the ESP32 and the airsoft gun are powered by the airsoft gun's battery, simplifying the hardware setup.

## Hardware Components

- **ESP32 Microcontroller**: Runs the Arduino code to receive Bluetooth commands and control the relay.
- **Relay**: Used to manage the power flow from the battery to the airsoft gun’s DC motor.
- **DC Motor Airsoft Gun**: Fires when powered, controlled via the relay mechanism.
- **Power Source**: Airsoft gun battery, which powers both the gun and the ESP32.
- **Airsoft Gun Used**: [Here is the link to the specific airsoft gun used in this project.](https://www.amazon.com/gp/product/B0082COWEI/ref=ppx_yo_dt_b_search_asin_title?ie=UTF8&psc=1)

## Software Components

- **Python with OpenCV (cv2)**: Analyzes the live Valorant gameplay feed to detect when the player takes damage.
- **Arduino Code on ESP32**: Manages Bluetooth communication and relay control to fire the airsoft gun in response to commands from the Python script.

## How It Works

1. **Setup**: The ESP32 is connected to the relay, which in turn is connected to the airsoft gun's DC motor. The ESP32 and airsoft gun share the same battery for power.
2. **Gameplay Detection**: The Python script uses OpenCV to continuously monitor the Valorant gameplay feed. When the script detects that the player has been shot, it sends a Bluetooth command to the ESP32.
3. **Relay Activation**: Upon receiving the command, the ESP32 activates the relay, allowing power from the battery to flow to the airsoft gun's motor, which then fires.
4. **Real-Time Feedback**: The firing of the airsoft gun is synchronized with the in-game damage detection, creating a physical response every time the player is hit in the game.

## Requirements

- **Python 3.x**
- **OpenCV (cv2)**
- **Arduino IDE** (for uploading code to the ESP32)
- **Bluetooth-enabled PC** (to communicate with the ESP32)

## Installation

1. **Clone the Repository**:
   ```bash
   git clone [repository-url]
2. **Install the required Python libraries**:
   ```bash
   pip install opencv-python
3. **Upload Arduino Code**:
   - Open the Arduino IDE, upload the ESP32 code to your ESP32 device
   - Turn on the ESP32 and connect it via bluetooth to your PC or other device as you would any other bluetooth device
4. **Run the Python script**

## Usage

1. Connect your ESP32 to the airsoft gun and battery
2. Start Valorant and ensure your game feed is visible on the screen. (You may need to adjust point array to fit your health in rectangle based on monitor resolution)
3. Run the Python script to begin real-time monitoring.
4. Play Valorant, and the airsoft gun will fire whenever the script detects that you've been shot.

## Safety Note

**WARNING**: This project involves physical feedback and should be used with caution. Ensure all safety measures are in place to prevent injury while using the airsoft gun.

## License

This project is licensed under the MIT License. See the `LICENSE` file for more details.

## Contact Me

If you have any questions or want to learn more about this project, feel free to reach out!

- **LinkedIn**: [David Lee](https://www.linkedin.com/in/david-lee-499a4a237/)
- **Email**: [david303lee@gmail.com](mailto:david303lee@gmail.com)
