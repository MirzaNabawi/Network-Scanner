import scapy.all as scapy

def scan(ip): 
    scapy.arping(ip) 

scan("192.168.115.1/24")