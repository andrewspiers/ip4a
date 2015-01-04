import socket as s

import getnifs

nifs = getnifs.get_network_interfaces()

l = list()

for i in nifs:
    l.append(i)

for i in l:
    print (i)
