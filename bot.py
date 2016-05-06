import socket
import winsound
from time import sleep, time

from cfg import *


time_play_last = -1


def play_audio():
	global time_play_last
	if time_play_last == -1 or time_play_last + COOL < time():
		winsound.PlaySound(SOUND, winsound.SND_FILENAME | winsound.SND_ASYNC)
		sleep(1.5)
		time_play_last = time()

sock = socket.socket()
try:
	sock.connect((HOST, PORT))
	sock.send("PASS {}\r\n".format(PASS).encode("UTF-8"))
	sock.send("NICK {}\r\n".format(NICK).encode("UTF-8"))
	sock.send("JOIN {}\r\n".format(CHAN).encode("UTF-8"))
except socket.error as e:
	print ("Socket connection error:", e.strerror)
	print ("Exiting ...")
	exit()

print ("Entering infinite loop, close CMD window or press CTRL+C to exit")

while True:
	try:
		msg = sock.recv(2048).decode("UTF-8")

		if msg == "PING :tmi.twitch.tv\r\n":
			sock.send("PONG :tmi.twitch.tv\r\n".encode("UTF-8"))
			continue

		print (HOST, "->", msg)
		print ("Play note")
		play_audio()
		sleep(1 / RATE)
	except socket.error as e:
		print ("Socket receiving error:", e.strerror)

