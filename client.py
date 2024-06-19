import socket



class Client:
    """
    Client side on the same host as the server is
    """

    def __init__(self, *args, **kwargs):
        super(Client, self).__init__(*args, **kwargs)

    def client_program(self):
        # TODO : choose a Host and Port
        host = socket.gethostname()
        port = 5000

        # TODO : create a socket Object
        client_socket = socket.socket()

        # TODO : bind the port and host to the socket object
        client_socket.connect((host, port))

        # TODO : if connection not interrupted
        message = input(" -> ")

        while message.lower().strip() != 'bye':
            # TODO : encode message and send it to server 
            client_socket.send(message.encode())

            # TODO : receive the message and decode it
            data = client_socket.recv(1024).decode()

            # TODO : print the message
            print('Received from server: ' + data)

            # TODO : let user send another message
            message = input(" -> ")

        # TODO : close the connection
        client_socket.close()


if __name__ == '__main__':
    client = Client()

    client.client_program()
