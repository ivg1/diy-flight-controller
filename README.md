# DIY flight controller
After looking at how much flight simulator controllers cost, I decided to make my own one.

## Installation
1. Download as a zip or clone this repo.
2. Navigate into the folder with the repo files
3. Run the modules.bat file to install required modules for python
```bash
./modules.bat
```
4. You will also need to install the vjoy driver here: https://sourceforge.net/projects/vjoystick/. along with the driver for vgamepad, but you should be prompted for it when you run python.
5. Flash the arduino (.ino file) code to the uno r3
6. Run the python file
7. Launch any game and use the controller

## Wiring
See the wiring of the project here: https://wokwi.com/projects/420510173310326785

## Demo
See the demo play here: https://www.youtube.com/watch?v=cUjkdGvfNZE

## Important notice
When using the pyvjoy module, make sure that you enabled the vJoystick in the configuration.  
To check:
1. Search using the windows key for "configure vjoy"
2. Open the app and in the bottom left corner make sure the checkbox "Enable vJoy" is ticked
![image](https://github.com/user-attachments/assets/438c2cbd-6096-42cb-857f-2cbd7da89a5b)
