import os, socket, time

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind((socket.gethostbyname(socket.gethostname()), 22222))
sock.listen(5)
print("HOST: ", sock.getsockname())

client, addr = sock.accept()

file_name = input("File name: ")
file_size = os.path.getsize(file_name)

client.send(file_name.encode().ljust(100))  # Ensure fixed-size name transmission
client.send(str(file_size).encode().ljust(100))  # Ensure proper size transmission

with open(file_name, "rb") as file:
     c = 0

     start_time = time.time()
    # while c <= file_size:
     #    data = file.read(1024)
      #   if not (data):
       #      break
     #client.sendall(data)
     #c += len(data)

    # end_time = time.time()

     while c < file_size:  # Corrected condition
        data = file.read(1024)  # Read up to 1024 bytes
        if not data:  # Break if no data left
            break
        client.sendall(data)  # Send every chunk properly
        c += len(data)

        end_time = time.time()

print("file transfer complete. Total time: ", end_time - start_time)

sock.close()