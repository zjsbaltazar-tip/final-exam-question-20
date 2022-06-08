from ncclient import manager as m


# Network Configuration
class NetConf(object):

    def __init__(self, parser):
        self.host = parser.get("NETCONF", "host")
        self.port = parser.get("NETCONF", "port")
        self.username = parser.get("NETCONF", "username")
        self.password = parser.get("NETCONF", "password")
        self.hostkey_verify = parser.getboolean("NETCONF", "hostkey_verify")

    def init(self):
        self.manager = m.connect(
            host=self.host, port=self.port,
            username=self.username, password=self.password,
            hostkey_verify=bool(self.hostkey_verify)
        )

    