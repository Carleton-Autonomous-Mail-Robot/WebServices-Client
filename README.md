
# WebServices-Client

A web client which facilitates confidential communications with a server.
All communications are encrypted, client doesn't care what the payload of the message is.
The payload is passed to another system which handles it. This client server pair, is meant
to be general and inserted into any enviroment.

## Requirements:

 - Python3.7 and up
 - Flask
 - PyCryptoDome
 - Linux/Unix Enviroment (Mac OS X is acceptable)

## Installation:

To install required libraries, run the following commands in WebServices-Client directory:
    

> pip3 install -r requirements.txt

## Running:
> export FLASK_APP=interface.py

> flask run


## Testing:
 Visit localhost:5000/inbox or use postman

