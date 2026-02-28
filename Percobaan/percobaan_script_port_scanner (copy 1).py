from colorama import Fore, Back, Style
import socket

def tampilkan_ascii_art():
    custom_art = """
   _____  _  ____  ____  ____  ____    ____ ___  _
  /__ __\/ \/  _ \/  _ \/  _ \/ ___\  /  __\\  \//
    / \  | || | \|| | \|| / \||    \  |  \/| \  / 
    | |  | || |_/|| |_/|| \_/|\___ |__|  __/ / /  
    \_/  \_/\____/\____/\____/\____/\/\_/   /_/                                                                                                           
    """
    print(Fore.GREEN + custom_art + Style.RESET_ALL)

def scanning_ip(domain):
    try:
        ip_address = socket.gethostbyname(domain)
        print(Fore.GREEN + f"IP Address dari {domain} : {ip_address}")
    except socket.gaierror:
        print(Fore.RED + "Domain tidak ditemukan")

def input_ip():
    domain = input(Fore.BLUE + "Masukkan Domain : ")
    get_ip = scanning_ip(domain)

def scanning_port(target_ip, start_port, end_port):
    open_port = []
    total_port = end_port - start_port + 1
    scanned_port = 0

    print("Scanning In Progessing...\n")
    for port in range(start_port, end_port + 1):
        try:
            # Create a socket object
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            # Set a timeout for the connection attempt
            socket.setdefaulttimeout(1)
            # Attempt to connect to the target IP and port
            result = sock.connect_ex((target_ip, port))
            # If the connection is successful, add the port to the list of open ports
            if result == 0:
                open_port.append(port)
                print(Fore.GREEN + f"[OPEN] Port {port}")
            else:
                print(Fore.RED + f"[CLOSED] Port {port}")
            # Close the socket
            sock.close()
        except socket.error as e:
            # Print an error message if an exception occurs
            print(f"Error on port {port}: {e}")

        scanned_port += 1
        progress_scanning = (scanned_port / total_port) * 100
        print(Fore.YELLOW + f"Progess Scanning : {progress_scanning:.2f}%", end="\r")
    
    return open_port

def main():
    tampilkan_ascii_art()
    # Get user input for target IP address and port range
    target_ip = input(Fore.GREEN + "Enter target IP address: ")
    start_port = int(input(Fore.RED + "Enter start port: "))
    end_port = int(input(Fore.BLUE + "Enter end port: "))
    # Perform the port scan
    open_ports = scanning_port(target_ip, start_port, end_port)
    # Print the list of open ports
    print("\n Scanning Completed!")
    print(Fore.MAGENTA + f"\nOpen ports: {open_ports}")

if __name__ == "__main__":
    main()

