from packet import Packet

from twisted.internet.protocol import DatagramProtocol




class DHCP(DatagramProtocol):

    def startProtocol(self):
        """
        Called when transport is connected
        """
        self.transport.joinGroup('224.0.0.1')


    def stopProtocol(self):
        """
        Clean up when protocol is getting ready to stop
        """
        pass


    def datagramReceived(self, data, (host, port)):
        """
        Heard a packet on port 67. There's no garuntee that
        it's a DHCP packet though!
        """
        a = Packet(data)
    
    
    def discoverRecieved(self,):
        pass
    

