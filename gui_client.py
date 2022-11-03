
import socket
# HOST = "127.0.0.1" 
HOST = "10.0.0.96"  # The server's hostname or IP address
PORT = 65432  # The port used by the server

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    while True:
        s.connect((HOST, PORT))
        value_from_host=s.recv(1024)
        print(f"received {value_from_host}")
        s.sendall(b"value_from_host")
        

