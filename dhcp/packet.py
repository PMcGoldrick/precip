""" Defines DHCP Packet structure, parsers, and generators """
import struct
from . import MAGIC_COOKIE, FIELDS


class Packet(object):
    """
    Class to build, modify, and parse DHCP packets
    """
    
    def __init__(self, data, reply=False, **kwargs):
        """
        If data is provide, parse the packet, otherwise
        build a packet with the provided keyword arguments
        """
        self._unpacked_data = None
        self.dirty = False      # flip switch to rebuild packet
        
        if reply:
            self.buildPacket(**kwargs)
        else:
            self.unpackedData = data # memoize binary packet data
            self.parsePacket(self.unpackedData)


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
            print("No data provided for parsing")
        
        # Parse the required DHCP headers
        for opt in FIELDS:
            offset = FIELDS[opt][0]
            length = FIELDS[opt][1]
            setattr(self, opt, data[offset:offset+length])
            print opt, ": ", data[offset:offset+length]
        print "################################"
        
        #Option Fields start AFTER the MAGIC_COOKIE
        opts_start = [(i, i+len(MAGIC_COOKIE)) for i in xrange(len(data)) if data[i:i+len(MAGIC_COOKIE)] == MAGIC_COOKIE][0][1]+1
        #TODO

    @property
    def unpackedData(self):
        """
        this holds the parsable unpacked struct for the packet
        """
        if self._unpacked_data:
            return self._unpacked_data

    
    @unpackedData.setter
    def unpackedData(self, data):
        """
        Transition the packet from wire format into a
        readable format, and set the attribute.
        Short circuits if data already exists. 
        """
        if self._unpacked_data: 
            print("Packet data not parsed as unpacked data already exists")
            return
        
        fmt = str(len(data)) + "c"
        temp = []
        for blk in struct.unpack(fmt, data):
            temp.append(ord(blk))
        
        if len(temp) and temp[236:240] == MAGIC_COOKIE:
            self._unpacked_data = temp
        else:
            print "Not a DHCP packet"
            



    


