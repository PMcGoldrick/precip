from twisted.internet import reactor

import dhcp.service

if __name__ == "__main__":
    reactor.listenMulticast(67, dhcp.service.DHCP(), listenMultiple=True)
    reactor.run()