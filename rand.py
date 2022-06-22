import random
import socket
from time import sleep
import os, sys
from threading import Thread

port = 0
thrs = []

def is_alive(host):
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.settimeout(0.5)
	try:
	    s.connect((host, port))
	    s.shutdown(socket.SHUT_RD)
	    return True   
	except:
	    return False





def random_ip():
	octets = []
	for x in range(4):
	    octets.append(str(random.randint(0,255)))
	return '.'.join(octets)


def run():
	global port
	host = random_ip()
	#print(host)
	if is_alive(host):
		print(f"Open port {port} in {host}")
		file = open("ip.txt", "a")
		file.write(host + "\n")
		file.close()
	else:
		pass

def main():
	global port
	if len(sys.argv) < 3:
		print("Usage: python " + sys.argv[0] + " <port> <threads>")
		exit()
	port = int(sys.argv[1])
	threads = int(sys.argv[2])
	while True:
		for x in range(threads):
			t = Thread(target=run)
			t.start()
			thrs.append(t)
		for thread in thrs:
			thread.join()
			thrs.remove(thread)

if __name__ == '__main__':
	try:
		main()
	except KeyboardInterrupt:
		exit()