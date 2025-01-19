import serial
import vgamepad as vg
import pyvjoy #use for dcs world as its just better, but idk why it doesnt work in browser fs's
import time

try:
    ser = serial.Serial("COM9", 9600)

    gear_state = True
    eng_left_state = False
    eng_right_state = False

    prompt = input("Start? (dcs/geofs): ")

    if prompt == "geofs":
        print("Starting...")
        gp = vg.VX360Gamepad()
        print("Done.")
        
        while True:
            lines = ser.readline().decode("utf-8", errors="ignore").strip().strip("\n").split(";")
            # print(lines)

            if len(lines) >= 7:
                #steering
                gp.left_joystick(int((float(lines[5])) * 32767), int((float(lines[6])) * 32767)) #x then y in args
                gp.update()

                #throttle
                gp.right_joystick(int(float(lines[4]) * 32767), 0)
                gp.update()

                #gears
                if lines[0] == "1" and not gear_state:
                    gp.press_button(vg.XUSB_BUTTON.XUSB_GAMEPAD_A)
                    gp.update()
                    time.sleep(0.01)
                    gp.release_button(vg.XUSB_BUTTON.XUSB_GAMEPAD_A)
                    gp.update()
                    gear_state = True
                elif lines[0] == "0" and gear_state:
                    gp.press_button(vg.XUSB_BUTTON.XUSB_GAMEPAD_DPAD_UP)
                    gp.update()
                    time.sleep(0.01)
                    gp.release_button(vg.XUSB_BUTTON.XUSB_GAMEPAD_DPAD_UP)
                    gp.update()
                    gear_state = False

                #left engine
                if lines[1] == "1" and not eng_left_state:
                    gp.press_button(vg.XUSB_BUTTON.XUSB_GAMEPAD_B)
                    gp.update()
                    time.sleep(0.01)
                    gp.release_button(vg.XUSB_BUTTON.XUSB_GAMEPAD_B)
                    gp.update()
                    eng_left_state = True
                elif lines[1] == "0" and eng_left_state:
                    gp.press_button(vg.XUSB_BUTTON.XUSB_GAMEPAD_DPAD_DOWN)
                    gp.update()
                    time.sleep(0.01)
                    gp.release_button(vg.XUSB_BUTTON.XUSB_GAMEPAD_DPAD_DOWN)
                    gp.update()
                    eng_left_state = False

                #right engine
                if lines[2] == "1" and not eng_right_state:
                    gp.press_button(vg.XUSB_BUTTON.XUSB_GAMEPAD_X)
                    gp.update()
                    time.sleep(0.01)
                    gp.release_button(vg.XUSB_BUTTON.XUSB_GAMEPAD_X)
                    gp.update()
                    eng_right_state = True
                elif lines[2] == "0" and eng_right_state:
                    gp.press_button(vg.XUSB_BUTTON.XUSB_GAMEPAD_DPAD_RIGHT)
                    gp.update()
                    time.sleep(0.01)
                    gp.release_button(vg.XUSB_BUTTON.XUSB_GAMEPAD_DPAD_RIGHT)
                    gp.update()
                    eng_right_state = False

                #brakes (button is on joystick)
                if lines[3] == "1":
                    gp.press_button(vg.XUSB_BUTTON.XUSB_GAMEPAD_Y)
                    gp.update()
                elif lines[3] == "0":
                    gp.release_button(vg.XUSB_BUTTON.XUSB_GAMEPAD_Y)
                    gp.update()

            time.sleep(0.001)

    elif prompt == "dcs":
        print("Starting...")
        j = pyvjoy.VJoyDevice(1)
        print("Done.")

        while True:
            lines = ser.readline().decode("utf-8", errors="ignore").strip().strip("\n").split(";")

            if len(lines) >= 7:
                #steering
                j.set_axis(pyvjoy.HID_USAGE_X, int((float(lines[5]) + 1) * 16383.5))
                j.set_axis(pyvjoy.HID_USAGE_Y, int((1 - float(lines[6])) * 16383.5))


                #throttle
                j.set_axis(pyvjoy.HID_USAGE_SL0, int(float(lines[4]) * 32767))

                #gears
                if lines[0] == "1" and not gear_state:
                    j.set_button(1, 1)
                    time.sleep(0.01)
                    j.set_button(1, 0)
                    gear_state = True
                elif lines[0] == "0" and gear_state:
                    j.set_button(4, 1)
                    time.sleep(0.01)
                    j.set_button(4, 0)
                    gear_state = False
                
                #left engine
                if lines[1] == "1" and not eng_left_state:
                    j.set_button(2, 1)
                    time.sleep(0.01)
                    j.set_button(2, 0)
                    eng_left_state = True
                elif lines[1] == "0" and eng_left_state:
                    j.set_button(5, 1)
                    time.sleep(0.01)
                    j.set_button(5, 0)
                    eng_left_state = False
                
                #right engine
                if lines[2] == "1" and not eng_right_state:
                    j.set_button(3, 1)
                    time.sleep(0.01)
                    j.set_button(3, 0)
                    eng_right_state = True
                elif lines[2] == "0" and eng_right_state:
                    j.set_button(6, 1)
                    time.sleep(0.01)
                    j.set_button(6, 0)
                    eng_right_state = False

                #brakes
                if lines[3] == "1":
                    j.set_button(7, 1)
                elif lines[3] == "0":
                    j.set_button(7, 0)

                #will probably add more functions such as rudder control, flaps, etc.

    else:
        print("Wrong input, please restart the app.")

except KeyboardInterrupt:
    print("Program terminated.")