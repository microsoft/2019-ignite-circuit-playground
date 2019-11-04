# Welcome to CircuitPython, the Circuit Playground Express, and the Device Simulator Express

This sample demonstrates the basic functionality of the Circuit Playground Express (CPX) and the Visual Studio Device Simulator Express extension. 

The Circuit Playground Express is brought to you by Adafruit. It's pre-loaded with CircuitPython! CircuitPython is Adafruit's branch of MicroPython, designed to simplify experimentation and education on low-cost microcontrollers. It makes it easier than ever to get prototyping with Visual Studio Code.

![Circuit Playground Express with lights on](https://github.com/microsoft/2019-ignite-circuit-playground/blob/master/Circuit_Playground_Express.jpg)

The Device Simulator Express extension for VS Code, a Microsoft Garage project, allows you to code in CircuitPython for CPX projects. Test and debug your code on the device simulator and see the same result when you plug in your actual microcontroller. Observe the output of the device with the serial monitor.

![Device Simulator Express new file side by side with simulator](https://github.com/microsoft/2019-ignite-circuit-playground/blob/master/Device-Simulator-Express-Screenshot.jpg)

## What's on the device

The pre-loaded demo shows off some of what your Circuit Playground Express can do with CircuitPython:
* The NeoPixel ring on the CPX animates with orange and white colors.
* The switch controls the direction of the animation. Move the switch left and right to change the direction.
* Press and hold Button A to dim the lights and Button B to brighten.
* The touch pads labeled A1-A7 to play a scale of tones. Change the `TONE_PIANO` variable to `False` at the top of the file to disable the tone piano.
* After installing the extension, connect to the serial port to print temperature, light intensity, and acceleration sensor readings in the console. 
* Shake the device to pause the lights and sensor reporting. Shake again to restart.

See "Formatting the device" below to return to this state or load the demo on a non-Ignite CPX.

## Prerequisites

The following dependencies are required before launching Device Simulator Express:
* [Visual Studio Code](https://code.visualstudio.com/)
* [Node](https://nodejs.org/en/download/)
* [Python 3.7.4](https://www.python.org/downloads/)
  * Make sure Python and pip are added to the PATH environment variables. To check whether Python has been added, type *python* in a terminal. Version 3.7.4 should print out. 
  * If installing Python, select the "Add to PATH" option to add directly on install.
  * If Python is already installed but not not a PATH variable, search for instructions given your OS.
  
Install the Device Simulator Express extension:
* [Device Simulator Express extension](https://marketplace.visualstudio.com/items?itemName=ms-python.devicesimulatorexpress)
* [Python VS Code extension](https://marketplace.visualstudio.com/items?itemName=ms-python.python)
  * This will be automatically installed with Device Simulator Express

The following Python dependencies will be installed by the Device Simulator Express extension on first use by clicking yes when prompted. Alternatively, install manually by typing the following commands in a console:
* **Playsound**: `pip install playsound`
* **Python-Socketio**: `pip install python-socketio`
* **Requests**: `pip install requests`
* **Application Insights**: `pip install applicationinsights`

If using Windows, install this additional Python dependency. It will not automatically install with the extension.
Type the following command in a console:
* **Pywin 32**: `pip install pywin32`

## Setup and running the sample
CircuitPython code can run with either the simulator in VS Code or be deployed to the device.

### Simulator - using the Device Simulator Express Extension
After installing the prerequisites and the Device Simulator Express extension, reload VS Code. To get started with the simulator:
1. Start with a new file or open an sample. Create a new file with the "New File" command. `CTRL+SHIFT+P` to open the command palette and type `Device Simulator Express: New File`. Alternatively, open an existing .py file or sample.
2. Run the code on the simulator. Run `Device Simulator Express: Run Simulator` from the command palette or the play icon in the editor toolbar.
 
For a detailed and visual walkthrough, visit the Device Simulator Express home page in the Visual Studio Marketplace: https://marketplace.visualstudio.com/items?itemName=ms-python.devicesimulatorexpress.
 
### Device - deploy and run code on the Circuit Playground Express
Deploy code to the device:
1. Save the file as "code.py".
2. Connect the device to the computer via USB. It should be recognized as a drive.
3. Replace the "code.py" file on the device. In the command palette type `Device Simulator Express: Deploy to Device`. The CPX will reboot and run the code.

If you want to work directly from the device, open the device as a folder in VS Code. Editing and saving the .py file will cause the device to reboot and run the code without the extra step of copying the file.

Use the Serial Monitor to see sensor data from the CPX (available on Windows or Mac only):
1. Plug in the CPX.
2. Run the command `Device Simulator Express: Open Serial Monitor`.
3. Select the serial port and, if required, set baud rate.
4. With the pre-loaded demo you'll see temperature, light, and accelerometer data. Use print() statements in code to show output in the console.

### Formatting the device

If you picked up the device from the Development and Architecture Center at Ignite and the device boots and animates with orange and white lights, you're good to go. Edit the code.py file.

If you acquired the device elsewhere, follow these tutorials for formatting: 
1. Download the firmware with the .uf2 file: https://learn.adafruit.com/adafruit-circuit-playground-express/circuitpython-quickstart
2. Download the latest version of the cpx library: https://learn.adafruit.com/welcome-to-circuitpython/circuitpython-libraries

If you'd like to return to the initial Ignite state, download the files from `initial_board`.

*Note: Name your file  "code.py". The device automatically runs the "code.py" file.*

## Useful links
Visit the CPX product page for more info on the device: https://adafruit.com/product/3333. To get started with CircuitPython, which comes built into the CPX, visit: https://learn.adafruit.com/welcome-to-circuitpython.

* Tutorials and Example Code for Adafruit CPX:
  * Adafruit CPX library tutorial: https://learn.adafruit.com/circuitpython-made-easy-on-circuit-playground-express/circuit-playground-express-library
  * Adafruit CPX Examples on GitHub: https://github.com/adafruit/Adafruit_CircuitPython_CircuitPlayground/tree/master/examples
  * Adafruit CPX Guided Tour (Intro for the Hardware): https://learn.adafruit.com/adafruit-circuit-playground-express/guided-tour

* Device Simulator Express download and guide: https://marketplace.visualstudio.com/items?itemName=ms-python.devicesimulatorexpress

## About Device Simulator Express
The Device Simulator Express extension is an open source extension built by Microsoft Garage interns. To learn more about the extension and contribute visit: https://github.com/microsoft/vscode-python-devicesimulator.

## Contents

| File/folder       | Description                                |
|-------------------|--------------------------------------------|
| `initial_board`   | Sample source code from Ignite.            |
| `.gitignore`      | Define what to ignore at commit time.      |
| `CHANGELOG.md`    | List of changes to the sample.             |
| `CONTRIBUTING.md` | Guidelines for contributing to the sample. |
| `README.md`       | This README file.                          |
| `LICENSE`         | The license for the sample.                |

## Contributing

This project welcomes contributions and suggestions.  Most contributions require you to agree to a
Contributor License Agreement (CLA) declaring that you have the right to, and actually do, grant us
the rights to use your contribution. For details, visit https://cla.opensource.microsoft.com.

When you submit a pull request, a CLA bot will automatically determine whether you need to provide
a CLA and decorate the PR appropriately (e.g., status check, comment). Simply follow the instructions
provided by the bot. You will only need to do this once across all repos using our CLA.

This project has adopted the [Microsoft Open Source Code of Conduct](https://opensource.microsoft.com/codeofconduct/).
For more information see the [Code of Conduct FAQ](https://opensource.microsoft.com/codeofconduct/faq/) or
contact [opencode@microsoft.com](mailto:opencode@microsoft.com) with any additional questions or comments.
