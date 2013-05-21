from packet import Packet
from . import MESSAGE_TYPES
from .errors import DHCPError

from twisted.internet.protocol import DatagramProtocol

from collections import defaultdict


def dhcpDebugPacketHandler(f):
    def wrapper(*args, **kwargs):
        print f.__name__[0:-8], " received"
        return f(*args, **kwargs)
    return wrapper


class DHCPMulti(DatagramProtocol):

    def startProtocol(self):
        """
        Called when transport is connected
        """
        self.transport.joinGroup('224.0.0.1')
        # { int(xid) : [Packet, Packet, Packet,...]}
        self.sessions = defaultdict(list)

    def stopProtocol(self):
        """
        Clean up when protocol is getting ready to stop
        """
        pass

    def datagramReceived(self, data, (host, port)):
        """
        Heard a packet on port 67. There's no guarantee that
        it's a DHCP packet though!
        """
        print host, port
        try:
            # Instantiate packet and extract the xid
            p = Packet(data)
            # store the packet in it's session
            xid = p.getHeader("xid")
            self.sessions[xid].append(p)

            # dispatch the packet to appropriate handler according
            # to the DHCP_MESSAGE_TYPE option
            msg_type = MESSAGE_TYPES[p.getOption("dhcp_message_type")].split("_")[1].lower()
            getattr(self, msg_type + "Received")(p)
        except DHCPError:
            import traceback
            print DHCPError
            traceback.print_exc()

    def undefReceived(self, packet):
        DHCPError("Packet with type ERROR_UNDEF received")

    @dhcpDebugPacketHandler
    def discoverReceived(self, packet):
        """
        We received a discover packet. In the simplest case
        we'll send an offer with the yiaddr field assigned to
        the ip address for the client.
        """
        pass

    @dhcpDebugPacketHandler
    def requestReceived(self, packet):
        """
        This, in most cases, will be recieved in response to an
        OFFER sent to the client.
        """
        pass

    @dhcpDebugPacketHandler
    def declineReceived(self, packet):
        """ Client has declined our OFFER """
        pass

    @dhcpDebugPacketHandler
    def releaseReceived(self, packet):
        """ Client has released it's assigned address """
        pass

    @dhcpDebugPacketHandler
    def informReceived(self, packet):
        pass
