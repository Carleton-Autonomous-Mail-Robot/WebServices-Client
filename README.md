
# WebServices-Client

A web client which facilitates confidential communications with a server.
All communications are encrypted, client doesn't care what the payload of the message is.
The payload is passed to another system which handles it. This client server pair, is meant
to be general and inserted into any enviroment.

## Requirements:

 - Python3.7 and up
 - PyCryptoDome

## Installation:

 To install required libraries, run the following commands in WebServices-Client directory:
    

> pip3 install -r requirements.txt

## Running:
> python3 client_controller.py

## Todo:
 - [x] basic client_server_interface
 - [x] basic cipher class
 - [x] client handles responses from server
 - [ ] key exhange handling
 - [ ] develop test cases
 - [ ] develop UML
 - [ ] passing the payload to the service which uses this client once recieved from server

