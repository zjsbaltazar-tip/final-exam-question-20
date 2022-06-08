from netconf import NetConf as nf
import xml.dom.minidom
import requests

class NetAuto(object):
    
    def __init__(self, netconf: nf):
        self.netconf = netconf
        
    def display_config(self):
        netconf_filter = """
        <filter>
            <native xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-native" />
        </filter>
        """
        netconf_reply = self.netconf.manager.get_config(source="running", filter=netconf_filter)
        print(xml.dom.minidom.parseString(netconf_reply.xml).toprettyxml())

    def set_ip_address(self, address, mask):
        ipconfig = f"""
        <config>
            <native xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-native">
                <interface>
                        <GigabitEthernet>
                                <name>1</name>
                                <ip>
                                        <address>
                                                <primary>
                                                        <address>{address}</address>
                                                        <mask>{mask}</mask>
                                                </primary>
                                        </address>
                                </ip>
                        </GigabitEthernet>
                </interface>
            </native>
        </config>
        """
        netconf_reply = self.netconf.manager.edit_config(target="running", config=ipconfig)
        print(xml.dom.minidom.parseString(netconf_reply.xml).toprettyxml())

    def set_rip_v2(self, address):
        ripv2 = f"""
        <config>
            <native xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-native">
                    <router>
                            <rip xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-rip">
                                    <network>
                                            <ip>{address}</ip>
                                    </network>
                            </rip>
                    </router>
            </native>
        </config>
        """
        netconf_reply = self.netconf.manager.edit_config(target="running", config=ripv2)
        print(xml.dom.minidom.parseString(netconf_reply.xml).toprettyxml())