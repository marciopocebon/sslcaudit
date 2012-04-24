__author__ = 'abb'

class ClientConnection(object):
    def __init__(self, sock, client_address):
        self.sock = sock
        self.client_address = client_address

    def get_client_id(self):
        '''
        This function returns a session key for a given socket. A key is used to distinguish
        between different clients under test. In the current implementation we use client IP
        address as a key.
        '''
        return self.client_address[0]

    def getpeername(self):
        return self.client_address
