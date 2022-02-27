# Tracy Qiu NUID: 001313852 
# I designed my client by first creating the TCP socket and a TCP connection. 
# Then the client socket was created and connected. The input nuid string was encoded and sent to the server.
# Once the message is received, it is decoded and the expressions are produced in a loop.
# The message containing the flag signifies the end of the communication or returns a fail. 
# I tesed my code by connecting to the local host which produced a secret key.
# An issue that I ran into at first was the client could not connect then I changed the 
# server port number from 12001 to 12008 and it was able to connect because the previous 
# port number was busy with too many conenctions being made to it. 


# Secret flag: c76abb95019e55621ab680bc45b0c9ff44dd0a170710baee1023c75bfdcecfcc

import math
from socket import *
# Create a TCP/IP socket

# TCP connection with the server. 
server_address = 'phase.coe.neu.edu'
#server_address = 'localhost'
server_port_number = 12008
identifier = ( server_address , server_port_number )

# Create client socket
client_socket = socket( AF_INET , SOCK_STREAM )
client_socket.connect( identifier )

# get input string and sent message to server 
intro_message = 'EECE2540 INTR 001313852' 
print(intro_message)
send_message = intro_message.encode()
client_socket.send( send_message )
receive_message = client_socket.recv( 1024 )
expression = receive_message.decode()

# Calculate and print results 
while 'EECE2540 EXPR' in expression:
  express_string=expression.replace('EECE2540 EXPR ','')
  input_string=eval(express_string)
  input_string='EECE2540 RSLT ' + str(input_string)
  send_message = input_string.encode()

  client_socket.send( send_message )
  receive_message = client_socket.recv( 1024 )
  expression = receive_message.decode()
  print(expression)

client_socket.close()