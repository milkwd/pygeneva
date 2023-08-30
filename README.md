# 用途
用于绕过运营商屏蔽
# 将上面代码保存成geneva.py，然后执行下面命令安装依赖
yum install -y python3 python3-devel gcc gcc-c++ git libnetfilter* libffi-devel

pip3 install --upgrade pip

pip3 install scapy netfilterqueue
# 运行程序
nohup ./python3 geneva.py -q 100 -w 4 &

iptables -I OUTPUT -p tcp -m multiport --sports 80,443 --tcp-flags SYN,RST,ACK,FIN,PSH SYN,ACK -j NFQUEUE --queue-num 100
# 免责声明
此软件是根据"[geneva 开源软件"](https://github.com/Kkevsterrr/geneva)提供的，无任何明示或暗示的担保，包括但不限于对适销性、特定目的的适用性和非侵权的担保。在任何情况下，开发者或版权所有者都不对任何索赔、损害或其他责任承担责任，无论在合同、侵权或其他行动中，出于使用该软件或其他交易与软件有关的行为而产生的。

此外，使用此开源软件的用户明白该软件可能涉及审查方面的功能，并同意使用此软件的所有风险将完全由用户承担。开发者及所有关联方均不对由于使用或不适当使用该软件导致的任何直接、间接、意外、特殊、惩戒性或后果性损失承担责任。

此软件并未设计或意图用于规避任何法律审查或监管。用户有责任确保他们对于该软件的使用遵循了所有适用的法律和法规。
