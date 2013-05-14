import struct

from . import magic_cookie, fields


class Packet(object):
    """
    Class to build, modify, and parse DHCP packets
    """
    
    def __init__(self, data=None, **kwargs):
        """
        If data is provide, parse the packet, otherwise
        build a packet with the provided keyword arguments
        """
        self._unpackedData = None
        self.dirty = False      # flip switch to rebuild packet
        
        if not data:
            self.buildPacket(kwargs)
        else:
            self.unpackedData = data # memoize binary packet data
            
        for opt,val in fields.items():
            setattr(self, opt, self.unpackedData[val[0]:val[1]])
            print opt, " : ", self.unpackedData[val[0]:val[1]]
    
    def buildPacket(self, **kwargs):
        """
        Create a packet from provided kwargs
        """
        pass
    
    
    def parsePacket(self, data):
        """
        Parse the provided packet
        """
        if not data:
            return
        
        for opt in fields:
            print opt
            setattr(self, opt, data[fields[opt][0]:fields[opt][1]])
   

    @property
    def unpackedData(self):
        if self._unpackedData:
            return self._unpackedData
    
    @unpackedData.setter
    def unpackedData(self, data):
        """
        Transition the packet from wire format into a
        readable format, and set the attribute.
        Short circuits if data already exists. 
        """
        if self._unpackedData: 
            print("Packet data not parsed as unpacked data already exists")
            return

        fmt = str(len(data)) + "c"
        temp = []
        for b in struct.unpack(fmt,data):
            temp.append(ord(b))
        
        if len(temp) and temp[236:240] == magic_cookie:
            self._unpackedData = temp
        else:
            print "Not a DHCP packet"



    


