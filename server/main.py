import socket

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

	def listen(self):
		self.socket.bind((self.host, self.port))
		self.socket.listen(1) # limit clients to one for security reasons

	def accept_client(self):
		conn, address = self.socket.accept()
		return ClientConnection(conn, address)

	def receive_commands(self, client):
		while True:
			data = client.connection.recv(32).decode()
			if data:
				print(data)

def server_program():
	server = Server('windows', 5000)
	server.listen()
	client = server.accept_client()
	server.receive_commands(client)
    # get the hostname
    # host = socket.gethostname()
    # port = 5000  # initiate port no above 1024
	#
    # server_socket = socket.socket()  # get instance
    # # look closely. The bind() function takes tuple as argument
    # server_socket.bind((host, port))  # bind host address and port together
	#
    # # configure how many client the server can listen simultaneously
    # server_socket.listen(2)
    # conn, address = server_socket.accept()  # accept new connection
    # print("Connection from: " + str(address))
    # while True:
    #     # receive data stream. it won't accept data packet greater than 1024 bytes
    #     data = conn.recv(1024).decode()
    #     if not data:
    #         # if data is not received break
    #         break
    #     print("from connected user: " + str(data))
    #     # data = input(' -> ')
    #     # conn.send(data.encode())  # send data to the client
	#
    # conn.close()  # close the connection


if __name__ == '__main__':
    server_program()
