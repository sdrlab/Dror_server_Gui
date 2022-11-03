
import socket
import os
SEPARATOR = "<SEPARATOR>"
# HOST = "127.0.0.1" 
HOST = "10.0.0.96"  # The server's hostname or IP address
PORT = 65432  # The port used by the server
BUFFER_SIZE=4096
path=os.getcwd()
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    phase_counter=0
    while True:
        if (phase_counter == 0):
            #open communication and receive the file name and type and open file 
            # with the same name
            s.connect((HOST, PORT))
            value1_from_host=s.recv(1024)
            print(f"we want to open {value1_from_host}")
            file_name=bytes.decode(value1_from_host)
            print(f"we want to open {file_name}")
            print(f"you are on {path}")
            new_file=open(file_name,"w")
            s.sendall(b"host clear to go to phase 1")
            phase_counter+=1
        if (phase_counter == 1):
            # s.connect((HOST, PORT))
            value2_from_host=s.recv(BUFFER_SIZE)
            new_file.write(bytes.decode(value2_from_host))
            phase_counter+=1
            s.sendall(b"host clear to go to final phase and finish call back")
        if (phase_counter == 2):
            break

  

