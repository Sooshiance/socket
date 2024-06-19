import socket


class Server:
    """
    Server on your localhost
    """
    
    def __init__(self, *args, **kwargs):
        super(Server, self).__init__(*args, **kwargs)
    
    def server_program(self):
        # TODO : choose a Host and Port
        host = socket.gethostname()
        port = 5000

        # TODO : create a socket Object
        server_socket = socket.socket()

        # TODO : bind the port and host to the socket object
        server_socket.bind((host, port))  


        server_socket.listen(2)
        conn, address = server_socket.accept()
        print("Connection from: " + str(address))
        while True:

            data = conn.recv(1024).decode()
            if not data:
                break
            print("from connected user: " + str(data))
            data = input(' -> ')
            conn.send(data.encode())

        conn.close()


if __name__ == '__main__':
    server = Server()

    server.server_program()
