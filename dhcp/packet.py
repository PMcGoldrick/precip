""" Defines DHCP Packet structure, parsers, and generators """

import struct
from . import MAGIC_COOKIE, FIELDS, OPTS, OPT_TYPES
from .errors import DHCPError


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

        # {string_name : [ID, Value]}
        self.enabled_options = {}
        
        # string_name : value
        self.headers = {}

        if reply:
            self.buildPacket(**kwargs)
        else:
            self.unpackedData = data  # memoize binary packet data
            self.parseHeaders(self.unpackedData)
            self.parseOptions(self.unpackedData)
    
    def convert(self, val, fmt):
        """
        The conversion methods aren't guaranteed
        to not be implementation specific - so we'll keep them scoped here
        for now.
        """
        print "Convert called with %s, %s" % (val, fmt)
        def convInt(val):
            """ Convert from list of 8 bit (char) to unsigned long """
            if len(val) == 4:
                return struct.unpack("!I", ''.join([chr(i) for i in val]))[0]
            
            elif len(val) == 2:
                return struct.unpack("!H", ''.join([chr(i) for i in val]))[0]
            
            elif len(val) == 1:
                return val[0]
        
        def convIPv4(val):
            """ Convert from a bytearray to IP address """
            if not len(val) == 4:
                raise ValueError("ByteArray not appropriate for an IPv4 address")
            raise NotImplementedError("Method has not been implemented yet")
        
        def convMAC(val, length=6):
            """
            Convert to a hardware address.
            For `chaddr` length should be set from `hlen` header.
            `htype` is ignored in this implementation because... yeah.
            """
            res = ["%02x" % i for i in val[:length]]
            return ":".join(res)
        
        def convStr(val):
            """ Convert list of 8 bit ints to a string!"""
            res = [chr(i) for i in val]
            return ''.join(res)
        
        if not val or fmt == "int":
            return val[0]
        elif "int" in fmt:
            return convInt(val)
        elif fmt == "ipv4":
            return convIPv4(val)
        elif fmt == "hwmac":
            return convMAC(val)
        elif fmt == "str":
            return convStr(val)
        
    def getHeader(self, header, force_type=False):
        """
        Get the value for the default header and unpack it to
        and appropriate format.
        """
        if force_type:
            raise NotImplementedError()
        val = self.headers[header]
        fmt = FIELDS[header][2]
        return self.convert(val, fmt)
    
    def getOption(self, option, force_type=False):
        """
        Get the value for the default header and unpack it to
        and appropriate format.
        """
        if force_type:
            raise NotImplementedError()
        val = self.enabled_options[option]
        fmt = OPT_TYPES[val[0]]
        print "optoin val, fmt: ", val, " ", fmt
        return self.convert(val[1], fmt)
    
    @property
    def messageType(self):
        """
        Return the string represented by this packets
        dhcp_message_type option #53
        """
        if not self.unpackedData:
            raise DHCPError("Invalid packet, or packet not parsed")
        return self.enabled_options["dhcp_message_type"][1][0]

    def buildPacket(self, **kwargs):
        """
        Create a packet from provided kwargs
        """
        pass

    def parseHeaders(self, data):
        """
        Parse the provided packet
        """
        if not data:
            DHCPError("No data provided for parsing")
        # Parse the required DHCP headers
        for opt in FIELDS:
            offset = FIELDS[opt][0]
            length = FIELDS[opt][1]
            self.headers[opt] = data[offset:offset + length]

    def parseOptions(self, data):
        """
        Extract and assign the optional params in the packet
        """
        index = self.magicCookieIndexes(data)[1]
        while index < len(data):
            # Octect indicates we've reached
            # the end of interesting packet data
            option = data[index]
            if option == 255:
                break
            # Padding
            elif option == 0:
                index += 1
            else:
                vlength = data[index + 1]
                vstart = index + 2
                vend = vstart + vlength
                #[ ID | length | Data ]
                self.enabled_options[OPTS[option]] = [option, data[vstart:vend]]
                index = vend
                vstart = vend = vlength = None

    def magicCookieIndexes(self, data):
        """
        Locate ant return a tuple containing
        indexes that represent the slice of ``data``
        which contains MAGIC_COOKIE
        """
        mc_index = ()
        # This is the generally accepted default location
        # for MAGIC_COOKIE, but it's not required. 
        if data[236:240] == MAGIC_COOKIE:
            mc_index = (236, 240)
        else:
            res = [(i, i + len(MAGIC_COOKIE)) for i in range(len(data) - len(MAGIC_COOKIE)) if data[i:i + len(MAGIC_COOKIE)] == MAGIC_COOKIE]
            if len(res):
                mc_index = res[0]
        return mc_index

    @property
    def unpackedData(self):
        """
        this holds the parsable unpacked struct for the packet
        """
        if self._unpacked_data:
            return self._unpacked_data
        else:
            return None

    @unpackedData.setter
    def unpackedData(self, data):
        """
        Transition the packet from wire format into a
        readable format, and set the attribute.
        Short circuits if data already exists.
        """
        if self._unpacked_data:
            raise DHCPError("Packet data not parsed as unpacked data already exists")
            return
        
        # Convert into 8bit ints
        fmt = str(len(data)) + "c"
        temp = [ord(char) for char in struct.unpack(fmt, data)]
        
        # find the magic cookie in the packet to ensure
        # this is actually a dhcp packet.
        if len(temp) and self.magicCookieIndexes(temp):
            self._unpacked_data = temp
        else:
            print "Not a DHCP packet"