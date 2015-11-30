from scapy.all import *
def arp_display(pkt):
  if pkt[ARP].op == 1: #who-has (request)
    if pkt[ARP].psrc == '0.0.0.0': # ARP Probe
      if pkt[ARP].hwsrc == 'RE:PL:AC:E_:TH:IS':
        print "My BigMACs bring all the boys to the yard"
      else:
        print "My BigMACs weren't big enough"

print sniff(prn=arp_display, filter="arp", store=0, count=10)
