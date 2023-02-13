import cv2
import socket
import struct

host = '192.168.1.31'
port = 9999

cap = cv2.VideoCapture(0)

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((host, port))
server_socket.listen(0)

connection, address = server_socket.accept()

while True:
    ret, frame = cap.read()
    data = cv2.imencode('.jpg', frame)[1].tobytes()
    connection.sendall(struct.pack("!i", len(data)) + data)

cap.release()
connection.close()
server_socket.close()