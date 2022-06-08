from netconf import NetConf as nf
from netauto import NetAuto as na
from configparser import ConfigParser as conf

# Application main file
if __name__ == "__main__":
    # Configuration Parser
    parser = conf()
    parser.read("conf.ini")
    # Network Configuration
    netconf = nf(parser)
    netconf.init()
    # Network Automation
    netauto = na(netconf)
    # Display current configuration of the router
    netauto.display_config()
    # Set the IP address of the Gigabit Ethernet 1 of the CSR1000v router to 192.168.56.101
    netauto.set_ip_address("192.168.56.101", "255.255.255.0")
    # Configure the routing protocol to RIP version 2
    netauto.set_rip_v2("192.168.56.0")
