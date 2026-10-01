from scapy.all import *
import sys
import pandas as pd
import matplotlib.pyplot as plt
from scapy.layers.dns import DNSRR
from scapy.layers.inet import TCP, UDP
from scapy.layers.l2 import Ether

#rdpcap comes from scapy and loads in our pcap file
packets = rdpcap('IN404.pcapng')

spoofed_mac_count=0
dos_attack_count = 0
port_count = 0
port = 135
pod_count = 0
reset_count = 0

while True:
    print("What would you like to do:")
    print(" 1. Check Ether count for aa:bb:cc:dd:ee:ff")
    print(" 2. Check DNS round robin queries")
    print(" 3. Check source port 135 access")
    print(" 4. Check for denial of service")
    print(" 5. Check reset flag")
    print(" 6. Visualize protocol traffic count")
    print(" 7. Quit program")
    print("Please enter a number (1-7)")
    choice = input()

    if(choice == '1'):
        for packet in packets:
            if (packet[Ether].src == "aa:bb:cc:dd:ee:ff"):
                spoofed_mac_count += 1
        print("Count result for spoofed MAC address", spoofed_mac_count)
        spoofed_mac_count = 0

    elif(choice == '2'):
        dns_count = 0
        for packet in packets:
            if packet.haslayer(DNSRR):
                dns_count +=1
                print(packet[DNSRR].rrname)
        print("DNS round robin query count:", dns_count)
        dns_count = 0

    elif(choice == '3'):
        for packet in packets:
            if packet.haslayer(UDP) or packet.haslayer(TCP):
                if(packet.dport == port):
                    port_count += 1
        print("Port 135 access count", port_count)
        port_count = 0

    elif(choice == '4'):
        for packet in packets:
            if packet.haslayer(TCP):
                if packet[TCP].window == 65535:
                    pod_count += 1
        print("Ping of death", pod_count)
        pod_count = 0

    elif(choice == '5'):
        for packet in packets:
            if packet.haslayer(TCP):
                if packet[TCP].flags == 'R':
                    reset_count += 1
        print("Packet resets", reset_count)
        reset_count = 0

    elif(choice == '6'):
        dataframe = pd.read_csv("IN404.csv")
        protocol = dataframe['Protocol'].value_counts().plot(kind='bar')
        plt.show()

    elif(choice == '7'):
        sys.exit()

    print()
    print()



