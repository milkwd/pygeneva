# pygeneva
For use with mobile operators
# 将上面代码保存成geneva.py，然后执行下面命令安装依赖
yum install -y python3 python3-devel gcc gcc-c++ git libnetfilter* libffi-devel
pip3 install --upgrade pip
pip3 install scapy netfilterqueue
# 运行程序
nohup ./python3 geneva.py -q 100 -w 4 &
iptables -I OUTPUT -p tcp -m multiport --sports 80,443 --tcp-flags SYN,RST,ACK,FIN,PSH SYN,ACK -j NFQUEUE --queue-num 100
