import scapy.all as scapy


def scan(ip):
    arp_request= scapy.ARP(pdst=ip)
    broadcast=scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    arp_request_broadcast=  broadcast/arp_request
    answered_list= scapy.srp(arp_request_broadcast,timeout=1)[0]
    
    for elements in answered_list:
        print(elements[1].psrc)
        print(elements[1].hwsrc)
        print("----------------------------------------------------------------------------")
  
    

scan("192.168.115.1/24")#use your IP here by typing \\route -n in terminal\\
