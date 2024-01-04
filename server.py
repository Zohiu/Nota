import socket
import json

HEADER_LENGTH = 10

IP = "127.0.0.1"
PORT = 65432

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

server_socket.bind((IP, PORT))
server_socket.listen()

print(f'Listening for connections on {IP}:{PORT}...')

def recieve():
    conn, addr = server_socket.accept()

    try:
        data = json.loads(conn.recv(1024).decode())
    except json.decoder.JSONDecodeError:
        return None, {"request": None}

    print(f"Data recieved from {addr}: {data}")

    return conn, data


def process(conn, data):
    if data["request"] == "get":
        response = {"response": f'You wanna get {data["value"]}?'}

    elif data["request"] == "post":
        response = {"response": f'You wanna post {data["value"]}?'}

    else:
        response = {"response": "Invalid request!"}

    if conn is not None:
        conn.sendall(json.dumps(response).encode())
        conn.close()

while True:
    conn, data = recieve()
    process(conn, data)