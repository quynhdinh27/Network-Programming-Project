import socket
import struct

# resolver information
SERVER_IP = "127.0.0.1"
SERVER_PORT = 5300
BUFFER = 4096


def send_to_resolver(message):

    # create UDP socket
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    # convert message to bytes
    msg_bytes = message.encode()

    # add length prefix (2 bytes)
    length = struct.pack("!H", len(msg_bytes))
    packet = length + msg_bytes

    # send packet to resolver
    s.sendto(packet, (SERVER_IP, SERVER_PORT))

    # receive response
    data, addr = s.recvfrom(BUFFER)

    # first 2 bytes = message length
    resp_len = struct.unpack("!H", data[:2])[0]

    # actual message
    resp_msg = data[2:2 + resp_len].decode()

    print("\n--- Resolver reply ---")
    print(resp_msg)
    print("----------------------\n")

    s.close()


def main():

    print("Simple DNS Client (bonus features)")
    print("Commands you can use:")
    print("  AAAA <domain>   -> ask for IPv6 address")
    print("  /cache          -> show resolver cache")
    print("  exit            -> quit program\n")

    while True:

        user_input = input(">>> ").strip()

        # exit program
        if user_input == "exit":
            break

        # AAAA query
        if user_input.startswith("AAAA "):
            send_to_resolver(user_input)

        # cache command
        elif user_input == "/cache":
            send_to_resolver(user_input)

        else:
            print("Invalid command. Try again.")


if __name__ == "__main__":
    main()