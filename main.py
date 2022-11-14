from pynput import keyboard

i = 0

def lazy_debug(event, key):
	global i
	i += 1
	print(f'{listener._suppress} -> {event} -> {key}')
	# if event == 'release':
	# 	

def unsuppress():
	listener._suppress = False

def toggel_suppress():
	listener._suppress = not listener._suppress

def on_press(key):
	lazy_debug('press', key)

def on_release(key):
	lazy_debug('release', key)


PRE_HOTKEYS = {
	'<ctrl>+<alt>+s': unsuppress,
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