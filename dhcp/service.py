from packet import Packet

from twisted.internet.protocol import DatagramProtocol
from twisted.internet import defer

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
        try:
            a = Packet(data)
            a.messageType()
        except DHCPError:
            import traceback
            print DHCPError
            traceback.print_exc()

    def discoverRecieved(self,):
        print "Recieved a DISCOVER packet"
