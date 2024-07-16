import os
import sys
import platform
import time

def usage():
    print("Usage: {} {{compile|flash|all}}".format(sys.argv[0]))
    sys.exit(1)

def compile_command(os_name):
    if os_name == 'Linux':
        print("Compiling on Linux. TODO")
    elif os_name == 'Darwin': # Compiling on macOS
        os.system("./arduino-cli compile --fqbn lgt8fx:avr:328 blink/")
    elif os_name == 'Windows':
        print("Compiling on Windows. TODO")
    else:
        print("Unknown OS:", os_name)

def flash_command(os_name):
    if os_name == 'Linux':
        print("Flashing on Linux. TODO")
    elif os_name == 'Darwin':
        os.system("./arduino-cli upload blink/ -p /dev/cu.wchusbserial110 -b lgt8fx:avr:328")
    elif os_name == 'Windows':
        print("Flashing on Windows. TODO")
    else:
        print("Unknown OS:", os_name)

def serial_command(os_name):
    if os_name == 'Linux':
        print("Flashing on Linux. TODO")
    elif os_name == 'Darwin':
        print("To kill screen process: control+A, k")
        time.sleep(2)
        os.system("screen /dev/cu.wchusbserial110 9600")
    elif os_name == 'Windows':
        print("Flashing on Windows. TODO")
    else:
        print("Unknown OS:", os_name)

def main():
    os_name = platform.system()
    if len(sys.argv) != 2:
        usage()

    command = sys.argv[1]

    if command == 'compile':
        compile_command(os_name)
    elif command == 'flash':
        flash_command(os_name)
    elif command == 'all':
        compile_command(os_name)
        flash_command(os_name)
    elif command == 'serial':
        serial_command(os_name)
    else:
        usage()

if __name__ == '__main__':
    main()
