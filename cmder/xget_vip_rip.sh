#!/bin/bash
# modified by Justice @2013.11.20
# xget_vrip_rip.sh v1.1


#IP=$(hostname -i)

R_URL=http://192.168.237.61/route.txt
R_URL_CNC=http://192.168.230.40/route.txt
ALLVIP_URL=http://192.168.1.10/viplist.txt

VIP=$1

if [[ -z "$1" ]] ;then
    echo "Usage: xget_vip_rip.sh <vip>"
    exit
fi

case $2 in
s|quite)
    curl -s $R_URL | grep "$VIP:" | awk -F, '{ print $2 }'
    curl -s $R_URL_CNC | grep "$VIP:" | awk -F, '{ print $2 }'
;;
*)
    curl -s $R_URL | grep "$VIP:"
    curl -s $R_URL_CNC | grep "$VIP:"
    echo " "
    echo "------other info-----"
    curl -s $ALLVIP_URL | grep "$VIP:"
;;
esac
