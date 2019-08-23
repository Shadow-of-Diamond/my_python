#!/usr/bin/python
# -*- coding: UTF-8 -*-
import sys
import datetime
def npath(vips,bind_vip):
    for s in vips:
        vips_vip = s.split(' ')[3]
        vips_protocol = s.split(' ')[4]
        if vips_vip == bind_vip :
            if vips_protocol == 'ANY':
                return 1
            else:
                return 0
        else:
            continue

def persistence(vips,bind_vip):
    for s in vips:
        vips_vip = s.split(' ')[3]
        persistence_type = s.split(' ')[8]
        if vips_vip == bind_vip :
            if persistence_type == 'NONE':
                return 0
            else:
                return 1
        else:
            continue

def method(vips,rip_group_2):
    try:
        for s in vips:
            vips_vip_2 = s.split(' ')[3].split('_',1)[1]
            if vips_vip_2 == rip_group_2 :
                if s.find('ROUNDROBIN') > -1:
                    return 'round-robin'
                if s.find('SOURCEIPHASH') > -1:
                    return 'src-ip-hash'
                else:
                    return 'least-connection'
            else:
                continue
    except:
        return 'least-connection'

def text_create(name, msg):
    local_path = sys.path[0]
    full_path = local_path + '/' + name + '.txt'
    file = open(full_path,'w')
    file.write(msg)
    file.close()
    print('Done')

slb_fname = 'a10_slb_%s'%datetime.datetime.now().strftime("%Y-%m-%d_%H%M%S")

vip_binds = []
vips = []
rip_groups = []
citrix_conf_file = '%s/ct-MPX-12500-2.conf'%sys.path[0]
file_object = open(citrix_conf_file)
try:
    for line in file_object.readlines():
        if line.find("bind lb vserver vip_") > -1:
            vip_binds.append(line)
        elif line.find("add lb vserver vip_") > -1:
            vips.append(line)
        elif line.find("bind serviceGroup pool_") > -1:
            rip_groups.append(line)
        else:
            continue
except:
    pass
finally:
    file_object.close()

a10_rip_group = ''
for i in rip_groups:
    rip_group = i.split(' ')[2]
    member_rip = i.split(' ')[3]
    port = i.split(' ')[4].replace('\n','')
    rip_group_2 = i.split(' ')[2].split('_',1)[1]
    method_type = method(vips,rip_group_2)
    if method_type == None:
        method_type = 'least-connection'
    else:
        pass
    if port != '53':
        protocol = 'tcp'
    elif port == '53':
        continue
    else:
        protocol = 'err'
    # print 'slb server ' + member_rip + ' ' + member_rip.split('_')[1] + '\nport %s %s'%(port.replace('\n',''),protocol)
    # print 'slb service-group ' + rip_group + ' ' + protocol
    # print 'method %s'%method_type
    # print 'member ' + member_rip + ':' + port + '\n'
    a10_rip_object = 'slb server ' + member_rip + ' ' + member_rip.split('_')[1] + '\nport %s %s'%(port.replace('\n',''),protocol) \
                     + '\nslb service-group ' + rip_group + ' ' + protocol\
                     + '\nmethod %s'%method_type + '\nmember ' + member_rip + ':' + port + '\n'
    a10_rip_group = a10_rip_group + '\n' + a10_rip_object
# print a10_rip_group
vip_count = 0
persistence_count = 0


a10_vip_group = ''
for i in vip_binds:
    bind_ip = i.split(' ')[3].split('_')[1]
    bind_vip = i.split(' ')[3]
    port = i.split(' ')[3].split('_')[2].replace('\n','')
    vip = 'vip_%s'%bind_ip
    bind_group = i.split(' ')[4]
    npath_value = npath(vips,bind_vip)
    persistence_type = persistence(vips,bind_vip)
    if port != '53':
        protocol = 'tcp'
    elif port == '53':
        continue
    else:
        protocol = 'err'
    if npath_value == 1 and persistence_type == 1:
        # print 'slb virtual-server ' + vip + ' ' + bind_ip + '\nha-group 1\nport %s %s'%(port,protocol)
        # print 'service-group %sno-dest-nat'%bind_group.replace('\n','')
        # print 'template persist source-ip source_ip\n'
        a10_vip_object = 'slb virtual-server ' + vip + ' ' + bind_ip + '\nha-group 1\nport %s %s'%(port,protocol)  \
                        + '\nservice-group %s\nno-dest-nat'%bind_group.replace('\n','') \
                        + '\ntemplate persist source-ip source_ip\n'
        vip_count += 1
        persistence_count += 1
    elif npath_value == 1 and persistence_type == 0:
        # print 'slb virtual-server ' + vip + ' ' + bind_ip + '\nha-group 1\nport %s %s' % (port, protocol)
        # print 'service-group %sno-dest-nat\n' % bind_group
        a10_vip_object = 'slb virtual-server ' + vip + ' ' + bind_ip + '\nha-group 1\nport %s %s' % (port, protocol) \
                        + '\nservice-group %sno-dest-nat\n' % bind_group
        vip_count += 1
    elif npath_value == 0 and persistence_type == 1:
        # print 'slb virtual-server ' + vip + ' ' + bind_ip + '\nha-group 1\nport %s %s' % (port, protocol)
        # print 'service-group %s '%bind_group.replace('\n','')
        # print 'template persist source-ip source_ip\n'
        a10_vip_object = 'slb virtual-server ' + vip + ' ' + bind_ip + '\nha-group 1\nport %s %s' % (port, protocol) \
                        + '\nservice-group %s '%bind_group.replace('\n','') \
                        + '\ntemplate persist source-ip source_ip\n'
        vip_count += 1
        persistence_count += 1
    elif npath_value == 0 and persistence_type == 0:
        # print 'slb virtual-server ' + vip + ' ' + bind_ip + '\nha-group 1\nport %s %s' % (port, protocol)
        # print 'service-group %s\n ' % bind_group
        a10_vip_object = 'slb virtual-server ' + vip + ' ' + bind_ip + '\nha-group 1\nport %s %s' % (port, protocol) \
                        + '\nservice-group %s ' % bind_group
        vip_count += 1
    else:
        # print 'err'
        # print 'slb virtual-server ' + vip + ' ' + bind_ip + '\nha-group 1\nport %s %s' % (port, protocol)
        # print 'service-group %s\n ' % bind_group
        a10_vip_object = 'err' \
                        + '\nslb virtual-server ' + vip + ' ' + bind_ip + '\nha-group 1\nport %s %s' % (port, protocol) \
                        + '\nservice-group %s\n ' % bind_group
    a10_vip_group = a10_vip_group +  '\n' + a10_vip_object
# print a10_vip_group
# DNS_Conf
a10_dns_conf =  '''\nslb server real_192.168.236.148 192.168.236.148
port 53 tcp
slb service-group pool_61.145.113.11_53_tcp tcp
member real_192.168.236.148:53

slb server real_192.168.236.245 192.168.236.245
port 53 tcp
slb service-group pool_61.145.113.11_53_tcp tcp
member real_192.168.236.245:53

slb server real_192.168.236.148 192.168.236.148
port 53 udp
slb service-group pool_61.145.113.11_53_udp udp
member real_192.168.236.148:53

slb server real_192.168.236.245 192.168.236.245
port 53 udp
slb service-group pool_61.145.113.11_53_udp udp
member real_192.168.236.245:53


slb virtual-server vip_61.145.113.11 61.145.113.11
ha-group 1
port 53 tcp
service-group pool_61.145.113.11_53_tcp

slb virtual-server vip_61.145.113.11 61.145.113.11
ha-group 1
port 53 udp
service-group pool_61.145.113.11_53_udp

slb server real_192.168.237.86 192.168.237.86
port 53 udp
slb service-group pool_219.136.244.68_53_udp udp
member real_192.168.237.86:53

slb server real_192.168.237.87 192.168.237.87
port 53 udp
slb service-group pool_219.136.244.68_53_udp udp
member real_192.168.237.87:53

slb server real_192.168.237.121 192.168.237.121
port 53 udp
slb service-group pool_219.136.244.68_53_udp udp
member real_192.168.237.121:53

slb server real_192.168.237.130 192.168.237.130
port 53 udp
slb service-group pool_219.136.244.68_53_udp udp
member real_192.168.237.130:53

slb server real_192.168.237.86 192.168.237.86
port 53 tcp
slb service-group pool_219.136.244.68_53_tcp tcp
member real_192.168.237.86:53

slb server real_192.168.237.87 192.168.237.87
port 53 tcp
slb service-group pool_219.136.244.68_53_tcp tcp
member real_192.168.237.87:53

slb server real_192.168.237.121 192.168.237.121
port 53 tcp
slb service-group pool_219.136.244.68_53_tcp tcp
member real_192.168.237.121:53

slb server real_192.168.237.130 192.168.237.130
port 53 tcp
slb service-group pool_219.136.244.68_53_tcp tcp
member real_192.168.237.130:53


slb virtual-server vip_219.136.244.68 219.136.244.68
ha-group 1
port 53 udp
service-group pool_219.136.244.68_53_udp


slb virtual-server vip_219.136.244.68 219.136.244.68
ha-group 1
port 53 tcp
service-group pool_219.136.244.68_53_tcp

slb server real_192.168.237.86 192.168.237.86
port 53 udp
slb service-group pool_192.168.238.75_53_udp udp
member real_192.168.237.86:53

slb server real_192.168.237.87 192.168.237.87
port 53 udp
slb service-group pool_192.168.238.75_53_udp udp
member real_192.168.237.87:53

slb server real_192.168.237.121 192.168.237.121
port 53 udp
slb service-group pool_192.168.238.75_53_udp udp
member real_192.168.237.121:53

slb server real_192.168.237.130 192.168.237.130
port 53 udp
slb service-group pool_192.168.238.75_53_udp udp
member real_192.168.237.130:53

slb virtual-server vip_192.168.238.75 192.168.238.75
ha-group 1
port 53 udp
service-group pool_192.168.238.75_53_udp
no-dest-nat'''

all_slb_conf = a10_rip_group + a10_vip_group + a10_dns_conf

text_create(slb_fname,all_slb_conf)

#
#
#
# print 'Citrix VIP count:%s'%(len(vip_binds))
# print 'A10 VIP count:%s'%(vip_count)
# print persistence_count
