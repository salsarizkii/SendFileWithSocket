import os, socket, time

host = input("Enter host name: ")
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    sock.connect((host, 22222))
    print("Connected Successfully")
except:
    print("Unable to connect")
    exit(0)

file_name = sock.recv(100).decode().strip()  # Ensure correct decoding
file_size = sock.recv(100).decode().strip()  # Remove potential whitespace issues

if not file_size.isdigit():  # Ensure file_size is valid
    print("Invalid file size received.")
    sock.close()
    exit(0)

file_size = int(file_size)

if file_size == 0:
    print("Empty file received.")
    sock.close()
    exit(0)

os.makedirs("./rec", exist_ok=True)  # Ensure directory exists
file_path = os.path.join("./rec", file_name)

with open(file_path, "wb") as file:
    received = 0
    start_time = time.time()

    while received < file_size:
        data = sock.recv(1024)
        if not data:
            break
        file.write(data)
        received += len(data)

    end_time = time.time()

print("File transfer complete. Total time:", end_time - start_time)
print(f"Received {received}/{file_size} bytes.")

sock.close()