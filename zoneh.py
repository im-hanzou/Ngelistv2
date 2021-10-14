import requests, httplib
import socket
from platform import system
import os
import sys, time
import re

#------------------ Help -----------------------------------
#Video How Use Script : 
#Use Python 27
#Install Requests : pip install requests
#Fuck Any One Edit To Logo -_- 
#--------------------------------------------------
url = "http://www.zone-h.org/archive/notifier="
urll = "http://zone-h.org/archive/published=0"

#-------------------- Cookies -------------------------
my_cook = {
	"ZHE" : "1dc7f16ed9974794a1dd59f8c6f7d4e7" ,
	"PHPSESSID" : "rds72v9b665opriq8e4860bpg7"
	}
#------------------------------------------------------

exploit = ["/admin/login.php","/admin/panel.php","/admin/","/login.php","/admin.html","/admin.php","/admin-login.php","_admin/","backoffice/","admin/","administrator/","moderator/","webadmin/","adminarea/","bb-admin/","adminLogin/","admin_area/","panel-administracion/","instadmin/",
"memberadmin/","administratorlogin/","adm/","account.asp","admin/account.asp","admin/index.asp","admin/login.asp","admin/admin.asp",
"admin_area/admin.asp","admin_area/login.asp","admin/account.html","admin/index.html","admin/login.html","admin/admin.html",
"admin_area/admin.html","admin_area/login.html","admin_area/index.html","admin_area/index.asp","bb-admin/index.asp","bb-admin/login.asp","bb-admin/admin.asp",
"bb-admin/index.html","bb-admin/login.html","bb-admin/admin.html","admin/home.html","admin/controlpanel.html","admin.html","admin/cp.html","cp.html",
"administrator/index.html","administrator/login.html","administrator/account.html","administrator.html","login.html","modelsearch/login.html","moderator.html",
"moderator/login.html","moderator/admin.html","account.html","controlpanel.html","admincontrol.html","admin_login.html","panel-administracion/login.html",
"admin/home.asp","admin/controlpanel.asp","admin.asp","pages/admin/admin-login.asp","admin/admin-login.asp","admin-login.asp","admin/cp.asp","cp.asp",
"administrator/account.asp","administrator.asp","login.asp","modelsearch/login.asp","moderator.asp","moderator/login.asp","administrator/login.asp",
"moderator/admin.asp","controlpanel.asp","admin/account.html","adminpanel.html","webadmin.html","pages/admin/admin-login.html","admin/admin-login.html",
"webadmin/index.html","webadmin/admin.html","webadmin/login.html","user.asp","user.html","admincp/index.asp","admincp/login.asp","admincp/index.html",
"admin/adminLogin.html","adminLogin.html","admin/adminLogin.html","home.html","adminarea/index.html","adminarea/admin.html","adminarea/login.html",
"panel-administracion/index.html","panel-administracion/admin.html","modelsearch/index.html","modelsearch/admin.html","admin/admin_login.html",
"admincontrol/login.html","adm/index.html","adm.html","admincontrol.asp","admin/account.asp","adminpanel.asp","webadmin.asp","webadmin/index.asp",
"webadmin/admin.asp","webadmin/login.asp","admin/admin_login.asp","admin_login.asp","panel-administracion/login.asp","adminLogin.asp",
"admin/adminLogin.asp","home.asp","admin.asp","adminarea/index.asp","adminarea/admin.asp","adminarea/login.asp","admin-login.html",
"panel-administracion/index.asp","panel-administracion/admin.asp","modelsearch/index.asp","modelsearch/admin.asp","administrator/index.asp",
"admincontrol/login.asp","adm/admloginuser.asp","admloginuser.asp","admin2.asp","admin2/login.asp","admin2/index.asp","adm/index.asp"]

def notifierr():
	notf = raw_input("\033[95mEntre notifier: \033[92m")
	zeb = int(raw_input("\033[95mEntre Num Of Page: \033[92m"))

	for i in range(1, zeb):
		dz = requests.get(url + notf +"/page=" + str(i), cookies=my_cook)
		dzz = dz.content
		if '<html><body>-<script type="text/javascript"' in dzz:
			sys.exit()
		elif "captcha" in dzz:
			print("Entre Captcha In Browser Of Site [zone-h.org]")
		else:
			print("\033[95m\tWait To Grabb Page: "),i
			Hunt_urls = re.findall('<td>(.*)\n							</td>', dzz)
			for xx in Hunt_urls:
				print '\033[91m    ['  + '*' + '] ' + xx.split('/')[0]
				with open( notf + '.txt', 'a') as rr:
					rr.write(xx.split('/')[0] + '\n')


def qqq():
	ok = int(raw_input("\033[95mEntre Num Of page [Maximum Page: 50]: \033[92m"))
	for qwd in range(1, ok):
		rb = requests.get(urll + "/page=" + str(qwd) , cookies=my_cook)
		dzq = rb.content

		if '<html><body>-<script type="text/javascript"' in dzq:
			print("Change Cookies Plz")
			sys.exit()
		elif "captcha" in dzq:
			print("Entre Captcha In Browser Of Site [zone-h.org]")

		else:
			print("\033[95m\tWait To Grabb Page: "),qwd
			Hunt_urlss = re.findall('<td>(.*)\n							</td>', dzq)
			for xxx in Hunt_urlss:
				print '\033[91m    ['  + '*' + '] ' + xxx.split('/')[0]
				with open('onhold.txt', 'a') as rrr:
					rrr.write(xxx.split('/')[0] + '\n')

def test():
    try:
    	q = raw_input('\033[96m Entre Liste Site: \033[90m ')
    	q = open(q, 'r')
    except:
    	print("Entre List Sites -_- #Noob ")

    for lst in q:
        lst = lst.rstrip()
        print("\033[94m 	Wait Scaning ....... \033[94m"), lst
        for exploits in exploit:
            exploits.rstrip()
            try:

                if lst[:7] == "http://":
                    lst = lst.replace("http://","")
                if lst[:8] == "https://":
                    lst = lst.replace("https://", "")
                if lst[-1] == "/":
                    lst = lst.replace("/","")
                socket.setdefaulttimeout(5)
                conn = httplib.HTTPConnection(lst)
                conn.request("POST", exploits)
                conn = conn.getresponse()
                htmlconn = conn.read()
                if conn.status == 200 and ('type="password"') in htmlconn:
                    print("\033[92m [+] Admin Panel [+] ======\033[96m=======> \033[96m ") , lst + exploits
                    with open("admin_panels.txt", "a") as by:
                        by.writelines(lst + exploits + "\n")
                else:
                    print("\033[91m [-] Not Found : [-]"),lst + exploits
            except:
                pass

def clearscrn():
    if system() == 'Linux':
        os.system('clear')
    if system() == 'Windows':
        os.system('cls')
        os.system('color a')
clearscrn()

def slowprint(s):
    for c in s + '\n':
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(4. / 100)

def logo():
    print("""\033[95m
                                   _       _       _    _ _ _ _____
          __ _ _ __ ___   __ _ ___(_) __ _| |__   | | _(_) | |___ / _ __
         / _` | '_ ` _ \ / _` |_  / |/ _` | '_ \  | |/ / | | | |_ \| '__|    \033[91m
        | (_| | | | | | | (_| |/ /| | (_| | | | | |   <| | | |___) | |       \033[90m       
         \__,_|_| |_| |_|\__,_/___|_|\__, |_| |_| |_|\_\_|_|_|____/|_|  
                                     |___/
                                     
                                	    Script Name : Mnanok Tester ^_^
                 		Developed By : Trojan Kill3r Amazigh / Aziz Messaoudi
                                     """)

logo()
slowprint("\n\t\t\t\t\tCoded By " + "\033[95m ./Trojan Kill3r Amazigh" + "\n\t\t\t\t\t\t            \033[92m Facebook: fb.com/amazigh.kil3r")
def help():
	print("""
		----_______________---

		[1] Grabb By Onhold :*
		[2] Grabb By Notifier <3
		
		<3_________________<3

		[3] Bypass Finder ^_^

			\t\t\tchoose number 1 / 2 / 3 : 
 		""")		
	try:
		qq = int(raw_input("\033[95mPress Number [1 / 2 / 3] : \033[92m"))
		if qq == 1:
			qqq()
		elif qq == 2:
			notifierr()
		elif qq == 3:
			test()
		else:
			logo()
			sys.exit()
	except:
		clearscrn()
		logo()
		print("\033[91mKi zebi Nta -_- Nooooooooooooob")
		print("\033[95mIf Script Not Grabbed Just Work Edit Script And Change The Cookies : [PHPSESSID & ZHE] ")
		print("For Get cookies Go  To  Zone [F12 --> Application --> cookies --> Copy Past [PHPSESSID & ZHE] To Script And Good Luck ^_^")
		print("\033[91mTrojan Kil3r Amazigh [Algerien] [We Are Not Pro But We Are Not Noob ^_^]")

help()
