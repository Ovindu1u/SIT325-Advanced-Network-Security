# Ovindu Undugoda
# BSCP|CS|61|103


# import mininet
from mininet.topo import Topo

# define class
class Topology(Topo):
    
    # this method is overridden to create our custom topology
    def build(self):
        # add hosts
        host1 = self.addHost("host1")
        host2 = self.addHost("host2")

        # add switch
        switch = self.addSwitch("switch1")
        
        # link hosts to switch
        self.addLink(switch, host1)
        self.addLink(switch, host2)


# mininet checks the global variable "topos" to see what topology classes are availbale
# topos should be a dictionary with of {key : inline function, ...} 
topos = {
    'topology' : (lambda : Topology())
}