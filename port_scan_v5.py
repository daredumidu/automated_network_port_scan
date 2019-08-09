try:
  import os
  import commands
  import sys

  # scan for hosts and create file with IP address.
  ip_range = raw_input("Enter IP range (eg: 192.168.1.0/24):")
  os.system('nmap -sn -PS -oG - %s | awk \'{print $2}\' > hosts.txt' % ip_range)
  num_lines = sum(1 for line in open('hosts.txt'))
  num_ip = num_lines - 2
  print ('%s hosts discovered.' % num_ip)
#- - - - - - - - - - - - 

  number = int(raw_input("Press 1 to lite port scan, press 2 to full port scan:"))

  if number == 1:

    # perform port scan for enumerated hosts.
    f = open ("hosts.txt", "r")
    f1 = f.readlines()
    print ('Lite port scan started.')

    progress = 0.0
    increment = 100.0 / float(num_lines)
    #print increment

    for ip_add in f1:
      ip_add = ip_add.rstrip()
      cmd = 'nmap -p 1-1000 -T4 -Pn %s' % ip_add
      output = commands.getoutput(cmd)
      f = open ("%s.txt" % ip_add, "w")
      f.write(output)

      progress += increment

      sys.stdout.write("\r")
      sys.stdout.write(str(progress) + "%")
      sys.stdout.flush()

    sys.stdout.write("\n")
    print ('Lite port scan complete. check the directory for files.')
#- - - - - - - - - - - - - - - -

  elif number == 2:

    # perform port scan for enumerated hosts.
    f = open ("hosts.txt", "r")
    f1 = f.readlines()
    print ('Full port scan started.')

    progress = 0.0
    increment = 100.0 / float(num_lines)
    #print increment

    for ip_add in f1:
      ip_add = ip_add.rstrip()
      cmd = 'nmap -p - -T4 -A -v -Pn %s' % ip_add
      output = commands.getoutput(cmd)
      f = open ("%s.txt" % ip_add, "w")
      f.write(output)

      progress += increment

      sys.stdout.write("\r")
      sys.stdout.write(str(progress) + "%")
      sys.stdout.flush()

    sys.stdout.write("\n")
    print ('Full port scan complete. check the directory for files.')
#- - - - - - - - - - - - - - - -

except KeyboardInterrupt:
  print ("Program aborted by user")
  exit()
