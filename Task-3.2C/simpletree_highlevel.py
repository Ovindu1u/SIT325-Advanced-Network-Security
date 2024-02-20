# Ovindu Undugoda
# BSCP|CS|61|103


# import libraries
from mininet.topo import Topo


class SimpleTree(Topo):

    def build(self, n : int = 2):

        # add the core switch
        core = self.addSwitch("c1")

        # connect n number of aggregate switches to core
        for a in range(n):
            agg = self.addSwitch(f"a{a+1}")
            self.addLink(core, agg)

            # the calculation x*n and x*n + n will give the correct range of numbers each iteration of the parent
            # this is to make sure each layer will count from 0 - n^X, x being how deep the layer is

            # connect n number of edge switches to parent aggregate switches
            for e in range(a*n, a*n + n):
                edge = self.addSwitch(f"e{e+1}")
                self.addLink(agg, edge)
                
                # connect n number of host switches to parent edge switches
                for h in range(e*n, e*n + n):
                    host = self.addHost(f"h{h+1}")
                    self.addLink(edge, host)



# expose topology to mininet
topos = { "simple" : SimpleTree }
        

            