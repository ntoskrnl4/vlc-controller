# Small program to make VLC skip to the previous song.
# See repo readme for full information.

from time import sleep
from socket import create_connection

try:
	s = create_connection(("127.0.0.1", 4212), timeout=0.1)  # for localhost 0.1s should be plenty, tbh
except:  # we'll assume it's a timeout, shhhh
	try:
		from win10toast import ToastNotifier
		toaster = ToastNotifier()
		toaster.show_toast("Python VLC Music Controller", "Socket connection to VLC timed out - VLC not running or very heavy system load", icon_path=None, duration=10)
	except ModuleNotFoundError:
		pass  # it's ok if win10toast isn't installed, we'll just silently exit
else:
	s.recv(16384)
	s.send(b"vlc\n")  # the interface password, mine is just 'vlc'
	s.recv(16384)
	sleep(0.005)  # not sure why but we need this sleep here for vlc to execute the command properly
	s.send(b"prev\n")
	s.recv(16384)
	s.close()
