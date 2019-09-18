#!/usr/bin/python
# -*- coding: utf-8 -*-
 
# Programa Cliente
# www.pythondiario.com

import socket
import sys
 
# Creando un socket TCP/IP
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
 
# Conecta el socket en el puerto cuando el servidor esté escuchando
server_address = ('localhost', 10000)
print >>sys.stderr, 'conectando a %s puerto %s' % server_address
sock.connect(server_address)

commands=['ls', 'pwd', 'exit', 'cd']
try:
     
    # Enviando datos
    
    message = raw_input('Digite un comando: ')
    print >>sys.stderr, 'enviando comando...'
    
            	
    if(message!='exit'):
        
        
        if(message[0:2]!='cd' and commands.count(message)==0):
        	print 'Este comando no existe'
                
        else:
                if(message[0:2]=='cd'):
            	    message+=' ; pwd'  
	        sock.sendall(message)
	        # Buscando respuesta
	        amount_received = 0
	        amount_expected = len(message)
	        print('recibiendo: ')
	    
	    
	        while amount_received<amount_expected:

	            data = sock.recv(1024)
	            amount_received += len(data)
	            #print('recibido: ')
	            print >>sys.stderr, '%s' %data
    else:
		sock.sendall(message)
finally:
    print >>sys.stderr, 'cerrando socket'
    sock.close()
