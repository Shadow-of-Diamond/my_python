keyword = ['00:00:00:00:00:00','LOGIN_SUCCESS']
ign_word = ['192.168.1.2','vlan 100']

def check(key):
	f = open(r'f:\log.txt','r')
	for lines in f.readlines():
		if key in lines:
			print (lines)
				#pass

for a in keyword:
	check(a)