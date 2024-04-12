import socket



class Client:
    """
    Client side on the same host as the server is
    """

    def __init__(self, *args, **kwargs):
        super(Client, self).__init__(*args, **kwargs)

    def client_program(self):
        host = socket.gethostname()
        port = 5000

        client_socket = socket.socket()
        client_socket.connect((host, port))

        message = input(" -> ")

        while message.lower().strip() != 'bye':
            client_socket.send(message.encode())
            data = client_socket.recv(1024).decode()

            print('Received from server: ' + data)

            message = input(" -> ")

        client_socket.close()


if __name__ == '__main__':
    client = Client()

    client.client_program()