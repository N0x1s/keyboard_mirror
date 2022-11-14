from pynput import keyboard
import os


class Client:
    def __init__(self, suppress):
        self.suppress = suppress
        self.listener = self._init_listener()

    def _init_listener(self):
        thread = keyboard.Listener(suppress=self.suppress, on_press=self.on_press, on_release=self.on_press)

    def _init_hotkeys(self, rules):
        pass

    def toggle_suppress(self):
        pass

class KeyboardClient(Client):
    def __init__(self):
        super().__init__(True)

    def on_press(key):
        print(key)

    def on_release(key):
        print(key)

client = KeyboardClient()

def lazy_debug(event, key):
    global i
    i += 1
    print(f'{hotkeys.is_alive()} -> {listener._suppress} -> {event} -> {key}')
    # if event == 'release':
    #   

def unsuppress():
    global listener
    if os.name != 'nt':
        listener = keyboard.Listener(suppress=False, on_press=on_press, on_release=on_release)
    else:
        listener._suppress = False

def toggel_suppress():
    global listener
    global hotkeys
    print('this was called :))')
    val = not listener._suppress
    if os.name != 'nt':
        listener.stop()
        hotkeys.stop()
        listener = keyboard.Listener(suppress=val, on_press=on_press, on_release=on_release)
        hotkeys = keyboard.GlobalHotKeys(PRE_HOTKEYS)
        hotkeys.start()
        listener.start()
        hotkeys.wait()
        listener.wait()
        hotkeys.join()
        listener.join()
    else:
        listener._suppress = val

def on_press(key):
    lazy_debug('press', key)

def on_release(key):
    lazy_debug('release', key)


PRE_HOTKEYS = {
    '<ctrl>+<alt>+t': toggel_suppress
}

hotkeys = keyboard.GlobalHotKeys(PRE_HOTKEYS)
listener = keyboard.Listener(suppress=True, on_press=on_press, on_release=on_release)
listener.start()
hotkeys.start()
hotkeys.wait()
listener.wait()
hotkeys.join()
listener.join()
