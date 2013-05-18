from packet import Packet
from . import MESSAGE_TYPES, FIELDS
from .errors import DHCPError
from .util import byteArrayToInt4

from twisted.internet.protocol import DatagramProtocol
from twisted.internet import defer


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
        self.sessions = {}

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
            for header in FIELDS:
                print header, ": ", p.getHeader(header)
            
            # store the packet in it's session
            # self.sessions[xid] = self.sessions.get(xid, []).append(p)

            # dispatch the packet to appropriate handler according
            # to the DHCP_MESSAGE_TYPE header
            msg_type = MESSAGE_TYPES[p.messageType].split("_")[1].lower()
            getattr(self, msg_type + "Received")(p)
        except DHCPError:
            import traceback
            print DHCPError
            traceback.print_exc()

    def undefReceived(self, packet):
        DHCPError("Packet with type ERROR_UNDEF received")

    @dhcpDebugPacketHandler
    def discoverReceived(self, packet):
        pass

    @dhcpDebugPacketHandler
    def requestReceived(self, packet):
        pass

    @dhcpDebugPacketHandler
    def declineReceived(self, packet):
        pass

    @dhcpDebugPacketHandler
    def releaseReceived(self, packet):
        pass

    @dhcpDebugPacketHandler
    def informReceived(self, packet):
        pass
