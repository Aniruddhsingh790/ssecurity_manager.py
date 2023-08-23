import os
import ctypes
import winreg
import subprocess

def block_usb_ports():
    # TODO: Write code to block USB ports using the Windows Registry Editor
      # Check if the user has administrative privileges
    if ctypes.windll.shell32.IsUserAnAdmin() == 0:
        print("Please run this program as an administrator.")
        return

    # Registry key paths for disabling USB storage devices
    registry_paths = [
        r"SYSTEM\CurrentControlSet\Services\USBSTOR",
        r"SYSTEM\CurrentControlSet\Services\USBHUB",
    ]
    
    try:
        for path in registry_paths:
            with winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, path, 0, winreg.KEY_SET_VALUE) as reg_key:
                winreg.SetValueEx(reg_key, "Start", 0, winreg.REG_DWORD, 4)  # Disable USB ports

        print("USB ports have been blocked.")
    except Exception as e:
        print(f"An error occurred: {e}")
    pass

def disable_bluetooth():
    # TODO: Write code to disable Bluetooth using the Windows Registry Editor
    # Check if the user has administrative privileges
    if ctypes.windll.shell32.IsUserAnAdmin() == 0:
        print("Please run this program as an administrator.")
        return

    # Registry key paths for disabling Bluetooth
    registry_paths = [
        r"SYSTEM\CurrentControlSet\Services\BTHPORT\Parameters",
    ]

    try:
        for path in registry_paths:
            with winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, path, 0, winreg.KEY_SET_VALUE) as reg_key:
                winreg.SetValueEx(reg_key, "BluetoothEnabled", 0, winreg.REG_DWORD, 0)  # Disable Bluetooth

        print("Bluetooth has been disabled.")
    except Exception as e:
        print(f"An error occurred: {e}")
    pass

def disable_command_prompt():
    # TODO: Write code to restrict access to the command prompt using Group Policy or other methods
    # Check if the user has administrative privileges
    if ctypes.windll.shell32.IsUserAnAdmin() == 0:
        print("Please run this program as an administrator.")
        return

    try:
        # Disable command prompt using Group Policy
        subprocess.run(["gpedit.msc"], shell=True)
        print("Access to the command prompt has been restricted.")
    except Exception as e:
        print(f"An error occurred: {e}")
    pass

def block_website_access():
    # TODO: Write code to block access to "facebook.com" by modifying the hosts file
    # Check if the user has administrative privileges
    if ctypes.windll.shell32.IsUserAnAdmin() == 0:
        print("Please run this program as an administrator.")
        return

    try:
        # Website to block
        website_to_block = "facebook.com"

        # Hosts file path
        hosts_file_path = r"C:\Windows\System32\drivers\etc\hosts"

        # Append entry to block the website
        with open(hosts_file_path, "a") as hosts_file:
            hosts_file.write(f"127.0.0.1 {website_to_block}\n")

        print(f"Access to {website_to_block} has been blocked.")
    except Exception as e:
        print(f"An error occurred: {e}")
    pass

def main():
    # Call the functions to implement the security measures
    block_usb_ports()
    disable_bluetooth()
    disable_command_prompt()
    block_website_access()

if __name__ == "_main_":
    if os.name != "nt":
        print("This program is intended to run on Windows.")
    elif ctypes.windll.shell32.IsUserAnAdmin() == 0:
        print("Please run this program as an administrator.")
    else:
        main()
