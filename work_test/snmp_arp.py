#!/usr/bin/python
# -*- coding:utf-8 -*-
import commands , re

def arp(community,ip,type):
    if type == 'cisco':
        arp_db = {}
        snmp_arp_db = commands.getoutput('snmpwalk -v 2c -c %s %s IP-MIB::ipNetToMediaPhysAddress'%(community,ip)).replace(' ', '')
        for snmp_arp in snmp_arp_db.split('\n'):
            if re.search(r'STRING:(.*)', snmp_arp).group(1) == '0:0:0:0:0:0' or re.search(r'STRING:(.*)', snmp_arp).group(1) == 'aa:aa:bb:bb:cc:cc':
                continue
            mac_address = re.sub(r'((?<=:)[0-9a-f](?=:)|(?<=^)[0-9a-f](?=:)|(?<=:)[0-9a-f](?=$))', r'0\1',re.search(r'STRING:(.*)', snmp_arp).group(1))
            ip_address = re.search(r'(.*?)(\d+.\d+.\d+.\d+)=(.*)', snmp_arp).group(2)
            arp_db[ip_address] = mac_address
        return arp_db
    elif type == 'pfsense':
        arp_db = {}
        snmp_arp_db = commands.getoutput('snmpwalk -v 2c -c %s %s IP-MIB::ipNetToMediaPhysAddress'%(community,ip)).replace(' ', '')
        for snmp_arp in snmp_arp_db.split('\n'):
            if re.search(r'STRING:(.*)', snmp_arp).group(1) == '0:0:0:0:0:0' or re.search(r'STRING:(.*)', snmp_arp).group(1) == 'aa:aa:bb:bb:cc:cc':
                continue
            mac_address = re.sub(r'((?<=:)[0-9a-f](?=:)|(?<=^)[0-9a-f](?=:)|(?<=:)[0-9a-f](?=$))', r'0\1',re.search(r'STRING:(.*)', snmp_arp).group(1))
            ip_address = re.search(r'(.*?)(\d+.\d+.\d+.\d+)=(.*)', snmp_arp).group(2)
            arp_db[ip_address] = mac_address
        return arp_db
    elif type == 'hillstone':
        arp_db = {}
        snmp_arp_db = commands.getoutput('snmpwalk -v 2c -c %s %s IP-MIB::ipNetToMediaPhysAddress'%(community,ip)).replace(' ', '')
        for snmp_arp in snmp_arp_db.split('\n'):
            if re.search(r'STRING:(.*)', snmp_arp).group(1) == '0:0:0:0:0:0' or re.search(r'STRING:(.*)', snmp_arp).group(1) == 'aa:aa:bb:bb:cc:cc':
                continue
            mac_address = re.sub(r'((?<=:)[0-9a-f](?=:)|(?<=^)[0-9a-f](?=:)|(?<=:)[0-9a-f](?=$))', r'0\1',re.search(r'STRING:(.*)', snmp_arp).group(1))
            ip_address = re.search(r'(.*?)(\d+.\d+.\d+.\d+)=(.*)', snmp_arp).group(2)
            arp_db[ip_address] = mac_address
        return arp_db
    elif type == 'other':
        arp_db = {}
        snmp_arp_db = commands.getoutput(
            'snmpwalk -v 2c -c %s %s IP-MIB::ipNetToMediaPhysAddress' % (community, ip)).replace(' ', '')
        for snmp_arp in snmp_arp_db.split('\n'):
            if re.search(r'STRING:(.*)', snmp_arp).group(1) == '0:0:0:0:0:0' or re.search(r'STRING:(.*)',snmp_arp).group(1) == 'aa:aa:bb:bb:cc:cc':
                continue
            mac_address = re.sub(r'((?<=:)[0-9a-f](?=:)|(?<=^)[0-9a-f](?=:)|(?<=:)[0-9a-f](?=$))', r'0\1',re.search(r'STRING:(.*)', snmp_arp).group(1))
            ip_address = re.search(r'(.*?)(\d+.\d+.\d+.\d+)=(.*)', snmp_arp).group(2)
            arp_db[ip_address] = mac_address
        return arp_db
def self_arp():
    arp_db = {}
    snmp_arp_db = commands.getoutput('snmpwalk -v 2c -c public 127.0.0.1 IP-MIB::ipNetToMediaPhysAddress').replace(' ', '')
    for snmp_arp in snmp_arp_db.split('\n'):
        if re.search(r'STRING:(.*)', snmp_arp).group(1) == '0:0:0:0:0:0' or re.search(r'STRING:(.*)', snmp_arp).group(1) == 'aa:aa:bb:bb:cc:cc':
            continue
        mac_address = re.sub(r'((?<=:)[0-9a-f](?=:)|(?<=^)[0-9a-f](?=:)|(?<=:)[0-9a-f](?=$))', r'0\1',re.search(r'STRING:(.*)', snmp_arp).group(1))
        ip_address = re.search(r'(.*?)(\d+.\d+.\d+.\d+)=(.*)', snmp_arp).group(2)
        arp_db[ip_address] = mac_address
    return arp_db
