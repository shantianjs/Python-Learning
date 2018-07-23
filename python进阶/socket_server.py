import  socket

s = socket.socket()

host = socket.gethostname()
port = 80
s.bind((host,port))

s.listen(2)
while True:
	c , addr = s.accept()
	print(f'got connetion from {addr}\nmessage is {c}')
	c.send('thank you for conneting.'.encode('utf-8'))
	c.close()