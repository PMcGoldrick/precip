class Packet(object):
    """
    Class to build, modify, and parse DHCP packets
    """
    
    def __init__(self, data=None, **kwargs):
        """
        If data is provide, parse the packet, otherwise
        build a packet with the provided keyword arguments
        """
        self.wireFormat = data  # memoize binary packet data
        self.dirty = False      # flip switch to rebuild packet
        if not data:
            self.buildPacket(kwargs)
        else:
            self.parsePacket(data)
    
    
    def buildPacket(self, **kwargs):
        """
        Create a packet from provided kwargs
        """
        pass
    
    
    def parsePacket(self, data):
        """
        Parse the provided packet
        """
        pass
    
    @property
    def wireFormat(self):
        if self.wireFormat and not self.dirty:
            return self.wireFormat
        else:
            # create the binary representation of this packet
            self.dirty = False
        
    


