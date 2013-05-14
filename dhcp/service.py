from packet import Packet

from twisted.internet.protocol import DatagramProtocol
from twisted.internet import reactor



class DHCP(DatagramProtocol):

    def startProtocol(self):
        """
        Called when transport is connected
        """
        self.transport.joinGroup('224.0.0.1')


    def stopProtocol(self):
        pass


    def datagramReceived(self, data, (host, port)): 
        a = Packet(data=data)
        

if __name__ == "__main__":
    __package__ = "dhcp.service"
    reactor.listenMulticast(67, DHCP(), listenMultiple=True)
    reactor.run()