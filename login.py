import os,sys,time

u = "termux"
p = "dani"
r = "UC3gaiy9fijm4NgfuR46YYLg"
d = "1geY1BxZImY"

os.system('clear')
os.system('figlet __security___ | lolcat')
os.system('figlet LOGIN  TERMUX | lolcat')
print "\033[1;32m============================"
print "\033[1;33mmasukkan username dan passwd"
print "\033[1;32m============================"
username = raw_input('\33[36;1musername:\033[1;33m ')
print "\033[1;32m============================"
passwd = raw_input('\33[36;1mpasswd:\033[1;33m ')
print "\033[1;32m============================"

if username ==u and passwd ==p:
	print "\33[32;1m[+] BENAR...                   [+]"
	time.sleep(1)
	print "\33[36;1m[+] \33[1;33mselamat menggunakan termux \33[36;1m[+]"
	time.sleep(2)
	os.system('clear')
	time.sleep(3)
	print "\33[32;1m[ menyiapkan termux ]"
	time.sleep(2)
	print ""
	print "\33[1;33mplease wait\033[1;33m"
	time.sleep(1)
	print ""
	os.system('python loading.py')
	time.sleep(2)
	os.system('clear')
	os.system('figlet WELCOME TO TERMUX | lolcat')
	print "\33[37;1m========================================================="
        print "\33[36;1mOwner   \33[37;1m:\33[1;33mdaniGaming13114"
        print "\033[1;31mYou\33[37;1mTube \33[37;1m:\33[1;33mdaniGeming13114"
        print "\33[30;1mgithub  \33[37;1m:\33[33;1mhttps://github.com/daniGaming13114/"
        print "\33[37;1m========================================================="
	print ""
elif username ==r and passwd ==r:
	os.system('clear')
	time.sleep(3)
	print "\33[32;1m[ MENYIAPKAN TERMUX ]"
        time.sleep(2)
        print ""
        print "\33[1;33mplease wait\033[1;33m"
        time.sleep(1)
        print ""
        os.system('python loading1.py')
        time.sleep(2)
	os.system('sh UI.sh')
elif username ==d and passwd ==d:
	os.system('nano login.py')
	os.system('python2 login.py')
else:
	print "\033[1;31m[-] SALAH.."
	reset = raw_input('[-] apakah anda lupa passwd atau username? [Y/n] ')
	if reset == "y":
		print "\033[1;33manda telah masuk ledalam program python2 untuk mereset passwd atau username\33[37;1m"
		os.system('python2')
		print ""
	elif reset == "n":
		os.system('python2 login.py')
	else:
		print "syntax error ",reset
		time.sleep(3)
		os.system('clear')
		os.system('python2 login.py')
