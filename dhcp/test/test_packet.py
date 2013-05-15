from twisted.trial import unittest
from mock import Mock, patch

from dhcp.packet import *

class PacketTestCase(unittest.TestCase):
    
    def setUp(self):
        self.good_decoded_packet = [1, 1, 6, 0, 40, 11, 153, 26, 0, 4, 128, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 8, 0, 39, 11, 153, 26, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 99, 130, 83, 99, 53, 1, 1, 55, 36, 1, 2, 3, 4, 5, 6, 11, 12, 13, 15, 16, 17, 18, 22, 23, 28, 40, 41, 42, 43, 50, 51, 54, 58, 59, 60, 66, 67, 128, 129, 130, 131, 132, 133, 134, 135, 57, 2, 4, 236, 97, 17, 0, 83, 207, 141, 203, 0, 41, 70, 17, 155, 185, 187, 80, 137, 0, 23, 98, 93, 2, 0, 0, 94, 3, 1, 2, 1, 60, 32, 80, 88, 69, 67, 108, 105, 101, 110, 116, 58, 65, 114, 99, 104, 58, 48, 48, 48, 48, 48, 58, 85, 78, 68, 73, 58, 48, 48, 50, 48, 48, 49, 255, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        self.mc_non_standard_offset = [6, 0, 40, 11, 153, 26, 0, 4, 128, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 8, 0, 39, 11, 153, 26, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 99, 130, 83, 99, 53, 1, 1, 55, 36, 1, 2, 3, 4, 5, 6, 11, 12, 13, 15, 16, 17, 18, 22, 23, 28, 40, 41, 42, 43, 50, 51, 54, 58, 59, 60, 66, 67, 128, 129, 130, 131, 132, 133, 134, 135, 57, 2, 4, 236, 97, 17, 0, 83, 207, 141, 203, 0, 41, 70, 17, 155, 185, 187, 80, 137, 0, 23, 98, 93, 2, 0, 0, 94, 3, 1, 2, 1, 60, 32, 80, 88, 69, 67, 108, 105, 101, 110, 116, 58, 65, 114, 99, 104, 58, 48, 48, 48, 48, 48, 58, 85, 78, 68, 73, 58, 48, 48, 50, 48, 48, 49, 255, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        self.gdp_enabled_options = {
                'client_system': [93, [0, 0]],
                'client_ndi': [94, [1, 2, 1]],
                'uuid_guid': [97, [0, 83, 207, 141, 203, 0, 41, 70, 17, 155, 185, 187, 80, 137, 0, 23, 98]],
                'vendor_class': [60, [80, 88, 69, 67, 108, 105, 101, 110, 116, 58, 65, 114, 99, 104, 58, 48, 48, 48, 48, 48, 58, 85, 78, 68, 73, 58, 48, 48, 50, 48, 48, 49]],
                'parameter_request_list': [55, [1, 2, 3, 4, 5, 6, 11, 12, 13, 15, 16, 17, 18, 22, 23, 28, 40, 41, 42, 43, 50, 51, 54, 58, 59, 60, 66, 67, 1, 28, 129, 130, 131, 132, 133, 134, 135]],
                'dhcp_message_type': [53, [1]],
                'maximum_dhcp_message_size': [57, [4, 236]]
        }
        
        self.packet = Mock(spec=Packet)

   
    def test_magic_cookie(self):
        """Test that output is correct with magic cookie at default offset"""
        self.packet.magicCookieIndexes = Packet.magicCookieIndexes
        res = self.packet.magicCookieIndexes(self.packet, self.good_decoded_packet)
        self.assertEqual(res, (236, 240))


    def test_no_magic_cookie(self,):
        """Test that ouput is an empty tuple if theres no magic cookie"""
        data = [0] * len(self.good_decoded_packet)
        self.packet.magicCookieIndexes = Packet.magicCookieIndexes
        res = self.packet.magicCookieIndexes(self.packet, data)
        self.assertEqual(res, ())


    def test_magic_cookie_nonstandard_offest(self):
        """Test that the results are correct for a packet that has the magic cookie at a non standard offset"""
        self.packet.magicCookieIndexes = Packet.magicCookieIndexes
        res = self.packet.magicCookieIndexes(self.packet, self.mc_non_standard_offset)
        self.assertEqual(res, (234, 238))

    
    def test_unpack_data(self):
        from pickle import loads
        data = loads("""S"\x01\x01\x06\x00(\x0b\x99\x1a\x00\x04\x80\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x08\x00'\x0b\x99\x1a\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00c\x82Sc5\x01\x017$\x01\x02\x03\x04\x05\x06\x0b\x0c\r\x0f\x10\x11\x12\x16\x17\x1c()*+236:;<BC\x80\x81\x82\x83\x84\x85\x86\x879\x02\x04\xeca\x11\x00S\xcf\x8d\xcb\x00)F\x11\x9b\xb9\xbbP\x89\x00\x17b]\x02\x00\x00^\x03\x01\x02\x01< PXEClient:Arch:00000:UNDI:002001\xff\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00"
p0
.""")
        self.packet.unpackedData = Packet.unpackedData
        # Make sure it returns whatever data is assigned locally
        self.packet._unpacked_data = 'foo' 
        should_be_foo = self.packet.unpackedData.__get__(self.packet    )
        
        # Make sure it returns none if not an assignment and no data
        # assigned locally
        self.packet._unpacked_data = None
        should_be_none = self.packet.unpackedData.__get__(self.packet)
        
        # Make sure it properly unpacks our data
        self.packet.unpackedData.__set__(self.packet, data)
        
        self.assertEqual(self.packet._unpacked_data, self.good_decoded_packet)
        self.assertIsNone(should_be_none)
        self.assertEqual(should_be_foo, "foo")
        
        self.packet._unpacked_data = "bar"
        self.packet.unpackedData.__set__(self.packet, "baz")
        self.assertEqual(self.packet._unpacked_data, "bar")
