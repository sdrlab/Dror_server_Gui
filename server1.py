#echo-server.py 

import socket
# HOST="10.0.0.96"
HOST= "10.0.0.27" #Standart loopback interface address(local host)
PORT=65432 # port to listen on ( non-privileged port are > 1023)

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    conn, addr =s.accept()
    with conn:
        print(f"Connected by {addr}")
        while True:
            data = conn.recv(1024)
            if not data:
                break
            conn.sendall(data)