import os
import commands

# scan for hosts and create file with IP address.
ip_range = raw_input("Enter IP range (eg: 192.168.1.0/24):")
os.system('nmap -sn -PS -oG - %s | awk \'{print $2}\' > hosts.txt' % ip_range)
#- - - - - - - - - - - - 

# perform port scan for enumerated hosts.
f = open ("hosts.txt", "r")
f1 = f.readlines()

for ip_add in f1:
  ip_add = ip_add.rstrip()
  #print ip_add
  #you can add various nmap host scanning commands below. 
  cmd = 'nmap -p 1-1000 -T4 -Pn %s' % ip_add
  output = commands.getoutput(cmd)
  f = open ("%s.txt" % ip_add, "w")
  f.write(output)
