# Ovindu Undugoda
# BSCP|CS|61|103


# import libraries
from mininet.topo import Topo

# not required, only here for type annotation
from mininet.net import Mininet
from mininet.link import Link
from mininet.node import Node

class C_Topology ( Topo ):
    # Simple topology example
    def __init__( self ):
        # Create custom topo.

        # Initialize topology
        Topo.__init__( self )

        # Add hosts and switches
        h1 = self.addHost( 'h1' )
        h2 = self.addHost( 'h2' )
        h3 = self.addHost( 'h3' )
        h4 = self.addHost( 'h4' )
        leftSwitch = self.addSwitch( 's1' )
        rightSwitch = self.addSwitch( 's2' )

        # Add links
        self.addLink( h1, leftSwitch )
        self.addLink( h2, leftSwitch )
        self.addLink( leftSwitch, rightSwitch )
        self.addLink( rightSwitch, h3 )
        self.addLink( rightSwitch, h4 )


# itterates through all the links in a net and get all that links the given host
def get_host_links(net : Mininet, host : Node) -> list[Link]:
    links = []
    for link in net.links:
        # check if either one of the hosts are the current host
        if host == link.intf1.node or host == link.intf2.node:
            # if so, add to list
            links.append(link)
    
    return links

# my custom net command
def my_net(net : Mininet):
    # iterates all hosts
    for host in net.values():
        # get hosts links
        links = get_host_links(net, host)
    
        # print them
        link_str = ""
        for link in links:
            # this is for aesthetic purposes only, this makes sure that the first
            # interface is always the current hosts interface
            # if the first interfaces host is current host
            if link.intf1.node == host:
                # we print the first interface first
                link_str += f" {link.intf1}:{link.intf2}"
            else:
                # else we print the second interface first
                link_str += f" {link.intf2}:{link.intf1}"

        # print the host and formatted link string  
        print(f"{host}{link_str}")

# calls the net and pingAll functions
def net_test(net : Mininet):
    print("Net command:\n")
    my_net(net)
    print("\nPing all:\n")
    net.pingAll()
    print()

# global dictionaries to expose topologies and tests to mininet
topos = { 'C_Topology' : C_Topology}
tests = { 'net_test' : net_test}

