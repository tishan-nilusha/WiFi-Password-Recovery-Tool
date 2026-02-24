#!/usr/bin/python3

import os
import subprocess
import sys
import traceback
import platform


def display_banner():
    print(" ")
    print(" ")
    print("⠀⠀⠀⠀⠀⢀⣤⠤⠤⠤⠤⠤⠤⠤⠤⠤⠤⢤⣤⣀⣀⡀⠀⠀⠀⠀⠀⠀")
    print("⠀⠀⠀⠀⢀⡼⠋⠀⣀⠄⡂⠍⣀⣒⣒⠂⠀⠬⠤⠤⠬⠍⠉⠝⠲⣄⡀⠀⠀")
    print("⠀⠀⠀⢀⡾⠁⠀⠊⢔⠕⠈⣀⣀⡀⠈⠆⠀⠀⠀⡍⠁⠀⠁⢂⠀⠈⣷⠀⠀")
    print("⠀⠀⣠⣾⠥⠀⠀⣠⢠⣞⣿⣿⣿⣉⠳⣄⠀⠀⣀⣤⣶⣶⣶⡄⠀⠀⣘⢦⡀")
    print("⢀⡞⡍⣠⠞⢋⡛⠶⠤⣤⠴⠚⠀⠈⠙⠁⠀⠀⢹⡏⠁⠀⣀⣠⠤⢤⡕⠱⣷")
    print("⠘⡇⠇⣯⠤⢾⡙⠲⢤⣀⡀⠤⠀⢲⡖⣂⣀⠀⠀⢙⣶⣄⠈⠉⣸⡄⠠⣠⡿")
    print("⠀⠹⣜⡪⠀⠈⢷⣦⣬⣏⠉⠛⠲⣮⣧⣁⣀⣀⠶⠞⢁⣀⣨⢶⢿⣧⠉⡼⠁")
    print("⠀⠀⠈⢷⡀⠀⠀⠳⣌⡟⠻⠷⣶⣧⣀⣀⣹⣉⣉⣿⣉⣉⣇⣼⣾⣿⠀⡇⠀")
    print("⠀⠀⠀⠈⢳⡄⠀⠀⠘⠳⣄⡀⡼⠈⠉⠛⡿⠿⠿⡿⠿⣿⢿⣿⣿⡇⠀⡇⠀")
    print("⠀⠀⠀⠀⠀⠙⢦⣕⠠⣒⠌⡙⠓⠶⠤⣤⣧⣀⣸⣇⣴⣧⠾⠾⠋⠀⠀⡇⠀")
    print("⠀⠀⠀⠀⠀⠀⠀⠈⠙⠶⣭⣒⠩⠖⢠⣤⠄⠀⠀⠀⠀⠀⠠⠔⠁⡰⠀⣧⠀")
    print("⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠛⠲⢤⣀⣀⠉⠉⠀⠀⠀⠀⠀⠁⠀⣠⠏⠀")
    print("⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠉⠉⠛⠒⠲⠶⠤⠴⠒⠚⠁")
    print(" ")

def handle_linux():
    """Handle WiFi password retrieval on Linux"""
    conn_dir = "/etc/NetworkManager/system-connections/"
    
    # Check if running as root
    if os.geteuid() != 0:
        print("\033[1;31m[!] This script requires root privileges on Linux!\033[0m")
        print("\033[1;33m[*] Please run with: sudo python3 wifresti.py\033[0m")
        return
    
    # Check if directory exists
    if not os.path.exists(conn_dir):
        print("\033[1;31m[!] NetworkManager connections directory not found!\033[0m")
        return
    
    print(" ")
    print("All wireless networks:")
    print(" ")
    
    # List all saved networks
    try:
        networks = os.listdir(conn_dir)
        if not networks:
            print("No saved networks found.")
            return
        for network in networks:
            print(f"  - {network}")
    except PermissionError:
        print("\033[1;31m[!] Permission denied. Run as root!\033[0m")
        return
    
    print(" ")
    print("Insert the network name, or press (a) to see all networks.")
    print(" ")
    nombre = input("> ")
    
    if nombre == "a":
        print("\033[1;36m############################ - Information about all networks - ############################\033[0m")
        print(" ")
        for network in networks:
            filepath = os.path.join(conn_dir, network)
            print(f"\033[1;33m--- {network} ---\033[0m")
            try:
                with open(filepath, "r") as f:
                    content = f.read()
                    for line in content.split("\n"):
                        if any(key in line.lower() for key in ["ssid=", "psk=", "key-mgmt=", "security="]):
                            print(f"  {line}")
            except Exception as e:
                print(f"  Error reading: {e}")
            print(" ")
        print("\033[1;36m#############################################################################################\033[0m")
        wifi_content = "All networks info displayed above"
    else:
        filepath = os.path.join(conn_dir, nombre)
        
        if not os.path.exists(filepath):
            print(f"\033[1;31m[!] Network '{nombre}' not found!\033[0m")
            return
        
        print(f"\033[1;36m###################################### - {nombre} - ######################################\033[0m")
        print(" ")
        wifi_content = ""
        try:
            with open(filepath, "r") as f:
                content = f.read()
                wifi_content = content
                for line in content.split("\n"):
                    if any(key in line.lower() for key in ["ssid=", "psk=", "key-mgmt=", "security="]):
                        print(f"  {line}")
        except Exception as e:
            print(f"Error: {e}")
        print(" ")
        print("\033[1;36m#############################################################################################\033[0m")
    
    # Option to save
    print(" ")
    guardar = input("Do you want to save the result? [y/n] > ")
    if guardar.lower() == "y":
        filename = nombre if nombre != "a" else "all_networks"
        with open(filename + ".txt", "w") as f:
            if nombre != "a":
                filepath = os.path.join(conn_dir, nombre)
                with open(filepath, "r") as source:
                    f.write(source.read())
            else:
                for network in networks:
                    filepath = os.path.join(conn_dir, network)
                    f.write(f"--- {network} ---\n")
                    try:
                        with open(filepath, "r") as source:
                            f.write(source.read())
                    except:
                        pass
                    f.write("\n\n")
        print(f"\033[1;32m[+] Saved to {filename}.txt\033[0m")


def handle_windows():
    """Handle WiFi password retrieval on Windows"""
    result = subprocess.run(
        ["netsh", "wlan", "show", "profile"],
        capture_output=True, text=True
    )
    print(result.stdout)
    print(" ")
    print("Insert the network name, or press (a) to see all networks.")
    print(" ")
    nombre = input("> ")

    if nombre == "a":
        print("############################ - Information about all networks - ############################")
        print(" ")
        wifi2 = subprocess.run(
            ["netsh", "wlan", "show", "profile", "name=*", "key=clear"],
            capture_output=True, text=True
        )
        print(wifi2.stdout)
        print(" ")
        print("#############################################################################################")
    else:
        print("###################################### - " + nombre + " - ######################################")
        print(" ")
        wifi2 = subprocess.run(
            ["netsh", "wlan", "show", "profile", f"name={nombre}", "key=clear"],
            capture_output=True, text=True
        )
        print(wifi2.stdout)
        print(" ")
        print("#############################################################################################")

    guardar = input("Do you want to save the result? [y/n] > ")
    if guardar.lower() == "y":
        filename = nombre if nombre != "a" else "all_networks"
        with open(filename + ".txt", "w") as f:
            f.write(wifi2.stdout + "\n")
        print(f"Saved to {filename}.txt")


def handle_macos():
    """Handle WiFi password retrieval on Mac OS"""
    
    # Check if running as root
    if os.geteuid() != 0:
        print("\033[1;31m[!] This script requires root privileges on Mac OS!\033[0m")
        print("\033[1;33m[*] Please run with: sudo python3 wifresti.py\033[0m")
        return
    
    print(" ")
    print("All wireless networks:")
    print(" ")
    
    # Get list of preferred networks
    try:
        result = subprocess.run(
            ["networksetup", "-listpreferredwirelessnetworks", "en0"],
            capture_output=True, text=True
        )
        
        if result.returncode != 0:
            # Try en1 if en0 doesn't work
            result = subprocess.run(
                ["networksetup", "-listpreferredwirelessnetworks", "en1"],
                capture_output=True, text=True
            )
        
        if result.returncode != 0:
            print("\033[1;31m[!] Could not find wireless interface!\033[0m")
            print("\033[1;33m[*] Try running: networksetup -listallhardwareports\033[0m")
            return
        
        # Parse network names
        lines = result.stdout.strip().split("\n")
        networks = []
        for line in lines[1:]:  # Skip header line
            network_name = line.strip()
            if network_name:
                networks.append(network_name)
                print(f"  - {network_name}")
        
        if not networks:
            print("No saved networks found.")
            return
            
    except Exception as e:
        print(f"\033[1;31m[!] Error listing networks: {e}\033[0m")
        return
    
    print(" ")
    print("Insert the network name, or press (a) to see all networks.")
    print(" ")
    nombre = input("> ")
    
    if nombre == "a":
        print("\033[1;36m############################ - Information about all networks - ############################\033[0m")
        print(" ")
        all_passwords = ""
        for network in networks:
            print(f"\033[1;33m--- {network} ---\033[0m")
            try:
                # Use security command to get password from keychain
                result = subprocess.run(
                    ["security", "find-generic-password", "-D", "AirPort network password", "-a", network, "-w"],
                    capture_output=True, text=True
                )
                if result.returncode == 0:
                    password = result.stdout.strip()
                    print(f"  SSID: {network}")
                    print(f"  Password: {password}")
                    all_passwords += f"--- {network} ---\nSSID: {network}\nPassword: {password}\n\n"
                else:
                    print(f"  SSID: {network}")
                    print(f"  Password: [Could not retrieve - check Keychain Access]")
                    all_passwords += f"--- {network} ---\nSSID: {network}\nPassword: [Not found]\n\n"
            except Exception as e:
                print(f"  Error: {e}")
            print(" ")
        print("\033[1;36m#############################################################################################\033[0m")
        wifi_content = all_passwords
    else:
        # Check if network exists
        if nombre not in networks:
            print(f"\033[1;31m[!] Network '{nombre}' not found in saved networks!\033[0m")
            return
        
        print(f"\033[1;36m###################################### - {nombre} - ######################################\033[0m")
        print(" ")
        try:
            # Use security command to get password from keychain
            result = subprocess.run(
                ["security", "find-generic-password", "-D", "AirPort network password", "-a", nombre, "-w"],
                capture_output=True, text=True
            )
            if result.returncode == 0:
                password = result.stdout.strip()
                print(f"  SSID: {nombre}")
                print(f"  Password: {password}")
                wifi_content = f"SSID: {nombre}\nPassword: {password}"
            else:
                print(f"  SSID: {nombre}")
                print(f"  Password: [Could not retrieve]")
                print(" ")
                print("\033[1;33m[*] Tip: You may need to allow access in the popup dialog\033[0m")
                print("\033[1;33m[*] Or check Keychain Access app manually\033[0m")
                wifi_content = f"SSID: {nombre}\nPassword: [Not found]"
        except Exception as e:
            print(f"Error: {e}")
            wifi_content = f"Error: {e}"
        print(" ")
        print("\033[1;36m#############################################################################################\033[0m")
    
    # Option to save
    print(" ")
    guardar = input("Do you want to save the result? [y/n] > ")
    if guardar.lower() == "y":
        filename = nombre if nombre != "a" else "all_networks"
        # Clean filename for saving
        filename = "".join(c for c in filename if c.isalnum() or c in (' ', '-', '_')).rstrip()
        with open(filename + ".txt", "w") as f:
            f.write(wifi_content + "\n")
        print(f"\033[1;32m[+] Saved to {filename}.txt\033[0m")


def main():
    try:
        display_banner()
        
        current_os = platform.system()
        
        print("Please choose your operating system.")
        print(" ")
        print(" 1) Linux")
        print(" 2) Windows")
        print(" 3) Mac OS")
        print(" ")
        print(f"[Detected OS: {current_os}]")
        print(" ")

        entrada = input("> ")

        if entrada == "1":
            if current_os == "Linux":
                handle_linux()
            else:
                print(f"\033[1;31m[!] You selected Linux but you're on {current_os}!\033[0m")

        elif entrada == "2":
            if current_os == "Windows":
                handle_windows()
            else:
                print(f"\033[1;31m[!] You selected Windows but you're on {current_os}!\033[0m")

        elif entrada == "3":
            if current_os == "Darwin":  # Mac OS is detected as "Darwin"
                handle_macos()
            else:
                print(f"\033[1;31m[!] You selected Mac OS but you're on {current_os}!\033[0m")

        else:
            print("Please select an option. (1) for Linux, (2) for Windows, and (3) for Mac OS.")

    except KeyboardInterrupt:
        print("\nShutdown requested...exiting")
    except Exception:
        traceback.print_exc(file=sys.stdout)
    sys.exit(0)


if __name__ == "__main__":
    main()