


# TCP Sockets Illustrated

Here's a ASCII art representation of a TCP socket connection between a client and a server, including the three-way handshake for establishing the connection and data transmission:

```
  +--------------+                        +--------------+
  |              |                        |              |
  |    Client    |                        |    Server    |
  |              |                        |              |
  +------+-------+                        +-------+------+
         |                                      |
         | --- SYN (Seq=x) -------------------> |
         |                                      |
         | <--- SYN-ACK (Seq=y, Ack=x+1) ------ |
         |                                      |
         | --- ACK (Seq=x+1, Ack=y+1) --------> |
         |                                      |
  Establishing TCP Connection (Three-way Handshake)
         |                                      |
         | --- Data (Seq=x+1, Ack=y+1) -------> |
         |                                      |
         | <--- Data (Seq=y+1, Ack=x+2) ------- |
         |                                      |
         | --- ACK (Seq=x+2, Ack=y+2) --------> |
         |                                      |
        Data Transmission (Bidirectional communication)
  +------+-------+                        +-------+------+
  |              |                        |              |
  |    Client    |                        |    Server    |
  |              |                        |              |
  +--------------+                        +--------------+
```

In this illustration, the three-way handshake for establishing a TCP connection is shown:

1. The client sends a SYN (Synchronize) packet with an initial sequence number (Seq=x).
2. The server responds with a SYN-ACK (Synchronize-Acknowledge) packet with its own sequence number (Seq=y) and the acknowledgement number (Ack=x+1).
3. The client sends an ACK (Acknowledge) packet with the sequence number (Seq=x+1) and acknowledgement number (Ack=y+1).

After the connection is established, data transmission takes place. In this example, the client sends data to the server, the server responds with its own data, and the client acknowledges the received data. This process can continue for as long as the connection is maintained.



# Python TCP Sockets

For this example, I'll use Python, as it's a popular and easy-to-understand language. We'll create a server that accepts client connections, sends and receives bytes, and displays the output.

First, let's create a simple TCP server. You can save this code in a file called `tcp_server.py`:

```python
import socket

def main():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_address = ('localhost', 5000)
    server_socket.bind(server_address)
    server_socket.listen(1)

    print('Server is listening on port 5000...')

    while True:
        client_socket, client_address = server_socket.accept()
        print(f'Accepted connection from {client_address}')

        data = client_socket.recv(1024)
        print(f'Received data: {data.decode()}')

        response = b'Hello, client!'
        client_socket.send(response)
        print(f'Sent response: {response}')

        client_socket.close()

if __name__ == '__main__':
    main()
```

Now, let's create a simple TCP client. Save this code in a file called `tcp_client.py`:

```python
import socket

def main():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_address = ('localhost', 5000)
    client_socket.connect(server_address)

    message = b'Hello, server!'
    client_socket.send(message)
    print(f'Sent message: {message}')

    response = client_socket.recv(1024)
    print(f'Received response: {response.decode()}')

    client_socket.close()

if __name__ == '__main__':
    main()
```

To test the server and client, follow these steps:

1. Open two terminal windows.
2. In the first terminal, navigate to the directory containing `tcp_server.py` and run the command `python tcp_server.py`. The server should start and display a message indicating it's listening on port 5000.
3. In the second terminal, navigate to the directory containing `tcp_client.py` and run the command `python tcp_client.py`. The client should send a message to the server and receive a response.

In this example, the server accepts a client connection, receives data, sends a response, and closes the connection. The client connects to the server, sends a message, receives a response, and closes the connection. The output is displayed in both the server and client terminals.


# Python 3 Libraries for TCP Sockets

In Python 3, there are several common libraries for working with TCP sockets. 

1. socket (Python Standard Library): The socket module provides a low-level interface for working with network sockets, including TCP sockets. It's the most commonly used library for this purpose in Python.

Example usage:

```python
import socket

def main():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect(('example.com', 80))
    s.send(b'GET / HTTP/1.1\r\nHost: example.com\r\n\r\n')
    response = s.recv(4096)
    print(response)
    s.close()

if __name__ == '__main__':
    main()
```

2. asyncio (Python Standard Library): The asyncio module provides asynchronous I/O, event loop, and concurrency support for Python. It includes support for TCP sockets using the asyncio.StreamReader and asyncio.StreamWriter classes.

Example usage:

```python
import asyncio

async def main():
    reader, writer = await asyncio.open_connection('example.com', 80)
    writer.write(b'GET / HTTP/1.1\r\nHost: example.com\r\n\r\n')
    await writer.drain()
    response = await reader.read(4096)
    print(response)
    writer.close()
    await writer.wait_closed()

asyncio.run(main())
```

3. Twisted: Twisted is a popular third-party library for event-driven networking in Python. It provides support for various network protocols, including TCP.

Example usage:

```python
from twisted.internet import protocol, reactor

class EchoClient(protocol.Protocol):
    def connectionMade(self):
        self.transport.write(b'GET / HTTP/1.1\r\nHost: example.com\r\n\r\n')

    def dataReceived(self, data):
        print(data)
        self.transport.loseConnection()

class EchoFactory(protocol.ClientFactory):
    def buildProtocol(self, addr):
        return EchoClient()

    def clientConnectionFailed(self, connector, reason):
        print("Connection failed.")
        reactor.stop()

    def clientConnectionLost(self, connector, reason):
        print("Connection lost.")
        reactor.stop()

reactor.connectTCP("example.com", 80, EchoFactory())
reactor.run()
```

