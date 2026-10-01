# IN404 Unit 1 - Step 3
# Mechanize websites and gather MAC addresses given an IP address

from subprocess import Popen, PIPE
import re
import mechanize
import sys

while True:
    print("What would you like to do:")
    print(" 1. Mechanize website")
    print(" 2. Get MAC address from IP")
    print(" 3. Quit program")
    print("Please enter a number (1-3)")
    choice = input()

    if(choice == '1'):
        #If you use mechanize.urlopen(), the module handles extraction
        # and adding of cookies by itself
        cookies = mechanize.CookieJar()
        cookie_opener = mechanize.build_opener(mechanize.HTTPCookieProcessor(cookies))
        mechanize.install_opener(cookie_opener)

        url = input("Which website do you want to mechanize? ")
        #url = "http://www.webscantest.com/crosstraining/aboutyou.php"
        res = mechanize.urlopen(url)
        content = res.read()
        print(content)

    elif(choice == '2'):
        IP = input("Please enter the IP address you want to use ")
        pid = Popen(["arp", "-n", IP], stdout=PIPE)
        s = str(pid.communicate()[0])
        try:
            mac = re.search(r"(([a-f\d]{2}\:){5}[a-f\d]{2})", s).groups()[0]
            print(mac)
        except:
            print("MAC not found")

    elif(choice == '3'):
        sys.exit()

    print()
    print()
