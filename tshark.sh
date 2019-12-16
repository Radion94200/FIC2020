#!/bin/sh

echo "These program serve to extract data from the pcap capture"
echo "$cb52ae4d15503c598f0bb42b8af1ce51.pcap"
tshark -r cb52ae4d15503c598f0bb42b8af1ce51.pcap -e dns.qry.name -Tfields -Y "ip.src == 172.16.42.99" -Y "dns.qry.name" > capture
