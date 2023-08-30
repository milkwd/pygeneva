#!/usr/bin/env python3

import os
import signal
from scapy.all import *
from netfilterqueue import NetfilterQueue
import argparse

window_size = 4

def modify_window(pkt):
    try:
        ip = IP(pkt.get_payload())
        if ip.haslayer(TCP) and ip[TCP].flags == "SA":
            ip[TCP].window = window_size
            del ip[IP].chksum
            del ip[TCP].chksum
            pkt.set_payload(bytes(ip))
        elif ip.haslayer(TCP) and ip[TCP].flags == "FA":
            ip[TCP].window = window_size
            del ip[IP].chksum
            del ip[TCP].chksum
            pkt.set_payload(bytes(ip))
        elif ip.haslayer(TCP) and ip[TCP].flags == "PA":
            ip[TCP].window = window_size
            del ip[IP].chksum
            del ip[TCP].chksum
            pkt.set_payload(bytes(ip))
        elif ip.haslayer(TCP) and ip[TCP].flags == "A":
            ip[TCP].window = window_size
            del ip[IP].chksum
            del ip[TCP].chksum
            pkt.set_payload(bytes(ip))
    except:
        pass

    pkt.accept()

def parsearg():
    parser = argparse.ArgumentParser(description='Description of your program')

    parser.add_argument('-q', '--queue', type=int, help='iptables Queue Num')
    parser.add_argument('-w', '--window_size', type=int, help='Tcp Window Size')

    args = parser.parse_args()

    if args.queue is None or args.window_size is None:
        exit(1)
    
    window_size = args.window_size

    return args.queue

def main():
    queue_num = parsearg()
    nfqueue = NetfilterQueue()
    nfqueue.bind(queue_num, modify_window)

    try:
        print("Starting netfilter_queue process...")
        nfqueue.run()
    except KeyboardInterrupt:
        pass

if __name__ == "__main__":
    #sys.stdout = os.fdopen(sys.stdout.fileno(), 'w', 0)
    signal.signal(signal.SIGINT, lambda signal, frame: sys.exit(0))
    main()

# 将上面代码保存成geneva.py，然后执行下面命令安装依赖
# yum install -y python3 python3-devel gcc gcc-c++ git libnetfilter* libffi-devel
# pip3 install --upgrade pip
# pip3 install scapy netfilterqueue
# 运行程序
# nohup ./python3 geneva.py -q 100 -w 4 &
# iptables -I OUTPUT -p tcp -m multiport --sports 80,443 --tcp-flags SYN,RST,ACK,FIN,PSH SYN,ACK -j NFQUEUE --queue-num 100



