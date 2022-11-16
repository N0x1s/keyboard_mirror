import socket
import logging
from pynput.keyboard import Key, Controller

logging.basicConfig(level=logging.WARNING, filename='app.log', filemode='w', format='%(name)s - %(levelname)s - %(message)s')

class ClientConnection:
	def __init__(self, connection, address):
		self.connection =connection
		self.address = address

	def __str__(self):
		return f'User 1: {self.address}'

	def __repr__(self):
		return str(self)

class Server:
	def __init__(self, host, port):
		self.host = host
		self.port = port
		self.socket = socket.socket()
		self.controller = Controller()

	def listen(self):
		self.socket.bind((self.host, self.port))
		self.socket.listen(1) # limit clients to one for security reasons

	def accept_client(self):
		conn, address = self.socket.accept()
		return ClientConnection(conn, address)

	def receive_commands(self, client):
		while True:
			data = client.connection.recv(1024).decode()
			if data:
				messages = [item for item in data.split('END;') if item]
				for message in messages:
					try:
						event, event_data = message.split('->')
					except Exception as e:
						logging.warning(f"{e} -> {data}")
					key = event_data
					if 'Key' in event_data:
						try:
							key = getattr(Key, event_data.split('.')[-1])
						except Exception as e:
							logging.warning(f"{e} -> {data}")
					try:
						getattr(self.controller, event)(key)
					except Exception as e:
						logging.warning(f"{e} -> {data}")
					print(message)

def server_program():
	server = Server('0.0.0.0', 5000)
	server.listen()
	client = server.accept_client()
	server.receive_commands(client)


if __name__ == '__main__':
    server_program()
