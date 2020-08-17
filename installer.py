import os,sys,time

os.system('clear')
print "============="
print "INSTALER hack"
print "============="
print ""
print "[+] MENU [+]"
print ""
print "[1] install tools"
print "[2] run script"
print ""
menu = raw_input('[+] PILIH : ')
if menu == "1":
	os.system('pkg install git')
	os.system('pkg install figlet')
	os.system('pkg install ruby')
	os.system('gem install lolcat')
	os.system('pkg install toilet')
	os.system('pip2 install requests')
	os.system('python2 installer.py')
elif menu == "2":
	os.system('clear')
	os.system('python2 hack_v1.5.py')
