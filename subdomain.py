import requests
import sys
import argparse
import bcolors

def banner():
    print("""
                        
                    ░██████╗██╗░░░██╗██████╗░░░░░░░██████╗░░█████╗░███╗░░░███╗░█████╗░██╗███╗░░██╗░░░░░░███████╗██╗███╗░░██╗██████╗░███████╗██████╗░
                    ██╔════╝██║░░░██║██╔══██╗░░░░░░██╔══██╗██╔══██╗████╗░████║██╔══██╗██║████╗░██║░░░░░░██╔════╝██║████╗░██║██╔══██╗██╔════╝██╔══██╗
                    ╚█████╗░██║░░░██║██████╦╝█████╗██║░░██║██║░░██║██╔████╔██║███████║██║██╔██╗██║█████╗█████╗░░██║██╔██╗██║██║░░██║█████╗░░██████╔╝
                    ░╚═══██╗██║░░░██║██╔══██╗╚════╝██║░░██║██║░░██║██║╚██╔╝██║██╔══██║██║██║╚████║╚════╝██╔══╝░░██║██║╚████║██║░░██║██╔══╝░░██╔══██╗
                    ██████╔╝╚██████╔╝██████╦╝░░░░░░██████╔╝╚█████╔╝██║░╚═╝░██║██║░░██║██║██║░╚███║░░░░░░██║░░░░░██║██║░╚███║██████╔╝███████╗██║░░██║
                    ╚═════╝░░╚═════╝░╚═════╝░░░░░░░╚═════╝░░╚════╝░╚═╝░░░░░╚═╝╚═╝░░╚═╝╚═╝╚═╝░░╚══╝░░░░░░╚═╝░░░░░╚═╝╚═╝░░╚══╝╚═════╝░╚══════╝╚═╝░░╚═╝
                                                                                                                                         Code by NG          
          """)

if len(sys.argv) > 1:
    banner()
    if((sys.argv[1] != '-l') or (sys.argv[1] != '-d')):
        try:
            input_location = sys.argv[2]
            input_domain = sys.argv[4]

            parser = argparse.ArgumentParser()
            parser.add_argument("-l", required=True)
            parser.add_argument("-d", required=True)
            args = parser.parse_args()

            input_file = open(input_location, "r")
            for file_text in input_file:
                    Full_url = "https://" + file_text.strip() + "." + input_domain + ".com/"
                    try:
                        if (requests.get(Full_url).status_code == 200):
                            print(bcolors.OKMSG +Full_url, requests.get(Full_url).status_code )
                    except:
                        print(bcolors.ERRMSG + Full_url + '  Not reachable')
        except:
            print('Please enter python subdomain.py -l < location of word file > -d < domain > ')
    elif((sys.argv[1] == '-h') | (sys.argv[1] == '--help')):
        print(bcolors.BOLD + 'usage: subdomain.py [-h] -l location ' '\n' 'OPTIONS:' '\n' '-h,--help    '
                             'show this help message and exit' '\n''-l Location,   --location Location' '\n' '-d domain    Domain ')
    elif (((sys.argv[1] != '-l') | (sys.argv[1] != '-d'))):
        print('Please enter -d <valid domain name> -o <output location>')
else:
  banner()
  print(bcolors.ERR + 'Please select atleast 1 option from (-l,-d) or -h, with a valid domain name')



