import socket

def Main():
    host = '127.0.0.1'
    port = 5000
 
    s = socket.socket()
    s.connect((host, port))
    
    message = raw_input("hey! Enter the message to send  ")
    while message != 'q':
        s.send(message)
        data = s.recv(1024)
        print 'Recieved from Server : ' + str(data)
        message = raw_input(" enter the message to send  ")
    s.close()
if __name__ == '__main__':
    Main()
