import mechanize
from mechanize import Browser
import time
import random
import http.cookiejar
import os, sys


G = '\033[32;1m'
R = '\033[31;1m'
W = '\033[0m'


#LOGO
FBI = """

                       .,,uod8B8bou,,.
              ..,uod8BBBBBBBBBBBBBBBBRPFT?l!i:.
         ,=m8BBBBBBBBBBBBBBBRPFT?!||||||||||||||
         !...:!TVBBBRPFT||||||||||!!^^""'   ||||
         !.......:!?|||||!!^^""'            ||||
         !.........||||                     ||||
         !.........||||  ##                 ||||
         !.........||||                     ||||
         !.........||||                     ||||
         !.........||||                     ||||
         !.........||||                     ||||
         `.........||||                    ,||||
          .;.......||||               _.-!!|||||
   .,uodWBBBBb.....||||       _.-!!|||||||||!:'
!YBBBBBBBBBBBBBBb..!|||:..-!!|||||||!iof68BBBBBb....
!..YBBBBBBBBBBBBBBb!!||||||||!iof68BBBBBBRPFT?!::   `.
!....YBBBBBBBBBBBBBBbaaitf68BBBBBBRPFT?!:::::::::     `.
!......YBBBBBBBBBBBBBBBBBBBRPFT?!::::::;:!^"`;:::       `.
!........YBBBBBBBBBBRPFT?!::::::::::^''...::::::;         iBBbo.
`..........YBRPFT?!::::::::::::::::::::::::;iof68bo.      WBBBBbo.
  `..........:::::::::::::::::::::::;iof688888888888b.     `YBBBP^'
    `........::::::::::::::::;iof688888888888888888888b.     `
      `......:::::::::;iof688888888888888888888888888888b.
        `....:::;iof688888888888888888888888888888888899fT!
          `..::!8888888888888888888888888888888899fT|!^"'
            `' !!988888888888888888888888899fT|!^"'
                `!!8888888888888888899fT|!^"'
                  `!988888888899fT|!^"'
                    `!9899fT|!^"'
                      `!^"'
        	
               		
"""


print(R + FBI + W)


X = raw_input("""
[+] FILE NAME : """)

P = str(X)


C = raw_input(G + """
[+] MESSAGE : """ )
#OUTPUT !
WT = """ 
[*] WAIT .... """
print(R + WT )

#BASICS

br = mechanize.Browser() 
cj = mechanize.CookieJar()
br.set_handle_robots(False)
br.set_handle_equiv(True)
br.set_handle_referer(True)
br.set_handle_redirect(True)
br.set_cookiejar(cj)
br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor() , max_time = (1,2,3) )
br.addheaders={('User-agent' , 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/33.0.1750.146 Safari/537.36')}
# select URL & open it
response = br.response()
br.open("https://www.facebook.com/login")

EML = raw_input('YOUR EMAIL : ')
PSW = raw_input("YOUR PASSWORD : ")
# select form

br.select_form(nr=0)

# ATTRS

br.form["email"] = EML
br.form["pass"] = PSW
br.submit(id = "loginbutton" )

#WAIT 1

time.sleep(1.5)

#print(br.title()) / un important .

#CHK
#if br.title() != "Facebook" :
	#print( R + "========[!] ERRoR [!]========")
#else :
# print(G + "SUCSSESFUL LOGIN ! >>> wait for comment ...")	


 

STRT = """ [!] PROGRAM START . """


print(G + STRT + W)  


 

def main() : 
    i= int(0)
    while(i<1000000000) :
        FBURL = ('https://m.facebook.com/messages/t/') 
        readFile = open(P)
        lines = readFile.readlines()
        readFile.close()
        lino=lines[1:]
        Ww = open(P, "w")
        Ww.writelines(lino)
        Ww.close()
        Ff=open(P, "r")
        ends = (Ff.readline(100))


        br.open(FBURL + ends) 

        br.select_form(nr=0)
        br.form['body'] = C
        br.submit()
        time.sleep(0.2)
        i+=1
        print( R +"{}".format(i) + " MSG SENT")
        
    print( G + " [!] PROGRAM END .")


if __name__ == '__main__':main() 
    
    
