#!/usr/bin/python
# -*- coding: utf-8 -*-
 
# Programa Servidor
# www.pythondiario.com
 
import socket
import sys
import subprocess
from socket import error as SocketError

 
# Creando el socket TCP/IP
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Enlace de socket y puerto
server_address = ('localhost', 10000)
print >>sys.stderr, 'empezando a levantar %s puerto %s' % server_address
sock.bind(server_address)

# Escuchando conexiones entrantes
sock.listen(1)
 
while True:
    # Esperando conexion
    print >>sys.stderr, 'Esperando para conectarse'
    connection, client_address = sock.accept()
    close=False
    try:
        print >>sys.stderr, 'concexion desde', client_address		
        # Recibe los datos en trozos y reetransmite
        while True:
            data = connection.recv(19)
        	
            if(data=='exit'):
           	    print('Has cerrado la conexion :c')
                    close=True
           	    break
            print('recibido: ')        
            print >>sys.stderr, "%s" %data
            message = subprocess.check_output(data, shell=True)
            if message:
                print >>sys.stderr, 'enviando mensaje de vuelta al cliente'
                print(message)
                connection.sendall(message)
            else:
                print >>sys.stderr, 'no hay mas datos', client_address
                break
        if(close):
             sock.listen(0)
             connection.close()
             break    
    except SocketError as e:
    	pass      
    finally:
        # Cerrando conexion
        connection.close()
   
