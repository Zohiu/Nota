import socket
import time
import json
import threading

port = 65432

ip = "localhost"

def send_request(num, x):
    try:
        # Sending the request
        s = socket.socket()
        s.connect((ip, port))
        snd = json.dumps({"request": "get", "value": num}).encode()
        s.send(snd)

        output = "Sent: " + snd.decode()

        # Getting the response
        try:
            data = json.loads(s.recv(1024).decode())
            print(output, "|", "Recieved:", data)
        except:
            print('no data received')

        # resetting everything
        s.close()
        del s

    except Exception as e:
        print("Server not responding!")
        time.sleep(1)

    send_request(num, x)

for i in range(1000):
    threading.Thread(target=send_request, args=(i, i)).start()
    time.sleep(0.01)

print("all started!")

while True:
    pass