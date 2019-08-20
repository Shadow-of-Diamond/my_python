from winpexpect import winspawn

#ssh = winspawn('ssh',['-tty','xiezhenkun@192.168.1.10'])
ssh = winspawn('ssh -tt xiezhenkun@192.168.1.10')
ssh.logfile = sys.stdout
i = ssh.expect(['word:'], timeout = 5)
print (i)
ssh.sendline('xzK343206603')