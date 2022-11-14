from pynput import keyboard
import socket
import os

PRE_HOTKEYS = {
	'<ctrl>+<alt>+t': lambda self: self.toggel_suppress
}

def lazy_debug(event, key):
	print(f'{hotkeys.is_alive()} -> {listener._suppress} -> {event} -> {key}')

class Client:
	def __init__(self, suppress, host, port):
		self.host = host
		self.port = port
		self.socket = socket.socket()
		self.socket.connect((self.host, self.port))
		self.suppress = suppress
		self._init_listener()
		self._init_hotkeys()

	def _init_listener(self):
		self.listener = keyboard.Listener(suppress=self.suppress,
		on_press= lambda key: self.on_press(key, self.socket),
			on_release = lambda key: self.on_release(key, self.socket))

	def _init_hotkeys(self):
		PRE_HOTKEYS = {
			'<ctrl>+<alt>+t': self.toggel_suppress
		}
		self.hotkeys = keyboard.GlobalHotKeys(PRE_HOTKEYS)

	def _start_client(self):
		self.listener.start()
		self.hotkeys.start()
		self.listener.wait()
		self.hotkeys.wait()
		self.listener.join()
		self.hotkeys.join()

	def _stop_client(self):
		self.listener.stop()
		self.hotkeys.stop()

	def toggel_suppress(self):
		print('toggel supppress')
		if os.name != 'nt':
			self._stop_client()
			self._init_listener()
			self._init_hotkeys()
			self.suppress = not self.suppress
			self._start_client()
		else:
			self.suppress = not self.suppress
			self.listener._suppress = self.suppress

	@staticmethod
	def on_press(key, socket_connection):
		key = [1:-1:]
		event = 'press'
		message = f'{event}->{key}END;'
		socket_connection.send(message.encode())
		print(key)

	@staticmethod
	def on_release(key, socket_connection):
		key = [1:-1:]
		event = 'release'
		message = f'{event}->{key}END;'
		socket_connection.send(message.encode())
		print(key)

client = Client(True, 'windows', 5000)
client._start_client()

# def toggel_suppress():
#     global listener
#     global hotkeys
#     print('this was called :))')
#     val = not listener._suppress
#     if os.name != 'nt':
#         listener.stop()
#         hotkeys.stop()
#         listener = keyboard.Listener(suppress=val, on_press=on_press, on_release=on_release)
#         hotkeys = keyboard.GlobalHotKeys(PRE_HOTKEYS)
#         hotkeys.start()
#         listener.start()
#         hotkeys.wait()
#         listener.wait()
#         hotkeys.join()
#         listener.join()
#     else:
#         listener._suppress = val
#
# def on_press(key):
#     lazy_debug('press', key)
#
# def on_release(key):
#     lazy_debug('release', key)
#
#
# listener.start()
# hotkeys.start()
# hotkeys.wait()
# listener.wait()
# hotkeys.join()
# listener.join()
