from twisted.internet import reactor

import dhcp.service

if __name__ == "__main__":
    reactor.listenMulticast(67, dhcp.service.DHCPMulti(), listenMultiple=True)
    reactor.run()