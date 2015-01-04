#!/usr/bin/env python3

import socket as s

import netifaces

interfaces = netifaces.interfaces()

l = list()

for i in interfaces:
    for j in netifaces.ifaddresses(i):
        if j == netifaces.AF_INET:
            print (i,end=' ')
            print(netifaces.ifaddresses(i)[j])
