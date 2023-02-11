from pynput import keyboard
import socket
import sys
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
        on_press= lambda key: self.on_press(key, self.suppress, self.socket),
            on_release = lambda key: self.on_release(key, self.suppress, self.socket))

    def _init_hotkeys(self):
        PRE_HOTKEYS = {
            '<ctrl>+<alt>+t': self.toggel_suppress
        }
        self.hotkeys = keyboard.GlobalHotKeys(PRE_HOTKEYS)

    def _start_client(self):
        self.listener.start()
        self.hotkeys.start()
        #self.listener.wait()
        #self.hotkeys.wait()
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
    def deliver_message(socket_connection, event, key):
        if hasattr(key, 'char'):
            char = key.char
        else:
            char = str(key)
        message = f'{event}->{char}END;'
        socket_connection.send(message.encode())
        print(key)

    @staticmethod
    def on_press(key, suppress, socket_connection):
        if not suppress:
            Client.deliver_message(socket_connection, 'press', key)

    @staticmethod
    def on_release(key, suppress, socket_connection):
        if not suppress:
            Client.deliver_message(socket_connection, 'release', key)

if len(sys.argv) < 3:
    print(f'usage: {sys.argv[0]} [server_ip] [port]')
    exit(1)

host = sys.argv[1]
port = int(sys.argv[2])

client = Client(True, host, port)
client._start_client()
